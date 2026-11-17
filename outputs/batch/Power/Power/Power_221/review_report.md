# Play-Annotation-Generator Annotation Review — Power_221

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_221`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 689
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `27` | `24` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 625 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 513 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 534 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 513 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 607 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 637 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 689 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 243 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `15` | `15` | 514 | START | 514 | 533 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `20` | `20` | 514 | START | 514 | 521 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `27` | `24` | 514 | START | 514 | 554 |
| ✅ EXACT | `Action_PullBlock` | LG | `17` | `17` | 514 | START | 514 | 554 |

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
- **Visible Frames:** 0–689
- **Visible Samples:** 671

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 637 | 638 | inferred_complete_timeline |
| `Action_PreSnap` | 644 | 645 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 647 | 654 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 667 | 689 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–673
- **Visible Samples:** 673

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 607 | 608 | inferred_complete_timeline |
| `Action_PreSnap` | 609 | 673 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 689 | 690 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–662
- **Visible Samples:** 657

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 625 | 626 | inferred_complete_timeline |
| `Action_PreSnap` | 627 | 642 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 648 | 662 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 689

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 534 | 535 | inferred_complete_timeline |
| `Action_PreSnap` | 536 | 689 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–640
- **Visible Samples:** 640

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 513 | 514 | inferred_complete_timeline |
| `Action_PullBlock` | 514 | 554 | 41 | inferred_complete_timeline |
| `Action_None` | 555 | 637 | 83 | inferred_complete_timeline |
| `Action_None` | 639 | 640 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 662

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 237 | 137 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 371 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 376 | 377 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 380 | 513 | 134 | inferred_complete_timeline |
| `Action_DownBlock` | 514 | 521 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 531 | 554 | 24 | inferred_complete_timeline |
| `Action_None` | 555 | 623 | 69 | inferred_complete_timeline |
| `Action_None` | 626 | 687 | 62 | inferred_complete_timeline |
| `Action_None` | 689 | 689 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 248 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 682

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 513 | 514 | inferred_complete_timeline |
| `Action_DownBlock` | 514 | 533 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 542 | 554 | 13 | inferred_complete_timeline |
| `Action_None` | 555 | 689 | 135 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 664

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 605 | 606 | inferred_complete_timeline |
| `Action_PreSnap` | 607 | 608 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 611 | 612 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 618 | 622 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 640 | 643 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 645 | 689 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–676
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 378 | 379 | inferred_complete_timeline |
| `Action_PreSnap` | 445 | 637 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 649 | 651 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 653 | 658 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 660 | 676 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 676

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 526 | 527 | inferred_complete_timeline |
| `Action_PreSnap` | 530 | 532 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 537 | 622 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 624 | 656 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 663 | 689 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 677

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 519 | 520 | inferred_complete_timeline |
| `Action_PreSnap` | 521 | 568 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 574 | 640 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 648 | 689 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–679
- **Visible Samples:** 679

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 634 | 635 | inferred_complete_timeline |
| `Action_PreSnap` | 636 | 679 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 677

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 323 | 324 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 368 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 396 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 398 | 543 | 146 | inferred_complete_timeline |
| `Action_PreSnap` | 546 | 547 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 553 | 689 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–653
- **Visible Samples:** 631

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 609 | 610 | inferred_complete_timeline |
| `Action_PreSnap` | 611 | 623 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 635 | 636 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 639 | 642 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 652 | 653 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–605
- **Visible Samples:** 606

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 605 | 606 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 689 | 690 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 684

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 627 | 628 | inferred_complete_timeline |
| `Action_PreSnap` | 629 | 649 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 653 | 670 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 673 | 689 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–672
- **Visible Samples:** 668

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 628 | 629 | inferred_complete_timeline |
| `Action_PreSnap` | 632 | 666 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 669 | 672 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–689 | 690 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–537 | 538 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 78–81 | 4 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 87–113 | 21 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 382–689 | 277 | 7 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 539–689 | 150 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 565–566 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 592–595 | 4 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 619–689 | 59 | 5 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 652–687 | 33 | 3 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 664–665 | 2 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 668–689 | 22 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 675–689 | 15 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 685–686 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 86 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 444: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-625] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [627-642] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [648-662] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-689] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-605] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-537] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-627] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [629-649] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [653-670] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-605] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [607-608] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [611-612] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [618-622] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [640-643] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [645-689] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-689] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-378] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [445-637] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [649-651] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [653-658] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [660-676] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-609] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [611-623] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [635-636] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [639-642] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [652-653] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-628] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [632-666] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [669-672] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-526] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [530-532] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [537-622] for track '11' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [624-656] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-634] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [636-679] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-323] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-368] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-396] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-543] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [546-547] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [553-689] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-519] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [521-568] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [574-640] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [648-689] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [514-533] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-534] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [536-689] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-637] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-640] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-607] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [609-673] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-637] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [644-645] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [647-654] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-237] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-371] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-377] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [514-521] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [531-554] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-623] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-687] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-243] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-248] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-81] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-89] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-108] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-386] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-616] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-622] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-633] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [539-540] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [542-689] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [565-566] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [592-595] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [619-652] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [655-658] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [661-673] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [679-680] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [652-674] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [676-681] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [684-687] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [664-665] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [685-686] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>