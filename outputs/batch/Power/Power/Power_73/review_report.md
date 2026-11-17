# Play-Annotation-Generator Annotation Review — Power_73

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_73`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 569
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | defense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 23 | START | 23 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 23 | START | 23 | 415 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 23 | START | 23 | 342 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 23 | START | 23 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 23 | START | 23 | 393 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `15` | `Group` | 23 | START | 23 | 401 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 23 | START | 23 | 546 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 23 | START | 23 | 367 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 23 | START | 23 | 342 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 23 | START | 23 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 23 | START | 23 | 453 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | `10` | `10` | 343 | START | 343 | 352 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `20` | `20` | 343 | START | 343 | 393 |
| ✅ EXACT | `Action_DownBlock` | RT | `21` | `21` | 343 | START | 343 | 394 |
| ✅ EXACT | `Action_PullBlock` | LG | `11` | `11` | 343 | START | 343 | 385 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 23–569
- **Visible Samples:** 543

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 546 | 524 | inferred_complete_timeline |
| `Action_PreSnap` | 551 | 569 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 23–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 359 | 337 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 23–419
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 419 | 397 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 23–415
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 415 | 393 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 23–393
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 393 | 371 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 23–569
- **Visible Samples:** 543

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 401 | 379 | inferred_complete_timeline |
| `Action_PreSnap` | 406 | 569 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 23–485
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 453 | 431 | inferred_complete_timeline |
| `Action_PreSnap` | 467 | 485 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 23–490
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 342 | 320 | inferred_complete_timeline |
| `Action_PullBlock` | 343 | 385 | 43 | inferred_complete_timeline |
| `Action_None` | 412 | 416 | 5 | inferred_complete_timeline |
| `Action_None` | 428 | 429 | 2 | inferred_complete_timeline |
| `Action_None` | 432 | 490 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 23–477
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 367 | 345 | inferred_complete_timeline |
| `Action_PreSnap` | 402 | 406 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 420 | 444 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 446 | 449 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 452 | 458 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 470 | 471 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 473 | 477 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 23–481
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 342 | 320 | inferred_complete_timeline |
| `Action_DownBlock` | 343 | 393 | 51 | inferred_complete_timeline |
| `Action_DownBlock` | 396 | 396 | 1 | inferred_complete_timeline |
| `Action_None` | 397 | 397 | 1 | inferred_complete_timeline |
| `Action_None` | 408 | 481 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 23–485
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 142 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 342 | 199 | inferred_complete_timeline |
| `Action_DownBlock` | 343 | 394 | 52 | inferred_complete_timeline |
| `Action_None` | 415 | 485 | 71 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 23–420
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 375 | 353 | inferred_complete_timeline |
| `Action_PreSnap` | 417 | 420 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 23–569
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 359 | 337 | inferred_complete_timeline |
| `Action_PreSnap` | 366 | 367 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 369 | 476 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 478 | 569 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 23–380
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 342 | 320 | inferred_complete_timeline |
| `Action_DownBlock` | 343 | 352 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 358 | 363 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 367 | 375 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 377 | 380 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 23–482
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 356 | 334 | inferred_complete_timeline |
| `Action_PreSnap` | 365 | 394 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 396 | 398 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 400 | 401 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 403 | 407 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 413 | 417 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 433 | 434 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 441 | 446 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 450 | 455 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 457 | 464 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 467 | 482 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 23–387
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 387 | 365 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 23–443
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 425 | 403 | inferred_complete_timeline |
| `Action_PreSnap` | 437 | 443 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 23–485
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 416 | 394 | inferred_complete_timeline |
| `Action_PreSnap` | 482 | 485 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 23–398
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 398 | 376 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 23–413
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 413 | 391 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 23–569
- **Visible Samples:** 542

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 542 | 520 | inferred_complete_timeline |
| `Action_PreSnap` | 544 | 551 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 556 | 569 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 23–365 | 343 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 367–569 | 203 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 412–420 | 7 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 431–569 | 138 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 435–569 | 134 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 438–569 | 130 | 3 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 441–445 | 5 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 441–448 | 6 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 454–499 | 42 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 470–483 | 14 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 483–485 | 3 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 556–563 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 75 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [23-419] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-415] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-365] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-367] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-476] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-413] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-542] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [544-551] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-375] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-420] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-398] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-356] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-394] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-398] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-401] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-407] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-417] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-434] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-446] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-455] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [457-464] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-482] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-453] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-485] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [343-352] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [358-363] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [367-375] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [377-380] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [343-385] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-416] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-490] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-425] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-443] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-393] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-401] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-569] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-387] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-416] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [482-485] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-546] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-367] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-406] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-444] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-449] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-458] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [470-471] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [473-477] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-342] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [343-393] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 397, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [397-397] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-481] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-142] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [343-394] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-485] for track '21' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-569] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-416] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-420] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-456] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-438] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-452] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-542] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-445] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-443] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-448] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-455] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [459-464] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-499] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [470-483] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [483-485] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [556-559] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [562-563] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>