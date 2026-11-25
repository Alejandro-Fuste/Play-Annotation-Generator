# Play-Annotation-Generator Annotation Review — InsideZoneRead_278

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_278`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 3
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT2 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `21` | `19` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `21` | `19` |
| ❌ MISSING SEGMENT | `Action_Keep` | Position_Unknown | Team_Unknown | `21` | `19` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 16 |
| ✅ EXACT | `Action_BallSnap` | DT2 | `11` | `10` | 14 | START | 14 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `12` | `11` | 17 | START | 17 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `13` | 17 | START | 17 | 22 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 17 | START | 17 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `8` | `7` | 17 | START | 17 | 53 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `21` | `19` | 31 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `21` | `19` | 36 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Keep` | Position_Unknown | `21` | `19` | 40 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `21` | `19` | 60 | START | 75 | 111 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 91 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 55 | 42 | inferred_complete_timeline |
| `Action_None` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_None` | 66 | 76 | 11 | inferred_complete_timeline |
| `Action_None` | 88 | 91 | 4 | inferred_complete_timeline |
| `Action_None` | 93 | 108 | 16 | inferred_complete_timeline |
| `Action_None` | 110 | 115 | 6 | inferred_complete_timeline |
| `Action_None` | 118 | 180 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 43 | 30 | inferred_complete_timeline |
| `Action_None` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_None` | 48 | 51 | 4 | inferred_complete_timeline |
| `Action_None` | 62 | 64 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 36 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 66 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 22 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 91 | 22 | inferred_complete_timeline |
| `Action_None` | 92 | 157 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 53 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 91 | 13 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_None` | 99 | 102 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 91 | 75 | inferred_complete_timeline |
| `Action_None` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_None` | 98 | 114 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 56 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 63 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 81 | 68 | inferred_complete_timeline |
| `Action_None` | 108 | 110 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–22
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_BallSnap` | 14 | 22 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 88 | 75 | inferred_complete_timeline |
| `Action_None` | 91 | 123 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 107 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 75 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 148 | 135 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 171 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–79 | 79 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 28–137 | 46 | 7 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 31–117 | 87 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 67–75 | 9 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 73–180 | 108 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 75–111 | 37 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 83–180 | 95 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 91–103 | 13 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 91–96 | 6 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 101–180 | 58 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 107–127 | 21 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 117–121 | 5 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 131–180 | 49 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 147–180 | 34 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 149–180 | 32 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 149–180 | 32 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 157–158 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 159–180 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `21` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `21` (Position_Unknown)
- ❌ Missing segment for action `Action_Keep` on target `21` (Position_Unknown)
- ⚠️ `Action_BallCarry` for actor_track_id `21` (Position_Unknown): Annotated start 60 != Inferred start 75

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '19' has invalid range: start=75, end=31. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '19' has invalid range: start=75, end=39. Clamping end to start.
- ⚠️ Segment 'Action_Keep' for track '19' has invalid range: start=75, end=59. Clamping end to start.
- ⚠️ Action 'Action_None' range [14-75] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-63] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-148] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-88] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-123] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-114] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-43] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-51] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-55] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-76] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-108] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-53] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-91] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-56] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [14-22] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-36] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-56] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-66] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-22] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-157] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-79] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-52] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-180] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [75-111] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-180] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-114] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-127] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-159] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-180] for track '32' has 2 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_278'; source metadata written as null.

</details>