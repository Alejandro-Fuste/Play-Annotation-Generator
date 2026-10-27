# Play-Annotation-Generator Annotation Review — CrackToss_86

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_86`
- **Frame Range:** 0 to 399 (400 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 399
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 141
- **Validation Warnings:** 142
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 120
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `2` | `1` |
| ✅ EXACT | `Action_PullBlock` | RB2 | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_Toss` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `13` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `5` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 142 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 143 | START | 143 | 150 |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | `2` | `1` | 147 | START | 147 | 236 |
| ✅ EXACT | `Action_PullBlock` | RB2 | `5` | `4` | 147 | START | 147 | 236 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | `7` | `6` | 147 | START | 147 | 201 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 150 | END | 143 | 150 |
| ✅ EXACT | `Action_Toss` | QB | `19` | `18` | 156 | START | 156 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | `13` | `12` | 174 | START | 174 | 235 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 236 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_SnapReceive` | 143 | 150 | 8 | inferred_complete_timeline |
| `Action_None` | 151 | 155 | 5 | inferred_complete_timeline |
| `Action_Toss` | 156 | 173 | 18 | inferred_complete_timeline |
| `Action_None` | 174 | 297 | 124 | inferred_complete_timeline |
| `Action_None` | 304 | 306 | 3 | inferred_complete_timeline |
| `Action_None` | 308 | 309 | 2 | inferred_complete_timeline |
| `Action_None` | 311 | 313 | 3 | inferred_complete_timeline |
| `Action_None` | 317 | 399 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_BallCarry` | 174 | 235 | 62 | inferred_complete_timeline |
| `Action_BallCarry` | 238 | 245 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 247 | 253 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 255 | 261 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 268 | 270 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 272 | 384 | 113 | inferred_complete_timeline |
| `Action_BallCarry` | 386 | 388 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 391 | 399 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_PullBlock` | 147 | 236 | 90 | inferred_complete_timeline |
| `Action_None` | 237 | 354 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 259 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 248 | 106 | inferred_complete_timeline |
| `Action_None` | 250 | 366 | 117 | inferred_complete_timeline |
| `Action_None` | 368 | 399 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 268 | 126 | inferred_complete_timeline |
| `Action_None` | 272 | 276 | 5 | inferred_complete_timeline |
| `Action_None` | 278 | 279 | 2 | inferred_complete_timeline |
| `Action_None` | 292 | 293 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–391
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 284 | 142 | inferred_complete_timeline |
| `Action_None` | 287 | 317 | 31 | inferred_complete_timeline |
| `Action_None` | 319 | 391 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_BallSnap` | 143 | 150 | 8 | inferred_complete_timeline |
| `Action_None` | 151 | 154 | 4 | inferred_complete_timeline |
| `Action_None` | 156 | 207 | 52 | inferred_complete_timeline |
| `Action_None` | 210 | 220 | 11 | inferred_complete_timeline |
| `Action_None` | 224 | 226 | 3 | inferred_complete_timeline |
| `Action_None` | 230 | 233 | 4 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |
| `Action_None` | 241 | 256 | 16 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_None` | 272 | 279 | 8 | inferred_complete_timeline |
| `Action_None` | 302 | 399 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_PullBlock` | 147 | 201 | 55 | inferred_complete_timeline |
| `Action_PullBlock` | 204 | 216 | 13 | inferred_complete_timeline |
| `Action_PullBlock` | 218 | 236 | 19 | inferred_complete_timeline |
| `Action_None` | 237 | 294 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–372
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 163 | 21 | inferred_complete_timeline |
| `Action_None` | 166 | 263 | 98 | inferred_complete_timeline |
| `Action_None` | 266 | 279 | 14 | inferred_complete_timeline |
| `Action_None` | 304 | 305 | 2 | inferred_complete_timeline |
| `Action_None` | 308 | 309 | 2 | inferred_complete_timeline |
| `Action_None` | 312 | 313 | 2 | inferred_complete_timeline |
| `Action_None` | 316 | 372 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 172 | 30 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–354
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 233 | 91 | inferred_complete_timeline |
| `Action_None` | 256 | 354 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 171 | 29 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 265 | 123 | inferred_complete_timeline |
| `Action_None` | 272 | 279 | 8 | inferred_complete_timeline |
| `Action_None` | 281 | 289 | 9 | inferred_complete_timeline |
| `Action_None` | 293 | 294 | 2 | inferred_complete_timeline |
| `Action_None` | 296 | 300 | 5 | inferred_complete_timeline |
| `Action_None` | 304 | 399 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 201 | 59 | inferred_complete_timeline |
| `Action_None` | 203 | 209 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 279 | 137 | inferred_complete_timeline |
| `Action_None` | 281 | 285 | 5 | inferred_complete_timeline |
| `Action_None` | 289 | 297 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 258 | 116 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 399 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–362
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 362 | 220 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–399 | 396 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–399 | 392 | 5 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 53–267 | 212 | 4 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 176–399 | 196 | 9 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 185–399 | 202 | 4 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 251–364 | 110 | 5 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 267–368 | 102 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 270–399 | 124 | 4 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 281–351 | 62 | 3 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 282–286 | 5 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 302–399 | 90 | 4 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 305–311 | 7 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 312–399 | 87 | 2 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 365–386 | 22 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 397–399 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (9 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 109 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 174: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 174: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 399 as fallback play end.
- ⚠️ Action 'Action_None' range [143-172] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-291] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-399] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-163] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-263] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-279] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-372] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [147-236] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '4' starts at frame 237, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [237-354] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-258] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [147-201] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [204-216] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [218-236] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-294] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-259] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-233] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-354] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-248] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-366] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-201] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-265] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-279] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-289] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-300] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-399] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [174-235] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [238-245] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [247-253] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [255-261] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [265-266] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [268-270] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [272-384] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [386-388] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [391-399] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-399] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-362] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-300] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-313] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-399] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-279] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-297] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-207] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-220] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-256] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-279] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-399] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-297] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-399] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-268] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-284] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-317] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-391] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-202] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-261] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-257] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-279] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-302] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-315] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-202] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-261] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-364] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-368] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-291] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-316] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-399] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-313] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-327] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-351] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-286] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-306] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-311] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-386] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>