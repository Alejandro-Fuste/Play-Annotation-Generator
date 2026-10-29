# Play-Annotation-Generator Annotation Review — Duo_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_33`
- **Frame Range:** 0 to 658 (659 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 658
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 67
- **Validation Warnings:** 65
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 38
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | DE1 | defense | `14` | `14` |
| ✅ EXACT | `Action_ComboBlock` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_ComboBlock` | LB1 | defense | `6` | `6` |
| ✅ EXACT | `Action_ComboBlock` | CB2 | defense | `9` | `9` |
| ✅ EXACT | `Action_BlockSecondLevel` | LB1 | defense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 658 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `11` | `Group` | 0 | START | 0 | 642 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 658 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 658 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 255 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 301 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `21` | `Group` | 0 | START | 0 | 312 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 547 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 553 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 551 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 513 |
| ✅ EXACT | `Action_ComboBlock` | DE1 | `14` | `14` | 256 | START | 256 | 304 |
| ✅ EXACT | `Action_ComboBlock` | QB | `17` | `17` | 256 | START | 256 | 304 |
| ✅ EXACT | `Action_ComboBlock` | LB1 | `6` | `6` | 256 | START | 256 | 257 |
| ✅ EXACT | `Action_ComboBlock` | CB2 | `9` | `9` | 256 | START | 256 | 304 |
| ✅ EXACT | `Action_BlockSecondLevel` | LB1 | `6` | `6` | 258 | START | 258 | 304 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 304 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–658
- **Visible Samples:** 659

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 255 | 256 | inferred_complete_timeline |
| `Action_ComboBlock` | 256 | 304 | 49 | inferred_complete_timeline |
| `Action_None` | 305 | 658 | 354 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–612
- **Visible Samples:** 611

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 553 | 554 | inferred_complete_timeline |
| `Action_PreSnap` | 556 | 612 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–658
- **Visible Samples:** 659

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 658 | 659 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–658
- **Visible Samples:** 659

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 658 | 659 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–658
- **Visible Samples:** 650

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 642 | 643 | inferred_complete_timeline |
| `Action_PreSnap` | 652 | 658 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–658
- **Visible Samples:** 632

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 312 | 313 | inferred_complete_timeline |
| `Action_PreSnap` | 336 | 339 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 344 | 658 | 315 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–658
- **Visible Samples:** 651

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 551 | 552 | inferred_complete_timeline |
| `Action_PreSnap` | 553 | 554 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 558 | 559 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 563 | 564 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 566 | 658 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–547
- **Visible Samples:** 548

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 547 | 548 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–658
- **Visible Samples:** 657

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 513 | 514 | inferred_complete_timeline |
| `Action_PreSnap` | 516 | 658 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–520
- **Visible Samples:** 513

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 301 | 302 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 308 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 314 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 520 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–658
- **Visible Samples:** 659

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 658 | 659 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–658
- **Visible Samples:** 659

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 255 | 256 | inferred_complete_timeline |
| `Action_ComboBlock` | 256 | 304 | 49 | inferred_complete_timeline |
| `Action_None` | 305 | 658 | 354 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–658
- **Visible Samples:** 655

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 553 | 554 | inferred_complete_timeline |
| `Action_PreSnap` | 558 | 658 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–658
- **Visible Samples:** 658

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 545 | 546 | inferred_complete_timeline |
| `Action_PreSnap` | 547 | 658 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–556
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 527 | 528 | inferred_complete_timeline |
| `Action_PreSnap` | 537 | 540 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 553 | 556 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–648
- **Visible Samples:** 636

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 255 | 256 | inferred_complete_timeline |
| `Action_ComboBlock` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 258 | 304 | 47 | inferred_complete_timeline |
| `Action_None` | 305 | 593 | 289 | inferred_complete_timeline |
| `Action_None` | 596 | 628 | 33 | inferred_complete_timeline |
| `Action_None` | 633 | 636 | 4 | inferred_complete_timeline |
| `Action_None` | 644 | 648 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–658
- **Visible Samples:** 659

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 658 | 659 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–600
- **Visible Samples:** 585

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 579 | 580 | inferred_complete_timeline |
| `Action_PreSnap` | 596 | 600 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–658
- **Visible Samples:** 659

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 255 | 256 | inferred_complete_timeline |
| `Action_ComboBlock` | 256 | 304 | 49 | inferred_complete_timeline |
| `Action_None` | 305 | 658 | 354 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–658
- **Visible Samples:** 643

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 600 | 601 | inferred_complete_timeline |
| `Action_PreSnap` | 609 | 614 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 623 | 658 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–658
- **Visible Samples:** 659

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 658 | 659 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–560
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 560 | 561 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 107–108 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 534–658 | 110 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 543–558 | 16 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 549–554 | 6 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 554–558 | 5 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 560–658 | 99 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 562–658 | 88 | 3 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 606–658 | 53 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 635–658 | 24 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 658–658 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 44 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 658 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-545] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-527] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [537-540] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [553-556] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-547] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-553] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [556-612] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-551] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [553-554] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [558-559] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [563-564] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-593] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-628] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-636] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-648] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-513] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [516-658] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-553] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [558-658] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-600] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [609-614] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-642] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-658] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-658] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-579] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [596-600] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-560] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-301] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-308] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-314] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-520] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-312] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-339] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-658] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [534-535] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [551-658] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [543-558] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [549-554] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [554-558] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [560-658] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [562-609] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [613-614] for track '28' has 1 frames without a visible bounding box.
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

</details>