# Play-Annotation-Generator Annotation Review — RPO_166

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_166`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 136
- **Validation Warnings:** 152
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantGoRoute` | actor_track_id `22` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 121
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | offense | `3` | `3` |
| ✅ EXACT | `Action_PullBall` | RB | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 80 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `0` | `0` | 82 | START | 82 | 166 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `1` | `1` | 82 | START | 82 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `4` | 82 | START | 82 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `6` | `6` | 82 | START | 82 | 87 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `8` | 82 | START | 82 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | `3` | `3` | 89 | START | 89 | 113 |
| ✅ EXACT | `Action_PullBall` | RB | `12` | `12` | 104 | START | 104 | 120 |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | `17` | `17` | 159 | START | 161 | 166 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 88 | 8 | inferred_complete_timeline |
| `Action_ReadDefender` | 89 | 113 | 25 | inferred_complete_timeline |
| `Action_ReadDefender` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 155 | 158 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 103 | 23 | inferred_complete_timeline |
| `Action_PullBall` | 104 | 120 | 17 | inferred_complete_timeline |
| `Action_None` | 121 | 142 | 22 | inferred_complete_timeline |
| `Action_None` | 144 | 154 | 11 | inferred_complete_timeline |
| `Action_None` | 158 | 161 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 81 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 134 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 166 | 30 | inferred_complete_timeline |
| `Action_None` | 167 | 329 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 81 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 166 | 85 | inferred_complete_timeline |
| `Action_None` | 167 | 195 | 29 | inferred_complete_timeline |
| `Action_None` | 210 | 329 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 81 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 103 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 81 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 166 | 85 | inferred_complete_timeline |
| `Action_None` | 167 | 183 | 17 | inferred_complete_timeline |
| `Action_None` | 186 | 318 | 133 | inferred_complete_timeline |
| `Action_None` | 324 | 329 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 81 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 166 | 85 | inferred_complete_timeline |
| `Action_None` | 167 | 231 | 65 | inferred_complete_timeline |
| `Action_None` | 233 | 236 | 4 | inferred_complete_timeline |
| `Action_None` | 238 | 240 | 3 | inferred_complete_timeline |
| `Action_None` | 242 | 320 | 79 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 131 | 51 | inferred_complete_timeline |
| `Action_None` | 139 | 194 | 56 | inferred_complete_timeline |
| `Action_None` | 200 | 326 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 196 | 116 | inferred_complete_timeline |
| `Action_None` | 201 | 269 | 69 | inferred_complete_timeline |
| `Action_None` | 271 | 329 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 95 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 173 | 93 | inferred_complete_timeline |
| `Action_None` | 175 | 178 | 4 | inferred_complete_timeline |
| `Action_None` | 180 | 189 | 10 | inferred_complete_timeline |
| `Action_None` | 195 | 202 | 8 | inferred_complete_timeline |
| `Action_None` | 204 | 242 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 130 | 50 | inferred_complete_timeline |
| `Action_None` | 133 | 152 | 20 | inferred_complete_timeline |
| `Action_None` | 154 | 230 | 77 | inferred_complete_timeline |
| `Action_None` | 232 | 307 | 76 | inferred_complete_timeline |
| `Action_None` | 314 | 329 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 43–329 | 262 | 7 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 107–329 | 207 | 6 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 107–117 | 11 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 123–156 | 34 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 126–210 | 34 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 132–329 | 183 | 6 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 138–306 | 164 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 159–329 | 171 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 174–177 | 4 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 191–329 | 137 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 193–318 | 82 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 195–309 | 115 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 198–329 | 130 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 213–329 | 116 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 217–329 | 101 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 223–323 | 96 | 4 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 237–263 | 13 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 237–318 | 58 | 7 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 245–272 | 6 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 246–293 | 45 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 264–329 | 59 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 269–312 | 44 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 295–310 | 13 | 3 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 307–329 | 19 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `3` (3 segments found)
- ⚠️ `Action_ThrowPass` for actor_track_id `17` (Position_Unknown): Annotated start 159 != Inferred start 161

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 103 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [167-231] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-320] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-195] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [89-113] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [141-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [155-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-329] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-196] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-269] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-87] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-130] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-307] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-183] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-318] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-173] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-189] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-202] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-242] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-131] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-326] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-154] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-59] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-73] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-113] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-237] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-329] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-135] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-284] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-291] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-308] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-324] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-117] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-156] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-266] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-283] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-269] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-306] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-277] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-201] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-318] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-309] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-241] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-329] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-316] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-329] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-243] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-281] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-319] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-246] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-254] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-268] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-284] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-304] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-288] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-317] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-312] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-304] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-310] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-317] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-327] for track '36' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>