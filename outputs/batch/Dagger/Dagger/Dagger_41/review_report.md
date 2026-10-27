# Play-Annotation-Generator Annotation Review — Dagger_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_41`
- **Frame Range:** 0 to 568 (569 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Rec`
- **Result Frame:** 568
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 180
- **Validation Warnings:** 235
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 1
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 6
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 139
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | RT | offense | `18` | `18` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LT | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `22` | `20` |
| ❌ MISSING SEGMENT | `Action_BreakInside` | WR3 | offense | `4` | `4` |
| ⚠️ START CHANGED | `Action_ClearToEdge` | WR2 | offense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `22` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 0 | START | 0 | 373 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 373 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `14` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 137 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 374 | START | 374 | 376 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | `15` | `15` | 377 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PassBlock` | RT | `18` | `18` | 377 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LT | `9` | `9` | 377 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `22` | `20` | 378 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BreakInside` | WR3 | `4` | `4` | 389 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_ClearToEdge` | WR2 | `14` | `14` | 389 | START | 404 | 405 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `22` | `20` | 452 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–438
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 150 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 182 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 190 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 204 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 256 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 293 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 306 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 346 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 351 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 361 | 373 | 13 | inferred_complete_timeline |
| `Action_None` | 374 | 379 | 6 | inferred_complete_timeline |
| `Action_None` | 401 | 404 | 4 | inferred_complete_timeline |
| `Action_None` | 413 | 421 | 9 | inferred_complete_timeline |
| `Action_None` | 423 | 433 | 11 | inferred_complete_timeline |
| `Action_None` | 435 | 438 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–430
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 373 | 374 | inferred_complete_timeline |
| `Action_None` | 374 | 399 | 26 | inferred_complete_timeline |
| `Action_None` | 401 | 408 | 8 | inferred_complete_timeline |
| `Action_None` | 414 | 430 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–544
- **Visible Samples:** 490

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 373 | 374 | inferred_complete_timeline |
| `Action_None` | 374 | 421 | 48 | inferred_complete_timeline |
| `Action_None` | 426 | 434 | 9 | inferred_complete_timeline |
| `Action_None` | 436 | 439 | 4 | inferred_complete_timeline |
| `Action_None` | 456 | 457 | 2 | inferred_complete_timeline |
| `Action_None` | 463 | 473 | 11 | inferred_complete_timeline |
| `Action_None` | 487 | 488 | 2 | inferred_complete_timeline |
| `Action_None` | 501 | 503 | 3 | inferred_complete_timeline |
| `Action_None` | 505 | 506 | 2 | inferred_complete_timeline |
| `Action_None` | 510 | 544 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–405
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 213 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 238 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 259 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 285 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 290 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 382 | 91 | inferred_complete_timeline |
| `Action_ClearToEdge` | 404 | 405 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–387
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 387 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 185 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 140 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–376
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 188 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 255 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 305 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 361 | 369 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 371 | 373 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 374 | 376 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–428
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 373 | 374 | inferred_complete_timeline |
| `Action_None` | 374 | 428 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 543

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 373 | 374 | inferred_complete_timeline |
| `Action_None` | 374 | 404 | 31 | inferred_complete_timeline |
| `Action_None` | 415 | 474 | 60 | inferred_complete_timeline |
| `Action_None` | 476 | 493 | 18 | inferred_complete_timeline |
| `Action_None` | 495 | 497 | 3 | inferred_complete_timeline |
| `Action_None` | 501 | 505 | 5 | inferred_complete_timeline |
| `Action_None` | 507 | 508 | 2 | inferred_complete_timeline |
| `Action_None` | 511 | 514 | 4 | inferred_complete_timeline |
| `Action_None` | 516 | 536 | 21 | inferred_complete_timeline |
| `Action_None` | 540 | 541 | 2 | inferred_complete_timeline |
| `Action_None` | 546 | 568 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–430
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 205 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 216 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 270 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 284 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 290 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 304 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 318 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 373 | 45 | inferred_complete_timeline |
| `Action_None` | 374 | 404 | 31 | inferred_complete_timeline |
| `Action_None` | 411 | 412 | 2 | inferred_complete_timeline |
| `Action_None` | 417 | 430 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 373 | 374 | inferred_complete_timeline |
| `Action_None` | 374 | 424 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 494

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 373 | 374 | inferred_complete_timeline |
| `Action_None` | 374 | 410 | 37 | inferred_complete_timeline |
| `Action_None` | 412 | 433 | 22 | inferred_complete_timeline |
| `Action_None` | 442 | 445 | 4 | inferred_complete_timeline |
| `Action_None` | 511 | 512 | 2 | inferred_complete_timeline |
| `Action_None` | 514 | 568 | 55 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–137 | 138 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 34–215 | 97 | 6 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 279–532 | 151 | 8 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 286–420 | 92 | 5 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 316–380 | 65 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 336–467 | 87 | 4 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 362–438 | 41 | 6 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 362–498 | 50 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 362–398 | 32 | 5 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 362–424 | 40 | 8 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 364–435 | 23 | 5 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 382–403 | 14 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 388–440 | 47 | 3 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 394–410 | 17 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 414–416 | 3 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 433–434 | 2 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 449–505 | 47 | 4 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 453–479 | 4 | 2 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 461–463 | 3 | 1 | Undefined position; Undefined team |
| `38` | `61` | Position_Unknown | Team_Unknown | 470–568 | 88 | 2 | Undefined position; Undefined team |
| `39` | `63` | Position_Unknown | Team_Unknown | 472–476 | 5 | 1 | Undefined position; Undefined team |
| `40` | `64` | Position_Unknown | Team_Unknown | 472–475 | 4 | 1 | Undefined position; Undefined team |
| `41` | `69` | Position_Unknown | Team_Unknown | 512–553 | 42 | 1 | Undefined position; Undefined team |
| `42` | `71` | Position_Unknown | Team_Unknown | 514–524 | 11 | 1 | Undefined position; Undefined team |
| `43` | `72` | Position_Unknown | Team_Unknown | 516–526 | 11 | 1 | Undefined position; Undefined team |
| `44` | `73` | Position_Unknown | Team_Unknown | 516–561 | 31 | 2 | Undefined position; Undefined team |
| `45` | `75` | Position_Unknown | Team_Unknown | 527–552 | 21 | 2 | Undefined position; Undefined team |
| `46` | `76` | Position_Unknown | Team_Unknown | 530–568 | 39 | 1 | Undefined position; Undefined team |
| `47` | `78` | Position_Unknown | Team_Unknown | 540–568 | 29 | 1 | Undefined position; Undefined team |
| `48` | `79` | Position_Unknown | Team_Unknown | 548–568 | 21 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_PassBlock` on target `15` (C)
- ❌ Missing segment for action `Action_PassBlock` on target `18` (RT)
- ❌ Missing segment for action `Action_PassBlock` on target `9` (LT)
- ❌ Missing segment for action `Action_SnapReceive` on target `22` (Position_Unknown)
- ❌ Missing segment for action `Action_BreakInside` on target `4` (WR3)
- ⚠️ `Action_ClearToEdge` for actor_track_id `14` (WR2): Annotated start 389 != Inferred start 404
- ❌ Missing segment for action `Action_ThrowPass` on target `22` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 168 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 568 as fallback play end.
- ⚠️ Segment 'Action_BreakInside' for track '4' has invalid range: start=389, end=387. Clamping end to start.
- ⚠️ Segment 'Action_PassBlock' for track '9' has invalid range: start=377, end=140. Clamping end to start.
- ⚠️ Segment 'Action_PassBlock' for track '15' has invalid range: start=377, end=376. Clamping end to start.
- ⚠️ Segment 'Action_PassBlock' for track '18' has invalid range: start=377, end=108. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '20' has invalid range: start=374, end=215. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '20' has invalid range: start=452, end=215. Clamping end to start.
- ⚠️ Action 'Action_None' range [374-399] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-408] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-430] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-421] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-434] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-439] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-473] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-488] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-503] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-506] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-544] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-410] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-433] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-445] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-424] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-238] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-263] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-387] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-428] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-404] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-474] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-493] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-497] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-505] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-508] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-514] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-536] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-541] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-568] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-177] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-205] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-216] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-270] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-284] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-290] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-304] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-318] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-404] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-430] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-141] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-142] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-213] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-238] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-259] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-285] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-290] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-382] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ClearToEdge' range [404-405] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-188] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-255] for track '15' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-305] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-369] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [374-376] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-143] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-150] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-182] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-190] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-204] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-221] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-256] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-263] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-293] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-306] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-346] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-351] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-373] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-379] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-404] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-421] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-433] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-438] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-143] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-142] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-43] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-54] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-66] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-215] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-290] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-373] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-384] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-441] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-500] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-532] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-339] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-373] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-417] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-380] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-373] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-404] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-422] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-467] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-373] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-377] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-432] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-438] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-369] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-373] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-498] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-365] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-369] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '27' starts at frame 374, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [374-377] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-398] for track '27' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-363] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-373] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-385] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-402] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-410] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-421] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-365] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-369] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-405] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-414] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-435] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-386] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-399] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-403] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-404] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-440] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-410] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-416] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-434] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-453] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-461] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-476] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-505] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-463] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-474] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-568] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-476] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-475] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-553] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-524] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-526] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-529] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-561] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-529] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-552] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-568] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.

</details>