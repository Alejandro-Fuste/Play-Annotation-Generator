# Play-Annotation-Generator Annotation Review — Power_222

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_222`
- **Frame Range:** 0 to 719 (720 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 719
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 122
- **Validation Warnings:** 169
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT2 | defense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 21 | START | 21 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 21 | START | 21 | 259 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 21 | START | 21 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 21 | START | 25 | 278 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `3` | `Group` | 21 | START | 21 | 719 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 21 | START | 21 | 540 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 21 | START | 21 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 21 | START | 21 | 289 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT2 | `7` | `7` | 533 | START | 533 | 562 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `9` | `9` | 533 | START | 533 | 583 |
| ✅ EXACT | `Action_PullBlock` | LG | `10` | `10` | 533 | START | 533 | 548 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 21–570
- **Visible Samples:** 544

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 540 | 520 | inferred_complete_timeline |
| `Action_PreSnap` | 546 | 548 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 550 | 570 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 21–719
- **Visible Samples:** 645

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 150 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 388 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 428 | 566 | 139 | inferred_complete_timeline |
| `Action_PreSnap` | 574 | 647 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 651 | 653 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 657 | 719 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 21–719
- **Visible Samples:** 699

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 719 | 699 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 21–653
- **Visible Samples:** 472

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 259 | 239 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 423 | 163 | inferred_complete_timeline |
| `Action_PreSnap` | 449 | 450 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 452 | 455 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 530 | 562 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 621 | 625 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 627 | 628 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 630 | 653 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 21–548
- **Visible Samples:** 518

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 60 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 143 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 532 | 388 | inferred_complete_timeline |
| `Action_PullBlock` | 533 | 548 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 21–630
- **Visible Samples:** 581

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 289 | 269 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 299 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 318 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 326 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 335 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 373 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 376 | 383 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 385 | 402 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 404 | 532 | 129 | inferred_complete_timeline |
| `Action_DownBlock` | 533 | 583 | 51 | inferred_complete_timeline |
| `Action_DownBlock` | 585 | 598 | 14 | inferred_complete_timeline |
| `Action_None` | 599 | 630 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 25–278
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 278 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 21–243
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 31 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 98 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 114 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 128 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 203 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 220 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 243 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 21–602
- **Visible Samples:** 581

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 187 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 602 | 414 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 21–621
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 564 | 544 | inferred_complete_timeline |
| `Action_PreSnap` | 580 | 621 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 21–655
- **Visible Samples:** 602

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 109 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 621 | 488 | inferred_complete_timeline |
| `Action_PreSnap` | 630 | 649 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 651 | 655 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 21–691
- **Visible Samples:** 641

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 279 | 259 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 532 | 235 | inferred_complete_timeline |
| `Action_DownBlock` | 533 | 562 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 568 | 579 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 587 | 598 | 12 | inferred_complete_timeline |
| `Action_None` | 599 | 691 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 21–590
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 173 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 590 | 416 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 21–653
- **Visible Samples:** 611

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 596 | 576 | inferred_complete_timeline |
| `Action_PreSnap` | 598 | 605 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 615 | 634 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 643 | 644 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 649 | 653 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 21–248
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 248 | 228 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 72–129 | 58 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 80–109 | 26 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 134–184 | 49 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 149–174 | 26 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 178–215 | 38 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 237–658 | 340 | 8 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 308–550 | 243 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 374–719 | 340 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 399–659 | 255 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 557–590 | 24 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 561–664 | 61 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 599–648 | 47 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 602–698 | 97 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 602–610 | 9 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 606–611 | 6 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 608–622 | 15 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 621–719 | 80 | 7 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 630–669 | 40 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 631–713 | 83 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 676–719 | 44 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 693–719 | 16 | 3 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 696–719 | 11 | 4 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 704–710 | 6 | 2 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 707–719 | 12 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 713–716 | 4 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 716–719 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 116 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 719 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [21-173] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-590] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-187] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-602] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-564] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [580-621] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-719] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-596] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [598-605] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [615-634] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [643-644] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [649-653] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-621] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [630-649] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [651-655] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-540] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [546-548] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [550-570] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-279] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-532] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [533-562] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [568-579] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-691] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-388] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-566] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [574-647] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [651-653] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-289] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-318] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-326] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-335] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-373] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-383] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-402] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-532] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [533-583] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [585-598] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 599, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [599-630] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-60] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-532] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [533-548] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-259] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-423] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [449-450] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-455] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [530-562] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [621-625] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [627-628] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [630-653] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-31] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-128] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-203] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-243] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-248] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-278] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-153] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-184] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-174] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-215] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-445] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [468-479] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [484-485] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [489-498] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [500-507] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [518-536] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [572-637] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [645-658] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-550] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-702] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-415] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-533] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [536-659] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [557-563] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [574-590] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [561-589] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [628-654] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [660-664] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [599-617] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [620-622] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [624-648] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [602-698] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [602-610] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [606-611] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [608-622] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [621-685] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [690-691] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [693-694] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [697-701] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [709-710] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [714-715] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [718-719] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [630-669] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [631-713] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [693-695] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [703-704] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [709-719] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [696-697] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [709-710] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [712-713] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [704-707] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [709-710] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [707-710] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [713-716] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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