# Play-Annotation-Generator Annotation Review — SplitZone_210

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_210`
- **Frame Range:** 0 to 779 (780 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 779
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 152
- **Validation Warnings:** 175
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 119
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `22` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 22 | START | 33 | 251 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 22 | START | 53 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 22 | START | 86 | 422 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 22 | START | 193 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 22 | START | 213 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 22 | START | 33 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 22 | START | 33 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 22 | START | 33 | 196 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 423 | START | 423 | 431 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `10` | 426 | START | 457 | 459 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `16` | 426 | START | 432 | 579 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `22` | `19` | 426 | START | 426 | 547 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `8` | 426 | START | 426 | 550 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 431 | END | 423 | 431 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `6` | `6` | 432 | START | 432 | 665 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `18` | 443 | START | 443 | 461 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `9` | 462 | START | 462 | 482 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 701 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 193–578
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 193 | 212 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 417 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 419 | 422 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 423 | 431 | 9 | inferred_complete_timeline |
| `Action_None` | 432 | 442 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 443 | 461 | 19 | inferred_complete_timeline |
| `Action_None` | 462 | 469 | 8 | inferred_complete_timeline |
| `Action_None` | 513 | 515 | 3 | inferred_complete_timeline |
| `Action_None` | 577 | 578 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 33–779
- **Visible Samples:** 705

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 33 | 196 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 461 | 264 | inferred_complete_timeline |
| `Action_BallCarry` | 462 | 482 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 486 | 488 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 492 | 642 | 151 | inferred_complete_timeline |
| `Action_BallCarry` | 647 | 672 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 696 | 765 | 70 | inferred_complete_timeline |
| `Action_BallCarry` | 773 | 774 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 776 | 779 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 53–779
- **Visible Samples:** 614

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 53 | 81 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 347 | 250 | inferred_complete_timeline |
| `Action_PreSnap` | 377 | 385 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 412 | 422 | 11 | inferred_complete_timeline |
| `Action_None` | 423 | 434 | 12 | inferred_complete_timeline |
| `Action_None` | 447 | 634 | 188 | inferred_complete_timeline |
| `Action_None` | 657 | 688 | 32 | inferred_complete_timeline |
| `Action_None` | 697 | 779 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 33–665
- **Visible Samples:** 626

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 33 | 38 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 431 | 386 | inferred_complete_timeline |
| `Action_SplitBlock` | 432 | 665 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 213–779
- **Visible Samples:** 544

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 213 | 216 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 425 | 196 | inferred_complete_timeline |
| `Action_ZoneBlock` | 426 | 547 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 551 | 694 | 144 | inferred_complete_timeline |
| `Action_None` | 706 | 779 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 33–630
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 33 | 94 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 425 | 321 | inferred_complete_timeline |
| `Action_ZoneBlock` | 426 | 550 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 552 | 630 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 86–779
- **Visible Samples:** 683

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 86 | 422 | 337 | inferred_complete_timeline |
| `Action_BallSnap` | 423 | 431 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 432 | 579 | 148 | inferred_complete_timeline |
| `Action_ZoneBlock` | 581 | 658 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 663 | 670 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 672 | 701 | 30 | inferred_complete_timeline |
| `Action_None` | 702 | 720 | 19 | inferred_complete_timeline |
| `Action_None` | 725 | 728 | 4 | inferred_complete_timeline |
| `Action_None` | 730 | 779 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 33–703
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 33 | 251 | 219 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 364 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 390 | 393 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 397 | 408 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 412 | 425 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 457 | 459 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 485 | 588 | 104 | inferred_complete_timeline |
| `Action_ZoneBlock` | 592 | 603 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 607 | 674 | 68 | inferred_complete_timeline |
| `Action_ZoneBlock` | 678 | 680 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 694 | 701 | 8 | inferred_complete_timeline |
| `Action_None` | 702 | 703 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 33–779
- **Visible Samples:** 729

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 33 | 422 | 390 | inferred_complete_timeline |
| `Action_None` | 423 | 647 | 225 | inferred_complete_timeline |
| `Action_None` | 651 | 690 | 40 | inferred_complete_timeline |
| `Action_None` | 700 | 719 | 20 | inferred_complete_timeline |
| `Action_None` | 726 | 779 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 106–707
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 106 | 422 | 317 | inferred_complete_timeline |
| `Action_None` | 423 | 636 | 214 | inferred_complete_timeline |
| `Action_None` | 641 | 651 | 11 | inferred_complete_timeline |
| `Action_None` | 655 | 707 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 33–732
- **Visible Samples:** 573

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 33 | 104 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 212 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 293 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 300 | 349 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 397 | 419 | 23 | inferred_complete_timeline |
| `Action_None` | 444 | 480 | 37 | inferred_complete_timeline |
| `Action_None` | 494 | 691 | 198 | inferred_complete_timeline |
| `Action_None` | 693 | 732 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 33–779
- **Visible Samples:** 697

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 33 | 60 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 72 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 422 | 345 | inferred_complete_timeline |
| `Action_None` | 423 | 598 | 176 | inferred_complete_timeline |
| `Action_None` | 605 | 672 | 68 | inferred_complete_timeline |
| `Action_None` | 710 | 779 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 33–702
- **Visible Samples:** 628

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 33 | 134 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 186 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 422 | 234 | inferred_complete_timeline |
| `Action_None` | 423 | 660 | 238 | inferred_complete_timeline |
| `Action_None` | 700 | 702 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 33–779
- **Visible Samples:** 733

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 33 | 422 | 390 | inferred_complete_timeline |
| `Action_None` | 423 | 619 | 197 | inferred_complete_timeline |
| `Action_None` | 625 | 706 | 82 | inferred_complete_timeline |
| `Action_None` | 710 | 739 | 30 | inferred_complete_timeline |
| `Action_None` | 744 | 758 | 15 | inferred_complete_timeline |
| `Action_None` | 761 | 779 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 33–779
- **Visible Samples:** 747

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 33 | 422 | 390 | inferred_complete_timeline |
| `Action_None` | 423 | 779 | 357 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 42–779
- **Visible Samples:** 738

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 42 | 422 | 381 | inferred_complete_timeline |
| `Action_None` | 423 | 779 | 357 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 33–593
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 33 | 422 | 390 | inferred_complete_timeline |
| `Action_None` | 423 | 593 | 171 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 33–93 | 61 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 33–99 | 67 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 33–161 | 104 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 550–563 | 14 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 570–629 | 49 | 6 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 597–608 | 12 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 612–705 | 66 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 617–779 | 144 | 4 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 650–779 | 82 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 670–773 | 78 | 7 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 671–678 | 8 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 673–779 | 106 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 677–779 | 103 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 682–777 | 83 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 687–754 | 20 | 3 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 715–774 | 60 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 717–720 | 4 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 717–779 | 63 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 717–779 | 60 | 2 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 721–722 | 2 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 723–779 | 57 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 723–725 | 3 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 723–779 | 57 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 748–759 | 12 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 756–779 | 24 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 779–779 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 117 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 779 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (LG) duration 205 frames exceeds threshold 90 frames [start=426, end=630].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 276 frames exceeds threshold 90 frames [start=426, end=701].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 276 frames exceeds threshold 90 frames [start=426, end=701].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [423–431], lower_priority='Action_ZoneBlock' annotated_start=426, effective_Action_ZoneBlock_start=432.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 276 frames exceeds threshold 90 frames [start=426, end=701].
- ⚠️ Action 'Action_None' range [423-647] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-690] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [700-719] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-104] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-212] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-293] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-349] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-480] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-691] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [693-732] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-134] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-186] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-660] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [700-702] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-93] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-133] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-161] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-38] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [432-665] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-619] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-706] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [710-739] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [744-758] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [426-550] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [552-630] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-196] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [462-482] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [486-488] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [492-642] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [647-672] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [696-765] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [773-774] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-251] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-290] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-364] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-393] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-408] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-425] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [457-459] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [485-588] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [592-603] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [607-674] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [678-680] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-703] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-422] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-72] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-598] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-672] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-422] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-593] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-347] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-385] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-434] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-634] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [657-688] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [697-779] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-422] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [432-579] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [581-658] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [663-670] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [672-701] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-720] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [725-728] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-636] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [641-651] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [655-707] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-212] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-417] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-469] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-515] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-216] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [426-547] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [551-694] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-563] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-574] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-586] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-595] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-601] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-616] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-629] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-608] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-649] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [678-705] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-618] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-680] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [683-751] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-653] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [685-694] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [670-697] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [706-709] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [711-716] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [725-742] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [744-745] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [748-754] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [761-773] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [671-678] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [673-698] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [682-714] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [728-777] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [687-694] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [697-706] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [753-754] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [715-774] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [717-720] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [717-751] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [721-722] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [723-725] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [748-759] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>