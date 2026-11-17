# Play-Annotation-Generator Annotation Review — Power_233

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_233`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 133
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
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `22` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 16 | START | 16 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 16 | START | 16 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 16 | START | 16 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 16 | START | 16 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 16 | START | 16 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 16 | START | 16 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 16 | START | 71 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 16 | START | 16 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 16 | START | 16 | 374 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 16 | START | 16 | 353 |
| ✅ EXACT | `Action_DownBlock` | LT | `15` | `15` | 281 | START | 281 | 354 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `17` | `17` | 281 | START | 281 | 281 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `22` | `22` | 281 | START | 281 | 352 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 16–444
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 374 | 359 | inferred_complete_timeline |
| `Action_PreSnap` | 377 | 423 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 428 | 429 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 432 | 439 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 441 | 444 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 16–353
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 353 | 338 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 16–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 449 | 434 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 16–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 449 | 434 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 16–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 449 | 434 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 16–382
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 30 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 104 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 124 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 340 | 201 | inferred_complete_timeline |
| `Action_PreSnap` | 344 | 367 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 380 | 382 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 16–449
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 26 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 75 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 109 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 132 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 280 | 146 | inferred_complete_timeline |
| `Action_DownBlock` | 281 | 354 | 74 | inferred_complete_timeline |
| `Action_None` | 355 | 361 | 7 | inferred_complete_timeline |
| `Action_None` | 366 | 387 | 22 | inferred_complete_timeline |
| `Action_None` | 390 | 391 | 2 | inferred_complete_timeline |
| `Action_None` | 395 | 449 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 16–356
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 24 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 73 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 278 | 204 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 281 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 330 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 333 | 337 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 356 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 16–291
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 26 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 44 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 280 | 227 | inferred_complete_timeline |
| `Action_DownBlock` | 281 | 281 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 290 | 291 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 71–449
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 130 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 322 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 449 | 121 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 16–319
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 23 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 86 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 132 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 282 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 297 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 319 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 16–447
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 447 | 432 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 16–449
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 26 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 336 | 224 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 372 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 376 | 386 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 395 | 408 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 411 | 412 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 426 | 449 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 60–412
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 60 | 323 | 264 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 336 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 373 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 377 | 385 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 392 | 393 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 395 | 402 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 407 | 412 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 16–402
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 36 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 42 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 340 | 295 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 346 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 349 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 365 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 374 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 377 | 386 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 388 | 390 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 395 | 402 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 16–449
- **Visible Samples:** 431

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 404 | 389 | inferred_complete_timeline |
| `Action_PreSnap` | 408 | 449 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 16–366
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 216 | 201 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 366 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 16–387
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 356 | 341 | inferred_complete_timeline |
| `Action_PreSnap` | 358 | 364 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 368 | 371 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 382 | 387 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 16–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 449 | 434 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 16–449
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 295 | 280 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 351 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 375 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 380 | 392 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 394 | 401 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 406 | 412 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 433 | 440 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 443 | 444 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 449 | 449 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 16–449
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 429 | 414 | inferred_complete_timeline |
| `Action_PreSnap` | 442 | 449 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 16–37 | 22 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 117–449 | 244 | 8 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 300–350 | 44 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 317–449 | 132 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 357–374 | 18 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 360–449 | 66 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 411–449 | 32 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 424–449 | 26 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 428–444 | 17 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 430–449 | 20 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 433–449 | 17 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 434–449 | 16 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 447–448 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (3 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 106 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [16-449] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-429] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-404] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-295] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-351] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-375] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-392] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-401] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-412] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-440] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-444] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-374] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-423] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-439] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-444] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-353] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-356] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-364] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-371] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-387] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-447] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-216] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-366] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-36] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-42] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-340] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-346] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-349] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-365] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-374] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-386] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-390] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-402] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-37] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-30] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-104] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-124] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-340] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-367] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-382] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-75] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-109] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-132] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [281-354] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-361] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-387] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-26] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-86] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-336] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-372] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-386] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-408] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-412] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-26] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' for track '17' starts at frame 281, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_DownBlock' range [281-281] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [286-287] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [290-291] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-24] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-278] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-281] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-330] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-337] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-356] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-23] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-86] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-132] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-282] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-297] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-319] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-323] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-336] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-373] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-385] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-393] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-402] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-412] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-86] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-130] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-322] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-124] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-182] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [281-352] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-401] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-411] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-435] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-449] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-305] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-335] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-350] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-322] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-449] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-374] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-405] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-412] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-449] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-444] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-449] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-448] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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