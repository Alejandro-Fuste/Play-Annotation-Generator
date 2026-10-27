# Play-Annotation-Generator Annotation Review — CrackToss_101

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_101`
- **Frame Range:** 0 to 324 (325 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 324
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 121
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR1 | offense | `3` | `2` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `39` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | RB1 | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `10` | `Group` | 0 | START | 0 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `5` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `19` | `16` | 186 | START | 186 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR1 | `3` | `2` | 188 | START | 188 | 211 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `39` | `20` | 189 | START | 189 | 272 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 190 | END | 186 | 190 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 195 | START | 195 | 216 |
| ✅ EXACT | `Action_BallCarry` | RB1 | `10` | `9` | 217 | START | 217 | 274 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 272 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 45 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 119 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 185 | 64 | inferred_complete_timeline |
| `Action_SnapReceive` | 186 | 190 | 5 | inferred_complete_timeline |
| `Action_None` | 191 | 194 | 4 | inferred_complete_timeline |
| `Action_Toss` | 195 | 216 | 22 | inferred_complete_timeline |
| `Action_None` | 217 | 285 | 69 | inferred_complete_timeline |
| `Action_None` | 293 | 296 | 4 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_None` | 306 | 312 | 7 | inferred_complete_timeline |
| `Action_None` | 316 | 324 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_BallCarry` | 217 | 274 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_None` | 186 | 281 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_CrackBlock` | 188 | 211 | 24 | inferred_complete_timeline |
| `Action_CrackBlock` | 214 | 216 | 3 | inferred_complete_timeline |
| `Action_CrackBlock` | 224 | 272 | 49 | inferred_complete_timeline |
| `Action_None` | 273 | 277 | 5 | inferred_complete_timeline |
| `Action_None` | 286 | 299 | 14 | inferred_complete_timeline |
| `Action_None` | 303 | 307 | 5 | inferred_complete_timeline |
| `Action_None` | 309 | 311 | 3 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 317 | 319 | 3 | inferred_complete_timeline |
| `Action_None` | 322 | 323 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_None` | 186 | 303 | 118 | inferred_complete_timeline |
| `Action_None` | 312 | 313 | 2 | inferred_complete_timeline |
| `Action_None` | 315 | 317 | 3 | inferred_complete_timeline |
| `Action_None` | 319 | 324 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 9 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 21 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 185 | 127 | inferred_complete_timeline |
| `Action_None` | 186 | 301 | 116 | inferred_complete_timeline |
| `Action_None` | 303 | 324 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_None` | 186 | 216 | 31 | inferred_complete_timeline |
| `Action_None` | 224 | 237 | 14 | inferred_complete_timeline |
| `Action_None` | 239 | 241 | 3 | inferred_complete_timeline |
| `Action_None` | 244 | 324 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 53 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 185 | 131 | inferred_complete_timeline |
| `Action_None` | 186 | 311 | 126 | inferred_complete_timeline |
| `Action_None` | 314 | 319 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_None` | 186 | 311 | 126 | inferred_complete_timeline |
| `Action_None` | 314 | 324 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 56 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 185 | 97 | inferred_complete_timeline |
| `Action_None` | 186 | 198 | 13 | inferred_complete_timeline |
| `Action_None` | 204 | 221 | 18 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 246 | 21 | inferred_complete_timeline |
| `Action_None` | 250 | 270 | 21 | inferred_complete_timeline |
| `Action_None` | 273 | 303 | 31 | inferred_complete_timeline |
| `Action_None` | 318 | 319 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_None` | 186 | 324 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_None` | 186 | 264 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_None` | 186 | 290 | 105 | inferred_complete_timeline |
| `Action_None` | 293 | 297 | 5 | inferred_complete_timeline |
| `Action_None` | 301 | 304 | 4 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_None` | 311 | 313 | 3 | inferred_complete_timeline |
| `Action_None` | 323 | 324 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 54 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 185 | 130 | inferred_complete_timeline |
| `Action_None` | 186 | 220 | 35 | inferred_complete_timeline |
| `Action_None` | 222 | 324 | 103 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–321 | 314 | 5 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 7–245 | 222 | 3 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 35–319 | 225 | 6 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 61–324 | 260 | 5 | Undefined position; Undefined team |
| `18` | `33` | Position_Unknown | Team_Unknown | 77–324 | 236 | 6 | Undefined position; Undefined team |
| `19` | `36` | Position_Unknown | Team_Unknown | 81–259 | 162 | 4 | Undefined position; Undefined team |
| `20` | `39` | Position_Unknown | Team_Unknown | 83–324 | 242 | 3 | Undefined position; Undefined team |
| `21` | `40` | Position_Unknown | Team_Unknown | 83–234 | 152 | 2 | Undefined position; Undefined team |
| `22` | `41` | Position_Unknown | Team_Unknown | 212–324 | 113 | 1 | Undefined position; Undefined team |
| `23` | `42` | Position_Unknown | Team_Unknown | 243–324 | 82 | 1 | Undefined position; Undefined team |
| `24` | `43` | Position_Unknown | Team_Unknown | 277–278 | 2 | 1 | Undefined position; Undefined team |
| `25` | `44` | Position_Unknown | Team_Unknown | 291–324 | 34 | 1 | Undefined position; Undefined team |
| `26` | `45` | Position_Unknown | Team_Unknown | 292–311 | 20 | 1 | Undefined position; Undefined team |
| `27` | `46` | Position_Unknown | Team_Unknown | 317–324 | 8 | 1 | Undefined position; Undefined team |
| `28` | `47` | Position_Unknown | Team_Unknown | 324–324 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 200: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 324 as fallback play end.
- ⚠️ Action 'Action_None' range [186-290] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-304] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-303] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [188-211] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [214-216] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-307] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-311] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-264] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-281] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-185] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-311] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-45] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-119] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-185] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-285] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-296] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-312] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-324] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-54] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-220] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-324] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-216] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [217-274] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-216] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-237] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-56] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-198] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-221] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-246] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-270] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-303] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-9] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-301] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-53] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-311] for track '13' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-319] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-243] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-311] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-321] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-17] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-245] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-185] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-311] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-319] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-66] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-185] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-196] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-324] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-185] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-193] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-217] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-237] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-270] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-324] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-207] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-241] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [189-272] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-234] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-324] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-324] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-311] for track '26' has 1 frames without a visible bounding box.
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

</details>