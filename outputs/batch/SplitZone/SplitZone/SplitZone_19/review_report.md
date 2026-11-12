# Play-Annotation-Generator Annotation Review — SplitZone_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_19`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 689
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 185
- **Validation Warnings:** 201
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 149
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `0` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 26 | START | 26 | 515 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 26 | START | 26 | 475 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 26 | START | 26 | 475 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `12` | `Group` | 26 | START | 26 | 391 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 26 | START | 40 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 26 | START | 42 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 26 | START | 44 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 26 | START | 26 | 485 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 26 | START | 26 | 475 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 476 | START | 476 | 484 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `17` | 479 | START | 479 | 480 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `18` | `18` | 479 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `19` | `19` | 479 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | `3` | `3` | 486 | START | 486 | 515 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 490 | END | 476 | 490 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `5` | `5` | 501 | START | 501 | 512 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `0` | `0` | 516 | START | 516 | 544 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 599 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 26–689
- **Visible Samples:** 663

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 475 | 450 | inferred_complete_timeline |
| `Action_SnapReceive` | 476 | 490 | 15 | inferred_complete_timeline |
| `Action_None` | 491 | 500 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 501 | 512 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 514 | 515 | 2 | inferred_complete_timeline |
| `Action_None` | 516 | 689 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 26–676
- **Visible Samples:** 604

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 515 | 490 | inferred_complete_timeline |
| `Action_BallCarry` | 516 | 544 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 566 | 567 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 576 | 583 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 586 | 590 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 607 | 676 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 26–599
- **Visible Samples:** 559

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 475 | 450 | inferred_complete_timeline |
| `Action_None` | 476 | 582 | 107 | inferred_complete_timeline |
| `Action_None` | 598 | 599 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 26–689
- **Visible Samples:** 663

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 475 | 450 | inferred_complete_timeline |
| `Action_None` | 476 | 659 | 184 | inferred_complete_timeline |
| `Action_None` | 661 | 689 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 26–526
- **Visible Samples:** 496

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 485 | 460 | inferred_complete_timeline |
| `Action_SplitBlock` | 486 | 515 | 30 | inferred_complete_timeline |
| `Action_SplitBlock` | 520 | 521 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 523 | 526 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 26–689
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 391 | 366 | inferred_complete_timeline |
| `Action_PreSnap` | 394 | 475 | 82 | inferred_complete_timeline |
| `Action_None` | 476 | 487 | 12 | inferred_complete_timeline |
| `Action_None` | 576 | 577 | 2 | inferred_complete_timeline |
| `Action_None` | 580 | 596 | 17 | inferred_complete_timeline |
| `Action_None` | 598 | 599 | 2 | inferred_complete_timeline |
| `Action_None` | 611 | 689 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 44–64
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 44 | 46 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 56 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 64 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 42–484
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 42 | 59 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 102 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 475 | 367 | inferred_complete_timeline |
| `Action_BallSnap` | 476 | 484 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 40–555
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 40 | 56 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 63 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 73 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 85 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 121 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 159 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 332 | 136 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 354 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 360 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 363 | 364 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 369 | 377 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 380 | 381 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 385 | 390 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 395 | 397 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 401 | 478 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 479 | 480 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 554 | 555 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 26–586
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 475 | 450 | inferred_complete_timeline |
| `Action_None` | 476 | 488 | 13 | inferred_complete_timeline |
| `Action_None` | 490 | 492 | 3 | inferred_complete_timeline |
| `Action_None` | 582 | 586 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 30–493
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 76 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 88 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 475 | 382 | inferred_complete_timeline |
| `Action_None` | 476 | 493 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 33–493
- **Visible Samples:** 461

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 33 | 475 | 443 | inferred_complete_timeline |
| `Action_None` | 476 | 493 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 26–689
- **Visible Samples:** 614

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 475 | 450 | inferred_complete_timeline |
| `Action_None` | 476 | 558 | 83 | inferred_complete_timeline |
| `Action_None` | 576 | 592 | 17 | inferred_complete_timeline |
| `Action_None` | 623 | 628 | 6 | inferred_complete_timeline |
| `Action_None` | 631 | 656 | 26 | inferred_complete_timeline |
| `Action_None` | 658 | 689 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 26–534
- **Visible Samples:** 502

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 475 | 450 | inferred_complete_timeline |
| `Action_None` | 476 | 524 | 49 | inferred_complete_timeline |
| `Action_None` | 532 | 534 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 26–689
- **Visible Samples:** 643

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 475 | 450 | inferred_complete_timeline |
| `Action_None` | 476 | 497 | 22 | inferred_complete_timeline |
| `Action_None` | 518 | 521 | 4 | inferred_complete_timeline |
| `Action_None` | 523 | 689 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 26–482
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 167 | 142 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 307 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 317 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 324 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 361 | 475 | 115 | inferred_complete_timeline |
| `Action_None` | 476 | 482 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 26–689
- **Visible Samples:** 661

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 475 | 450 | inferred_complete_timeline |
| `Action_None` | 476 | 610 | 135 | inferred_complete_timeline |
| `Action_None` | 612 | 670 | 59 | inferred_complete_timeline |
| `Action_None` | 672 | 678 | 7 | inferred_complete_timeline |
| `Action_None` | 680 | 689 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 26–689
- **Visible Samples:** 664

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 475 | 450 | inferred_complete_timeline |
| `Action_None` | 476 | 689 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 26–689
- **Visible Samples:** 634

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 475 | 450 | inferred_complete_timeline |
| `Action_None` | 476 | 595 | 120 | inferred_complete_timeline |
| `Action_None` | 623 | 628 | 6 | inferred_complete_timeline |
| `Action_None` | 632 | 689 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 26–489
- **Visible Samples:** 460

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 310 | 285 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 320 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 475 | 152 | inferred_complete_timeline |
| `Action_None` | 476 | 489 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `22` | Position_Unknown | Team_Unknown | 206–480 | 243 | 7 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 206–595 | 176 | 12 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 218–226 | 7 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 314–476 | 64 | 7 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 511–512 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 519–689 | 112 | 9 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 533–627 | 56 | 6 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 543–689 | 104 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 551–648 | 66 | 5 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 551–583 | 25 | 4 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 555–689 | 106 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 555–689 | 87 | 5 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 577–689 | 78 | 3 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 581–689 | 74 | 6 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 593–675 | 69 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 622–689 | 62 | 2 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 624–689 | 64 | 2 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 626–689 | 60 | 3 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 633–689 | 57 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 641–689 | 49 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 668–681 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `18` (C)
- ❌ Missing segment for action `Action_ZoneBlock` on target `19` (LG)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 156 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [476–484], lower_priority='Action_ZoneBlock' annotated_start=479, effective_Action_ZoneBlock_start=485.
- ⚠️ Segment 'Action_ZoneBlock' for track '19' has invalid range: start=479, end=64. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [26-515] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [516-544] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [566-567] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [576-583] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [586-590] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [607-676] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-582] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-599] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-310] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-320] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-489] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [486-515] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [520-521] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [523-526] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-497] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-521] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-689] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [501-512] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-610] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-670] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [672-678] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [680-689] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-595] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-628] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-689] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-524] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-534] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-659] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [661-689] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-307] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-317] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-324] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-482] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-391] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-487] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-577] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-596] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-599] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-689] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-558] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-592] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-628] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-656] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-689] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-488] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-492] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-586] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-76] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-493] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-493] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-56] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-63] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-73] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-85] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-159] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-332] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-354] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-360] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-364] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-377] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-381] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-390] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-397] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [479-480] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [554-555] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-59] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-102] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [476-484] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-56] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-64] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-240] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-248] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-265] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-362] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-377] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-475] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-480] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-208] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-234] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-263] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-298] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-306] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-316] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-323] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-346] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-390] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-475] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-482] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-595] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-222] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-316] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-411] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-421] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-424] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [429-430] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '23' starts at frame 476, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [476-476] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-562] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-582] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-592] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-595] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-612] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-638] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-668] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [678-681] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [684-689] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-535] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-546] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-550] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-595] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-627] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-544] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-595] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-556] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-582] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-617] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-628] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-648] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-559] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-563] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-571] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-583] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-558] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-578] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-559] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-571] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-590] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-627] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-689] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-589] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-629] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-590] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-601] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-634] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-643] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-674] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-657] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [672-675] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-665] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-627] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [630-689] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-628] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-686] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-689] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [641-689] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [668-681] for track '40' has 2 frames without a visible bounding box.
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

</details>