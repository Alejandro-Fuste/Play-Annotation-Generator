# Play-Annotation-Generator Annotation Review — Power_349

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_349`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 539
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 161
- **Validation Warnings:** 200
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 0
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 20 | START | 20 | 415 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 20 | START | 20 | 302 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 20 | START | 20 | 356 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 20 | START | 20 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 20 | START | 20 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 20 | START | 20 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 20 | START | 20 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 20 | START | 20 | 337 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 20 | START | 20 | 371 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `8` | `Group` | 20 | START | 20 | 361 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `14` | `14` | 303 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RT | `20` | `20` | 303 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `21` | `21` | 303 | START | 320 | 327 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 20–395
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 356 | 337 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 369 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 386 | 391 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 393 | 395 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 20–539
- **Visible Samples:** 513

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 337 | 318 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 358 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 361 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 367 | 539 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 20–539
- **Visible Samples:** 489

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 371 | 352 | inferred_complete_timeline |
| `Action_PreSnap` | 384 | 394 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 398 | 401 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 406 | 480 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 483 | 484 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 486 | 489 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 497 | 526 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 528 | 535 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 537 | 539 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 20–415
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 415 | 396 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 20–539
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 361 | 342 | inferred_complete_timeline |
| `Action_PreSnap` | 363 | 364 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 376 | 377 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 404 | 405 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 408 | 420 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 423 | 539 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 20–299
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 47 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 59 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 156 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 282 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 20–539
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 43 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 99 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 124 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 286 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 302 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 320 | 327 | 8 | inferred_complete_timeline |
| `Action_PullBlock` | 330 | 343 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 347 | 356 | 10 | inferred_complete_timeline |
| `Action_None` | 362 | 539 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 20–302
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 302 | 283 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 20–301
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 65 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 157 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 289 | 131 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 301 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 20–297
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 64 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 86 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 100 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 124 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 157 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 288 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 297 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 20–450
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 302 | 283 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 393 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 398 | 401 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 403 | 444 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 446 | 450 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 20–301
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 288 | 269 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 301 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 20–299
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 46 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 61 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 149 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 282 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 295 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 20–335
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 288 | 269 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 301 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 335 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 20–539
- **Visible Samples:** 496

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 361 | 342 | inferred_complete_timeline |
| `Action_PreSnap` | 372 | 379 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 392 | 418 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 420 | 429 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 431 | 539 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 20–539
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 394 | 375 | inferred_complete_timeline |
| `Action_PreSnap` | 397 | 404 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 407 | 447 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 490 | 539 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 20–307
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 49 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 106 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 268 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 307 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 20–539
- **Visible Samples:** 520

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 539 | 520 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 20–539
- **Visible Samples:** 511

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 421 | 402 | inferred_complete_timeline |
| `Action_PreSnap` | 426 | 449 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 451 | 468 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 470 | 474 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 477 | 478 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 480 | 539 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 20–417
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 417 | 398 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 20–539 | 509 | 3 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 20–481 | 452 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 318–319 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 323–372 | 41 | 4 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 323–331 | 4 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 368–373 | 5 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 373–539 | 152 | 4 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 379–497 | 82 | 6 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 381–535 | 140 | 4 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 381–535 | 145 | 3 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 390–488 | 92 | 5 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 399–524 | 94 | 6 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 399–400 | 2 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 408–418 | 10 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 412–539 | 124 | 2 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 416–490 | 64 | 3 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 427–539 | 107 | 3 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 433–539 | 107 | 1 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 438–484 | 34 | 4 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 465–539 | 70 | 2 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 486–512 | 16 | 2 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 528–539 | 12 | 1 | Undefined position; Undefined team |
| `42` | `48` | Position_Unknown | Team_Unknown | 530–539 | 10 | 1 | Undefined position; Undefined team |
| `43` | `49` | Position_Unknown | Team_Unknown | 535–539 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_DownBlock` on target `14` (C)
- ❌ Missing segment for action `Action_DownBlock` on target `20` (RT)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 149 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Segment 'Action_DownBlock' for track '14' has invalid range: start=303, end=302. Clamping end to start.
- ⚠️ Segment 'Action_DownBlock' for track '20' has invalid range: start=303, end=297. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [20-415] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-513] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [521-527] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-417] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-337] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-358] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-361] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-539] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-361] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-379] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-418] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-429] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-371] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-394] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-401] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-480] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [483-484] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [486-489] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [497-526] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [528-535] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [537-539] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-421] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-449] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [451-468] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [470-474] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-478] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-361] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-364] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-377] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-405] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-420] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-539] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-394] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-404] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-447] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-288] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-301] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-335] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-49] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-106] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-268] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-307] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-288] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-301] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-38] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-458] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-481] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-302] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-356] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-369] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-391] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-395] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-46] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-61] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-149] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-282] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-302] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-393] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-401] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-444] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-450] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-51] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-59] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-282] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-65] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-157] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-289] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-301] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-64] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-86] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-124] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-288] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-297] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-286] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-302] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [320-327] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [330-343] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [347-356] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-319] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-337] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-341] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-356] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-372] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-324] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-331] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-370] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-373] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-375] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-386] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-401] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-384] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-396] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-400] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-418] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-470] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [491-497] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-428] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-517] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [523-526] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [533-535] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-514] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [519-526] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [533-535] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-418] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-457] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [459-467] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [469-478] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [483-488] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-400] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-418] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-455] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [459-460] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-478] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [483-524] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-400] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-415] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-418] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-418] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-539] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-418] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-473] for track '35' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [481-490] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-448] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [451-513] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-444] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-456] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [459-473] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [483-484] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [465-468] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [486-499] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [511-512] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [535-539] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>