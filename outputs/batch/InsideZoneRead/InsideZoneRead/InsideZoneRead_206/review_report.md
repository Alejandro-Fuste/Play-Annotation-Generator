# Play-Annotation-Generator Annotation Review — InsideZoneRead_206

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_206`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 629
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 125
- **Validation Warnings:** 135
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 363 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 335 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 459 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 459 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 459 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 459 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 462 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 232 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 459 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 459 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 459 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 460 | START | 460 | 479 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `12` | `11` | 463 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `15` | `14` | 463 | START | 463 | 524 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `18` | 463 | START | 480 | 486 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 463 | START | 463 | 510 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `22` | `21` | 463 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 479 | END | 460 | 479 |
| ✅ EXACT | `Action_ReadDefender` | QB | `17` | `16` | 484 | START | 484 | 513 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `17` | `16` | 514 | START | 514 | 596 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 543 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–604
- **Visible Samples:** 602

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_SnapReceive` | 460 | 479 | 20 | inferred_complete_timeline |
| `Action_None` | 480 | 483 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 484 | 513 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 514 | 596 | 83 | inferred_complete_timeline |
| `Action_BallCarry` | 599 | 600 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 602 | 604 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_None` | 460 | 629 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–628
- **Visible Samples:** 625

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_None` | 460 | 590 | 131 | inferred_complete_timeline |
| `Action_None` | 592 | 597 | 6 | inferred_complete_timeline |
| `Action_None` | 599 | 616 | 18 | inferred_complete_timeline |
| `Action_None` | 619 | 628 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 624

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_None` | 460 | 597 | 138 | inferred_complete_timeline |
| `Action_None` | 599 | 606 | 8 | inferred_complete_timeline |
| `Action_None` | 608 | 609 | 2 | inferred_complete_timeline |
| `Action_None` | 613 | 616 | 4 | inferred_complete_timeline |
| `Action_None` | 618 | 629 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–628
- **Visible Samples:** 616

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_None` | 460 | 604 | 145 | inferred_complete_timeline |
| `Action_None` | 607 | 610 | 4 | inferred_complete_timeline |
| `Action_None` | 612 | 616 | 5 | inferred_complete_timeline |
| `Action_None` | 627 | 628 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 619

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_None` | 460 | 610 | 151 | inferred_complete_timeline |
| `Action_None` | 622 | 629 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 610

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 335 | 336 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 462 | 118 | inferred_complete_timeline |
| `Action_ZoneBlock` | 463 | 524 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 526 | 527 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 531 | 532 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 535 | 537 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 539 | 543 | 5 | inferred_complete_timeline |
| `Action_None` | 544 | 606 | 63 | inferred_complete_timeline |
| `Action_None` | 609 | 610 | 2 | inferred_complete_timeline |
| `Action_None` | 613 | 629 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 256 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–619
- **Visible Samples:** 582

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_BallSnap` | 460 | 479 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 480 | 486 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 491 | 543 | 53 | inferred_complete_timeline |
| `Action_None` | 544 | 565 | 22 | inferred_complete_timeline |
| `Action_None` | 569 | 570 | 2 | inferred_complete_timeline |
| `Action_None` | 580 | 595 | 16 | inferred_complete_timeline |
| `Action_None` | 618 | 619 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 462 | 463 | inferred_complete_timeline |
| `Action_ZoneBlock` | 463 | 510 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 512 | 543 | 32 | inferred_complete_timeline |
| `Action_None` | 544 | 629 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–381
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 363 | 364 | inferred_complete_timeline |
| `Action_PreSnap` | 368 | 381 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_None` | 460 | 625 | 166 | inferred_complete_timeline |
| `Action_None` | 627 | 629 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–527
- **Visible Samples:** 517

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_None` | 460 | 504 | 45 | inferred_complete_timeline |
| `Action_None` | 514 | 517 | 4 | inferred_complete_timeline |
| `Action_None` | 520 | 527 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_None` | 460 | 629 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 623

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_None` | 460 | 499 | 40 | inferred_complete_timeline |
| `Action_None` | 504 | 528 | 25 | inferred_complete_timeline |
| `Action_None` | 531 | 537 | 7 | inferred_complete_timeline |
| `Action_None` | 539 | 629 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_None` | 460 | 629 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 623

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_None` | 460 | 607 | 148 | inferred_complete_timeline |
| `Action_None` | 613 | 626 | 14 | inferred_complete_timeline |
| `Action_None` | 629 | 629 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_None` | 460 | 629 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_None` | 460 | 598 | 139 | inferred_complete_timeline |
| `Action_None` | 600 | 629 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_None` | 460 | 629 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–612
- **Visible Samples:** 613

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 459 | 460 | inferred_complete_timeline |
| `Action_None` | 460 | 612 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–611
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 406 | 407 | inferred_complete_timeline |
| `Action_PreSnap` | 409 | 459 | 51 | inferred_complete_timeline |
| `Action_None` | 460 | 595 | 136 | inferred_complete_timeline |
| `Action_None` | 597 | 598 | 2 | inferred_complete_timeline |
| `Action_None` | 601 | 602 | 2 | inferred_complete_timeline |
| `Action_None` | 610 | 611 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 260–267 | 8 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 286–292 | 5 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 292–629 | 288 | 3 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 333–345 | 13 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 348–629 | 244 | 9 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 473–479 | 5 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 508–629 | 122 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 518–519 | 2 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 552–556 | 5 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 555–564 | 10 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 555–557 | 3 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 564–566 | 3 | 1 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 575–581 | 7 | 1 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 577–578 | 2 | 1 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 583–584 | 2 | 1 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 590–629 | 32 | 4 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 599–601 | 3 | 1 | Undefined position; Undefined team |
| `39` | `60` | Position_Unknown | Team_Unknown | 608–610 | 3 | 1 | Undefined position; Undefined team |
| `40` | `62` | Position_Unknown | Team_Unknown | 621–623 | 3 | 1 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 621–629 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `12` (RT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `22` (LG)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (3 segments found)

### Track Identity Issues

- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 91 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '11' has invalid range: start=463, end=381. Clamping end to start.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [460–479], lower_priority='Action_ZoneBlock' annotated_start=463, effective_Action_ZoneBlock_start=480.
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=463, end=256. Clamping end to start.
- ⚠️ Action 'Action_None' range [460-504] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-517] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-527] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-590] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-597] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-616] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-628] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-610] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-604] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-610] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-616] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-628] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-597] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-606] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-609] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-616] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-629] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-598] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-629] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-499] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-528] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-537] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-629] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-607] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-626] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-625] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-629] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-363] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-381] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-612] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-629] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-335] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [463-524] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [526-527] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [531-532] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [535-537] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-606] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-610] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-406] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-595] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-598] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-602] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-611] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [484-513] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [514-596] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [599-600] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [602-604] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-629] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [460-479] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [480-486] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-565] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-570] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-595] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-619] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [463-510] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [512-543] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-629] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-232] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-256] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-267] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-288] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-292] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-303] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-629] for track '24' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-345] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-349] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-376] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-481] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-491] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-495] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-512] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-475] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-629] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-519] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-556] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-564] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-557] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-566] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-581] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-584] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-592] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-601] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-605] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-629] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-601] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-610] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-623] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-625] for track '41' has 1 frames without a visible bounding box.
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

</details>