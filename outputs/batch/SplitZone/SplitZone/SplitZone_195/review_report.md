# Play-Annotation-Generator Annotation Review — SplitZone_195

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_195`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 629
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 138
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 111
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `17` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 18 | START | 19 | 287 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 18 | START | 19 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 18 | START | 19 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 18 | START | 19 | 290 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `20` | `Group` | 18 | START | 19 | 286 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 18 | START | 19 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 18 | START | 19 | 287 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 18 | START | 19 | 290 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 18 | START | 19 | 287 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 18 | START | 19 | 287 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 18 | START | 19 | 302 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 288 | START | 288 | 405 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 291 | START | 406 | 408 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `18` | `18` | 291 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 291 | START | 291 | 478 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `21` | 291 | START | 306 | 313 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `4` | 291 | START | 291 | 416 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `9` | `9` | 303 | START | 303 | 453 |
| ✅ EXACT | `Action_SnapReceive` | RB | `7` | `7` | 405 | END | 288 | 405 |
| ✅ EXACT | `Action_Handoff` | RB | `7` | `7` | 410 | START | 410 | 416 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `17` | `17` | 417 | START | 417 | 446 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 484 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 19–601
- **Visible Samples:** 553

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 37 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 188 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 413 | 211 | inferred_complete_timeline |
| `Action_BallCarry` | 417 | 446 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 453 | 458 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 462 | 474 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 476 | 480 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 482 | 601 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 19–629
- **Visible Samples:** 611

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 287 | 269 | inferred_complete_timeline |
| `Action_SnapReceive` | 288 | 405 | 118 | inferred_complete_timeline |
| `Action_None` | 406 | 409 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 410 | 416 | 7 | inferred_complete_timeline |
| `Action_None` | 417 | 629 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 19–629
- **Visible Samples:** 611

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 287 | 269 | inferred_complete_timeline |
| `Action_None` | 288 | 629 | 342 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 19–629
- **Visible Samples:** 611

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 287 | 269 | inferred_complete_timeline |
| `Action_None` | 288 | 629 | 342 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 19–629
- **Visible Samples:** 610

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 286 | 268 | inferred_complete_timeline |
| `Action_None` | 288 | 629 | 342 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 19–629
- **Visible Samples:** 608

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 302 | 284 | inferred_complete_timeline |
| `Action_SplitBlock` | 303 | 453 | 151 | inferred_complete_timeline |
| `Action_SplitBlock` | 456 | 476 | 21 | inferred_complete_timeline |
| `Action_SplitBlock` | 478 | 484 | 7 | inferred_complete_timeline |
| `Action_None` | 485 | 629 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 19–569
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 290 | 272 | inferred_complete_timeline |
| `Action_ZoneBlock` | 291 | 416 | 126 | inferred_complete_timeline |
| `Action_ZoneBlock` | 421 | 462 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 469 | 471 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 473 | 478 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 480 | 484 | 5 | inferred_complete_timeline |
| `Action_None` | 485 | 569 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 19–149
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 149 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 19–420
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 287 | 269 | inferred_complete_timeline |
| `Action_BallSnap` | 288 | 405 | 118 | inferred_complete_timeline |
| `Action_ZoneBlock` | 406 | 408 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 411 | 420 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 19–562
- **Visible Samples:** 543

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 290 | 272 | inferred_complete_timeline |
| `Action_ZoneBlock` | 291 | 478 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 480 | 484 | 5 | inferred_complete_timeline |
| `Action_None` | 485 | 562 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 19–566
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 126 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 151 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 165 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 264 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 288 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 306 | 313 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 315 | 349 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 351 | 352 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 354 | 358 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 360 | 361 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 379 | 380 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 382 | 387 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 392 | 484 | 93 | inferred_complete_timeline |
| `Action_None` | 485 | 566 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 19–586
- **Visible Samples:** 543

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 287 | 269 | inferred_complete_timeline |
| `Action_None` | 288 | 462 | 175 | inferred_complete_timeline |
| `Action_None` | 464 | 465 | 2 | inferred_complete_timeline |
| `Action_None` | 487 | 488 | 2 | inferred_complete_timeline |
| `Action_None` | 491 | 493 | 3 | inferred_complete_timeline |
| `Action_None` | 495 | 586 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 19–586
- **Visible Samples:** 526

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 287 | 269 | inferred_complete_timeline |
| `Action_None` | 288 | 417 | 130 | inferred_complete_timeline |
| `Action_None` | 421 | 422 | 2 | inferred_complete_timeline |
| `Action_None` | 460 | 462 | 3 | inferred_complete_timeline |
| `Action_None` | 465 | 586 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 19–608
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 166 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 287 | 95 | inferred_complete_timeline |
| `Action_None` | 288 | 412 | 125 | inferred_complete_timeline |
| `Action_None` | 414 | 430 | 17 | inferred_complete_timeline |
| `Action_None` | 433 | 608 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 19–411
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 287 | 269 | inferred_complete_timeline |
| `Action_None` | 288 | 411 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 19–513
- **Visible Samples:** 490

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 287 | 269 | inferred_complete_timeline |
| `Action_None` | 288 | 498 | 211 | inferred_complete_timeline |
| `Action_None` | 504 | 513 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 19–460
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 287 | 269 | inferred_complete_timeline |
| `Action_None` | 288 | 460 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 19–629
- **Visible Samples:** 608

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 287 | 269 | inferred_complete_timeline |
| `Action_None` | 288 | 469 | 182 | inferred_complete_timeline |
| `Action_None` | 471 | 622 | 152 | inferred_complete_timeline |
| `Action_None` | 624 | 625 | 2 | inferred_complete_timeline |
| `Action_None` | 627 | 629 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 19–629
- **Visible Samples:** 610

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 287 | 269 | inferred_complete_timeline |
| `Action_None` | 288 | 593 | 306 | inferred_complete_timeline |
| `Action_None` | 595 | 629 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 19–621
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 287 | 269 | inferred_complete_timeline |
| `Action_None` | 288 | 456 | 169 | inferred_complete_timeline |
| `Action_None` | 465 | 538 | 74 | inferred_complete_timeline |
| `Action_None` | 540 | 621 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 19–476
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 287 | 269 | inferred_complete_timeline |
| `Action_None` | 288 | 476 | 189 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 19–418 | 400 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 298–629 | 282 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 410–411 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 448–577 | 125 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 453–629 | 177 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 455–526 | 51 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 455–533 | 36 | 7 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 470–482 | 8 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 477–629 | 153 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 479–629 | 138 | 3 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 498–507 | 10 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 503–563 | 57 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 507–509 | 3 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 512–588 | 70 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 518–596 | 55 | 4 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 541–545 | 4 | 2 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 543–545 | 3 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 561–596 | 31 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `18` (LG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (8 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (5 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 103 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (LT) duration 194 frames exceeds threshold 90 frames [start=291, end=484].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 130 frames exceeds threshold 90 frames [start=291, end=420].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [288–405], lower_priority='Action_ZoneBlock' annotated_start=291, effective_Action_ZoneBlock_start=406.
- ⚠️ Segment 'Action_ZoneBlock' for track '18' has invalid range: start=291, end=149. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (RG) duration 194 frames exceeds threshold 90 frames [start=291, end=484].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 194 frames exceeds threshold 90 frames [start=291, end=484].
- ⚠️ Action 'Action_None' range [288-411] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-469] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-622] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-625] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-462] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-488] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-493] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-586] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [291-416] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [421-462] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [469-471] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [473-478] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-569] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-166] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-412] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-430] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-608] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-460] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [303-453] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [456-476] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-629] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-456] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-538] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-621] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-593] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-498] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-513] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [406-408] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [411-420] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-418] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-476] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-417] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-462] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-586] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-37] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-188] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-413] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [417-446] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [453-458] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [462-474] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [476-480] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [482-601] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-149] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [291-478] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-562] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-286] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-629] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-126] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-165] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-218] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-264] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-288] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [306-313] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [315-349] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [351-352] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [354-358] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [360-361] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [379-380] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [382-387] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-566] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-424] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-549] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-556] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-488] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-533] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-542] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-577] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-465] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-503] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-515] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-526] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-457] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-473] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-486] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-492] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-504] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-513] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-533] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-478] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-482] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-482] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-588] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-507] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-511] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-516] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-563] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-509] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-555] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-588] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-558] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-570] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-577] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-596] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-542] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-545] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-545] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-588] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-596] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>