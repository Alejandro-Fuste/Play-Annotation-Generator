# Play-Annotation-Generator Annotation Review — CrackToss_12

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_12`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | RG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR1 | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | DT1 | defense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | DT1 | defense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | C | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 47 |
| ⚠️ START CHANGED | `Action_BallSnap` | RG | `6` | `5` | 48 | START | 50 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR1 | `5` | `4` | 51 | START | 51 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | `3` | `2` | 51 | START | 51 | 71 |
| ✅ EXACT | `Action_SnapReceive` | DT1 | `8` | `7` | 51 | END | 48 | 51 |
| ✅ EXACT | `Action_Toss` | DT1 | `8` | `7` | 58 | START | 58 | 81 |
| ✅ EXACT | `Action_BallCarry` | C | `2` | `1` | 82 | START | 82 | 159 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 142 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_CrackBlock` | 51 | 75 | 25 | inferred_complete_timeline |
| `Action_CrackBlock` | 77 | 142 | 66 | inferred_complete_timeline |
| `Action_None` | 143 | 186 | 44 | inferred_complete_timeline |
| `Action_None` | 189 | 210 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PullBlock` | 51 | 71 | 21 | inferred_complete_timeline |
| `Action_PullBlock` | 73 | 87 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 83 | 36 | inferred_complete_timeline |
| `Action_None` | 90 | 111 | 22 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_BallCarry` | 82 | 159 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_BallSnap` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_None` | 52 | 210 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 47 | 4 | inferred_complete_timeline |
| `Action_None` | 48 | 117 | 70 | inferred_complete_timeline |
| `Action_None` | 139 | 186 | 48 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 70 | 23 | inferred_complete_timeline |
| `Action_None` | 75 | 88 | 14 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 97 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SnapReceive` | 48 | 51 | 4 | inferred_complete_timeline |
| `Action_None` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_None` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_Toss` | 58 | 81 | 24 | inferred_complete_timeline |
| `Action_None` | 82 | 121 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 104 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 121 | 74 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 183 | 186 | 4 | inferred_complete_timeline |
| `Action_None` | 189 | 208 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–17
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 75 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–100 | 101 | 2 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–107 | 108 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–168 | 167 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–104 | 105 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–210 | 166 | 5 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 11–30 | 20 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 20–203 | 129 | 5 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 34–53 | 19 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 45–92 | 48 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 58–210 | 140 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 67–111 | 38 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 75–113 | 27 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 100–119 | 20 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 108–210 | 103 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 128–164 | 37 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 137–210 | 73 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 144–210 | 67 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 147–210 | 13 | 3 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 162–210 | 49 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 170–210 | 41 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 203–210 | 8 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `6` (RG): Annotated start 48 != Inferred start 50
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 25: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 26: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ Row 26: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [48-75] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [82-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [51-71] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [73-87] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-104] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [51-75] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-186] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-70] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-88] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-117] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-186] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-100] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-208] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-104] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-83] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-111] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-10] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-58] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-30] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-28] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-44] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-171] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-203] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-83] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-71] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-105] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-79] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-113] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-119] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-164] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-207] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>