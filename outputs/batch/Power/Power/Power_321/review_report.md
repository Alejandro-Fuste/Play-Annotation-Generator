# Play-Annotation-Generator Annotation Review — Power_321

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_321`
- **Frame Range:** 0 to 779 (780 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Touchdown`
- **Result Frame:** 779
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 120
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 514 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 581 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 260 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 445 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 469 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 547 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 554 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 574 |
| ✅ EXACT | `Action_DownBlock` | C | `15` | `15` | 446 | START | 446 | 450 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `21` | `21` | 446 | START | 446 | 454 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `18` | `18` | 446 | START | 446 | 505 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–608
- **Visible Samples:** 606

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 260 | 261 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 608 | 345 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–627
- **Visible Samples:** 616

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 547 | 548 | inferred_complete_timeline |
| `Action_PreSnap` | 559 | 560 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 562 | 627 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–574
- **Visible Samples:** 575

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 574 | 575 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–581
- **Visible Samples:** 582

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 581 | 582 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–514
- **Visible Samples:** 515

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 514 | 515 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–779
- **Visible Samples:** 707

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 182 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 289 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 445 | 155 | inferred_complete_timeline |
| `Action_DownBlock` | 446 | 454 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 458 | 506 | 49 | inferred_complete_timeline |
| `Action_None` | 507 | 523 | 17 | inferred_complete_timeline |
| `Action_None` | 529 | 756 | 228 | inferred_complete_timeline |
| `Action_None` | 759 | 766 | 8 | inferred_complete_timeline |
| `Action_None` | 768 | 779 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–557
- **Visible Samples:** 557

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 554 | 555 | inferred_complete_timeline |
| `Action_PreSnap` | 556 | 557 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–450
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 445 | 446 | inferred_complete_timeline |
| `Action_DownBlock` | 446 | 450 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–779
- **Visible Samples:** 754

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 469 | 470 | inferred_complete_timeline |
| `Action_PreSnap` | 478 | 482 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 488 | 521 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 525 | 527 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 537 | 565 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 567 | 779 | 213 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–779
- **Visible Samples:** 762

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 487 | 488 | inferred_complete_timeline |
| `Action_PreSnap` | 506 | 779 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–779
- **Visible Samples:** 770

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 530 | 531 | inferred_complete_timeline |
| `Action_PreSnap` | 536 | 704 | 169 | inferred_complete_timeline |
| `Action_PreSnap` | 707 | 727 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 731 | 779 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–537
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 537 | 538 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–693
- **Visible Samples:** 694

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 693 | 694 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–779
- **Visible Samples:** 772

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 517 | 518 | inferred_complete_timeline |
| `Action_PreSnap` | 520 | 521 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 523 | 529 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 531 | 535 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 538 | 542 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 545 | 779 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–779
- **Visible Samples:** 776

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 484 | 485 | inferred_complete_timeline |
| `Action_PreSnap` | 489 | 779 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–779
- **Visible Samples:** 771

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 500 | 501 | inferred_complete_timeline |
| `Action_PreSnap` | 507 | 755 | 249 | inferred_complete_timeline |
| `Action_PreSnap` | 759 | 779 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–558
- **Visible Samples:** 559

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 558 | 559 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–524
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 524 | 525 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–779
- **Visible Samples:** 776

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 699 | 700 | inferred_complete_timeline |
| `Action_PreSnap` | 702 | 741 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 744 | 779 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–680
- **Visible Samples:** 680

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 525 | 526 | inferred_complete_timeline |
| `Action_PreSnap` | 527 | 680 | 154 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–779 | 780 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–779 | 777 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 355–357 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 461–654 | 194 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 516–522 | 7 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 521–523 | 3 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 547–564 | 13 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 584–586 | 3 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 586–779 | 194 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 590–779 | 172 | 7 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 615–616 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 621–622 | 2 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 660–779 | 120 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 674–779 | 106 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 675–676 | 2 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 685–779 | 95 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 686–779 | 94 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 690–692 | 3 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 703–704 | 2 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 758–779 | 22 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 759–761 | 3 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 760–779 | 20 | 1 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 779–779 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 73 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 779 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-514] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-581] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-524] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-574] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-530] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [536-704] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [707-727] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-699] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [702-741] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-500] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [507-755] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-693] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-517] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [520-521] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [523-529] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [531-535] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [538-542] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [545-779] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-537] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-525] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [527-680] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-260] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-608] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-558] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-484] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [446-450] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-487] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-469] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [478-482] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [488-521] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [525-527] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [537-565] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [567-779] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [446-505] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-547] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [559-560] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [562-627] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-554] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [556-557] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-182] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-289] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-445] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [446-454] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-523] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-756] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [759-766] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-357] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-654] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [516-522] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [521-523] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [547-550] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [555-559] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [561-564] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [584-586] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [586-779] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [590-592] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [598-602] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [607-632] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [634-637] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [642-646] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [648-709] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [713-779] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [615-616] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [621-622] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [674-779] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [675-676] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [690-692] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [703-704] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [759-761] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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