# Play-Annotation-Generator Annotation Review — CrackToss_47

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_47`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 101
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | DT1 | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | TE1 | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_Toss` | QB | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | defense | `11` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 137 |
| ✅ EXACT | `Action_BallSnap` | RG | `20` | `19` | 138 | START | 138 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | DT1 | `15` | `14` | 141 | START | 141 | 258 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | TE1 | `17` | `16` | 141 | START | 141 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | `21` | `20` | 141 | START | 141 | 178 |
| ✅ EXACT | `Action_SnapReceive` | QB | `22` | `21` | 142 | END | 138 | 142 |
| ✅ EXACT | `Action_Toss` | QB | `22` | `21` | 159 | START | 159 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | `11` | `10` | 172 | START | 172 | 239 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 137 | 132 | inferred_complete_timeline |
| `Action_SnapReceive` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 143 | 158 | 16 | inferred_complete_timeline |
| `Action_Toss` | 159 | 171 | 13 | inferred_complete_timeline |
| `Action_None` | 172 | 250 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 195 | 58 | inferred_complete_timeline |
| `Action_None` | 199 | 250 | 52 | inferred_complete_timeline |
| `Action_None` | 252 | 254 | 3 | inferred_complete_timeline |
| `Action_None` | 256 | 260 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 229 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_PullBlock` | 141 | 178 | 38 | inferred_complete_timeline |
| `Action_PullBlock` | 181 | 253 | 73 | inferred_complete_timeline |
| `Action_PullBlock` | 255 | 258 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–279
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 194 | 57 | inferred_complete_timeline |
| `Action_None` | 196 | 253 | 58 | inferred_complete_timeline |
| `Action_None` | 265 | 269 | 5 | inferred_complete_timeline |
| `Action_None` | 275 | 279 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 179 | 42 | inferred_complete_timeline |
| `Action_None` | 181 | 194 | 14 | inferred_complete_timeline |
| `Action_None` | 197 | 266 | 70 | inferred_complete_timeline |
| `Action_None` | 269 | 277 | 9 | inferred_complete_timeline |
| `Action_None` | 284 | 285 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 299 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 21 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 137 | 108 | inferred_complete_timeline |
| `Action_BallSnap` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 143 | 178 | 36 | inferred_complete_timeline |
| `Action_None` | 181 | 299 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 140 | 138 | inferred_complete_timeline |
| `Action_PullBlock` | 141 | 178 | 38 | inferred_complete_timeline |
| `Action_PullBlock` | 181 | 255 | 75 | inferred_complete_timeline |
| `Action_PullBlock` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 267 | 268 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 270 | 296 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_BallCarry` | 172 | 239 | 68 | inferred_complete_timeline |
| `Action_BallCarry` | 257 | 263 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 178 | 41 | inferred_complete_timeline |
| `Action_None` | 181 | 186 | 6 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 268 | 70 | inferred_complete_timeline |
| `Action_None` | 270 | 293 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_CrackBlock` | 141 | 258 | 118 | inferred_complete_timeline |
| `Action_CrackBlock` | 260 | 299 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 178 | 41 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 187 | 196 | 10 | inferred_complete_timeline |
| `Action_None` | 203 | 299 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 261 | 124 | inferred_complete_timeline |
| `Action_None` | 263 | 299 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 175 | 38 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_None` | 187 | 194 | 8 | inferred_complete_timeline |
| `Action_None` | 197 | 221 | 25 | inferred_complete_timeline |
| `Action_None` | 223 | 299 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 260 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 275 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 264 | 127 | inferred_complete_timeline |
| `Action_None` | 275 | 286 | 12 | inferred_complete_timeline |
| `Action_None` | 291 | 299 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–265 | 255 | 4 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–290 | 291 | 2 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–299 | 295 | 5 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–286 | 278 | 6 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–163 | 162 | 3 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 211–256 | 23 | 4 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 212–272 | 60 | 2 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 255–261 | 7 | 1 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 269–271 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 200 targets track ID '227', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 96: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 96: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 96: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '16' (TE1) duration 118 frames exceeds threshold 90 frames [start=141, end=258].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '20' (RT) duration 156 frames exceeds threshold 90 frames [start=141, end=296].
- ⚠️ Action 'Action_None' range [138-195] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-250] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-229] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-194] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-253] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-279] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-275] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-260] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-261] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-247] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-290] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-179] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-253] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-264] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-286] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-239] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [257-263] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-196] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-194] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-221] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-178] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-286] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [141-258] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [141-178] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [181-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [255-258] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-179] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-194] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-266] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-277] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-178] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-268] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-293] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-21] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-178] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [141-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [181-255] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [263-264] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [267-268] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [270-296] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-137] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-250] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-218] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-256] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-228] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-272] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-261] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>