# Play-Annotation-Generator Annotation Review — CrackToss_63

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_63`
- **Frame Range:** 0 to 349 (350 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 349
- **Player Tracks:** 24
- **Ball Tracks:** 1
- **Action Segments:** 90
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 3
- **Group Expanded Events:** 3
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 7 | START | 7 | 298 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 7 | START | 7 | 267 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 7 | START | 7 | 36 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `18` | `17` | 268 | START | 268 | 280 |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | `16` | `15` | 271 | START | 271 | 342 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `4` | `3` | 271 | START | 271 | 283 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | `8` | `7` | 271 | START | 271 | 288 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 280 | END | 268 | 280 |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | `13` | `12` | 284 | START | 284 | 291 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `11` | `10` | 300 | START | 301 | 302 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 342 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 7–326
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 267 | 261 | inferred_complete_timeline |
| `Action_SnapReceive` | 268 | 280 | 13 | inferred_complete_timeline |
| `Action_None` | 281 | 283 | 3 | inferred_complete_timeline |
| `Action_Toss` | 284 | 291 | 8 | inferred_complete_timeline |
| `Action_Toss` | 293 | 299 | 7 | inferred_complete_timeline |
| `Action_None` | 300 | 326 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 7–302
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 298 | 292 | inferred_complete_timeline |
| `Action_BallCarry` | 301 | 302 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 7–345
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 36 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 270 | 233 | inferred_complete_timeline |
| `Action_PullBlock` | 271 | 288 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 308 | 322 | 15 | inferred_complete_timeline |
| `Action_PullBlock` | 332 | 342 | 11 | inferred_complete_timeline |
| `Action_None` | 343 | 345 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 7–333
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 267 | 261 | inferred_complete_timeline |
| `Action_None` | 268 | 293 | 26 | inferred_complete_timeline |
| `Action_None` | 300 | 303 | 4 | inferred_complete_timeline |
| `Action_None` | 322 | 333 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 7–348
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 267 | 261 | inferred_complete_timeline |
| `Action_None` | 268 | 328 | 61 | inferred_complete_timeline |
| `Action_None` | 330 | 331 | 2 | inferred_complete_timeline |
| `Action_None` | 338 | 348 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 7–349
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 8 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 267 | 252 | inferred_complete_timeline |
| `Action_None` | 268 | 305 | 38 | inferred_complete_timeline |
| `Action_None` | 318 | 346 | 29 | inferred_complete_timeline |
| `Action_None` | 348 | 349 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 7–294
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 8 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 267 | 256 | inferred_complete_timeline |
| `Action_None` | 268 | 294 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–349
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 267 | 268 | inferred_complete_timeline |
| `Action_None` | 268 | 349 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–349
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 267 | 268 | inferred_complete_timeline |
| `Action_None` | 268 | 328 | 61 | inferred_complete_timeline |
| `Action_None` | 338 | 345 | 8 | inferred_complete_timeline |
| `Action_None` | 348 | 349 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 7–349
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 267 | 261 | inferred_complete_timeline |
| `Action_None` | 268 | 349 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 7–208
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 33 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 208 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 7–349
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 267 | 261 | inferred_complete_timeline |
| `Action_None` | 268 | 349 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–348 | 308 | 4 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–349 | 320 | 7 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 7–349 | 309 | 7 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 7–349 | 343 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 20–349 | 316 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 30–349 | 318 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 49–178 | 26 | 7 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 197–215 | 13 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 308–349 | 42 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 309–310 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 319–348 | 21 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 323–349 | 26 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | 47 | 85 | 11 | 28.2% | 50–69, 71, 75–76, 80–84 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Toss` and target `13` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `11` (RB): Annotated start 300 != Inferred start 301

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 128: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 349 as fallback play end.
- ⚠️ Action 'Action_None' range [268-328] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-345] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-302] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-348] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-349] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [271-283] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [289-318] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [338-342] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '3' starts at frame 343, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [343-343] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-328] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-348] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-36] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [271-288] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [308-322] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [332-342] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-8] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-294] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-20] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-81] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-238] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-244] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-267] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-272] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-349] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-298] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [301-302] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-293] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-303] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-333] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [284-291] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-326] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-33] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-208] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-8] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-305] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-346] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [271-342] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-349] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-202] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-267] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-345] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-52] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-58] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-110] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-199] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-207] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-215] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-349] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-329] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-338] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-348] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-349] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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