# Play-Annotation-Generator Annotation Review — JetSweep_182

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_182`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 115
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `15` | `14` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | Team_Unknown | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 57 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `15` | `14` | 56 | START | 66 | 66 |
| ✅ EXACT | `Action_LeadBlock` | RB | `8` | `7` | 58 | START | 58 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `1` | `0` | 58 | START | 58 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `9` | 58 | START | 58 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `13` | `12` | 58 | START | 61 | 64 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 58 | START | 58 | 99 |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | `14` | `13` | 62 | START | 63 | 85 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 65 | END | 56 | 65 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 85 | START | 85 | 85 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `14` | `13` | 86 | START | 86 | 136 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 112 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_SnapReceive` | 56 | 65 | 10 | inferred_complete_timeline |
| `Action_None` | 66 | 84 | 19 | inferred_complete_timeline |
| `Action_Toss` | 85 | 85 | 1 | inferred_complete_timeline |
| `Action_None` | 86 | 190 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_LeadBlock` | 58 | 96 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 99 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 81 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 112 | 18 | inferred_complete_timeline |
| `Action_None` | 113 | 196 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 86 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 112 | 21 | inferred_complete_timeline |
| `Action_None` | 113 | 210 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 14 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 55 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 64 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 112 | 42 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 59 | 70 | 12 | inferred_complete_timeline |
| `Action_None` | 72 | 96 | 25 | inferred_complete_timeline |
| `Action_None` | 98 | 210 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 67 | 98 | 32 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 67 | 12 | inferred_complete_timeline |
| `Action_None` | 87 | 91 | 5 | inferred_complete_timeline |
| `Action_None` | 98 | 141 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 90 | 35 | inferred_complete_timeline |
| `Action_None` | 145 | 149 | 5 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 129 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 205 | 150 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–105 | 102 | 3 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 63–136 | 74 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 66–210 | 122 | 7 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 113–168 | 56 | 1 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 119–197 | 79 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 133–207 | 69 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 134–190 | 57 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 141–210 | 70 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 143–153 | 10 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 145–210 | 66 | 1 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 154–192 | 37 | 2 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 154–210 | 44 | 3 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 157–199 | 43 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 160–209 | 41 | 3 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 160–210 | 51 | 1 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 164–196 | 33 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 164–192 | 25 | 2 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 174–207 | 34 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 175–189 | 14 | 2 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 176–210 | 30 | 4 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `15` (Position_Unknown): Annotated start 56 != Inferred start 66
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ `Action_JetMotion` for actor_track_id `14` (Position_Unknown): Annotated start 62 != Inferred start 63

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 365: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '14' has invalid range: start=66, end=65. Clamping end to start.
- ⚠️ Action 'Action_ZoneBlock' range [58-86] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-99] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-205] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-99] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-190] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [58-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-67] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-141] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-196] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-96] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-14] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-55] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [86-136] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-183] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-207] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-178] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-199] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-185] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-209] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-196] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-185] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-207] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-189] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-184] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-196] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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