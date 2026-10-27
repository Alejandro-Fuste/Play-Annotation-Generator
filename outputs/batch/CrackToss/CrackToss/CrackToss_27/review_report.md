# Play-Annotation-Generator Annotation Review — CrackToss_27

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_27`
- **Frame Range:** 0 to 268 (269 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 268
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 129
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 2 | START | 2 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 2 | START | 2 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `12` | `Group` | 2 | START | 2 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 2 | START | 2 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 2 | START | 2 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 2 | START | 2 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 2 | START | 2 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 2 | START | 2 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 2 | START | 2 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 2 | START | 2 | 96 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 97 | START | 97 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | `13` | `12` | 100 | START | 100 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `19` | `18` | 100 | START | 100 | 175 |
| ✅ EXACT | `Action_PullBlock` | LT | `5` | `4` | 100 | START | 100 | 186 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 102 | END | 97 | 102 |
| ✅ EXACT | `Action_Toss` | QB | `16` | `15` | 122 | START | 122 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `9` | 141 | START | 141 | 153 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 186 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 2–268
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 96 | 95 | inferred_complete_timeline |
| `Action_SnapReceive` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_None` | 103 | 121 | 19 | inferred_complete_timeline |
| `Action_Toss` | 122 | 140 | 19 | inferred_complete_timeline |
| `Action_None` | 141 | 245 | 105 | inferred_complete_timeline |
| `Action_None` | 249 | 268 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 2–252
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 140 | 139 | inferred_complete_timeline |
| `Action_BallCarry` | 141 | 153 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 155 | 221 | 67 | inferred_complete_timeline |
| `Action_BallCarry` | 250 | 252 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 2–268
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 99 | 98 | inferred_complete_timeline |
| `Action_CrackBlock` | 100 | 152 | 53 | inferred_complete_timeline |
| `Action_CrackBlock` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_CrackBlock` | 161 | 175 | 15 | inferred_complete_timeline |
| `Action_CrackBlock` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_CrackBlock` | 181 | 183 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 268 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 2–261
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 96 | 95 | inferred_complete_timeline |
| `Action_None` | 97 | 261 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 2–268
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 96 | 95 | inferred_complete_timeline |
| `Action_None` | 97 | 214 | 118 | inferred_complete_timeline |
| `Action_None` | 248 | 251 | 4 | inferred_complete_timeline |
| `Action_None` | 254 | 268 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 2–263
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 99 | 98 | inferred_complete_timeline |
| `Action_PullBlock` | 100 | 186 | 87 | inferred_complete_timeline |
| `Action_None` | 187 | 263 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 2–225
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 12 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 15 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 23 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 96 | 60 | inferred_complete_timeline |
| `Action_None` | 97 | 138 | 42 | inferred_complete_timeline |
| `Action_None` | 143 | 174 | 32 | inferred_complete_timeline |
| `Action_None` | 196 | 213 | 18 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 2–268
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 96 | 95 | inferred_complete_timeline |
| `Action_BallSnap` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_None` | 103 | 189 | 87 | inferred_complete_timeline |
| `Action_None` | 191 | 221 | 31 | inferred_complete_timeline |
| `Action_None` | 236 | 238 | 3 | inferred_complete_timeline |
| `Action_None` | 240 | 268 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 2–172
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 96 | 95 | inferred_complete_timeline |
| `Action_None` | 97 | 158 | 62 | inferred_complete_timeline |
| `Action_None` | 160 | 172 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 2–174
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 96 | 95 | inferred_complete_timeline |
| `Action_None` | 97 | 174 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 2–175
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 96 | 95 | inferred_complete_timeline |
| `Action_None` | 97 | 141 | 45 | inferred_complete_timeline |
| `Action_None` | 143 | 153 | 11 | inferred_complete_timeline |
| `Action_None` | 155 | 175 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 2–175
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 22 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 96 | 61 | inferred_complete_timeline |
| `Action_None` | 97 | 132 | 36 | inferred_complete_timeline |
| `Action_None` | 140 | 172 | 33 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 2–30
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 22 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 30 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 2–268
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 96 | 95 | inferred_complete_timeline |
| `Action_None` | 97 | 138 | 42 | inferred_complete_timeline |
| `Action_None` | 141 | 229 | 89 | inferred_complete_timeline |
| `Action_None` | 231 | 268 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 2–268
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 96 | 95 | inferred_complete_timeline |
| `Action_None` | 97 | 172 | 76 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 214 | 17 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_None` | 240 | 268 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 2–268
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 96 | 95 | inferred_complete_timeline |
| `Action_None` | 97 | 268 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 2–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 96 | 95 | inferred_complete_timeline |
| `Action_None` | 97 | 210 | 114 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 3–268 | 266 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 3–212 | 207 | 6 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 3–268 | 266 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 3–34 | 22 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 44–121 | 78 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 53–268 | 200 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 67–241 | 120 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 144–268 | 125 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 183–247 | 41 | 7 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 186–221 | 36 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 192–241 | 45 | 4 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 195–211 | 17 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 195–268 | 57 | 4 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 215–268 | 54 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 237–268 | 32 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 242–268 | 26 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 248–268 | 18 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 257–268 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `13` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 91 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 56: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
- ⚠️ Action 'Action_None' range [97-214] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-268] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-22] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-132] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-172] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-174] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-138] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-229] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-268] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-263] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-268] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-189] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-221] for track '6' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-141] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-153] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-175] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-22] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '9' starts at frame 141, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [141-153] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [155-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [250-252] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-96] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-172] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-214] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-261] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [100-152] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [155-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [161-175] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [178-179] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [181-183] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-268] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-158] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-245] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-268] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-12] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-174] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-213] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-268] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [100-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [177-186] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-202] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-17] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-34] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-96] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-268] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-229] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-268] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-217] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-221] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-218] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-211] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-221] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-268] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-268] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-263] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '33' has 1 frames without a visible bounding box.
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