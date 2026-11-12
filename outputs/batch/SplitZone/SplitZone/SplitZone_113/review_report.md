# Play-Annotation-Generator Annotation Review — SplitZone_113

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_113`
- **Frame Range:** 0 to 839 (840 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 839
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 152
- **Validation Warnings:** 142
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 104
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `22` | `22` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `16` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 5 | START | 6 | 701 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 5 | START | 6 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 5 | START | 6 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 5 | START | 6 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 5 | START | 6 | 722 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 5 | START | 6 | 324 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 5 | START | 6 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 5 | START | 6 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 5 | START | 6 | 701 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 5 | START | 6 | 702 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 5 | START | 6 | 701 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 702 | START | 702 | 715 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `4` | `4` | 703 | START | 703 | 763 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `11` | `11` | 705 | START | 705 | 728 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `12` | `12` | 705 | START | 705 | 763 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `15` | 705 | START | 716 | 717 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `20` | 705 | START | 705 | 726 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `22` | `22` | 705 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 715 | END | 702 | 715 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `19` | 719 | START | 719 | 722 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `16` | `16` | 723 | START | 723 | 728 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 770 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 6–839
- **Visible Samples:** 815

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 324 | 319 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 701 | 363 | inferred_complete_timeline |
| `Action_SnapReceive` | 702 | 715 | 14 | inferred_complete_timeline |
| `Action_None` | 716 | 718 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 719 | 722 | 4 | inferred_complete_timeline |
| `Action_None` | 723 | 762 | 40 | inferred_complete_timeline |
| `Action_None` | 768 | 839 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 6–839
- **Visible Samples:** 828

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 722 | 717 | inferred_complete_timeline |
| `Action_BallCarry` | 723 | 728 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 735 | 839 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 6–839
- **Visible Samples:** 834

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 701 | 696 | inferred_complete_timeline |
| `Action_None` | 702 | 839 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 6–839
- **Visible Samples:** 834

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 701 | 696 | inferred_complete_timeline |
| `Action_None` | 702 | 839 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 6–839
- **Visible Samples:** 834

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 701 | 696 | inferred_complete_timeline |
| `Action_None` | 702 | 839 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 6–839
- **Visible Samples:** 823

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 702 | 697 | inferred_complete_timeline |
| `Action_SplitBlock` | 703 | 763 | 61 | inferred_complete_timeline |
| `Action_SplitBlock` | 768 | 770 | 3 | inferred_complete_timeline |
| `Action_None` | 778 | 839 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 6–839
- **Visible Samples:** 717

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 33 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 52 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 92 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 704 | 611 | inferred_complete_timeline |
| `Action_ZoneBlock` | 705 | 726 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 728 | 735 | 8 | inferred_complete_timeline |
| `Action_None` | 814 | 815 | 2 | inferred_complete_timeline |
| `Action_None` | 819 | 820 | 2 | inferred_complete_timeline |
| `Action_None` | 823 | 839 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 6–839
- **Visible Samples:** 749

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 34 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 78 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 332 | 253 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 340 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 348 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 351 | 358 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 361 | 704 | 344 | inferred_complete_timeline |
| `Action_ZoneBlock` | 705 | 728 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 730 | 763 | 34 | inferred_complete_timeline |
| `Action_None` | 800 | 807 | 8 | inferred_complete_timeline |
| `Action_None` | 810 | 811 | 2 | inferred_complete_timeline |
| `Action_None` | 813 | 839 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 6–839
- **Visible Samples:** 723

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 21 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 332 | 268 | inferred_complete_timeline |
| `Action_PreSnap` | 372 | 376 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 386 | 701 | 316 | inferred_complete_timeline |
| `Action_BallSnap` | 702 | 715 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 716 | 717 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 726 | 730 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 754 | 770 | 17 | inferred_complete_timeline |
| `Action_None` | 771 | 839 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 6–340
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 12 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 17 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 33 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 167 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 332 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 340 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 6–763
- **Visible Samples:** 744

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 52 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 704 | 636 | inferred_complete_timeline |
| `Action_ZoneBlock` | 705 | 763 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 6–762
- **Visible Samples:** 735

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 59 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 328 | 264 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 332 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 507 | 173 | inferred_complete_timeline |
| `Action_PreSnap` | 509 | 530 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 539 | 540 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 545 | 548 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 550 | 701 | 152 | inferred_complete_timeline |
| `Action_None` | 702 | 732 | 31 | inferred_complete_timeline |
| `Action_None` | 735 | 762 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 6–839
- **Visible Samples:** 810

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 701 | 696 | inferred_complete_timeline |
| `Action_None` | 702 | 763 | 62 | inferred_complete_timeline |
| `Action_None` | 768 | 771 | 4 | inferred_complete_timeline |
| `Action_None` | 789 | 809 | 21 | inferred_complete_timeline |
| `Action_None` | 813 | 839 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 6–839
- **Visible Samples:** 731

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 40 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 44 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 48 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 363 | 281 | inferred_complete_timeline |
| `Action_PreSnap` | 366 | 701 | 336 | inferred_complete_timeline |
| `Action_None` | 702 | 741 | 40 | inferred_complete_timeline |
| `Action_None` | 746 | 751 | 6 | inferred_complete_timeline |
| `Action_None` | 821 | 839 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 6–839
- **Visible Samples:** 684

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 48 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 312 | 248 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 324 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 374 | 375 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 386 | 387 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 389 | 390 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 397 | 398 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 401 | 481 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 483 | 701 | 219 | inferred_complete_timeline |
| `Action_None` | 702 | 758 | 57 | inferred_complete_timeline |
| `Action_None` | 761 | 762 | 2 | inferred_complete_timeline |
| `Action_None` | 822 | 825 | 4 | inferred_complete_timeline |
| `Action_None` | 827 | 836 | 10 | inferred_complete_timeline |
| `Action_None` | 838 | 839 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 6–763
- **Visible Samples:** 756

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 12 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 17 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 701 | 683 | inferred_complete_timeline |
| `Action_None` | 702 | 763 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 6–839
- **Visible Samples:** 795

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 701 | 696 | inferred_complete_timeline |
| `Action_None` | 702 | 746 | 45 | inferred_complete_timeline |
| `Action_None` | 749 | 762 | 14 | inferred_complete_timeline |
| `Action_None` | 794 | 810 | 17 | inferred_complete_timeline |
| `Action_None` | 814 | 815 | 2 | inferred_complete_timeline |
| `Action_None` | 819 | 839 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 6–837
- **Visible Samples:** 832

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 701 | 696 | inferred_complete_timeline |
| `Action_None` | 702 | 837 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 6–839
- **Visible Samples:** 832

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 701 | 696 | inferred_complete_timeline |
| `Action_None` | 702 | 805 | 104 | inferred_complete_timeline |
| `Action_None` | 808 | 839 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 6–839
- **Visible Samples:** 830

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 701 | 696 | inferred_complete_timeline |
| `Action_None` | 702 | 831 | 130 | inferred_complete_timeline |
| `Action_None` | 836 | 839 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 6–839
- **Visible Samples:** 827

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 701 | 696 | inferred_complete_timeline |
| `Action_None` | 702 | 768 | 67 | inferred_complete_timeline |
| `Action_None` | 773 | 835 | 63 | inferred_complete_timeline |
| `Action_None` | 839 | 839 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 6–839
- **Visible Samples:** 833

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 701 | 696 | inferred_complete_timeline |
| `Action_None` | 702 | 817 | 116 | inferred_complete_timeline |
| `Action_None` | 819 | 839 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 6–7 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 81–83 | 3 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 250–253 | 4 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 562–763 | 195 | 3 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 741–742 | 2 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 762–839 | 12 | 4 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 773–774 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 781–839 | 59 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 782–839 | 57 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 801–839 | 39 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 823–825 | 3 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 839–839 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `22` (RG)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 115 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 839 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [702–715], lower_priority='Action_ZoneBlock' annotated_start=705, effective_Action_ZoneBlock_start=716.
- ⚠️ Segment 'Action_ZoneBlock' for track '22' has invalid range: start=705, end=340. Clamping end to start.
- ⚠️ Action 'Action_None' range [702-837] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-746] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [749-762] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [794-810] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [814-815] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [819-839] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [703-763] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [768-770] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-817] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [819-839] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-768] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [773-835] for track '6' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-763] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [768-771] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [789-809] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [813-839] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-839] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-831] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-805] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-34] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-332] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-340] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-348] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-358] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-704] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [705-728] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [730-763] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [800-807] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [810-811] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [813-839] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-52] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-704] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [705-763] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-312] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-324] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-375] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-387] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-390] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-398] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-481] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [483-701] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-758] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [761-762] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [822-825] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [827-836] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-59] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-328] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-332] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-507] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [509-530] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [539-540] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [545-548] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [550-701] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-732] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [735-762] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-52] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-332] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-376] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [716-717] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [726-730] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [723-728] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-40] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-52] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-363] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-741] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [746-751] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-12] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-17] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-701] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-763] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-324] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-701] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [723-762] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-33] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-52] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-85] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-92] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [705-726] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [728-735] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [814-815] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [819-820] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [823-839] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-12] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-17] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-33] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-77] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-167] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-174] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-332] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-340] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-83] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-253] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [562-573] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-763] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [741-742] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [762-766] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [827-829] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [835-836] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [773-774] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [782-820] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [823-825] for track '32' has 1 frames without a visible bounding box.
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

</details>