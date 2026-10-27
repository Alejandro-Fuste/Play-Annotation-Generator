# Play-Annotation-Generator Annotation Review — Counter_2

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_2`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 569
- **Player Tracks:** 41
- **Ball Tracks:** 1
- **Action Segments:** 151
- **Validation Warnings:** 167
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `7` | `6` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 393 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 386 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 2 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 386 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 397 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 394 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 397 |
| ✅ EXACT | `Action_PullBlock` | LG | `13` | `12` | 385 | START | 385 | 469 |
| ⚠️ START CHANGED | `Action_BallSnap` | C | `17` | `16` | 387 | START | 389 | 397 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | `10` | `9` | 394 | START | 394 | 422 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `7` | `6` | 395 | START | 395 | 454 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `17` | `16` | 398 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `5` | `4` | 398 | START | 398 | 453 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `8` | `7` | 398 | START | 398 | 411 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 401 | END | 387 | 401 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `12` | `11` | 417 | START | 417 | 420 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `9` | 425 | START | 425 | 516 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 469 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–470
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 386 | 387 | inferred_complete_timeline |
| `Action_SnapReceive` | 387 | 401 | 15 | inferred_complete_timeline |
| `Action_None` | 402 | 416 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 417 | 420 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 422 | 424 | 3 | inferred_complete_timeline |
| `Action_None` | 425 | 470 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 393 | 394 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 394 | 422 | 29 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 424 | 424 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 425 | 516 | 92 | inferred_complete_timeline |
| `Action_BallCarry` | 519 | 527 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 530 | 536 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 544 | 569 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 564

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 394 | 395 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 395 | 454 | 60 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 456 | 460 | 5 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 465 | 469 | 5 | inferred_complete_timeline |
| `Action_None` | 470 | 471 | 2 | inferred_complete_timeline |
| `Action_None` | 473 | 569 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 386 | 387 | inferred_complete_timeline |
| `Action_None` | 387 | 447 | 61 | inferred_complete_timeline |
| `Action_None` | 456 | 569 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 564

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 384 | 194 | inferred_complete_timeline |
| `Action_PullBlock` | 385 | 469 | 85 | inferred_complete_timeline |
| `Action_None` | 470 | 509 | 40 | inferred_complete_timeline |
| `Action_None` | 513 | 569 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 2–397
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 22 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 68 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 163 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 172 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 246 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 268 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 318 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 327 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 333 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 343 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 356 | 366 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 368 | 369 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 377 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 389 | 397 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 397 | 398 | inferred_complete_timeline |
| `Action_DownBlock` | 398 | 411 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 413 | 415 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 436 | 437 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 445 | 448 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–517
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 397 | 398 | inferred_complete_timeline |
| `Action_DownBlock` | 398 | 453 | 56 | inferred_complete_timeline |
| `Action_DownBlock` | 457 | 458 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 460 | 461 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 469 | 469 | 1 | inferred_complete_timeline |
| `Action_None` | 470 | 491 | 22 | inferred_complete_timeline |
| `Action_None` | 493 | 505 | 13 | inferred_complete_timeline |
| `Action_None` | 507 | 517 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 252 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 386 | 387 | inferred_complete_timeline |
| `Action_None` | 387 | 505 | 119 | inferred_complete_timeline |
| `Action_None` | 509 | 569 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 44 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 84 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 143 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 170 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 183 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 192 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 207 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 217 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–464
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 180 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 211 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 264 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 320 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 386 | 63 | inferred_complete_timeline |
| `Action_None` | 387 | 390 | 4 | inferred_complete_timeline |
| `Action_None` | 417 | 458 | 42 | inferred_complete_timeline |
| `Action_None` | 461 | 464 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–503
- **Visible Samples:** 461

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 386 | 387 | inferred_complete_timeline |
| `Action_None` | 387 | 458 | 72 | inferred_complete_timeline |
| `Action_None` | 502 | 503 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 529

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 386 | 387 | inferred_complete_timeline |
| `Action_None` | 387 | 425 | 39 | inferred_complete_timeline |
| `Action_None` | 465 | 466 | 2 | inferred_complete_timeline |
| `Action_None` | 469 | 569 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–496
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 386 | 387 | inferred_complete_timeline |
| `Action_None` | 387 | 449 | 63 | inferred_complete_timeline |
| `Action_None` | 452 | 453 | 2 | inferred_complete_timeline |
| `Action_None` | 463 | 466 | 4 | inferred_complete_timeline |
| `Action_None` | 487 | 493 | 7 | inferred_complete_timeline |
| `Action_None` | 495 | 496 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 557

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 386 | 387 | inferred_complete_timeline |
| `Action_None` | 387 | 537 | 151 | inferred_complete_timeline |
| `Action_None` | 539 | 540 | 2 | inferred_complete_timeline |
| `Action_None` | 548 | 560 | 13 | inferred_complete_timeline |
| `Action_None` | 566 | 569 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–538
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 386 | 387 | inferred_complete_timeline |
| `Action_None` | 387 | 526 | 140 | inferred_complete_timeline |
| `Action_None` | 535 | 538 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 74–75 | 2 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 218–290 | 5 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 250–569 | 319 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 284–569 | 195 | 13 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 319–327 | 9 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 406–489 | 84 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 427–569 | 143 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 433–569 | 128 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 450–451 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 455–459 | 5 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 467–539 | 73 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 467–569 | 103 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 469–478 | 5 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 470–539 | 70 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 470–569 | 100 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 474–569 | 85 | 4 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 474–478 | 4 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 478–566 | 89 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 490–491 | 2 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 490–569 | 77 | 2 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 499–500 | 2 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 513–569 | 48 | 2 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 546–569 | 24 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 562–569 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `35` | `44` | 488 | 495 | 8 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `17` (C): Annotated start 387 != Inferred start 389
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `7` (3 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `17` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (4 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 117 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Segment 'Action_DownBlock' for track '16' has invalid range: start=398, end=397. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-386] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-505] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-569] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-526] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-538] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-447] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-537] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-560] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [398-453] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [457-458] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [460-461] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-491] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-505] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-517] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-425] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-466] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [395-454] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [456-460] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [398-411] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [413-415] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [436-437] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [445-448] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-171] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-211] for track '8' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-264] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-320] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-386] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-390] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-458] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-464] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [394-422] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [425-516] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [519-527] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [530-536] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-449] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-466] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-493] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-496] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [417-420] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-470] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-384] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-509] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-44] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-84] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-143] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-146] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-170] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-183] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-192] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-200] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-207] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-217] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-252] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-458] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-22] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-63] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-68] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-163] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-246] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-268] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-318] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-327] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-333] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-343] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-366] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-369] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-377] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [389-397] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-219] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-290] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-386] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-541] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-290] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-373] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-381] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-392] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-397] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-411] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-419] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-449] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-453] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-468] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-509] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-327] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-489] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-449] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-569] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-451] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-459] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-539] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-471] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-539] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-476] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-484] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-500] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-566] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-549] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-553] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-564] for track '41' has 1 frames without a visible bounding box.
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

</details>