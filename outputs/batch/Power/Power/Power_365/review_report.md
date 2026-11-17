# Play-Annotation-Generator Annotation Review — Power_365

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_365`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 59
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 38
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `17` | `17` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `0` | `Group` | 13 | START | 13 | 364 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 13 | START | 13 | 367 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 13 | START | 13 | 417 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `15` | `Group` | 13 | START | 13 | 337 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 13 | START | 13 | 300 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 13 | START | 13 | 298 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 13 | START | 13 | 298 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `23` | `Group` | 13 | START | 28 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 13 | START | 13 | 298 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 13 | START | 13 | 401 |
| ✅ EXACT | `Action_DownBlock` | RT | `17` | `17` | 299 | START | 299 | 307 |
| ✅ EXACT | `Action_DownBlock` | C | `6` | `6` | 299 | START | 299 | 308 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `20` | `20` | 299 | START | 299 | 327 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 13–405
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 367 | 355 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 388 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 390 | 391 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 398 | 405 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 13–417
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 417 | 405 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 13–449
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 337 | 325 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 449 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 13–449
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 364 | 352 | inferred_complete_timeline |
| `Action_PreSnap` | 366 | 449 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 28–449
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 449 | 422 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 13–401
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 401 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 13–338
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 298 | 286 | inferred_complete_timeline |
| `Action_PullBlock` | 299 | 327 | 29 | inferred_complete_timeline |
| `Action_PullBlock` | 330 | 338 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 13–308
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 298 | 286 | inferred_complete_timeline |
| `Action_DownBlock` | 299 | 308 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 13–429
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 300 | 288 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 429 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 13–439
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 298 | 286 | inferred_complete_timeline |
| `Action_DownBlock` | 299 | 307 | 9 | inferred_complete_timeline |
| `Action_None` | 375 | 439 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 13–405
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 21 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 35 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 66 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 336 | 265 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 405 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 13–378
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 352 | 340 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 378 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 21–449
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 73 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 449 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 13–352
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 352 | 340 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 13–371
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 371 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 13–449
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 313 | 301 | inferred_complete_timeline |
| `Action_PreSnap` | 333 | 335 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 449 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 13–408
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 408 | 396 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 13–449
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 449 | 437 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 13–449
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 391 | 379 | inferred_complete_timeline |
| `Action_PreSnap` | 394 | 419 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 421 | 422 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 424 | 449 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 13–449
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 420 | 408 | inferred_complete_timeline |
| `Action_PreSnap` | 431 | 449 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–342
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 342 | 330 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 13–449 | 437 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 13–25 | 13 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 298–449 | 150 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 347–373 | 27 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 354–449 | 96 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 372–449 | 78 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 374–417 | 44 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 378–381 | 4 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 380–381 | 2 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 388–449 | 62 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 400–449 | 49 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 412–449 | 38 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 414–449 | 36 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 730: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [13-364] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-449] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-420] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-391] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-419] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-422] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-352] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-342] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [299-308] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-401] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-313] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-335] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-371] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-408] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-367] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-388] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-391] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-405] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-417] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-21] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-35] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-66] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-336] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-405] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-337] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-300] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-429] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [299-307] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-439] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-352] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-378] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-298] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [299-327] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [330-338] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-449] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-323] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-373] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-449] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-417] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-381] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-381] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-401] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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