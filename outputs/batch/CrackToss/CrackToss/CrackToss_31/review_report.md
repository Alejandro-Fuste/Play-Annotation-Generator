# Play-Annotation-Generator Annotation Review — CrackToss_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_31`
- **Frame Range:** 0 to 358 (359 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Unknown`
- **Result Frame:** 358
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | CB3 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR1 | offense | `2` | `1` |
| ✅ EXACT | `Action_CrackBlock` | WR2 | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | offense | `16` | `15` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_Toss` | Position_Unknown | Team_Unknown | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | CB3 | `11` | `10` | 90 | START | 90 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR1 | `2` | `1` | 93 | START | 93 | 186 |
| ✅ EXACT | `Action_CrackBlock` | WR2 | `5` | `4` | 93 | START | 93 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `15` | `14` | 93 | START | 93 | 256 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | `16` | `15` | 93 | START | 93 | 248 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `17` | `16` | 114 | END | 90 | 114 |
| ✅ EXACT | `Action_Toss` | Position_Unknown | `17` | `16` | 125 | START | 125 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `22` | `21` | 170 | START | 170 | 172 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 318 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_CrackBlock` | 93 | 186 | 94 | inferred_complete_timeline |
| `Action_CrackBlock` | 190 | 204 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_CrackBlock` | 93 | 130 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 358 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–314
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 314 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PullBlock` | 93 | 248 | 156 | inferred_complete_timeline |
| `Action_PullBlock` | 258 | 318 | 61 | inferred_complete_timeline |
| `Action_None` | 319 | 339 | 21 | inferred_complete_timeline |
| `Action_None` | 341 | 345 | 5 | inferred_complete_timeline |
| `Action_None` | 357 | 358 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PullBlock` | 93 | 256 | 164 | inferred_complete_timeline |
| `Action_PullBlock` | 258 | 318 | 61 | inferred_complete_timeline |
| `Action_None` | 319 | 349 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 80 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 89 | 8 | inferred_complete_timeline |
| `Action_None` | 90 | 90 | 1 | inferred_complete_timeline |
| `Action_None` | 96 | 160 | 65 | inferred_complete_timeline |
| `Action_None` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_None` | 172 | 192 | 21 | inferred_complete_timeline |
| `Action_None` | 196 | 204 | 9 | inferred_complete_timeline |
| `Action_None` | 216 | 222 | 7 | inferred_complete_timeline |
| `Action_None` | 224 | 358 | 135 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 140 | 51 | inferred_complete_timeline |
| `Action_None` | 142 | 144 | 3 | inferred_complete_timeline |
| `Action_None` | 154 | 162 | 9 | inferred_complete_timeline |
| `Action_None` | 174 | 176 | 3 | inferred_complete_timeline |
| `Action_None` | 186 | 198 | 13 | inferred_complete_timeline |
| `Action_None` | 218 | 358 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 162 | 73 | inferred_complete_timeline |
| `Action_None` | 164 | 358 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 122 | 33 | inferred_complete_timeline |
| `Action_None` | 126 | 150 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 180 | 91 | inferred_complete_timeline |
| `Action_None` | 182 | 358 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–341
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 331 | 242 | inferred_complete_timeline |
| `Action_None` | 339 | 341 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–339
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 200 | 111 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_None` | 206 | 254 | 49 | inferred_complete_timeline |
| `Action_None` | 256 | 264 | 9 | inferred_complete_timeline |
| `Action_None` | 266 | 335 | 70 | inferred_complete_timeline |
| `Action_None` | 337 | 339 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 260 | 171 | inferred_complete_timeline |
| `Action_None` | 272 | 288 | 17 | inferred_complete_timeline |
| `Action_None` | 300 | 304 | 5 | inferred_complete_timeline |
| `Action_None` | 318 | 358 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_BallSnap` | 90 | 98 | 9 | inferred_complete_timeline |
| `Action_BallSnap` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 106 | 114 | 9 | inferred_complete_timeline |
| `Action_None` | 115 | 124 | 10 | inferred_complete_timeline |
| `Action_None` | 168 | 220 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 216 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 132 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–154 | 155 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–252 | 253 | 5 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 105–146 | 15 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 113–358 | 246 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 121–358 | 233 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 185–302 | 117 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 201–358 | 158 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 201–208 | 8 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 209–358 | 138 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 227–295 | 67 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 239–358 | 96 | 3 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 249–358 | 91 | 5 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 324–358 | 34 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 64: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 64: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '14' (LG) duration 226 frames exceeds threshold 90 frames [start=93, end=318].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '15' (LT) duration 226 frames exceeds threshold 90 frames [start=93, end=318].
- ⚠️ Action 'Action_None' range [90-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [93-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [190-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-331] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-341] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-314] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [93-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-254] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-264] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-335] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-339] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-132] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-260] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-288] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-304] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-122] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-216] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [90-98] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [102-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-220] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [93-256] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-349] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [93-248] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-339] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-345] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-252] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-140] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-198] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-89] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 90, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [90-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-160] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-192] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-222] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-358] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [170-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-236] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-302] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-208] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-244] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-254] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-295] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-268] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-270] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-314] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-333] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-349] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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