# Play-Annotation-Generator Annotation Review — CrackToss_92

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_92`
- **Frame Range:** 0 to 399 (400 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 399
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 68
- **Validation Warnings:** 51
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
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `23` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR1 | offense | `23` | `21` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | CB2 | defense | `5` | `4` |
| ✅ EXACT | `Action_Toss` | CB2 | defense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | RG | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `13` | `Group` | 0 | START | 0 | 298 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 331 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 298 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 2 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 4 | 301 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `23` | `Group` | 0 | START | 10 | 301 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 299 | START | 299 | 314 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR1 | `23` | `21` | 302 | START | 302 | 334 |
| ✅ EXACT | `Action_PullBlock` | LT | `21` | `20` | 302 | START | 302 | 367 |
| ✅ EXACT | `Action_SnapReceive` | CB2 | `5` | `4` | 314 | END | 299 | 314 |
| ✅ EXACT | `Action_Toss` | CB2 | `5` | `4` | 319 | START | 319 | 331 |
| ✅ EXACT | `Action_BallCarry` | RG | `15` | `14` | 332 | START | 332 | 383 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 367 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |
| `Action_None` | 299 | 369 | 71 | inferred_complete_timeline |
| `Action_None` | 372 | 399 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 10–399
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 301 | 292 | inferred_complete_timeline |
| `Action_CrackBlock` | 302 | 334 | 33 | inferred_complete_timeline |
| `Action_CrackBlock` | 339 | 367 | 29 | inferred_complete_timeline |
| `Action_None` | 368 | 369 | 2 | inferred_complete_timeline |
| `Action_None` | 374 | 394 | 21 | inferred_complete_timeline |
| `Action_None` | 399 | 399 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 4–399
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 301 | 298 | inferred_complete_timeline |
| `Action_PullBlock` | 302 | 367 | 66 | inferred_complete_timeline |
| `Action_None` | 368 | 399 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 2–399
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 11 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 298 | 286 | inferred_complete_timeline |
| `Action_None` | 299 | 371 | 73 | inferred_complete_timeline |
| `Action_None` | 375 | 399 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |
| `Action_BallSnap` | 299 | 314 | 16 | inferred_complete_timeline |
| `Action_None` | 315 | 399 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–383
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 331 | 332 | inferred_complete_timeline |
| `Action_BallCarry` | 332 | 383 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |
| `Action_None` | 299 | 329 | 31 | inferred_complete_timeline |
| `Action_None` | 335 | 337 | 3 | inferred_complete_timeline |
| `Action_None` | 339 | 399 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–369
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |
| `Action_None` | 299 | 369 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–346
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |
| `Action_None` | 299 | 346 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |
| `Action_None` | 299 | 399 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |
| `Action_None` | 299 | 399 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |
| `Action_None` | 299 | 399 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |
| `Action_None` | 299 | 399 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |
| `Action_SnapReceive` | 299 | 314 | 16 | inferred_complete_timeline |
| `Action_None` | 315 | 318 | 4 | inferred_complete_timeline |
| `Action_Toss` | 319 | 331 | 13 | inferred_complete_timeline |
| `Action_None` | 332 | 399 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–393
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |
| `Action_None` | 299 | 377 | 79 | inferred_complete_timeline |
| `Action_None` | 387 | 393 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |
| `Action_None` | 299 | 319 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–399 | 400 | 2 | Undefined position; Undefined team |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–399 | 400 | 2 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–399 | 400 | 2 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–399 | 388 | 3 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–399 | 400 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–325 | 322 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 314–318 | 5 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 333–399 | 65 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 354–399 | 38 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 368–399 | 32 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 376–399 | 24 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `23` (2 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 24 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 185: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 186: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ Row 186: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 186: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 399 as fallback play end.
- ⚠️ Action 'Action_None' range [299-369] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-337] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-399] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-377] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-393] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-399] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-369] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-399] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [332-383] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-319] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-319] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-346] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-11] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-371] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [302-334] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-394] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-318] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-360] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-399] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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