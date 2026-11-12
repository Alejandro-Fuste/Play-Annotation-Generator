# Play-Annotation-Generator Annotation Review — SplitZone_135

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_135`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 539
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `26` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LB2 | defense | `20` | `20` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `25` | `23` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `26` | `24` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `15` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `25` | `23` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 14 | START | 15 | 374 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 14 | START | 15 | 211 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 14 | START | 15 | 377 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 14 | START | 15 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 14 | START | 15 | 374 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 14 | START | 15 | 400 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `25` | `Group` | 14 | START | 44 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `26` | `Group` | 14 | START | 156 | 233 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 14 | START | 15 | 376 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 14 | START | 15 | 374 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 14 | START | 15 | 374 |
| ✅ EXACT | `Action_BallSnap` | LB2 | `20` | `20` | 375 | START | 375 | 386 |
| ✅ EXACT | `Action_SplitBlock` | TE | `3` | `3` | 377 | START | 377 | 466 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `10` | 378 | START | 378 | 466 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `12` | 378 | START | 378 | 466 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 378 | START | 378 | 400 |
| ✅ EXACT | `Action_ZoneBlock` | C | `25` | `23` | 378 | START | 378 | 402 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `26` | `24` | 378 | START | 378 | 466 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 386 | END | 375 | 386 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `14` | 393 | START | 393 | 400 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `15` | `15` | 401 | START | 401 | 403 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `25` | `23` | 403 | START | 403 | 466 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 466 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 15–536
- **Visible Samples:** 514

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 374 | 360 | inferred_complete_timeline |
| `Action_SnapReceive` | 375 | 386 | 12 | inferred_complete_timeline |
| `Action_None` | 387 | 392 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 393 | 400 | 8 | inferred_complete_timeline |
| `Action_None` | 401 | 440 | 40 | inferred_complete_timeline |
| `Action_None` | 445 | 451 | 7 | inferred_complete_timeline |
| `Action_None` | 453 | 521 | 69 | inferred_complete_timeline |
| `Action_None` | 525 | 536 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 15–539
- **Visible Samples:** 522

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 400 | 386 | inferred_complete_timeline |
| `Action_BallCarry` | 401 | 403 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 407 | 539 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 15–539
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 374 | 360 | inferred_complete_timeline |
| `Action_None` | 375 | 539 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 15–539
- **Visible Samples:** 520

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 374 | 360 | inferred_complete_timeline |
| `Action_None` | 375 | 437 | 63 | inferred_complete_timeline |
| `Action_None` | 441 | 442 | 2 | inferred_complete_timeline |
| `Action_None` | 444 | 446 | 3 | inferred_complete_timeline |
| `Action_None` | 448 | 539 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 15–539
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 374 | 360 | inferred_complete_timeline |
| `Action_None` | 375 | 539 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 15–539
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 376 | 362 | inferred_complete_timeline |
| `Action_SplitBlock` | 377 | 466 | 90 | inferred_complete_timeline |
| `Action_None` | 467 | 539 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 15–539
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 377 | 363 | inferred_complete_timeline |
| `Action_ZoneBlock` | 378 | 466 | 89 | inferred_complete_timeline |
| `Action_None` | 467 | 539 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `26`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `26`
- **team_side:** `offense`
- **Visible Frames:** 156–539
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 156 | 233 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 377 | 138 | inferred_complete_timeline |
| `Action_ZoneBlock` | 378 | 466 | 89 | inferred_complete_timeline |
| `Action_None` | 467 | 539 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `25`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 44–539
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 44 | 57 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 89 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 107 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 377 | 269 | inferred_complete_timeline |
| `Action_ZoneBlock` | 378 | 402 | 25 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 403 | 466 | 64 | inferred_complete_timeline |
| `Action_None` | 467 | 475 | 9 | inferred_complete_timeline |
| `Action_None` | 477 | 505 | 29 | inferred_complete_timeline |
| `Action_None` | 510 | 521 | 12 | inferred_complete_timeline |
| `Action_None` | 526 | 539 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 15–539
- **Visible Samples:** 483

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 93 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 103 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 132 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 235 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 377 | 138 | inferred_complete_timeline |
| `Action_ZoneBlock` | 378 | 400 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 403 | 412 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 436 | 466 | 31 | inferred_complete_timeline |
| `Action_None` | 467 | 539 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 15–539
- **Visible Samples:** 519

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 211 | 197 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 235 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 377 | 138 | inferred_complete_timeline |
| `Action_ZoneBlock` | 378 | 466 | 89 | inferred_complete_timeline |
| `Action_None` | 467 | 539 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 15–539
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 374 | 360 | inferred_complete_timeline |
| `Action_None` | 375 | 539 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 15–539
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 374 | 360 | inferred_complete_timeline |
| `Action_None` | 375 | 408 | 34 | inferred_complete_timeline |
| `Action_None` | 413 | 539 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 15–539
- **Visible Samples:** 515

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 81 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 374 | 283 | inferred_complete_timeline |
| `Action_None` | 375 | 461 | 87 | inferred_complete_timeline |
| `Action_None` | 463 | 487 | 25 | inferred_complete_timeline |
| `Action_None` | 489 | 539 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 15–403
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 374 | 360 | inferred_complete_timeline |
| `Action_None` | 375 | 403 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 15–539
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 374 | 360 | inferred_complete_timeline |
| `Action_None` | 375 | 539 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 15–463
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 22 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 374 | 349 | inferred_complete_timeline |
| `Action_BallSnap` | 375 | 386 | 12 | inferred_complete_timeline |
| `Action_None` | 387 | 463 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 15–503
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 374 | 360 | inferred_complete_timeline |
| `Action_None` | 375 | 453 | 79 | inferred_complete_timeline |
| `Action_None` | 456 | 460 | 5 | inferred_complete_timeline |
| `Action_None` | 487 | 491 | 5 | inferred_complete_timeline |
| `Action_None` | 498 | 503 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 15–65
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 65 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 15–539
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 374 | 360 | inferred_complete_timeline |
| `Action_None` | 375 | 539 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 15–539
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 374 | 360 | inferred_complete_timeline |
| `Action_None` | 375 | 539 | 165 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 15–539 | 525 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 15–534 | 516 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 24–35 | 6 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 26–27 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 406–539 | 134 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 464–465 | 2 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 481–539 | 54 | 4 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 511–512 | 2 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 515–529 | 15 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 515–539 | 23 | 3 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 526–529 | 4 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 533–539 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 58 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action 'Action_None' range [467-539] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-528] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-534] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-408] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-437] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-446] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-211] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-235] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-377] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-93] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-132] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-235] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-377] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [378-400] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [403-412] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-440] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-451] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-521] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-536] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [401-403] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-453] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-460] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-491] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-503] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-403] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-81] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-374] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-461] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-487] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-22] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-463] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-32] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-27] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-57] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-89] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-107] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-377] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [378-402] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-475] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-505] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-521] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-233] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-377] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-492] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-499] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-507] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-529] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-529] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-537] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-529] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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