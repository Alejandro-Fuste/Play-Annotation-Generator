# Play-Annotation-Generator Annotation Review — Counter_234

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_234`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 599
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 179
- **Validation Warnings:** 205
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 124
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `10` | `9` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | offense | `18` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | LG | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 400 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 400 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 400 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 0 | START | 0 | 399 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `18` | `Group` | 0 | START | 7 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 425 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 399 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `16` | `15` | 400 | START | 400 | 400 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `10` | `9` | 401 | START | 401 | 410 |
| ✅ EXACT | `Action_DownBlock` | LG | `13` | `12` | 401 | START | 401 | 402 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `16` | `15` | 401 | START | 401 | 413 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `11` | `10` | 401 | START | 401 | 421 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | `18` | `16` | 401 | START | 401 | 405 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | LG | `13` | `12` | 403 | START | 403 | 444 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 417 | END | 400 | 417 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `5` | `4` | 432 | START | 432 | 448 |
| ✅ EXACT | `Action_BallCarry` | RB | `3` | `2` | 454 | START | 454 | 479 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 526 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–488
- **Visible Samples:** 485

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_SnapReceive` | 400 | 417 | 18 | inferred_complete_timeline |
| `Action_None` | 418 | 431 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 432 | 448 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 453 | 453 | 1 | inferred_complete_timeline |
| `Action_None` | 454 | 488 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_PreSnap` | 427 | 453 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 454 | 479 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–454
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_None` | 400 | 407 | 8 | inferred_complete_timeline |
| `Action_None` | 410 | 421 | 12 | inferred_complete_timeline |
| `Action_None` | 423 | 427 | 5 | inferred_complete_timeline |
| `Action_None` | 430 | 454 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 7–411
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 15 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 19 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 32 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 42 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 49 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 118 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 224 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 263 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 366 | 101 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 401 | 405 | 5 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 410 | 411 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–476
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 400 | 401 | inferred_complete_timeline |
| `Action_DownBlock` | 401 | 410 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 475 | 476 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 400 | 401 | inferred_complete_timeline |
| `Action_DownBlock` | 401 | 402 | 2 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 403 | 444 | 42 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 450 | 599 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–425
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 400 | 401 | inferred_complete_timeline |
| `Action_PullBlock` | 401 | 421 | 21 | inferred_complete_timeline |
| `Action_PullBlock` | 424 | 425 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–468
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_None` | 400 | 448 | 49 | inferred_complete_timeline |
| `Action_None` | 466 | 468 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–546
- **Visible Samples:** 518

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_None` | 400 | 512 | 113 | inferred_complete_timeline |
| `Action_None` | 542 | 546 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 544

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_None` | 400 | 435 | 36 | inferred_complete_timeline |
| `Action_None` | 446 | 459 | 14 | inferred_complete_timeline |
| `Action_None` | 462 | 464 | 3 | inferred_complete_timeline |
| `Action_None` | 473 | 482 | 10 | inferred_complete_timeline |
| `Action_None` | 502 | 503 | 2 | inferred_complete_timeline |
| `Action_None` | 506 | 518 | 13 | inferred_complete_timeline |
| `Action_None` | 522 | 523 | 2 | inferred_complete_timeline |
| `Action_None` | 528 | 529 | 2 | inferred_complete_timeline |
| `Action_None` | 532 | 534 | 3 | inferred_complete_timeline |
| `Action_None` | 538 | 559 | 22 | inferred_complete_timeline |
| `Action_None` | 563 | 599 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–487
- **Visible Samples:** 488

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_None` | 400 | 487 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 596

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_None` | 400 | 514 | 115 | inferred_complete_timeline |
| `Action_None` | 519 | 599 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 592

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_None` | 400 | 487 | 88 | inferred_complete_timeline |
| `Action_None` | 489 | 551 | 63 | inferred_complete_timeline |
| `Action_None` | 553 | 587 | 35 | inferred_complete_timeline |
| `Action_None` | 590 | 591 | 2 | inferred_complete_timeline |
| `Action_None` | 596 | 599 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_None` | 400 | 599 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–537
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_None` | 400 | 504 | 105 | inferred_complete_timeline |
| `Action_None` | 508 | 537 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–482 | 483 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 2–599 | 358 | 14 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 13–17 | 5 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 45–425 | 233 | 17 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 48–447 | 279 | 12 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 128–403 | 117 | 13 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 362–403 | 42 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 409–543 | 135 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 424–427 | 4 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 429–597 | 152 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 429–431 | 3 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 447–517 | 68 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 464–494 | 31 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 466–599 | 128 | 4 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 475–489 | 15 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 501–599 | 74 | 5 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 521–595 | 75 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 527–599 | 57 | 6 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 527–596 | 24 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 537–599 | 63 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 540–599 | 60 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 542–577 | 26 | 4 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 553–591 | 38 | 2 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 556–599 | 7 | 2 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 560–572 | 9 | 2 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 571–599 | 29 | 1 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 581–599 | 12 | 2 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 583–599 | 17 | 1 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 588–591 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 141 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 470: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 470: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (Unknown) duration 126 frames exceeds threshold 90 frames [start=401, end=526].
- ⚠️ Action 'Action_None' range [400-487] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-514] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-425] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [454-479] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-512] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-546] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [432-448] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-488] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-435] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-459] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-464] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-482] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-518] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-523] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-529] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-534] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-559] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-487] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-551] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-587] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-591] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-599] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-504] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-537] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [401-410] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [475-476] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [401-421] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [424-425] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-448] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-468] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [403-444] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-482] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-407] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-421] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-427] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-454] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-73] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-174] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-205] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-318] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [401-413] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [440-507] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-567] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-15] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-19] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-32] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-42] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-224] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-263] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-366] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [401-405] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [410-411] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-17] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-49] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-59] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-77] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-135] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-152] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-161] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-164] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-244] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-270] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-279] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-283] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-304] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-326] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-425] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-127] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-280] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-288] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-305] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-317] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-338] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-414] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-436] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-447] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-138] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-272] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-278] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-281] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-300] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-318] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-325] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-403] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-399] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-403] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-543] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-427] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-435] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-519] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-529] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-597] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-431] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-468] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-485] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-517] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-494] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-517] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-533] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-543] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-489] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-528] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-562] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-566] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-581] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-595] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-540] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-548] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-559] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-562] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-572] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-599] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-548] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-596] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-547] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-567] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-577] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-572] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-591] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-559] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-561] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-572] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-586] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-591] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>