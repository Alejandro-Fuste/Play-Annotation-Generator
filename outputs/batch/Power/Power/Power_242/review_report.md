# Play-Annotation-Generator Annotation Review — Power_242

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_242`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 599
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `16` | `14` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 4 | START | 4 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 4 | START | 11 | 387 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 4 | START | 4 | 418 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 4 | START | 4 | 387 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 4 | START | 4 | 415 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 4 | START | 4 | 387 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 4 | START | 4 | 591 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `16` | `14` | 388 | START | 388 | 400 |
| ✅ EXACT | `Action_DownBlock` | LG | `4` | `4` | 388 | START | 388 | 427 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `8` | `8` | 388 | START | 388 | 414 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `7` | `7` | 388 | START | 388 | 404 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 4–591
- **Visible Samples:** 588

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 591 | 588 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 4–493
- **Visible Samples:** 483

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 415 | 412 | inferred_complete_timeline |
| `Action_PreSnap` | 423 | 493 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 4–599
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 100 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 284 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 297 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 318 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 322 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 396 | 410 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 425 | 432 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 453 | 455 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 462 | 471 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 478 | 488 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 490 | 491 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 505 | 523 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 538 | 599 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 4–496
- **Visible Samples:** 489

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 418 | 415 | inferred_complete_timeline |
| `Action_PreSnap` | 420 | 458 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 462 | 496 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 4–511
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 387 | 384 | inferred_complete_timeline |
| `Action_DownBlock` | 388 | 414 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 417 | 427 | 11 | inferred_complete_timeline |
| `Action_None` | 428 | 471 | 44 | inferred_complete_timeline |
| `Action_None` | 477 | 487 | 11 | inferred_complete_timeline |
| `Action_None` | 496 | 511 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 4–478
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 387 | 384 | inferred_complete_timeline |
| `Action_DownBlock` | 388 | 427 | 40 | inferred_complete_timeline |
| `Action_None` | 428 | 439 | 12 | inferred_complete_timeline |
| `Action_None` | 445 | 478 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 11–599
- **Visible Samples:** 556

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 387 | 377 | inferred_complete_timeline |
| `Action_DownBlock` | 388 | 400 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 404 | 427 | 24 | inferred_complete_timeline |
| `Action_None` | 428 | 462 | 35 | inferred_complete_timeline |
| `Action_None` | 485 | 532 | 48 | inferred_complete_timeline |
| `Action_None` | 541 | 599 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 4–599
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 191 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 241 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 251 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 471 | 208 | inferred_complete_timeline |
| `Action_PreSnap` | 478 | 599 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 13–599
- **Visible Samples:** 573

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 466 | 454 | inferred_complete_timeline |
| `Action_PreSnap` | 470 | 552 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 557 | 559 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 561 | 591 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 598 | 599 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 11–599
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 54 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 108 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 249 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 296 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 310 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 388 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 435 | 599 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 12–599
- **Visible Samples:** 516

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 108 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 114 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 150 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 393 | 240 | inferred_complete_timeline |
| `Action_PreSnap` | 402 | 403 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 406 | 413 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 415 | 419 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 422 | 472 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 481 | 483 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 485 | 505 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 507 | 550 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 557 | 559 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 597 | 599 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 4–528
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 413 | 410 | inferred_complete_timeline |
| `Action_PreSnap` | 417 | 464 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 474 | 500 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 505 | 528 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 4–474
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 184 | 181 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 474 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 4–599
- **Visible Samples:** 590

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 472 | 469 | inferred_complete_timeline |
| `Action_PreSnap` | 478 | 499 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 501 | 599 | 99 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 4–420 | 417 | 1 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 4–599 | 552 | 10 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 6–238 | 233 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 284–443 | 153 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 424–425 | 2 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 453–559 | 101 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 475–599 | 125 | 1 | Undefined position; Undefined team |
| `21` | `31` | Position_Unknown | Team_Unknown | 500–501 | 2 | 1 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 504–543 | 40 | 1 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 508–599 | 87 | 2 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 510–519 | 10 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 510–595 | 78 | 2 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 518–599 | 81 | 2 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 555–578 | 20 | 2 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 575–599 | 25 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 594–599 | 6 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 594–599 | 6 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 598–599 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 88 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 486: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ Row 486: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [4-413] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-464] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-500] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [505-528] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-420] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-472] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [478-499] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [501-599] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-418] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-458] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [462-496] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-439] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-478] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-191] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-241] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-251] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-471] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-415] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-493] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [388-404] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-472] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-515] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-533] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-561] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-567] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [388-414] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-471] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-487] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-511] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-591] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-184] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-474] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-100] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-284] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-297] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-318] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-322] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-410] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-432] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [453-455] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [462-471] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [478-488] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [490-491] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [505-523] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-238] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-54] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-249] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-296] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-310] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-388] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [388-400] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-462] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-532] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-393] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-403] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-413] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-419] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-472] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [481-483] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [485-505] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [507-550] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [557-559] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-466] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [470-552] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [557-559] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [561-591] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-287] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-443] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-425] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [453-475] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [478-531] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [536-559] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [500-501] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [504-543] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [508-561] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [510-519] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [510-565] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [574-595] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [518-566] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [555-572] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [577-578] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [575-599] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>