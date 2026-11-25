# Play-Annotation-Generator Annotation Review — InsideZoneRead_316

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_316`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 125
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `27` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | LB1 | defense | `6` | `5` |
| ✅ EXACT | `Action_ReadDefender` | LB1 | defense | `6` | `5` |
| ✅ EXACT | `Action_Keep` | LB1 | defense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB1 | defense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 13 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `12` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `13` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `14` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 13 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `8` | `Group` | 0 | START | 13 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 13 | 20 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `27` | `21` | 18 | START | 121 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `11` | 21 | START | 25 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `14` | `13` | 21 | START | 58 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `4` | 21 | START | 21 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `9` | `8` | 21 | START | 21 | 78 |
| ✅ EXACT | `Action_SnapReceive` | LB1 | `6` | `5` | 33 | END | 18 | 33 |
| ✅ EXACT | `Action_ReadDefender` | LB1 | `6` | `5` | 38 | START | 38 | 46 |
| ✅ EXACT | `Action_Keep` | LB1 | `6` | `5` | 47 | START | 47 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB1 | `6` | `5` | 67 | START | 67 | 135 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 102 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 13–208
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 17 | 5 | inferred_complete_timeline |
| `Action_None` | 18 | 94 | 77 | inferred_complete_timeline |
| `Action_None` | 99 | 108 | 10 | inferred_complete_timeline |
| `Action_None` | 128 | 208 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 13–184
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 17 | 5 | inferred_complete_timeline |
| `Action_None` | 18 | 150 | 133 | inferred_complete_timeline |
| `Action_None` | 163 | 169 | 7 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 25–104
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_None` | 33 | 55 | 23 | inferred_complete_timeline |
| `Action_None` | 57 | 90 | 34 | inferred_complete_timeline |
| `Action_None` | 93 | 104 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 13–248
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 20 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 65 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 102 | 11 | inferred_complete_timeline |
| `Action_None` | 103 | 143 | 41 | inferred_complete_timeline |
| `Action_None` | 151 | 187 | 37 | inferred_complete_timeline |
| `Action_None` | 197 | 198 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 202 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 248 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 13–124
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 20 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 78 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 102 | 8 | inferred_complete_timeline |
| `Action_None` | 103 | 124 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 25–166
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 25 | 54 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 102 | 46 | inferred_complete_timeline |
| `Action_None` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_None` | 105 | 116 | 12 | inferred_complete_timeline |
| `Action_None` | 123 | 166 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 58–143
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 58 | 82 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 102 | 12 | inferred_complete_timeline |
| `Action_None` | 103 | 143 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 13–267
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 17 | 5 | inferred_complete_timeline |
| `Action_None` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_None` | 104 | 111 | 8 | inferred_complete_timeline |
| `Action_None` | 136 | 185 | 50 | inferred_complete_timeline |
| `Action_None` | 187 | 200 | 14 | inferred_complete_timeline |
| `Action_None` | 202 | 240 | 39 | inferred_complete_timeline |
| `Action_None` | 244 | 267 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 13–133
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 17 | 5 | inferred_complete_timeline |
| `Action_None` | 18 | 91 | 74 | inferred_complete_timeline |
| `Action_None` | 101 | 111 | 11 | inferred_complete_timeline |
| `Action_None` | 127 | 133 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 13–157
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 17 | 5 | inferred_complete_timeline |
| `Action_None` | 18 | 87 | 70 | inferred_complete_timeline |
| `Action_None` | 89 | 100 | 12 | inferred_complete_timeline |
| `Action_None` | 103 | 111 | 9 | inferred_complete_timeline |
| `Action_None` | 114 | 157 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 13–98
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 17 | 5 | inferred_complete_timeline |
| `Action_None` | 18 | 98 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 13–269
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 17 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 18 | 33 | 16 | inferred_complete_timeline |
| `Action_None` | 34 | 37 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 38 | 46 | 9 | inferred_complete_timeline |
| `Action_Keep` | 47 | 66 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 67 | 135 | 69 | inferred_complete_timeline |
| `Action_BallCarry` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 147 | 154 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 162 | 251 | 90 | inferred_complete_timeline |
| `Action_BallCarry` | 259 | 269 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 13–269
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 17 | 5 | inferred_complete_timeline |
| `Action_None` | 18 | 167 | 150 | inferred_complete_timeline |
| `Action_None` | 171 | 213 | 43 | inferred_complete_timeline |
| `Action_None` | 216 | 230 | 15 | inferred_complete_timeline |
| `Action_None` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_None` | 246 | 269 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 13–269 | 244 | 5 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 69–257 | 168 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 90–125 | 22 | 3 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 95–189 | 95 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 103–269 | 166 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 113–116 | 4 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 116–132 | 17 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 119–269 | 147 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 121–179 | 53 | 3 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 131–232 | 102 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 143–244 | 99 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 156–264 | 91 | 3 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 165–167 | 3 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 173–269 | 94 | 3 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 178–269 | 92 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 185–269 | 85 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 205–269 | 65 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 210–221 | 12 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 222–225 | 4 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 227–269 | 43 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 236–269 | 34 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 253–268 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `27` (Position_Unknown): Annotated start 18 != Inferred start 121
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (5 segments found)

### Track Identity Issues

- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '21' has invalid range: start=121, end=33. Clamping end to start.
- ⚠️ Action 'Action_None' range [18-91] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-111] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-133] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-125] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-203] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-88] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-111] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-185] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-200] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-240] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-267] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-167] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-213] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-230] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-65] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-143] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-187] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-248] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [67-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [137-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [147-154] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [162-251] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-150] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-78] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-124] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-94] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-208] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-87] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-111] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-157] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-54] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 103, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [103-103] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-166] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-26] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-90] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-104] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-257] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-116] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-189] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-124] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-132] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-169] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-232] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-236] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-244] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-188] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-235] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-264] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-242] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-269] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-221] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-269] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-269] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-268] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_316'; source metadata written as null.

</details>