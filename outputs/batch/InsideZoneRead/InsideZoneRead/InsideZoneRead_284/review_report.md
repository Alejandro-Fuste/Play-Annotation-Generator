# Play-Annotation-Generator Annotation Review — InsideZoneRead_284

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_284`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 22
- **Ball Tracks:** 0
- **Action Segments:** 65
- **Validation Warnings:** 67
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 42
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | SAF | defense | `6` | `5` |
| ✅ EXACT | `Action_ReadDefender` | SAF | defense | `6` | `5` |
| ✅ EXACT | `Action_Keep` | SAF | defense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | SAF | defense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 27 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `20` | `17` | 25 | START | 116 | 116 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `9` | 28 | START | 28 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 28 | START | 28 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `2` | `1` | 28 | START | 28 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `3` | 28 | START | 28 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `8` | 28 | START | 28 | 91 |
| ✅ EXACT | `Action_SnapReceive` | SAF | `6` | `5` | 36 | END | 25 | 36 |
| ✅ EXACT | `Action_ReadDefender` | SAF | `6` | `5` | 40 | START | 40 | 55 |
| ✅ EXACT | `Action_Keep` | SAF | `6` | `5` | 56 | START | 56 | 69 |
| ✅ EXACT | `Action_BallCarry` | SAF | `6` | `5` | 70 | START | 70 | 83 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 110 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 82 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 43 | 19 | inferred_complete_timeline |
| `Action_None` | 47 | 60 | 14 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 72 | 73 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 91 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 102 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_None` | 111 | 153 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 27 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 82 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 92 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 110 | 17 | inferred_complete_timeline |
| `Action_None` | 111 | 171 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 75 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 110 | 32 | inferred_complete_timeline |
| `Action_None` | 111 | 118 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 52 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 110 | 35 | inferred_complete_timeline |
| `Action_None` | 111 | 121 | 11 | inferred_complete_timeline |
| `Action_None` | 124 | 132 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 110 | 83 | inferred_complete_timeline |
| `Action_None` | 111 | 148 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 121 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 83 | 130 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 24 | 22 | inferred_complete_timeline |
| `Action_None` | 25 | 74 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 107 | 83 | inferred_complete_timeline |
| `Action_None` | 130 | 180 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 101 | 77 | inferred_complete_timeline |
| `Action_None` | 115 | 180 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 36 | 12 | inferred_complete_timeline |
| `Action_None` | 37 | 39 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 40 | 55 | 16 | inferred_complete_timeline |
| `Action_Keep` | 56 | 69 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 83 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 26–180 | 145 | 5 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 66–72 | 7 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 71–122 | 52 | 1 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 80–137 | 57 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 116–134 | 19 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 124–180 | 57 | 1 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 132–180 | 49 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 133–180 | 48 | 1 | Undefined position; Undefined team |
| `21` | `33` | Position_Unknown | Team_Unknown | 174–180 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `20` (Position_Unknown): Annotated start 25 != Inferred start 116
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=116, end=36. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-130] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-82] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-92] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-110] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-43] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-60] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-52] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-57] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-132] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-121] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-83] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-82] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-91] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-110] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-148] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-107] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-75] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-118] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-70] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-72] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-122] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-102] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 117, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [117-134] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '21' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_284'; source metadata written as null.

</details>