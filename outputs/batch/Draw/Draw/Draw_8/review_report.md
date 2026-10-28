# Play-Annotation-Generator Annotation Review — Draw_8

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_8`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 60
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `6` | `5` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 43 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 41 | START | 41 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `4` | `3` | 44 | START | 44 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `5` | `4` | 44 | START | 44 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `6` | `5` | 44 | START | 44 | 111 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `7` | `6` | 44 | START | 54 | 111 |
| ✅ EXACT | `Action_PassBlock` | RG | `9` | `8` | 44 | START | 44 | 111 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 53 | END | 41 | 53 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `11` | `10` | 61 | START | 61 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `11` | `10` | 81 | START | 81 | 303 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 111 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 53 | 13 | inferred_complete_timeline |
| `Action_None` | 54 | 60 | 7 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 61 | 80 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 81 | 303 | 223 | inferred_complete_timeline |
| `Action_BallCarry` | 305 | 307 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 321 | 322 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 324 | 325 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 329 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 131 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 111 | 68 | inferred_complete_timeline |
| `Action_None` | 112 | 228 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 93 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_BallSnap` | 41 | 53 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 111 | 58 | inferred_complete_timeline |
| `Action_None` | 112 | 329 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 111 | 68 | inferred_complete_timeline |
| `Action_None` | 112 | 159 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 111 | 68 | inferred_complete_timeline |
| `Action_None` | 112 | 142 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 86 | 46 | inferred_complete_timeline |
| `Action_None` | 94 | 158 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 135 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 251 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 44 | 4 | inferred_complete_timeline |
| `Action_None` | 46 | 178 | 133 | inferred_complete_timeline |
| `Action_None` | 183 | 198 | 16 | inferred_complete_timeline |
| `Action_None` | 200 | 228 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 250 | 210 | inferred_complete_timeline |
| `Action_None` | 256 | 263 | 8 | inferred_complete_timeline |
| `Action_None` | 266 | 290 | 25 | inferred_complete_timeline |
| `Action_None` | 294 | 308 | 15 | inferred_complete_timeline |
| `Action_None` | 311 | 329 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 119 | 79 | inferred_complete_timeline |
| `Action_None` | 122 | 329 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 90 | 50 | inferred_complete_timeline |
| `Action_None` | 92 | 137 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 83–329 | 247 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 89–259 | 156 | 5 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 138–148 | 11 | 1 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 138–139 | 2 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 150–329 | 180 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 153–329 | 177 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 163–329 | 161 | 3 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 183–329 | 130 | 4 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 201–329 | 129 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `7` (C): Annotated start 44 != Inferred start 54
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [41–53], lower_priority='Action_PassBlock' annotated_start=44, effective_Action_PassBlock_start=54.
- ⚠️ Action 'Action_None' range [41-90] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-137] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-131] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-329] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-228] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-93] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-142] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-250] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-263] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-290] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-308] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-119] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [81-303] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [305-307] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [321-322] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [324-325] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-86] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-178] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-228] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-249] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-259] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-148] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-252] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-301] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-259] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-285] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '22' has 1 frames without a visible bounding box.
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

</details>