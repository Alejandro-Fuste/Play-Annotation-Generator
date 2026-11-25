# Play-Annotation-Generator Annotation Review — InsideZoneRead_358

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_358`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | RB | offense | `9` | `8` |
| ✅ EXACT | `Action_Keep` | RB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `11` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 16 |
| ✅ EXACT | `Action_BallSnap` | RT | `14` | `13` | 17 | START | 17 | 19 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `10` | `9` | 20 | START | 20 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `11` | 20 | START | 20 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `12` | 20 | START | 20 | 104 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `13` | 20 | START | 20 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `4` | 20 | START | 20 | 45 |
| ✅ EXACT | `Action_SnapReceive` | RB | `9` | `8` | 30 | END | 17 | 30 |
| ✅ EXACT | `Action_ReadDefender` | RB | `9` | `8` | 35 | START | 35 | 42 |
| ✅ EXACT | `Action_Keep` | RB | `9` | `8` | 43 | START | 43 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `8` | 62 | START | 63 | 68 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 104 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 62 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 30 | 14 | inferred_complete_timeline |
| `Action_None` | 31 | 34 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 35 | 42 | 8 | inferred_complete_timeline |
| `Action_Keep` | 43 | 61 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 63 | 68 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 117 | 48 | inferred_complete_timeline |
| `Action_BallCarry` | 124 | 210 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 42 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 104 | 55 | inferred_complete_timeline |
| `Action_None` | 105 | 153 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 90 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 104 | 85 | inferred_complete_timeline |
| `Action_None` | 105 | 128 | 24 | inferred_complete_timeline |
| `Action_None` | 132 | 205 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 47 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 77 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 104 | 22 | inferred_complete_timeline |
| `Action_None` | 105 | 165 | 61 | inferred_complete_timeline |
| `Action_None` | 167 | 210 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 19 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 104 | 85 | inferred_complete_timeline |
| `Action_None` | 105 | 125 | 21 | inferred_complete_timeline |
| `Action_None` | 127 | 206 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 69 | 53 | inferred_complete_timeline |
| `Action_None` | 86 | 176 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 61 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 41 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 73 | 57 | inferred_complete_timeline |
| `Action_None` | 78 | 210 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 86 | 70 | inferred_complete_timeline |
| `Action_None` | 92 | 124 | 33 | inferred_complete_timeline |
| `Action_None` | 126 | 143 | 18 | inferred_complete_timeline |
| `Action_None` | 148 | 210 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 147 | 131 | inferred_complete_timeline |
| `Action_None` | 152 | 207 | 56 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `16` | Position_Unknown | Team_Unknown | 8–140 | 81 | 4 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 66–67 | 2 | 1 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 71–161 | 36 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 72–157 | 43 | 6 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 80–85 | 6 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 92–210 | 109 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 99–210 | 112 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 104–164 | 48 | 2 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 108–133 | 18 | 3 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 109–210 | 102 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 121–133 | 13 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 125–210 | 79 | 3 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 127–149 | 22 | 2 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 132–210 | 79 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 138–188 | 51 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 144–147 | 4 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 146–210 | 65 | 1 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 159–210 | 52 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 174–210 | 35 | 2 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 191–210 | 20 | 1 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 195–210 | 16 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 202–210 | 9 | 1 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 70 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [17-86] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-124] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-143] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-147] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-207] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-61] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-69] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-176] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-45] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-153] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-73] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-41] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-62] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [43-61] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [63-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-117] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [124-210] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-90] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-42] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-205] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-109] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-94] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-161] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-85] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-129] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-210] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-136] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-164] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-114] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-133] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-210] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-133] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-170] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-136] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-149] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-188] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '36' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_358'; source metadata written as null.

</details>