# Play-Annotation-Generator Annotation Review — InsideZoneRead_203

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_203`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `14` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `2` | `1` | 15 | START | 15 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 18 | START | 18 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `12` | `11` | 18 | START | 18 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `12` | 18 | START | 18 | 53 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `7` | 18 | START | 18 | 120 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 29 | END | 15 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | `4` | `3` | 32 | START | 32 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `4` | 54 | START | 54 | 142 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 120 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_SnapReceive` | 15 | 29 | 15 | inferred_complete_timeline |
| `Action_None` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 32 | 43 | 12 | inferred_complete_timeline |
| `Action_ReadDefender` | 45 | 113 | 69 | inferred_complete_timeline |
| `Action_ReadDefender` | 131 | 200 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_BallCarry` | 54 | 142 | 89 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 155 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 160 | 195 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 86 | 72 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 106 | 4 | inferred_complete_timeline |
| `Action_None` | 110 | 118 | 9 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 46 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 120 | 57 | inferred_complete_timeline |
| `Action_None` | 121 | 126 | 6 | inferred_complete_timeline |
| `Action_None` | 131 | 247 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 53 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 60 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 90 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 120 | 21 | inferred_complete_timeline |
| `Action_None` | 121 | 252 | 132 | inferred_complete_timeline |
| `Action_None` | 254 | 267 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 120 | 103 | inferred_complete_timeline |
| `Action_None` | 121 | 158 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 78 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 59 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 130 | 116 | inferred_complete_timeline |
| `Action_None` | 133 | 269 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 80 | 66 | inferred_complete_timeline |
| `Action_None` | 82 | 114 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 144 | 130 | inferred_complete_timeline |
| `Action_None` | 146 | 208 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–176 | 177 | 3 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–100 | 98 | 3 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 16–215 | 199 | 2 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 45–153 | 108 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 75–88 | 6 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 86–210 | 124 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 99–269 | 168 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 100–147 | 48 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 103–269 | 167 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 104–181 | 66 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 107–269 | 153 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 108–146 | 39 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 135–269 | 126 | 5 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 142–164 | 23 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 148–205 | 56 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 214–251 | 38 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 216–269 | 54 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 406: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 406: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 103 frames exceeds threshold 90 frames [start=18, end=120].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RG) duration 103 frames exceeds threshold 90 frames [start=18, end=120].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (LT) duration 103 frames exceeds threshold 90 frames [start=18, end=120].
- ⚠️ Action 'Action_None' range [15-130] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-269] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-176] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-144] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-208] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [32-43] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [45-113] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [131-200] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [54-142] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-155] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [160-195] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-78] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-80] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-114] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-158] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-54] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-100] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-59] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-90] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-252] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-267] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-46] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-247] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-53] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-118] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-31] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-215] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-177] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-145] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-114] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-181] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-255] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-146] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-141] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-249] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-251] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-269] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>