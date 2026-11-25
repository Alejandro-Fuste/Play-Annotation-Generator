# Play-Annotation-Generator Annotation Review — InsideZoneRead_155

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_155`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 3
- **Action Segments:** 81
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `15` | N/A |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `24` | `21` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `15` | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 10 | START | 5 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 10 | START | 23 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 10 | START | 48 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 10 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 10 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 10 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 10 | START | 0 | 97 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `16` | 105 | START | 105 | 120 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `14` | `13` | 108 | START | 108 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `16` | 108 | START | 121 | 124 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `17` | 108 | START | 108 | 154 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 108 | START | 108 | 186 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 108 | START | 108 | 136 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `15` | N/A | 120 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | Position_Unknown | `24` | `21` | 144 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `15` | N/A | 150 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 200 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 104 | 6 | inferred_complete_timeline |
| `Action_None` | 105 | 127 | 23 | inferred_complete_timeline |
| `Action_None` | 129 | 162 | 34 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 104 | 8 | inferred_complete_timeline |
| `Action_None` | 105 | 111 | 7 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 124 | 176 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 186 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 48–154
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 48 | 86 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 154 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 23–143
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 104 | 82 | inferred_complete_timeline |
| `Action_BallSnap` | 105 | 120 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 124 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 133 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 143 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 5–145
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 10 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 25 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 107 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 145 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 136 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 104 | 69 | inferred_complete_timeline |
| `Action_None` | 105 | 172 | 68 | inferred_complete_timeline |
| `Action_None` | 175 | 179 | 5 | inferred_complete_timeline |
| `Action_None` | 181 | 259 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 104 | 83 | inferred_complete_timeline |
| `Action_None` | 105 | 122 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 140 | 36 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 219 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 104 | 44 | inferred_complete_timeline |
| `Action_None` | 105 | 150 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 4–269
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 69 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 104 | 20 | inferred_complete_timeline |
| `Action_None` | 105 | 181 | 77 | inferred_complete_timeline |
| `Action_None` | 185 | 188 | 4 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_None` | 196 | 269 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 104 | 36 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–12 | 13 | 1 | Undefined position; Undefined team |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–36 | 34 | 2 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–50 | 51 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 92–267 | 174 | 4 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 93–193 | 100 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 99–118 | 20 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 109–125 | 17 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 117–157 | 29 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 127–137 | 11 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 154–269 | 116 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 157–269 | 104 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 167–261 | 95 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 201–206 | 5 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 213–269 | 57 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 224–261 | 38 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 228–232 | 5 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 239–269 | 31 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | 12 | 20 | 2 | 22.2% | 13–19 |
| `15` | `17` | 17 | 19 | 3 | 100.0% | None |
| `18` | `21` | 55 | 63 | 9 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `15` (Position_Unknown)
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `21` (Position_Unknown)
- ❌ Missing segment for action `Action_BallCarry` on target `15` (Position_Unknown)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [105–120], lower_priority='Action_ZoneBlock' annotated_start=108, effective_Action_ZoneBlock_start=121.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-36] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-186] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-172] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-259] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-122] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-97] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-127] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-162] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 105, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [105-107] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-219] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-69] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-181] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-10] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-25] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [126-133] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-86] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-154] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-117] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-264] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-193] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-118] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-125] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-157] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-137] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-261] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-261] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_155'; source metadata written as null.

</details>