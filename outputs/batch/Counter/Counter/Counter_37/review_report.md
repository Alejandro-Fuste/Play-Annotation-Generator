# Play-Annotation-Generator Annotation Review — Counter_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_37`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 46
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `13` | `12` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `18` | `17` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 352 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 352 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 357 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 344 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 344 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 354 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 344 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 344 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 344 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 345 | START | 345 | 360 |
| ✅ EXACT | `Action_DownBlock` | RT | `11` | `10` | 353 | START | 353 | 432 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `19` | `18` | 353 | START | 361 | 418 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `13` | `12` | 353 | START | 353 | 432 |
| ✅ EXACT | `Action_PullBlock` | LG | `18` | `17` | 355 | START | 355 | 432 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `14` | `13` | 358 | START | 358 | 396 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 360 | END | 345 | 360 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `16` | `15` | 372 | START | 372 | 390 |
| ✅ EXACT | `Action_BallCarry` | RB | `14` | `13` | 397 | START | 397 | 479 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 432 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_SnapReceive` | 345 | 360 | 16 | inferred_complete_timeline |
| `Action_None` | 361 | 371 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 372 | 390 | 19 | inferred_complete_timeline |
| `Action_Handoff` | 392 | 396 | 5 | inferred_complete_timeline |
| `Action_None` | 397 | 479 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 357 | 358 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 358 | 396 | 39 | inferred_complete_timeline |
| `Action_BallCarry` | 397 | 479 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_None` | 345 | 479 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_None` | 345 | 458 | 114 | inferred_complete_timeline |
| `Action_None` | 462 | 479 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 352 | 353 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 353 | 432 | 80 | inferred_complete_timeline |
| `Action_None` | 433 | 479 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_None` | 345 | 479 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 354 | 355 | inferred_complete_timeline |
| `Action_PullBlock` | 355 | 432 | 78 | inferred_complete_timeline |
| `Action_None` | 433 | 479 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_BallSnap` | 345 | 360 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 361 | 418 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 344 | 324 | inferred_complete_timeline |
| `Action_None` | 345 | 368 | 24 | inferred_complete_timeline |
| `Action_None` | 371 | 479 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 352 | 353 | inferred_complete_timeline |
| `Action_DownBlock` | 353 | 432 | 80 | inferred_complete_timeline |
| `Action_None` | 433 | 479 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_None` | 345 | 479 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_None` | 345 | 413 | 69 | inferred_complete_timeline |
| `Action_None` | 415 | 416 | 2 | inferred_complete_timeline |
| `Action_None` | 420 | 438 | 19 | inferred_complete_timeline |
| `Action_None` | 440 | 460 | 21 | inferred_complete_timeline |
| `Action_None` | 466 | 479 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–367
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_None` | 345 | 367 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_None` | 345 | 388 | 44 | inferred_complete_timeline |
| `Action_None` | 399 | 479 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–405
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_None` | 345 | 405 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_None` | 345 | 479 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_None` | 345 | 479 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_None` | 345 | 409 | 65 | inferred_complete_timeline |
| `Action_None` | 425 | 464 | 40 | inferred_complete_timeline |
| `Action_None` | 478 | 479 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_None` | 345 | 466 | 122 | inferred_complete_timeline |
| `Action_None` | 470 | 471 | 2 | inferred_complete_timeline |
| `Action_None` | 475 | 479 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_None` | 345 | 479 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_None` | 345 | 479 | 135 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–411 | 410 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 87–93 | 7 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 386–479 | 94 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 401–479 | 76 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 404–409 | 6 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 405–422 | 11 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 416–479 | 64 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 422–479 | 58 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `19` (C): Annotated start 353 != Inferred start 361
- ⚠️ Ambiguous match for action `Action_Handoff` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 27 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 76: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [345–360], lower_priority='Action_DownBlock' annotated_start=353, effective_Action_DownBlock_start=361.
- ⚠️ Action 'Action_None' range [345-413] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-438] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-460] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-466] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-479] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-409] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-464] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-458] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-479] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-405] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-388] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [372-390] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [361-418] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-367] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-396] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-411] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-368] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-479] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-408] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-479] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-409] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-409] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-422] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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