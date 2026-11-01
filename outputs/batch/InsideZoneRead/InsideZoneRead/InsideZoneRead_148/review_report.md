# Play-Annotation-Generator Annotation Review — InsideZoneRead_148

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_148`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 539
- **Player Tracks:** 58
- **Ball Tracks:** 0
- **Action Segments:** 155
- **Validation Warnings:** 191
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 125
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `23` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `23` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 320 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 320 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `23` | `Group` | 0 | START | 0 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 320 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 317 |
| ✅ EXACT | `Action_BallSnap` | C | `23` | `22` | 318 | START | 318 | 334 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `15` | `14` | 321 | START | 321 | 412 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `15` | 321 | START | 321 | 338 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `19` | `18` | 321 | START | 321 | 335 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `23` | `22` | 321 | START | 335 | 351 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `6` | 321 | START | 321 | 347 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 334 | END | 318 | 334 |
| ✅ EXACT | `Action_ReadDefender` | QB | `14` | `13` | 338 | START | 338 | 362 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `14` | `13` | 363 | START | 363 | 429 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 412 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 502

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_SnapReceive` | 318 | 334 | 17 | inferred_complete_timeline |
| `Action_None` | 335 | 337 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 338 | 362 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 363 | 429 | 67 | inferred_complete_timeline |
| `Action_BallCarry` | 431 | 433 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 438 | 443 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 445 | 499 | 55 | inferred_complete_timeline |
| `Action_BallCarry` | 532 | 539 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–482
- **Visible Samples:** 483

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_None` | 318 | 482 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_None` | 318 | 539 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_None` | 318 | 393 | 76 | inferred_complete_timeline |
| `Action_None` | 395 | 539 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_None` | 318 | 421 | 104 | inferred_complete_timeline |
| `Action_None` | 423 | 430 | 8 | inferred_complete_timeline |
| `Action_None` | 432 | 433 | 2 | inferred_complete_timeline |
| `Action_None` | 435 | 438 | 4 | inferred_complete_timeline |
| `Action_None` | 440 | 539 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–412
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_None` | 318 | 412 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 320 | 321 | inferred_complete_timeline |
| `Action_ZoneBlock` | 321 | 412 | 92 | inferred_complete_timeline |
| `Action_None` | 413 | 430 | 18 | inferred_complete_timeline |
| `Action_None` | 437 | 442 | 6 | inferred_complete_timeline |
| `Action_None` | 444 | 539 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–335
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 320 | 321 | inferred_complete_timeline |
| `Action_ZoneBlock` | 321 | 335 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 0–364
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_BallSnap` | 318 | 334 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 335 | 351 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 355 | 360 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 363 | 364 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 320 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 321 | 338 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 348 | 353 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–415
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 320 | 321 | inferred_complete_timeline |
| `Action_ZoneBlock` | 321 | 347 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 360 | 412 | 53 | inferred_complete_timeline |
| `Action_None` | 413 | 415 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–364
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_None` | 318 | 359 | 42 | inferred_complete_timeline |
| `Action_None` | 361 | 364 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–379
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_None` | 318 | 374 | 57 | inferred_complete_timeline |
| `Action_None` | 376 | 379 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–497
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_None` | 318 | 391 | 74 | inferred_complete_timeline |
| `Action_None` | 396 | 404 | 9 | inferred_complete_timeline |
| `Action_None` | 409 | 412 | 4 | inferred_complete_timeline |
| `Action_None` | 442 | 448 | 7 | inferred_complete_timeline |
| `Action_None` | 453 | 454 | 2 | inferred_complete_timeline |
| `Action_None` | 457 | 459 | 3 | inferred_complete_timeline |
| `Action_None` | 467 | 469 | 3 | inferred_complete_timeline |
| `Action_None` | 472 | 473 | 2 | inferred_complete_timeline |
| `Action_None` | 475 | 491 | 17 | inferred_complete_timeline |
| `Action_None` | 496 | 497 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–410
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_None` | 318 | 358 | 41 | inferred_complete_timeline |
| `Action_None` | 375 | 377 | 3 | inferred_complete_timeline |
| `Action_None` | 387 | 393 | 7 | inferred_complete_timeline |
| `Action_None` | 396 | 397 | 2 | inferred_complete_timeline |
| `Action_None` | 405 | 410 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–409
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_None` | 318 | 409 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–384
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_None` | 318 | 384 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_None` | 318 | 539 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_None` | 318 | 433 | 116 | inferred_complete_timeline |
| `Action_None` | 437 | 539 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–410
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_None` | 318 | 410 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–395
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_None` | 318 | 395 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>CB6 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_None` | 318 | 473 | 156 | inferred_complete_timeline |
| `Action_None` | 477 | 480 | 4 | inferred_complete_timeline |
| `Action_None` | 482 | 484 | 3 | inferred_complete_timeline |
| `Action_None` | 487 | 539 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–104 | 91 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 0–55 | 13 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 166–193 | 24 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 256–269 | 10 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 333–348 | 4 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 347–539 | 187 | 4 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 353–539 | 162 | 5 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 360–539 | 130 | 7 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 375–376 | 2 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 402–403 | 2 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 402–430 | 20 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 406–539 | 134 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 408–411 | 4 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 410–539 | 120 | 2 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 417–434 | 12 | 2 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 417–435 | 16 | 2 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 428–430 | 3 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 435–539 | 104 | 2 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 438–539 | 102 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 440–441 | 2 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 449–454 | 6 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 449–539 | 91 | 1 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 452–539 | 88 | 1 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 453–539 | 83 | 2 | Undefined position; Undefined team |
| `46` | `63` | Position_Unknown | Team_Unknown | 453–539 | 85 | 2 | Undefined position; Undefined team |
| `47` | `64` | Position_Unknown | Team_Unknown | 454–489 | 23 | 2 | Undefined position; Undefined team |
| `48` | `66` | Position_Unknown | Team_Unknown | 465–539 | 75 | 1 | Undefined position; Undefined team |
| `49` | `67` | Position_Unknown | Team_Unknown | 475–479 | 5 | 1 | Undefined position; Undefined team |
| `50` | `68` | Position_Unknown | Team_Unknown | 478–539 | 55 | 2 | Undefined position; Undefined team |
| `51` | `73` | Position_Unknown | Team_Unknown | 498–539 | 42 | 1 | Undefined position; Undefined team |
| `52` | `74` | Position_Unknown | Team_Unknown | 499–500 | 2 | 1 | Undefined position; Undefined team |
| `53` | `75` | Position_Unknown | Team_Unknown | 508–539 | 32 | 1 | Undefined position; Undefined team |
| `54` | `78` | Position_Unknown | Team_Unknown | 523–539 | 17 | 1 | Undefined position; Undefined team |
| `55` | `79` | Position_Unknown | Team_Unknown | 532–539 | 8 | 1 | Undefined position; Undefined team |
| `56` | `82` | Position_Unknown | Team_Unknown | 535–539 | 5 | 1 | Undefined position; Undefined team |
| `57` | `83` | Position_Unknown | Team_Unknown | 535–539 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `23` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (5 segments found)

### Track Identity Issues

- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 114 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 296: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 92 frames exceeds threshold 90 frames [start=321, end=412].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (LT) duration 92 frames exceeds threshold 90 frames [start=321, end=412].
- ⚠️ Resolved action overlap for track '22' (C): higher_priority='Action_BallSnap' [318–334], lower_priority='Action_ZoneBlock' annotated_start=321, effective_Action_ZoneBlock_start=335.
- ⚠️ Action 'Action_None' range [318-374] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-379] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-421] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-430] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-433] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-438] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-539] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-412] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-410] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-384] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-393] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [321-347] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '6' starts at frame 413, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [413-415] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-364] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-482] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-358] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-377] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-393] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-410] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-473] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-480] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-484] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-539] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [363-429] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [431-433] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [438-443] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [445-499] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [532-539] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-430] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-442] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [321-338] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [348-353] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-433] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-539] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-391] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-404] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-412] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-448] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-459] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-469] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-491] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [321-335] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-395] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-46] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-104] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-409] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [335-351] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [355-360] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [363-364] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-31] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-38] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-55] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-185] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-259] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-263] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-369] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-376] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-423] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-539] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-364] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-397] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-455] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-539] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-404] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-412] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-438] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-415] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-430] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-539] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-411] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-426] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-418] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-434] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-420] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-435] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-430] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-443] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-539] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-539] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-441] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-454] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-539] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-524] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-460] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-489] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-479] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-480] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-539] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-539] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-539] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>