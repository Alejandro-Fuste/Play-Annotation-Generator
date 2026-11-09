# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_98

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_98`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 539
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 172
- **Validation Warnings:** 211
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 134
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | QB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | RB | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `0` | `Group` | 0 | START | 3 | 355 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 3 | 316 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 3 | 292 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `18` | `Group` | 0 | START | 3 | 324 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 3 | 292 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 3 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `22` | `Group` | 0 | START | 6 | 294 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 0 | START | 3 | 292 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 3 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `8` | `Group` | 0 | START | 3 | 335 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `15` | `15` | 293 | START | 293 | 300 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 293 | START | 293 | 298 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 293 | START | 293 | 314 |
| ✅ EXACT | `Action_ZoneBlock` | C | `3` | `3` | 293 | START | 293 | 307 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | QB | `7` | `7` | 304 | START | 304 | 319 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | RB | `14` | `14` | 317 | START | 317 | 321 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 3–322
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 303 | 195 | inferred_complete_timeline |
| `Action_PressEdge` | 304 | 319 | 16 | inferred_complete_timeline |
| `Action_PressEdge` | 321 | 322 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 3–431
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 316 | 314 | inferred_complete_timeline |
| `Action_Handoff` | 317 | 321 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 323 | 333 | 11 | inferred_complete_timeline |
| `Action_None` | 334 | 380 | 47 | inferred_complete_timeline |
| `Action_None` | 382 | 405 | 24 | inferred_complete_timeline |
| `Action_None` | 410 | 431 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 3–355
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 355 | 353 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 6–308
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 294 | 289 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 308 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 3–538
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 324 | 322 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 334 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 342 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 346 | 360 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 367 | 371 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 381 | 388 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 415 | 420 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 422 | 487 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 494 | 495 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 511 | 514 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 518 | 519 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 525 | 533 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 535 | 538 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 3–539
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 335 | 333 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 352 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 377 | 382 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 386 | 388 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 419 | 503 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 509 | 513 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 524 | 532 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 535 | 539 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 3–539
- **Visible Samples:** 486

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 292 | 290 | inferred_complete_timeline |
| `Action_ZoneBlock` | 293 | 300 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 302 | 312 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 329 | 333 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 338 | 363 | 26 | inferred_complete_timeline |
| `Action_None` | 385 | 388 | 4 | inferred_complete_timeline |
| `Action_None` | 391 | 392 | 2 | inferred_complete_timeline |
| `Action_None` | 397 | 426 | 30 | inferred_complete_timeline |
| `Action_None` | 429 | 471 | 43 | inferred_complete_timeline |
| `Action_None` | 473 | 539 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 3–334
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 44 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 292 | 246 | inferred_complete_timeline |
| `Action_ZoneBlock` | 293 | 314 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 317 | 326 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 331 | 334 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 3–307
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 292 | 290 | inferred_complete_timeline |
| `Action_ZoneBlock` | 293 | 307 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 3–332
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 292 | 290 | inferred_complete_timeline |
| `Action_ZoneBlock` | 293 | 298 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 300 | 303 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 307 | 314 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 331 | 332 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 3–539
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 334 | 332 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 343 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 421 | 539 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–539
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 315 | 313 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 324 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 332 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 342 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 350 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 356 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 377 | 378 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 381 | 385 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 391 | 392 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 396 | 397 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 400 | 401 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 404 | 407 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 415 | 539 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 3–357
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 334 | 332 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 342 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 357 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 3–310
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 310 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 3–369
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 369 | 367 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 3–451
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 352 | 350 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 356 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 392 | 396 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 401 | 451 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 3–404
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 335 | 333 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 404 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–389
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 324 | 322 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 332 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 337 | 346 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 352 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 356 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 363 | 369 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 376 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 388 | 389 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 3–388
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 388 | 386 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–536
- **Visible Samples:** 507

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 485 | 483 | inferred_complete_timeline |
| `Action_PreSnap` | 489 | 490 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 495 | 496 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 501 | 503 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 505 | 507 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 512 | 514 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 517 | 518 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 525 | 529 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 532 | 533 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 535 | 536 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 3–539
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 411 | 409 | inferred_complete_timeline |
| `Action_PreSnap` | 413 | 510 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 512 | 514 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 518 | 539 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 3–173 | 159 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 3–322 | 319 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 219–220 | 2 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 335–413 | 79 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 349–382 | 17 | 3 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 356–357 | 2 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 360–364 | 5 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 368–395 | 27 | 2 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 377–378 | 2 | 1 | Undefined position; Undefined team |
| `30` | `48` | Position_Unknown | Team_Unknown | 380–539 | 132 | 6 | Undefined position; Undefined team |
| `31` | `52` | Position_Unknown | Team_Unknown | 385–539 | 132 | 6 | Undefined position; Undefined team |
| `32` | `53` | Position_Unknown | Team_Unknown | 387–539 | 141 | 6 | Undefined position; Undefined team |
| `33` | `55` | Position_Unknown | Team_Unknown | 395–539 | 118 | 8 | Undefined position; Undefined team |
| `34` | `56` | Position_Unknown | Team_Unknown | 398–539 | 127 | 6 | Undefined position; Undefined team |
| `35` | `57` | Position_Unknown | Team_Unknown | 403–539 | 137 | 1 | Undefined position; Undefined team |
| `36` | `58` | Position_Unknown | Team_Unknown | 412–508 | 97 | 1 | Undefined position; Undefined team |
| `37` | `59` | Position_Unknown | Team_Unknown | 413–502 | 90 | 1 | Undefined position; Undefined team |
| `38` | `65` | Position_Unknown | Team_Unknown | 434–468 | 34 | 2 | Undefined position; Undefined team |
| `39` | `66` | Position_Unknown | Team_Unknown | 434–539 | 105 | 2 | Undefined position; Undefined team |
| `40` | `67` | Position_Unknown | Team_Unknown | 474–539 | 62 | 3 | Undefined position; Undefined team |
| `41` | `68` | Position_Unknown | Team_Unknown | 479–539 | 59 | 2 | Undefined position; Undefined team |
| `42` | `69` | Position_Unknown | Team_Unknown | 481–482 | 2 | 1 | Undefined position; Undefined team |
| `43` | `70` | Position_Unknown | Team_Unknown | 485–489 | 5 | 1 | Undefined position; Undefined team |
| `44` | `73` | Position_Unknown | Team_Unknown | 519–538 | 12 | 4 | Undefined position; Undefined team |
| `45` | `74` | Position_Unknown | Team_Unknown | 528–539 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 159 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '24' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [3-355] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-388] for track '1' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-334] for track '2' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-342] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-357] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [293-307] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-334] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-343] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-539] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-324] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-332] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-346] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-352] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-356] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-369] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-376] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-389] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-315] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-324] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-332] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-342] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-350] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-356] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-378] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-385] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-392] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-397] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-401] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-407] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-539] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-106] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [304-319] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [321-322] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-335] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-352] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-382] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-388] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-503] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [509-513] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [524-532] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-485] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [489-490] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [495-496] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [501-503] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [505-507] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [512-514] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [517-518] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [525-529] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [532-533] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [535-536] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-310] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-369] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-352] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-356] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-396] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-451] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-411] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-510] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [512-514] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [317-321] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [323-333] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-380] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-405] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-431] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [293-300] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [302-312] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [329-333] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [338-363] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-388] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-426] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-471] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-539] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-164] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-335] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-404] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-324] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-334] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-342] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-360] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-371] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-388] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-420] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-487] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [494-495] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [511-514] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [518-519] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [525-533] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [535-538] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [293-298] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [300-303] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [307-314] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [331-332] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-44] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-292] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [293-314] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [317-326] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [331-334] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-302] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-322] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-294] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-308] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-413] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-357] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-375] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-382] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-357] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-364] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-384] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-395] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-378] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-390] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-403] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-419] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-496] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [499-505] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-497] for track '31' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [499-505] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [508-511] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [515-518] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [535-537] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-388] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-398] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-406] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-515] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [517-522] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [524-539] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-487] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [495-496] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [500-506] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [510-514] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [517-522] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [524-525] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [527-528] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-487] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [489-490] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [494-495] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [499-501] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [509-514] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-508] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-502] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-436] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-468] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-441] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-539] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-515] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [517-519] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [523-539] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [479-532] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [535-539] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [481-482] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [485-489] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [519-524] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [528-529] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [531-532] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [537-538] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>