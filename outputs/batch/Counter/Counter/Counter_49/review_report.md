# Play-Annotation-Generator Annotation Review — Counter_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_49`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 689
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `15` | `14` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `19` | `18` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `20` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 40 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 30 | START | 30 | 43 |
| ✅ EXACT | `Action_DownBlock` | LG | `15` | `14` | 41 | START | 41 | 96 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `21` | `20` | 41 | START | 44 | 96 |
| ✅ EXACT | `Action_PullBlock` | RG | `19` | `18` | 41 | START | 41 | 96 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `9` | `8` | 41 | START | 41 | 96 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 43 | END | 30 | 43 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `17` | 51 | START | 51 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `13` | `12` | 65 | START | 65 | 523 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 96 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 688

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_SnapReceive` | 30 | 43 | 14 | inferred_complete_timeline |
| `Action_None` | 44 | 50 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 51 | 64 | 14 | inferred_complete_timeline |
| `Action_None` | 65 | 538 | 474 | inferred_complete_timeline |
| `Action_None` | 541 | 689 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–557
- **Visible Samples:** 542

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_BallCarry` | 65 | 523 | 459 | inferred_complete_timeline |
| `Action_BallCarry` | 528 | 529 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 531 | 544 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 556 | 557 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 686

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 641 | 612 | inferred_complete_timeline |
| `Action_None` | 644 | 645 | 2 | inferred_complete_timeline |
| `Action_None` | 648 | 689 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 677

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 556 | 527 | inferred_complete_timeline |
| `Action_None` | 570 | 689 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 645

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 247 | 218 | inferred_complete_timeline |
| `Action_None` | 252 | 263 | 12 | inferred_complete_timeline |
| `Action_None` | 267 | 304 | 38 | inferred_complete_timeline |
| `Action_None` | 317 | 526 | 210 | inferred_complete_timeline |
| `Action_None` | 528 | 537 | 10 | inferred_complete_timeline |
| `Action_None` | 542 | 554 | 13 | inferred_complete_timeline |
| `Action_None` | 569 | 574 | 6 | inferred_complete_timeline |
| `Action_None` | 577 | 639 | 63 | inferred_complete_timeline |
| `Action_None` | 645 | 689 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 688

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 640 | 611 | inferred_complete_timeline |
| `Action_None` | 643 | 689 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–576
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_DownBlock` | 41 | 96 | 56 | inferred_complete_timeline |
| `Action_None` | 97 | 556 | 460 | inferred_complete_timeline |
| `Action_None` | 558 | 559 | 2 | inferred_complete_timeline |
| `Action_None` | 568 | 576 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_BallSnap` | 30 | 43 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 44 | 96 | 53 | inferred_complete_timeline |
| `Action_None` | 97 | 148 | 52 | inferred_complete_timeline |
| `Action_None` | 152 | 169 | 18 | inferred_complete_timeline |
| `Action_None` | 195 | 198 | 4 | inferred_complete_timeline |
| `Action_None` | 245 | 256 | 12 | inferred_complete_timeline |
| `Action_None` | 261 | 267 | 7 | inferred_complete_timeline |
| `Action_None` | 269 | 273 | 5 | inferred_complete_timeline |
| `Action_None` | 276 | 306 | 31 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 317 | 683 | 367 | inferred_complete_timeline |
| `Action_None` | 687 | 689 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–682
- **Visible Samples:** 677

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PullBlock` | 41 | 96 | 56 | inferred_complete_timeline |
| `Action_None` | 97 | 667 | 571 | inferred_complete_timeline |
| `Action_None` | 673 | 678 | 6 | inferred_complete_timeline |
| `Action_None` | 680 | 682 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 678

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 41 | 96 | 56 | inferred_complete_timeline |
| `Action_None` | 97 | 563 | 467 | inferred_complete_timeline |
| `Action_None` | 566 | 567 | 2 | inferred_complete_timeline |
| `Action_None` | 577 | 647 | 71 | inferred_complete_timeline |
| `Action_None` | 649 | 689 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 662

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 532 | 503 | inferred_complete_timeline |
| `Action_None` | 551 | 560 | 10 | inferred_complete_timeline |
| `Action_None` | 566 | 577 | 12 | inferred_complete_timeline |
| `Action_None` | 583 | 689 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 689 | 660 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 684

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 425 | 396 | inferred_complete_timeline |
| `Action_None` | 432 | 689 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 683

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 640 | 611 | inferred_complete_timeline |
| `Action_None` | 648 | 689 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 689 | 660 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 689

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 641 | 612 | inferred_complete_timeline |
| `Action_None` | 643 | 689 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 689 | 660 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 689 | 660 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 689

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 641 | 612 | inferred_complete_timeline |
| `Action_None` | 643 | 689 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 689

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 650 | 621 | inferred_complete_timeline |
| `Action_None` | 652 | 689 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 689

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 626 | 597 | inferred_complete_timeline |
| `Action_None` | 628 | 689 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 0–569 | 565 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 277–292 | 10 | 3 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 303–315 | 13 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 568–569 | 2 | 1 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 579–689 | 111 | 1 | Undefined position; Undefined team |
| `27` | `42` | Position_Unknown | Team_Unknown | 583–689 | 107 | 1 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 607–619 | 11 | 2 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 633–689 | 48 | 2 | Undefined position; Undefined team |
| `30` | `51` | Position_Unknown | Team_Unknown | 643–644 | 2 | 1 | Undefined position; Undefined team |
| `31` | `52` | Position_Unknown | Team_Unknown | 651–654 | 4 | 1 | Undefined position; Undefined team |
| `32` | `55` | Position_Unknown | Team_Unknown | 679–680 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `21` (C): Annotated start 41 != Inferred start 44
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [30–43], lower_priority='Action_DownBlock' annotated_start=41, effective_Action_DownBlock_start=44.
- ⚠️ Action 'Action_None' range [30-641] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-645] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-641] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-641] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-650] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-626] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-689] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-563] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-647] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-640] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-425] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-689] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-532] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-560] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-577] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-689] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [65-523] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [528-529] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [531-544] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [556-557] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-556] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-559] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-576] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-556] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-689] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-640] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-538] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-689] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-667] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [673-678] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [680-682] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-247] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-263] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-304] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-526] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-537] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-554] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-574] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-639] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [645-689] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-169] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-267] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-273] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-306] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-683] for track '20' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [687-689] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-537] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-569] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-292] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-315] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-569] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-609] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-619] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-640] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [643-644] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-654] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [679-680] for track '32' has 1 frames without a visible bounding box.
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

</details>