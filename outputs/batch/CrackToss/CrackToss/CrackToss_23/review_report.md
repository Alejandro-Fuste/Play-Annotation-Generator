# Play-Annotation-Generator Annotation Review — CrackToss_23

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_23`
- **Frame Range:** 0 to 328 (329 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 328
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_CrackBlock` | WR2 | offense | `3` | `2` |
| ✅ EXACT | `Action_CrackBlock` | CB5 | defense | `8` | `7` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Toss` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `18` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 119 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 80 | START | 80 | 83 |
| ✅ EXACT | `Action_CrackBlock` | WR2 | `3` | `2` | 83 | START | 83 | 199 |
| ✅ EXACT | `Action_CrackBlock` | CB5 | `8` | `7` | 83 | START | 83 | 199 |
| ✅ EXACT | `Action_PullBlock` | LG | `20` | `19` | 83 | START | 83 | 196 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 83 | END | 80 | 83 |
| ✅ EXACT | `Action_Toss` | QB | `15` | `14` | 102 | START | 102 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `4` | 120 | START | 120 | 196 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 199 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_SnapReceive` | 80 | 83 | 4 | inferred_complete_timeline |
| `Action_None` | 84 | 101 | 18 | inferred_complete_timeline |
| `Action_Toss` | 102 | 119 | 18 | inferred_complete_timeline |
| `Action_None` | 120 | 222 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_BallCarry` | 120 | 196 | 77 | inferred_complete_timeline |
| `Action_BallCarry` | 198 | 328 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_CrackBlock` | 83 | 199 | 117 | inferred_complete_timeline |
| `Action_None` | 200 | 328 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 161 | 82 | inferred_complete_timeline |
| `Action_None` | 165 | 296 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 328 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 13 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 149 | 65 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 254 | 92 | inferred_complete_timeline |
| `Action_None` | 256 | 258 | 3 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 24 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 56 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 68 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 79 | 10 | inferred_complete_timeline |
| `Action_PullBlock` | 83 | 196 | 114 | inferred_complete_timeline |
| `Action_None` | 201 | 328 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–311
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_BallSnap` | 80 | 83 | 4 | inferred_complete_timeline |
| `Action_None` | 84 | 311 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 149 | 70 | inferred_complete_timeline |
| `Action_None` | 151 | 263 | 113 | inferred_complete_timeline |
| `Action_None` | 265 | 328 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 85 | 135 | 51 | inferred_complete_timeline |
| `Action_None` | 140 | 328 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 156 | 77 | inferred_complete_timeline |
| `Action_None` | 158 | 183 | 26 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 191 | 196 | 6 | inferred_complete_timeline |
| `Action_None` | 200 | 328 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 162 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 28 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 79 | 41 | inferred_complete_timeline |
| `Action_None` | 80 | 168 | 89 | inferred_complete_timeline |
| `Action_None` | 171 | 328 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 141 | 62 | inferred_complete_timeline |
| `Action_None` | 143 | 149 | 7 | inferred_complete_timeline |
| `Action_None` | 152 | 154 | 3 | inferred_complete_timeline |
| `Action_None` | 159 | 328 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 172 | 93 | inferred_complete_timeline |
| `Action_None` | 178 | 191 | 14 | inferred_complete_timeline |
| `Action_None` | 193 | 328 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 328 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 149 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 168 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 328 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_CrackBlock` | 83 | 199 | 117 | inferred_complete_timeline |
| `Action_None` | 200 | 267 | 68 | inferred_complete_timeline |
| `Action_None` | 273 | 282 | 10 | inferred_complete_timeline |
| `Action_None` | 284 | 328 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–328 | 321 | 6 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 3–328 | 249 | 8 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 172–328 | 157 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 203–206 | 4 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 213–328 | 116 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 262–328 | 67 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 48: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 48: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '19' (LG) duration 117 frames exceeds threshold 90 frames [start=83, end=199].
- ⚠️ Action 'Action_None' range [80-168] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-162] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-172] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [120-196] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-267] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-282] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-141] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-328] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-156] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-149] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-311] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-222] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-28] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-168] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-135] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-328] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-161] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-296] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-104] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-149] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-328] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-68] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-79] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [83-196] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-13] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-254] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-5] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '21' starts at frame 80, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [80-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-148] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-328] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-328] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>