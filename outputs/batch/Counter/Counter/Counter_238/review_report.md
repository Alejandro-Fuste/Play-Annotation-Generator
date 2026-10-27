# Play-Annotation-Generator Annotation Review — Counter_238

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_238`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 99
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
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `14` | `13` |
| ✅ EXACT | `Action_PullLeadBlock` | CB | defense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 116 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 117 | START | 117 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `11` | `10` | 118 | START | 118 | 148 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `13` | `12` | 118 | START | 131 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `15` | `14` | 118 | START | 118 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `14` | `13` | 118 | START | 118 | 134 |
| ✅ EXACT | `Action_PullLeadBlock` | CB | `4` | `3` | 118 | START | 118 | 134 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 130 | END | 117 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `8` | `7` | 139 | START | 139 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `6` | 164 | START | 164 | 166 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 195 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–168
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_SnapReceive` | 117 | 130 | 14 | inferred_complete_timeline |
| `Action_None` | 131 | 138 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 139 | 147 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 163 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 168 | 223 | 56 | inferred_complete_timeline |
| `Action_BallCarry` | 231 | 237 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_DownBlock` | 118 | 148 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 155 | 167 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 195 | 22 | inferred_complete_timeline |
| `Action_None` | 196 | 238 | 43 | inferred_complete_timeline |
| `Action_None` | 240 | 269 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 117 | 79 | inferred_complete_timeline |
| `Action_DownBlock` | 118 | 151 | 34 | inferred_complete_timeline |
| `Action_DownBlock` | 153 | 157 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_BallSnap` | 117 | 130 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 131 | 173 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_PullBlock` | 118 | 134 | 17 | inferred_complete_timeline |
| `Action_PullBlock` | 151 | 195 | 45 | inferred_complete_timeline |
| `Action_None` | 196 | 215 | 20 | inferred_complete_timeline |
| `Action_None` | 221 | 223 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 196 | 80 | inferred_complete_timeline |
| `Action_None` | 224 | 252 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 174 | 58 | inferred_complete_timeline |
| `Action_None` | 176 | 179 | 4 | inferred_complete_timeline |
| `Action_None` | 216 | 269 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 216 | 100 | inferred_complete_timeline |
| `Action_None` | 225 | 263 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 161 | 45 | inferred_complete_timeline |
| `Action_None` | 167 | 203 | 37 | inferred_complete_timeline |
| `Action_None` | 209 | 245 | 37 | inferred_complete_timeline |
| `Action_None` | 249 | 269 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 234 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 157 | 41 | inferred_complete_timeline |
| `Action_None` | 187 | 267 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 118 | 134 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 160 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–151 | 152 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 146–151 | 6 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 146–212 | 57 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 151–269 | 69 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 158–269 | 106 | 4 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 173–269 | 77 | 5 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 180–269 | 86 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 182–269 | 88 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 183–269 | 74 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 188–269 | 79 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 193–260 | 63 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 216–248 | 33 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 237–269 | 13 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 238–269 | 32 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 246–269 | 24 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 252–269 | 18 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (3 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `13` (C): Annotated start 118 != Inferred start 131
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 478: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ Row 478: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [117–130], lower_priority='Action_DownBlock' annotated_start=118, effective_Action_DownBlock_start=131.
- ⚠️ Action 'Action_None' range [117-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-157] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-267] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-216] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-263] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [118-134] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-151] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-147] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [164-166] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [168-223] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [231-237] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [139-147] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [152-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [158-161] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-234] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-203] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-245] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [118-148] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [155-167] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-238] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-196] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-252] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [131-173] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [118-134] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [151-195] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-215] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-117] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [118-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [153-157] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-212] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-185] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-217] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-215] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-219] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-198] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-216] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-250] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-248] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-242] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-261] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>