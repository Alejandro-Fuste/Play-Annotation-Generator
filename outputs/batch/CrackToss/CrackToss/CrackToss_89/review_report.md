# Play-Annotation-Generator Annotation Review — CrackToss_89

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_89`
- **Frame Range:** 0 to 424 (425 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 424
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | WR3 | offense | `17` | `16` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Toss` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 249 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `17` | `Group` | 0 | START | 0 | 252 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `19` | `Group` | 0 | START | 0 | 249 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `7` | `Group` | 0 | START | 0 | 249 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 250 | START | 250 | 262 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `16` | `15` | 253 | START | 253 | 277 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | WR3 | `17` | `16` | 253 | START | 253 | 302 |
| ✅ EXACT | `Action_PullBlock` | LT | `20` | `19` | 253 | START | 253 | 323 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 262 | END | 250 | 262 |
| ✅ EXACT | `Action_Toss` | QB | `13` | `12` | 265 | START | 265 | 281 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `2` | `1` | 282 | START | 282 | 328 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 323 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–383
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_SnapReceive` | 250 | 262 | 13 | inferred_complete_timeline |
| `Action_None` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_Toss` | 265 | 281 | 17 | inferred_complete_timeline |
| `Action_None` | 282 | 383 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–424
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_None` | 250 | 424 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–415
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_PullBlock` | 253 | 302 | 50 | inferred_complete_timeline |
| `Action_PullBlock` | 308 | 310 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 315 | 323 | 9 | inferred_complete_timeline |
| `Action_None` | 324 | 415 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–424
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_None` | 250 | 424 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–343
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 252 | 163 | inferred_complete_timeline |
| `Action_PullBlock` | 253 | 323 | 71 | inferred_complete_timeline |
| `Action_None` | 324 | 338 | 15 | inferred_complete_timeline |
| `Action_None` | 342 | 343 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–424
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 249 | 163 | inferred_complete_timeline |
| `Action_None` | 250 | 307 | 58 | inferred_complete_timeline |
| `Action_None` | 309 | 312 | 4 | inferred_complete_timeline |
| `Action_None` | 317 | 320 | 4 | inferred_complete_timeline |
| `Action_None` | 330 | 424 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–424
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 249 | 167 | inferred_complete_timeline |
| `Action_BallSnap` | 250 | 262 | 13 | inferred_complete_timeline |
| `Action_None` | 263 | 424 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 249 | 167 | inferred_complete_timeline |
| `Action_None` | 250 | 274 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–424
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 249 | 167 | inferred_complete_timeline |
| `Action_None` | 250 | 424 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_None` | 250 | 306 | 57 | inferred_complete_timeline |
| `Action_None` | 310 | 424 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_None` | 250 | 424 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_None` | 250 | 300 | 51 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_None` | 307 | 424 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_None` | 250 | 424 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_None` | 250 | 353 | 104 | inferred_complete_timeline |
| `Action_None` | 355 | 371 | 17 | inferred_complete_timeline |
| `Action_None` | 373 | 374 | 2 | inferred_complete_timeline |
| `Action_None` | 376 | 377 | 2 | inferred_complete_timeline |
| `Action_None` | 380 | 424 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_None` | 250 | 311 | 62 | inferred_complete_timeline |
| `Action_None` | 313 | 374 | 62 | inferred_complete_timeline |
| `Action_None` | 411 | 412 | 2 | inferred_complete_timeline |
| `Action_None` | 416 | 424 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_None` | 250 | 273 | 24 | inferred_complete_timeline |
| `Action_None` | 277 | 279 | 3 | inferred_complete_timeline |
| `Action_None` | 282 | 291 | 10 | inferred_complete_timeline |
| `Action_None` | 320 | 358 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_None` | 250 | 343 | 94 | inferred_complete_timeline |
| `Action_None` | 345 | 424 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 249 | 144 | inferred_complete_timeline |
| `Action_None` | 250 | 424 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_None` | 250 | 424 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_None` | 250 | 424 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–413 | 394 | 10 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–281 | 280 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 279–424 | 146 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 294–416 | 123 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 301–309 | 9 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 318–320 | 3 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 409–420 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 179: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 180: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 424 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-87] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [282-328] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [330-366] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [370-371] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [376-378] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [380-400] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [403-407] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [412-413] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-273] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-291] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-358] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-311] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-374] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-249] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-353] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-371] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-424] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-383] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-343] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-424] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-249] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-307] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-312] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-320] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [253-277] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [280-281] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [253-302] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [308-310] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [315-323] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-415] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-249] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-274] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-424] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-338] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-300] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-306] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-416] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-309] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-420] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.

</details>