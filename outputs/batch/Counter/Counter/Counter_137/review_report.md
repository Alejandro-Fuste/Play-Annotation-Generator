# Play-Annotation-Generator Annotation Review — Counter_137

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_137`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Fumble`
- **Result Frame:** 629
- **Player Tracks:** 71
- **Ball Tracks:** 0
- **Action Segments:** 325
- **Validation Warnings:** 389
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 301
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB2 | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `10` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `22` | `Group` | 0 | START | 0 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 88 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 86 | START | 86 | 99 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `13` | `12` | 89 | START | 100 | 200 |
| ✅ EXACT | `Action_DownBlock` | LT | `9` | `8` | 89 | START | 89 | 200 |
| ✅ EXACT | `Action_PullBlock` | RG | `21` | `20` | 89 | START | 89 | 174 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `20` | `19` | 89 | START | 89 | 182 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 99 | END | 86 | 99 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `16` | 110 | START | 110 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB2 | `22` | `21` | 142 | START | 142 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 200 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–463
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_SnapReceive` | 86 | 99 | 14 | inferred_complete_timeline |
| `Action_None` | 100 | 109 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 110 | 141 | 32 | inferred_complete_timeline |
| `Action_None` | 142 | 463 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–498
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 270 | 185 | inferred_complete_timeline |
| `Action_None` | 273 | 331 | 59 | inferred_complete_timeline |
| `Action_None` | 336 | 340 | 5 | inferred_complete_timeline |
| `Action_None` | 344 | 377 | 34 | inferred_complete_timeline |
| `Action_None` | 381 | 389 | 9 | inferred_complete_timeline |
| `Action_None` | 393 | 394 | 2 | inferred_complete_timeline |
| `Action_None` | 398 | 399 | 2 | inferred_complete_timeline |
| `Action_None` | 402 | 403 | 2 | inferred_complete_timeline |
| `Action_None` | 406 | 408 | 3 | inferred_complete_timeline |
| `Action_None` | 414 | 416 | 3 | inferred_complete_timeline |
| `Action_None` | 423 | 424 | 2 | inferred_complete_timeline |
| `Action_None` | 450 | 454 | 5 | inferred_complete_timeline |
| `Action_None` | 461 | 466 | 6 | inferred_complete_timeline |
| `Action_None` | 468 | 498 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_BallCarry` | 142 | 269 | 128 | inferred_complete_timeline |
| `Action_BallCarry` | 276 | 281 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 285 | 334 | 50 | inferred_complete_timeline |
| `Action_BallCarry` | 337 | 344 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 347 | 349 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 352 | 354 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 356 | 513 | 158 | inferred_complete_timeline |
| `Action_BallCarry` | 526 | 538 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 542 | 629 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–625
- **Visible Samples:** 623

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 465 | 380 | inferred_complete_timeline |
| `Action_None` | 467 | 602 | 136 | inferred_complete_timeline |
| `Action_None` | 605 | 625 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–600
- **Visible Samples:** 593

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 345 | 260 | inferred_complete_timeline |
| `Action_None` | 349 | 593 | 245 | inferred_complete_timeline |
| `Action_None` | 599 | 600 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–501
- **Visible Samples:** 489

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 316 | 231 | inferred_complete_timeline |
| `Action_None` | 322 | 324 | 3 | inferred_complete_timeline |
| `Action_None` | 328 | 469 | 142 | inferred_complete_timeline |
| `Action_None` | 473 | 474 | 2 | inferred_complete_timeline |
| `Action_None` | 477 | 501 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 620

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_DownBlock` | 89 | 200 | 112 | inferred_complete_timeline |
| `Action_None` | 201 | 302 | 102 | inferred_complete_timeline |
| `Action_None` | 305 | 619 | 315 | inferred_complete_timeline |
| `Action_None` | 628 | 629 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–501
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 129 | 44 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 294 | 141 | inferred_complete_timeline |
| `Action_None` | 298 | 302 | 5 | inferred_complete_timeline |
| `Action_None` | 305 | 483 | 179 | inferred_complete_timeline |
| `Action_None` | 485 | 501 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–424
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_BallSnap` | 86 | 99 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 100 | 200 | 101 | inferred_complete_timeline |
| `Action_None` | 201 | 238 | 38 | inferred_complete_timeline |
| `Action_None` | 242 | 271 | 30 | inferred_complete_timeline |
| `Action_None` | 277 | 281 | 5 | inferred_complete_timeline |
| `Action_None` | 288 | 294 | 7 | inferred_complete_timeline |
| `Action_None` | 314 | 319 | 6 | inferred_complete_timeline |
| `Action_None` | 326 | 411 | 86 | inferred_complete_timeline |
| `Action_None` | 414 | 420 | 7 | inferred_complete_timeline |
| `Action_None` | 422 | 424 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_PullBlock` | 89 | 174 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 89 | 182 | 94 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 282 | 197 | inferred_complete_timeline |
| `Action_None` | 284 | 287 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 209 | 124 | inferred_complete_timeline |
| `Action_None` | 217 | 219 | 3 | inferred_complete_timeline |
| `Action_None` | 225 | 228 | 4 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_None` | 233 | 269 | 37 | inferred_complete_timeline |
| `Action_None` | 287 | 292 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 114 | 29 | inferred_complete_timeline |
| `Action_None` | 127 | 195 | 69 | inferred_complete_timeline |
| `Action_None` | 197 | 201 | 5 | inferred_complete_timeline |
| `Action_None` | 205 | 269 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 269 | 184 | inferred_complete_timeline |
| `Action_None` | 277 | 279 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–282
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 229 | 144 | inferred_complete_timeline |
| `Action_None` | 234 | 242 | 9 | inferred_complete_timeline |
| `Action_None` | 249 | 269 | 21 | inferred_complete_timeline |
| `Action_None` | 279 | 282 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 268 | 183 | inferred_complete_timeline |
| `Action_None` | 271 | 288 | 18 | inferred_complete_timeline |
| `Action_None` | 290 | 293 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–468
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 400 | 315 | inferred_complete_timeline |
| `Action_None` | 402 | 420 | 19 | inferred_complete_timeline |
| `Action_None` | 422 | 450 | 29 | inferred_complete_timeline |
| `Action_None` | 461 | 468 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 163 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 597

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 328 | 243 | inferred_complete_timeline |
| `Action_None` | 330 | 334 | 5 | inferred_complete_timeline |
| `Action_None` | 343 | 352 | 10 | inferred_complete_timeline |
| `Action_None` | 356 | 416 | 61 | inferred_complete_timeline |
| `Action_None` | 423 | 432 | 10 | inferred_complete_timeline |
| `Action_None` | 438 | 535 | 98 | inferred_complete_timeline |
| `Action_None` | 537 | 577 | 41 | inferred_complete_timeline |
| `Action_None` | 587 | 629 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 585

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 250 | 165 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 283 | 29 | inferred_complete_timeline |
| `Action_None` | 287 | 297 | 11 | inferred_complete_timeline |
| `Action_None` | 302 | 320 | 19 | inferred_complete_timeline |
| `Action_None` | 323 | 386 | 64 | inferred_complete_timeline |
| `Action_None` | 389 | 411 | 23 | inferred_complete_timeline |
| `Action_None` | 414 | 583 | 170 | inferred_complete_timeline |
| `Action_None` | 612 | 616 | 5 | inferred_complete_timeline |
| `Action_None` | 618 | 619 | 2 | inferred_complete_timeline |
| `Action_None` | 621 | 629 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 388 | 303 | inferred_complete_timeline |
| `Action_None` | 390 | 392 | 3 | inferred_complete_timeline |
| `Action_None` | 398 | 400 | 3 | inferred_complete_timeline |
| `Action_None` | 403 | 406 | 4 | inferred_complete_timeline |
| `Action_None` | 408 | 420 | 13 | inferred_complete_timeline |
| `Action_None` | 422 | 427 | 6 | inferred_complete_timeline |
| `Action_None` | 430 | 503 | 74 | inferred_complete_timeline |
| `Action_None` | 505 | 572 | 68 | inferred_complete_timeline |
| `Action_None` | 579 | 593 | 15 | inferred_complete_timeline |
| `Action_None` | 600 | 601 | 2 | inferred_complete_timeline |
| `Action_None` | 605 | 606 | 2 | inferred_complete_timeline |
| `Action_None` | 609 | 613 | 5 | inferred_complete_timeline |
| `Action_None` | 620 | 629 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 168–170 | 3 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 173–629 | 386 | 13 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 173–402 | 230 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 190–384 | 195 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 252–256 | 4 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 283–629 | 339 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 289–623 | 202 | 29 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 291–292 | 2 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 294–295 | 2 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 296–629 | 311 | 3 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 299–300 | 2 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 316–513 | 111 | 15 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 316–317 | 2 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 320–629 | 285 | 3 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 328–489 | 84 | 16 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 346–629 | 236 | 13 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 361–629 | 211 | 7 | Undefined position; Undefined team |
| `40` | `60` | Position_Unknown | Team_Unknown | 365–368 | 4 | 1 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 381–384 | 4 | 1 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 392–417 | 22 | 2 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 406–408 | 3 | 1 | Undefined position; Undefined team |
| `44` | `71` | Position_Unknown | Team_Unknown | 419–629 | 149 | 9 | Undefined position; Undefined team |
| `45` | `72` | Position_Unknown | Team_Unknown | 419–476 | 31 | 5 | Undefined position; Undefined team |
| `46` | `79` | Position_Unknown | Team_Unknown | 426–531 | 97 | 4 | Undefined position; Undefined team |
| `47` | `81` | Position_Unknown | Team_Unknown | 433–446 | 14 | 1 | Undefined position; Undefined team |
| `48` | `91` | Position_Unknown | Team_Unknown | 445–450 | 6 | 1 | Undefined position; Undefined team |
| `49` | `96` | Position_Unknown | Team_Unknown | 474–629 | 151 | 3 | Undefined position; Undefined team |
| `50` | `100` | Position_Unknown | Team_Unknown | 482–496 | 12 | 4 | Undefined position; Undefined team |
| `51` | `102` | Position_Unknown | Team_Unknown | 483–576 | 85 | 3 | Undefined position; Undefined team |
| `52` | `103` | Position_Unknown | Team_Unknown | 484–629 | 146 | 1 | Undefined position; Undefined team |
| `53` | `105` | Position_Unknown | Team_Unknown | 488–543 | 52 | 2 | Undefined position; Undefined team |
| `54` | `106` | Position_Unknown | Team_Unknown | 496–516 | 19 | 2 | Undefined position; Undefined team |
| `55` | `108` | Position_Unknown | Team_Unknown | 510–620 | 111 | 1 | Undefined position; Undefined team |
| `56` | `109` | Position_Unknown | Team_Unknown | 512–611 | 48 | 7 | Undefined position; Undefined team |
| `57` | `113` | Position_Unknown | Team_Unknown | 522–629 | 80 | 6 | Undefined position; Undefined team |
| `58` | `114` | Position_Unknown | Team_Unknown | 522–617 | 96 | 1 | Undefined position; Undefined team |
| `59` | `116` | Position_Unknown | Team_Unknown | 536–613 | 70 | 3 | Undefined position; Undefined team |
| `60` | `120` | Position_Unknown | Team_Unknown | 550–551 | 2 | 1 | Undefined position; Undefined team |
| `61` | `124` | Position_Unknown | Team_Unknown | 566–567 | 2 | 1 | Undefined position; Undefined team |
| `62` | `125` | Position_Unknown | Team_Unknown | 570–590 | 21 | 1 | Undefined position; Undefined team |
| `63` | `126` | Position_Unknown | Team_Unknown | 577–606 | 29 | 2 | Undefined position; Undefined team |
| `64` | `127` | Position_Unknown | Team_Unknown | 585–588 | 4 | 1 | Undefined position; Undefined team |
| `65` | `129` | Position_Unknown | Team_Unknown | 588–629 | 39 | 2 | Undefined position; Undefined team |
| `66` | `131` | Position_Unknown | Team_Unknown | 602–616 | 10 | 2 | Undefined position; Undefined team |
| `67` | `132` | Position_Unknown | Team_Unknown | 605–629 | 25 | 1 | Undefined position; Undefined team |
| `68` | `134` | Position_Unknown | Team_Unknown | 615–629 | 15 | 1 | Undefined position; Undefined team |
| `69` | `136` | Position_Unknown | Team_Unknown | 621–629 | 9 | 1 | Undefined position; Undefined team |
| `70` | `137` | Position_Unknown | Team_Unknown | 622–629 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `13` (C): Annotated start 89 != Inferred start 100
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (9 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 49 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 49 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 98 |
| Missing visible bounding boxes during action | 287 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (LT) duration 112 frames exceeds threshold 90 frames [start=89, end=200].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (C) duration 112 frames exceeds threshold 90 frames [start=89, end=200].
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [86–99], lower_priority='Action_DownBlock' annotated_start=89, effective_Action_DownBlock_start=100.
- ⚠️ Action 'Action_None' range [86-465] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-602] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-625] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-345] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-593] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-600] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-282] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-114] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-195] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-400] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-420] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-450] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-468] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-316] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-469] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-501] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-229] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-242] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [89-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-302] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-619] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-270] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-331] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-377] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-389] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-394] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-408] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-416] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-454] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-466] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-498] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-268] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-288] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-250] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-283] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-297] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-320] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-386] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-411] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-583] for track '11' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-616] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-619] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-629] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-238] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-271] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-294] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-319] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-411] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-420] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-424] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-163] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-209] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-292] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-388] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-392] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-400] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-406] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-420] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-427] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-503] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-572] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-593] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-601] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-606] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-613] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-463] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-328] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-334] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-352] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-416] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-432] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-535] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-577] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-629] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-129] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-294] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-302] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-483] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-501] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [89-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [89-174] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [142-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [276-281] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [285-334] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [337-344] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [347-349] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [352-354] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [356-513] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [526-538] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-268] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-280] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-402] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-421] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-476] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-502] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-518] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-532] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-577] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-629] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-402] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-384] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-370] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-623] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-294] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-308] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-335] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-353] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-368] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-379] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-397] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-435] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-438] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-446] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-459] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-475] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-485] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-498] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-506] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-515] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-525] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-544] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-558] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-571] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-580] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-594] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-598] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-604] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-623] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-300] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-629] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-327] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-345] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-354] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-367] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-383] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-403] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-425] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-445] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-473] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-486] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-491] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-501] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-507] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-513] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-533] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-560] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-342] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-353] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-362] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-372] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-376] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-391] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-420] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-423] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-459] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-474] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-478] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-489] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-366] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-374] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-400] for track '38' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-437] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-440] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-453] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-473] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-535] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-579] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-595] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-602] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-609] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-629] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-364] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-407] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-368] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-411] for track '42' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-408] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-430] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-435] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-445] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-478] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-489] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-537] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-554] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-616] for track '44' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-424] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-443] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-467] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-476] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-435] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-459] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-523] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-531] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-446] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-450] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-481] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-528] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-629] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-486] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-490] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-493] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-496] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-486] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-569] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-576] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-629] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-533] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-543] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-508] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-516] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-620] for track '55' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-513] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-523] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-558] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-569] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-585] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-611] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-528] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-537] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-546] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-549] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-611] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-629] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-617] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-572] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-581] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-613] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-590] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-587] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-606] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-588] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-603] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-609] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-616] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-629] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-623] for track '70' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.

</details>