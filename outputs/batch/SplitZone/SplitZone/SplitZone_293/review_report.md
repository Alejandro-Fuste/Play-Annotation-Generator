# Play-Annotation-Generator Annotation Review — SplitZone_293

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `SplitZone_293`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 121
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadEdgeDefender` | QB | offense | `9` | `9` |
| ⚠️ START CHANGED | `Action_PressEdge` | RB | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 11 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `12` | `Group` | 0 | START | 17 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 27 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `13` | `13` | 107 | START | 109 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `12` | `12` | 114 | START | 114 | 117 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `10` | 120 | START | 120 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `11` | `11` | 120 | START | 120 | 124 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `5` | 120 | START | 120 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `9` | `9` | 121 | END | 113 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadEdgeDefender` | QB | `9` | `9` | 128 | START | 128 | 133 |
| ⚠️ START CHANGED | `Action_PressEdge` | RB | `7` | `7` | 130 | START | 155 | 161 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 136 | START | 136 | 137 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `18` | `17` | 150 | START | 150 | 329 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | `14` | `14` | 155 | START | 155 | 306 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | `8` | `8` | 155 | START | 155 | 159 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 51 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 60 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 72 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 89 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 106 | 12 | inferred_complete_timeline |
| `Action_SnapReceive` | 113 | 117 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 128 | 133 | 6 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 135 | 135 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–321
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 47 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 72 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 88 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 101 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 129 | 15 | inferred_complete_timeline |
| `Action_PressEdge` | 155 | 161 | 7 | inferred_complete_timeline |
| `Action_None` | 163 | 321 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 17–324
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 45 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 65 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 113 | 45 | inferred_complete_timeline |
| `Action_SplitBlock` | 114 | 117 | 4 | inferred_complete_timeline |
| `Action_SplitBlock` | 122 | 163 | 42 | inferred_complete_timeline |
| `Action_None` | 164 | 324 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 11–149
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 23 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 51 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 119 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 124 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 149 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 50 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 111 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 119 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 122 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 126 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 131 | 25 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_None` | 137 | 146 | 10 | inferred_complete_timeline |
| `Action_None` | 149 | 173 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 205 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 129 | 23 | inferred_complete_timeline |
| `Action_None` | 131 | 135 | 5 | inferred_complete_timeline |
| `Action_None` | 137 | 143 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 297 | 191 | inferred_complete_timeline |
| `Action_None` | 306 | 329 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 185 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 141 | 35 | inferred_complete_timeline |
| `Action_None` | 143 | 329 | 187 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–329 | 316 | 5 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 109–164 | 6 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 121–329 | 201 | 5 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 130–329 | 200 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 146–329 | 178 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 150–329 | 180 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 150–329 | 176 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 154–329 | 165 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 170–187 | 18 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 179–329 | 147 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 180–328 | 144 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 196–329 | 134 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 197–329 | 132 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 210–329 | 120 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 215–329 | 115 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 215–323 | 108 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 220–329 | 110 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 240–329 | 90 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 259–282 | 23 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 272–329 | 58 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 276–329 | 54 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 301–302 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `13` (Position_Unknown): Annotated start 107 != Inferred start 109
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ReadEdgeDefender` and target `9` (2 segments found)
- ⚠️ `Action_PressEdge` for actor_track_id `7` (RB): Annotated start 130 != Inferred start 155
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_BlockSecondLevel' at frame 155 targets track ID '164', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 588: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '8' (Unknown) duration 175 frames exceeds threshold 90 frames [start=155, end=329].
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '14' (Unknown) duration 175 frames exceeds threshold 90 frames [start=155, end=329].
- ⚠️ Action 'Action_None' range [107-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-205] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-185] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-131] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-146] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-173] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-126] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-47] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-50] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-72] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-88] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-111] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [155-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-321] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-135] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [155-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-51] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-60] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-72] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-89] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [113-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [119-120] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [128-133] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [136-137] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-50] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-111] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-19] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-51] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-124] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-149] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-45] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-65] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [114-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-324] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [109-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-146] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [155-306] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-163] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-161] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-328] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-321] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-312] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-323] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-279] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>