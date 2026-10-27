# Play-Annotation-Generator Annotation Review — CrackToss_83

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_83`
- **Frame Range:** 0 to 399 (400 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 399
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Toss` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 271 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 269 | START | 269 | 274 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | `6` | `5` | 272 | START | 272 | 305 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `14` | `13` | 272 | START | 272 | 341 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 274 | END | 269 | 274 |
| ✅ EXACT | `Action_Toss` | QB | `18` | `17` | 279 | START | 279 | 297 |
| ✅ EXACT | `Action_BallCarry` | RB | `21` | `20` | 298 | START | 298 | 308 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 346 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_SnapReceive` | 269 | 274 | 6 | inferred_complete_timeline |
| `Action_None` | 275 | 278 | 4 | inferred_complete_timeline |
| `Action_Toss` | 279 | 297 | 19 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_None` | 301 | 399 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–308
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 297 | 218 | inferred_complete_timeline |
| `Action_BallCarry` | 298 | 308 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–339
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 329 | 61 | inferred_complete_timeline |
| `Action_None` | 332 | 333 | 2 | inferred_complete_timeline |
| `Action_None` | 338 | 339 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_CrackBlock` | 272 | 305 | 34 | inferred_complete_timeline |
| `Action_CrackBlock` | 307 | 346 | 40 | inferred_complete_timeline |
| `Action_None` | 347 | 399 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 399 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 371 | 103 | inferred_complete_timeline |
| `Action_None` | 384 | 399 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–390
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 372 | 104 | inferred_complete_timeline |
| `Action_None` | 389 | 390 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_BallSnap` | 269 | 274 | 6 | inferred_complete_timeline |
| `Action_None` | 275 | 376 | 102 | inferred_complete_timeline |
| `Action_None` | 399 | 399 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 280 | 12 | inferred_complete_timeline |
| `Action_None` | 284 | 373 | 90 | inferred_complete_timeline |
| `Action_None` | 378 | 399 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 373 | 105 | inferred_complete_timeline |
| `Action_None` | 382 | 399 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 286 | 18 | inferred_complete_timeline |
| `Action_None` | 288 | 399 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 276 | 8 | inferred_complete_timeline |
| `Action_None` | 280 | 399 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 399 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 327 | 59 | inferred_complete_timeline |
| `Action_None` | 330 | 335 | 6 | inferred_complete_timeline |
| `Action_None` | 337 | 399 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 399 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–369
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 364 | 96 | inferred_complete_timeline |
| `Action_None` | 366 | 369 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 399 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 399 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–375
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 375 | 107 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–399 | 392 | 5 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–395 | 371 | 5 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–397 | 384 | 7 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 309–399 | 62 | 6 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 359–399 | 36 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 383–392 | 10 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 387–399 | 13 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 395–399 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 168: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Row 168: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 168: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 399 as fallback play end.
- ⚠️ Action 'Action_None' range [269-372] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-386] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-395] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-371] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-364] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-369] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [272-305] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-399] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-276] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-399] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-375] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-286] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-327] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-335] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-373] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-329] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [272-341] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-369] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-280] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-373] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-399] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-376] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-337] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-346] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-374] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-379] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-385] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-397] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [298-308] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-372] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-313] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-347] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-373] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-395] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-377] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-392] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-399] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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