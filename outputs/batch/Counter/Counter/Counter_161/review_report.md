# Play-Annotation-Generator Annotation Review — Counter_161

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_161`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | SAF | defense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF | defense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | SAF | defense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | SAF | defense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 106 |
| ✅ EXACT | `Action_BallSnap` | SAF | `16` | `15` | 107 | START | 107 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF | `16` | `15` | 112 | START | 112 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `20` | `19` | 112 | START | 112 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `14` | `13` | 112 | START | 112 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LG | `11` | `10` | 112 | START | 112 | 153 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RG | `7` | `6` | 114 | START | 114 | 163 |
| ✅ EXACT | `Action_SnapReceive` | SAF | `8` | `7` | 122 | END | 107 | 122 |
| ✅ EXACT | `Action_Handoff` | SAF | `8` | `7` | 142 | START | 142 | 163 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | `7` | `6` | 164 | START | 164 | 167 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 205 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 130 | 24 | inferred_complete_timeline |
| `Action_None` | 134 | 148 | 15 | inferred_complete_timeline |
| `Action_None` | 154 | 158 | 5 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 329 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 194 | 88 | inferred_complete_timeline |
| `Action_None` | 196 | 329 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 247 | 141 | inferred_complete_timeline |
| `Action_None` | 249 | 329 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 112 | 153 | 42 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 183 | 190 | 8 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 192 | 205 | 14 | inferred_complete_timeline |
| `Action_None` | 206 | 233 | 28 | inferred_complete_timeline |
| `Action_None` | 236 | 249 | 14 | inferred_complete_timeline |
| `Action_None` | 251 | 329 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–306
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 114 | 163 | 50 | inferred_complete_timeline |
| `Action_BallCarry` | 164 | 167 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 190 | 204 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 206 | 297 | 92 | inferred_complete_timeline |
| `Action_BallCarry` | 299 | 302 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 305 | 306 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 143 | 37 | inferred_complete_timeline |
| `Action_None` | 146 | 150 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 329 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 329 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 162 | 56 | inferred_complete_timeline |
| `Action_None` | 169 | 236 | 68 | inferred_complete_timeline |
| `Action_None` | 238 | 329 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 277 | 171 | inferred_complete_timeline |
| `Action_None` | 280 | 328 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 325 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 329 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 158 | 52 | inferred_complete_timeline |
| `Action_None` | 163 | 168 | 6 | inferred_complete_timeline |
| `Action_None` | 174 | 229 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_SnapReceive` | 107 | 122 | 16 | inferred_complete_timeline |
| `Action_None` | 123 | 141 | 19 | inferred_complete_timeline |
| `Action_Handoff` | 142 | 163 | 22 | inferred_complete_timeline |
| `Action_None` | 164 | 329 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_BallSnap` | 107 | 111 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 112 | 128 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 151 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–300 | 295 | 4 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–329 | 292 | 8 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–325 | 320 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–329 | 299 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–128 | 122 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 4–191 | 102 | 10 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 81–155 | 20 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 170–329 | 158 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 177–329 | 153 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 178–329 | 150 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 184–329 | 138 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 213–329 | 117 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 244–329 | 75 | 5 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 263–305 | 7 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 322–323 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `14` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 323: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 324: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 324: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '13' (Unknown) duration 94 frames exceeds threshold 90 frames [start=112, end=205].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (SAF) duration 94 frames exceeds threshold 90 frames [start=112, end=205].
- ⚠️ Action 'Action_None' range [107-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-300] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-325] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-277] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-328] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-247] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [164-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [177-178] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [190-204] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [206-297] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [299-302] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [305-306] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [142-163] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-143] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-194] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [112-153] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [183-190] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-233] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-249] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-329] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-229] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-130] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-148] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [112-132] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [134-135] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [142-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [146-150] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [177-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-162] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-236] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-329] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [112-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [134-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [139-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [154-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [157-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-329] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-164] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-311] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-325] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-140] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [112-118] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [126-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-9] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-51] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-191] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-104] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-321] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-205] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-268] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-287] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-295] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-305] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>