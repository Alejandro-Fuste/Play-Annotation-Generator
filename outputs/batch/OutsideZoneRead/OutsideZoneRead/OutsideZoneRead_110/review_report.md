# Play-Annotation-Generator Annotation Review — OutsideZoneRead_110

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_110`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 23
- **Ball Tracks:** 1
- **Action Segments:** 59
- **Validation Warnings:** 59
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 40
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `7` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_Keep` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 8 | START | 8 | 26 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `13` | `12` | 11 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `3` | 11 | START | 11 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `7` | `6` | 11 | START | 11 | 74 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `7` | 11 | START | 11 | 65 |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | C | `13` | `12` | 21 | START | 27 | 78 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `1` | 26 | END | 8 | 26 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `2` | `1` | 31 | START | 31 | 35 |
| ✅ EXACT | `Action_Keep` | QB | `2` | `1` | 36 | START | 36 | 47 |
| ✅ EXACT | `Action_BallCarry` | QB | `2` | `1` | 48 | START | 48 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 78 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 8 | 26 | 19 | inferred_complete_timeline |
| `Action_None` | 27 | 30 | 4 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 31 | 35 | 5 | inferred_complete_timeline |
| `Action_Keep` | 36 | 47 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 48 | 210 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 44 | 37 | inferred_complete_timeline |
| `Action_None` | 48 | 77 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 52 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 65 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 74 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 8 | 26 | 19 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 27 | 78 | 52 | inferred_complete_timeline |
| `Action_None` | 79 | 93 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 43 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 78 | 34 | inferred_complete_timeline |
| `Action_None` | 79 | 91 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_None` | 27 | 70 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 38 | 31 | inferred_complete_timeline |
| `Action_None` | 48 | 192 | 145 | inferred_complete_timeline |
| `Action_None` | 196 | 200 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 37 | 30 | inferred_complete_timeline |
| `Action_None` | 39 | 54 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 84 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 152 | 145 | inferred_complete_timeline |
| `Action_None` | 156 | 210 | 55 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–196 | 197 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 15–43 | 12 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 22–32 | 8 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 78–81 | 4 | 1 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 89–98 | 10 | 1 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 89–210 | 117 | 2 | Undefined position; Undefined team |
| `21` | `31` | Position_Unknown | Team_Unknown | 101–210 | 108 | 2 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 108–210 | 103 | 1 | Undefined position; Undefined team |
| `23` | `38` | Position_Unknown | Team_Unknown | 140–210 | 69 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | 19 | 21 | 3 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `13` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `13` (C): Annotated start 21 != Inferred start 27

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 37 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 222: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [8–26], lower_priority='Action_ZoneBlock' annotated_start=11, effective_Action_ZoneBlock_start=27.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [8–26], lower_priority='Action_BlockSecondLevel' annotated_start=21, effective_Action_BlockSecondLevel_start=27.
- ⚠️ Action 'Action_None' range [8-52] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [48-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-44] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-77] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-43] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-91] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-196] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-84] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-74] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-65] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-37] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-54] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-152] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-22] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-25] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-70] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-93] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-38] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-192] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-19] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-23] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-32] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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