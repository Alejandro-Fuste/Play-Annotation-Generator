# Play-Annotation-Generator Annotation Review — CrackToss_22

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_22`
- **Frame Range:** 0 to 298 (299 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 298
- **Player Tracks:** 32
- **Ball Tracks:** 1
- **Action Segments:** 92
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DE2 | defense | `20` | `19` |
| ⚠️ START CHANGED | `Action_PullBlock` | SAF1 | defense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_BallCarry` | RT | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 141 |
| ✅ EXACT | `Action_BallSnap` | DE2 | `20` | `19` | 142 | START | 142 | 146 |
| ⚠️ START CHANGED | `Action_PullBlock` | SAF1 | `1` | `0` | 145 | START | 148 | 240 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 146 | END | 142 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | `12` | `11` | 148 | START | 148 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | `17` | `16` | 159 | START | 159 | 159 |
| ✅ EXACT | `Action_BallCarry` | RT | `4` | `3` | 182 | START | 182 | 287 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 240 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_SnapReceive` | 142 | 146 | 5 | inferred_complete_timeline |
| `Action_None` | 147 | 158 | 12 | inferred_complete_timeline |
| `Action_Toss` | 159 | 159 | 1 | inferred_complete_timeline |
| `Action_Toss` | 161 | 181 | 21 | inferred_complete_timeline |
| `Action_None` | 182 | 209 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 273 | 132 | inferred_complete_timeline |
| `Action_None` | 275 | 297 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 157 | 16 | inferred_complete_timeline |
| `Action_None` | 159 | 184 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 147 | 25 | inferred_complete_timeline |
| `Action_CrackBlock` | 148 | 194 | 47 | inferred_complete_timeline |
| `Action_CrackBlock` | 197 | 240 | 44 | inferred_complete_timeline |
| `Action_None` | 241 | 298 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 161 | 20 | inferred_complete_timeline |
| `Action_None` | 163 | 227 | 65 | inferred_complete_timeline |
| `Action_None` | 229 | 266 | 38 | inferred_complete_timeline |
| `Action_None` | 269 | 273 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 181 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 182 | 287 | 106 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 141 | 1 | inferred_complete_timeline |
| `Action_None` | 142 | 154 | 13 | inferred_complete_timeline |
| `Action_None` | 181 | 184 | 4 | inferred_complete_timeline |
| `Action_None` | 197 | 202 | 6 | inferred_complete_timeline |
| `Action_None` | 207 | 298 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_BallSnap` | 142 | 146 | 5 | inferred_complete_timeline |
| `Action_None` | 147 | 228 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 151 | 10 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 160 | 19 | inferred_complete_timeline |
| `Action_None` | 165 | 167 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 162 | 21 | inferred_complete_timeline |
| `Action_None` | 165 | 196 | 32 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 206 | 224 | 19 | inferred_complete_timeline |
| `Action_None` | 229 | 231 | 3 | inferred_complete_timeline |
| `Action_None` | 233 | 289 | 57 | inferred_complete_timeline |
| `Action_None` | 291 | 292 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 281 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 105 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 141 | 7 | inferred_complete_timeline |
| `Action_None` | 142 | 168 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 298 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_PullBlock` | 148 | 240 | 93 | inferred_complete_timeline |
| `Action_None` | 241 | 298 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 172 | 31 | inferred_complete_timeline |
| `Action_None` | 176 | 264 | 89 | inferred_complete_timeline |
| `Action_None` | 277 | 298 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–279 | 280 | 2 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–298 | 298 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–198 | 199 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 63–65 | 3 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 146–243 | 93 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 159–168 | 10 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 161–291 | 130 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 174–245 | 72 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 185–298 | 86 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 190–298 | 109 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 218–252 | 10 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 243–298 | 52 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 257–260 | 4 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 290–298 | 9 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 292–298 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `24` | `27` | 171 | 174 | 3 | 75.0% | 173 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PullBlock` for actor_track_id `1` (SAF1): Annotated start 145 != Inferred start 148
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Toss` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 46: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ Row 46: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Row 46: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '0' (SAF1) duration 96 frames exceeds threshold 90 frames [start=145, end=240].
- ⚠️ Action 'Action_PreSnap' range [0-144] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-227] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-266] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-273] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-165] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [182-287] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-279] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-152] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-138] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-154] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-184] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-298] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-141] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-264] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-141] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-184] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-196] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-224] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-289] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-273] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-297] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [148-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [197-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-298] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-105] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-281] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' for track '16' starts at frame 159, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_Toss' range [159-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-209] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-198] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-160] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-228] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-65] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-154] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-236] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-168] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-213] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-291] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-245] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-205] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-298] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-225] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
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

</details>