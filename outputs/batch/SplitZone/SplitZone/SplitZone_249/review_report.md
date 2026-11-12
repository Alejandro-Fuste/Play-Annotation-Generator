# Play-Annotation-Generator Annotation Review — SplitZone_249

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_249`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 569
- **Player Tracks:** 57
- **Ball Tracks:** 0
- **Action Segments:** 210
- **Validation Warnings:** 252
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 191
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LB1 | defense | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `18` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 4 | START | 5 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 4 | START | 5 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 4 | START | 5 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 4 | START | 5 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 4 | START | 5 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 4 | START | 5 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 4 | START | 5 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 4 | START | 5 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 4 | START | 5 | 184 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 185 | START | 185 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `12` | 190 | START | 199 | 204 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `17` | `17` | 190 | START | 190 | 202 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `19` | 190 | START | 190 | 194 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `20` | 190 | START | 190 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LB1 | `15` | `15` | 195 | START | 195 | 227 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 198 | END | 185 | 198 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `11` | 204 | START | 204 | 216 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `18` | `18` | 217 | START | 217 | 487 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 319 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 5–379
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 184 | 180 | inferred_complete_timeline |
| `Action_SnapReceive` | 185 | 198 | 14 | inferred_complete_timeline |
| `Action_None` | 199 | 203 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 204 | 216 | 13 | inferred_complete_timeline |
| `Action_None` | 217 | 366 | 150 | inferred_complete_timeline |
| `Action_None` | 368 | 370 | 3 | inferred_complete_timeline |
| `Action_None` | 372 | 375 | 4 | inferred_complete_timeline |
| `Action_None` | 378 | 379 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 5–497
- **Visible Samples:** 489

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 31 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 216 | 184 | inferred_complete_timeline |
| `Action_BallCarry` | 217 | 487 | 271 | inferred_complete_timeline |
| `Action_BallCarry` | 489 | 491 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 494 | 497 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 5–467
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 184 | 180 | inferred_complete_timeline |
| `Action_None` | 185 | 467 | 283 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 5–500
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 184 | 180 | inferred_complete_timeline |
| `Action_None` | 185 | 406 | 222 | inferred_complete_timeline |
| `Action_None` | 409 | 419 | 11 | inferred_complete_timeline |
| `Action_None` | 421 | 423 | 3 | inferred_complete_timeline |
| `Action_None` | 447 | 453 | 7 | inferred_complete_timeline |
| `Action_None` | 468 | 471 | 4 | inferred_complete_timeline |
| `Action_None` | 473 | 480 | 8 | inferred_complete_timeline |
| `Action_None` | 484 | 495 | 12 | inferred_complete_timeline |
| `Action_None` | 497 | 500 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 5–557
- **Visible Samples:** 513

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 184 | 180 | inferred_complete_timeline |
| `Action_None` | 185 | 239 | 55 | inferred_complete_timeline |
| `Action_None` | 241 | 269 | 29 | inferred_complete_timeline |
| `Action_None` | 273 | 275 | 3 | inferred_complete_timeline |
| `Action_None` | 280 | 282 | 3 | inferred_complete_timeline |
| `Action_None` | 285 | 294 | 10 | inferred_complete_timeline |
| `Action_None` | 297 | 329 | 33 | inferred_complete_timeline |
| `Action_None` | 341 | 342 | 2 | inferred_complete_timeline |
| `Action_None` | 348 | 351 | 4 | inferred_complete_timeline |
| `Action_None` | 362 | 371 | 10 | inferred_complete_timeline |
| `Action_None` | 374 | 557 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 5–202
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 189 | 185 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 202 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 5–569
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 189 | 185 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 194 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 202 | 319 | 118 | inferred_complete_timeline |
| `Action_None` | 320 | 539 | 220 | inferred_complete_timeline |
| `Action_None` | 541 | 543 | 3 | inferred_complete_timeline |
| `Action_None` | 546 | 559 | 14 | inferred_complete_timeline |
| `Action_None` | 561 | 569 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 5–424
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 184 | 180 | inferred_complete_timeline |
| `Action_BallSnap` | 185 | 198 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 199 | 204 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 245 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 255 | 319 | 65 | inferred_complete_timeline |
| `Action_None` | 320 | 364 | 45 | inferred_complete_timeline |
| `Action_None` | 368 | 372 | 5 | inferred_complete_timeline |
| `Action_None` | 375 | 401 | 27 | inferred_complete_timeline |
| `Action_None` | 403 | 405 | 3 | inferred_complete_timeline |
| `Action_None` | 415 | 416 | 2 | inferred_complete_timeline |
| `Action_None` | 419 | 420 | 2 | inferred_complete_timeline |
| `Action_None` | 423 | 424 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 5–206
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 189 | 185 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 206 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 5–237
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 184 | 180 | inferred_complete_timeline |
| `Action_None` | 185 | 237 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 5–362
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 184 | 180 | inferred_complete_timeline |
| `Action_None` | 185 | 362 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 5–219
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 184 | 180 | inferred_complete_timeline |
| `Action_None` | 185 | 219 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 5–563
- **Visible Samples:** 514

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 194 | 190 | inferred_complete_timeline |
| `Action_SplitBlock` | 195 | 227 | 33 | inferred_complete_timeline |
| `Action_SplitBlock` | 229 | 231 | 3 | inferred_complete_timeline |
| `Action_SplitBlock` | 234 | 319 | 86 | inferred_complete_timeline |
| `Action_None` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_None` | 326 | 378 | 53 | inferred_complete_timeline |
| `Action_None` | 380 | 383 | 4 | inferred_complete_timeline |
| `Action_None` | 386 | 410 | 25 | inferred_complete_timeline |
| `Action_None` | 413 | 414 | 2 | inferred_complete_timeline |
| `Action_None` | 417 | 437 | 21 | inferred_complete_timeline |
| `Action_None` | 446 | 453 | 8 | inferred_complete_timeline |
| `Action_None` | 462 | 494 | 33 | inferred_complete_timeline |
| `Action_None` | 503 | 505 | 3 | inferred_complete_timeline |
| `Action_None` | 507 | 515 | 9 | inferred_complete_timeline |
| `Action_None` | 519 | 531 | 13 | inferred_complete_timeline |
| `Action_None` | 533 | 544 | 12 | inferred_complete_timeline |
| `Action_None` | 547 | 563 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 5–569
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 184 | 180 | inferred_complete_timeline |
| `Action_None` | 185 | 569 | 385 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 5–569
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 184 | 180 | inferred_complete_timeline |
| `Action_None` | 185 | 485 | 301 | inferred_complete_timeline |
| `Action_None` | 491 | 569 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 5–569
- **Visible Samples:** 551

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 184 | 180 | inferred_complete_timeline |
| `Action_None` | 185 | 288 | 104 | inferred_complete_timeline |
| `Action_None` | 299 | 302 | 4 | inferred_complete_timeline |
| `Action_None` | 305 | 477 | 173 | inferred_complete_timeline |
| `Action_None` | 480 | 569 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 5–517
- **Visible Samples:** 513

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 184 | 180 | inferred_complete_timeline |
| `Action_None` | 185 | 517 | 333 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 5–467
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 184 | 180 | inferred_complete_timeline |
| `Action_None` | 185 | 467 | 283 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 5–496
- **Visible Samples:** 481

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 184 | 180 | inferred_complete_timeline |
| `Action_None` | 185 | 267 | 83 | inferred_complete_timeline |
| `Action_None` | 272 | 481 | 210 | inferred_complete_timeline |
| `Action_None` | 483 | 487 | 5 | inferred_complete_timeline |
| `Action_None` | 494 | 496 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 5–567
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 184 | 180 | inferred_complete_timeline |
| `Action_None` | 185 | 303 | 119 | inferred_complete_timeline |
| `Action_None` | 308 | 318 | 11 | inferred_complete_timeline |
| `Action_None` | 325 | 327 | 3 | inferred_complete_timeline |
| `Action_None` | 339 | 345 | 7 | inferred_complete_timeline |
| `Action_None` | 350 | 357 | 8 | inferred_complete_timeline |
| `Action_None` | 364 | 375 | 12 | inferred_complete_timeline |
| `Action_None` | 378 | 395 | 18 | inferred_complete_timeline |
| `Action_None` | 414 | 416 | 3 | inferred_complete_timeline |
| `Action_None` | 436 | 437 | 2 | inferred_complete_timeline |
| `Action_None` | 469 | 504 | 36 | inferred_complete_timeline |
| `Action_None` | 506 | 515 | 10 | inferred_complete_timeline |
| `Action_None` | 518 | 523 | 6 | inferred_complete_timeline |
| `Action_None` | 525 | 538 | 14 | inferred_complete_timeline |
| `Action_None` | 542 | 543 | 2 | inferred_complete_timeline |
| `Action_None` | 547 | 551 | 5 | inferred_complete_timeline |
| `Action_None` | 553 | 554 | 2 | inferred_complete_timeline |
| `Action_None` | 561 | 567 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 5–569 | 548 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 19–45 | 24 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 219–558 | 319 | 8 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 232–466 | 216 | 3 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 237–569 | 333 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 247–569 | 290 | 11 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 268–387 | 120 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 312–313 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 340–569 | 230 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 351–354 | 4 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 352–353 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 389–403 | 13 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 402–403 | 2 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 408–409 | 2 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 411–413 | 3 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 417–529 | 86 | 4 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 419–438 | 15 | 2 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 434–435 | 2 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 448–449 | 2 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 449–569 | 78 | 11 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 457–567 | 60 | 8 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 466–468 | 3 | 1 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 472–569 | 98 | 1 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 494–516 | 7 | 2 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 502–569 | 61 | 3 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 502–569 | 66 | 3 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 509–510 | 2 | 1 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 515–518 | 4 | 1 | Undefined position; Undefined team |
| `49` | `72` | Position_Unknown | Team_Unknown | 518–520 | 3 | 1 | Undefined position; Undefined team |
| `50` | `73` | Position_Unknown | Team_Unknown | 519–569 | 45 | 5 | Undefined position; Undefined team |
| `51` | `77` | Position_Unknown | Team_Unknown | 526–569 | 44 | 1 | Undefined position; Undefined team |
| `52` | `78` | Position_Unknown | Team_Unknown | 526–528 | 3 | 1 | Undefined position; Undefined team |
| `53` | `80` | Position_Unknown | Team_Unknown | 540–547 | 8 | 1 | Undefined position; Undefined team |
| `54` | `81` | Position_Unknown | Team_Unknown | 541–569 | 29 | 1 | Undefined position; Undefined team |
| `55` | `82` | Position_Unknown | Team_Unknown | 545–558 | 14 | 1 | Undefined position; Undefined team |
| `56` | `84` | Position_Unknown | Team_Unknown | 569–569 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 37 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 37 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 74 |
| Missing visible bounding boxes during action | 173 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 500: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (C) duration 130 frames exceeds threshold 90 frames [start=190, end=319].
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [185–198], lower_priority='Action_ZoneBlock' annotated_start=190, effective_Action_ZoneBlock_start=199.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 130 frames exceeds threshold 90 frames [start=190, end=319].
- ⚠️ Action 'Action_None' range [185-406] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-419] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-423] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-453] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-471] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-480] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-495] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-500] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-467] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-467] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-269] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-294] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-351] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-371] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-557] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-303] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-318] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-345] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-357] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-375] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-395] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-416] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-437] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-504] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-515] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-523] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-538] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-543] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-551] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-554] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-567] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-569] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-288] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-302] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-477] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-569] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-517] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-362] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-485] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-267] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-481] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-487] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-496] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-366] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-370] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-375] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [199-204] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [206-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-364] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-372] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-401] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-405] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-293] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-324] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-463] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-237] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [195-227] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [229-231] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-378] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-383] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-410] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-414] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-437] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-453] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-494] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-505] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-515] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-531] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-544] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-563] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-219] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [217-487] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [489-491] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [494-497] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-194] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-539] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-543] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-559] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-206] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-33] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-45] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-272] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-289] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-325] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-339] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-395] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-416] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-558] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-260] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-278] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-466] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-377] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-416] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-441] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-456] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-477] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-522] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-550] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-554] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-565] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-387] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-569] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-397] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-403] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-413] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-443] for track '36' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-507] for track '36' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-516] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-529] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-426] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-438] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-435] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-465] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-470] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-481] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-491] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-510] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-521] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-526] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-529] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-548] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-556] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-569] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-463] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-481] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-489] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-505] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-521] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-543] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-549] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-567] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-468] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-516] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-524] for track '45' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-530] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-569] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-540] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-559] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-569] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-518] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-520] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-551] for track '50' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-554] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-561] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-566] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-528] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-547] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-569] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-558] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>