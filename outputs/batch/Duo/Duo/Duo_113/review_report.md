# Play-Annotation-Generator Annotation Review — Duo_113

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_113`
- **Frame Range:** 0 to 568 (569 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 568
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 221
- **Validation Warnings:** 216
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 148
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BlockSecondLevel` | RB | offense | `3` | `3` |
| ✅ EXACT | `Action_ComboBlock` | LB3 | defense | `10` | `10` |
| ✅ EXACT | `Action_ComboBlock` | C | offense | `18` | `18` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | RB | offense | `3` | `3` |
| ✅ EXACT | `Action_ComboBlock` | WR2 | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 497 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 295 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 513 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 135 |
| ✅ EXACT | `Action_BlockSecondLevel` | RB | `3` | `3` | 136 | START | 136 | 191 |
| ✅ EXACT | `Action_ComboBlock` | LB3 | `10` | `10` | 136 | START | 136 | 191 |
| ✅ EXACT | `Action_ComboBlock` | C | `18` | `18` | 136 | START | 136 | 191 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | RB | `3` | `3` | 136 | START | N/A | N/A |
| ✅ EXACT | `Action_ComboBlock` | WR2 | `7` | `7` | 136 | START | 136 | 191 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 191 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–513
- **Visible Samples:** 514

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 513 | 514 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–527
- **Visible Samples:** 527

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 136 | 191 | 56 | inferred_complete_timeline |
| `Action_None` | 192 | 482 | 291 | inferred_complete_timeline |
| `Action_None` | 484 | 527 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–568
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 497 | 498 | inferred_complete_timeline |
| `Action_PreSnap` | 502 | 539 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 544 | 545 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 547 | 568 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–568
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_ComboBlock` | 136 | 191 | 56 | inferred_complete_timeline |
| `Action_None` | 192 | 568 | 377 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–556
- **Visible Samples:** 548

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 539 | 417 | inferred_complete_timeline |
| `Action_PreSnap` | 548 | 556 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–506
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 295 | 296 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 303 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 311 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 429 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 432 | 433 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 436 | 437 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 440 | 441 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 452 | 453 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 456 | 458 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 460 | 461 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 470 | 474 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 487 | 490 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 495 | 496 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 498 | 500 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 503 | 506 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–568
- **Visible Samples:** 542

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 21 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 121 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 130 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 211 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 279 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 474 | 189 | inferred_complete_timeline |
| `Action_PreSnap` | 477 | 496 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 499 | 541 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 544 | 546 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 552 | 553 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 555 | 568 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–457
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_ComboBlock` | 136 | 191 | 56 | inferred_complete_timeline |
| `Action_None` | 192 | 457 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 21 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 121 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 211 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 228 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–568
- **Visible Samples:** 519

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 21 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 117 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 151 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 207 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 279 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 295 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 303 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 453 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 458 | 462 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 464 | 538 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 540 | 541 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 543 | 568 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 5 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 41 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 105 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 117 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 207 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 275 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 279 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 291 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 295 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 303 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 311 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 433 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 436 | 437 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 440 | 441 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 444 | 445 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 448 | 521 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 524 | 525 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 528 | 533 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 536 | 537 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 540 | 541 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 544 | 545 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 552 | 553 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 556 | 568 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 500

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 114 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 437 | 317 | inferred_complete_timeline |
| `Action_PreSnap` | 440 | 441 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 444 | 481 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 528 | 538 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 548 | 549 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 551 | 557 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 562 | 568 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 5 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 46 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 105 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 114 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 211 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 275 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 279 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 295 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 303 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 311 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 316 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 429 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 432 | 433 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 450 | 568 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–563
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 5 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 45 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 71 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 279 | 172 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 538 | 258 | inferred_complete_timeline |
| `Action_PreSnap` | 544 | 554 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 556 | 563 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–563
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 211 | 185 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 522 | 309 | inferred_complete_timeline |
| `Action_PreSnap` | 524 | 525 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 527 | 558 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 562 | 563 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–518
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 117 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 211 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 279 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 421 | 136 | inferred_complete_timeline |
| `Action_PreSnap` | 424 | 426 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 432 | 433 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 449 | 466 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 474 | 518 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–525
- **Visible Samples:** 520

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_ComboBlock` | 136 | 191 | 56 | inferred_complete_timeline |
| `Action_None` | 192 | 517 | 326 | inferred_complete_timeline |
| `Action_None` | 524 | 525 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 490 | 491 | inferred_complete_timeline |
| `Action_PreSnap` | 492 | 568 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 504 | 505 | inferred_complete_timeline |
| `Action_PreSnap` | 512 | 568 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 568 | 569 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 568 | 569 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–5 | 4 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 113–568 | 171 | 17 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 314–568 | 222 | 7 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 479–498 | 20 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 563–568 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ComboBlock` on target `3` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 204 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 568 as fallback play end.
- ⚠️ Overlapping action conflict at frame 136 for track '3': 'Action_ComboBlock' vs 'Action_BlockSecondLevel'. Overriding with 'Action_BlockSecondLevel'.
- ⚠️ Action 'Action_PreSnap' range [0-497] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [502-539] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [544-545] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [547-568] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-295] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-303] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-311] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-429] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-433] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-437] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-441] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-453] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [456-458] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [460-461] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [470-474] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-490] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [495-496] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [498-500] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [503-506] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-539] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [548-556] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-482] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-527] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-490] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-117] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-211] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-279] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-421] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-426] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-433] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [449-466] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-518] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-568] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-504] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-517] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-211] for track '11' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-522] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [524-525] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [527-558] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [562-563] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-121] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-130] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-211] for track '12' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-279] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-474] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-496] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [499-541] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [544-546] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [552-553] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-114] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-437] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-441] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-481] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [528-538] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [548-549] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [551-557] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [562-568] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-41] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-105] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-117] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-207] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-275] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-279] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-291] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-295] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-303] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-311] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-433] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-437] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-441] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-445] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [448-521] for track '14' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [524-525] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [528-533] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [536-537] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [540-541] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [544-545] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [552-553] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-45] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-71] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-279] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-538] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [544-554] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [556-563] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-46] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-105] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-114] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-211] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-275] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-279] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-295] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-303] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-311] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-316] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-429] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-433] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-568] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-513] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-457] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-21] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-211] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-228] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-21] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-117] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-137] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-151] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-163] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-207] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-279] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-295] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-303] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-453] for track '20' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [458-462] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [464-538] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [540-541] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-114] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-231] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-337] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-342] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-350] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-377] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-383] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-401] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [448-534] for track '22' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [536-537] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [544-546] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-442] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-447] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [449-463] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-474] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [497-521] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [528-530] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [532-568] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [479-498] for track '24' has 1 frames without a visible bounding box.
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

</details>