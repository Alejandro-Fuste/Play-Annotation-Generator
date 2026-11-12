# Play-Annotation-Generator Annotation Review — SplitZone_80

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_80`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 539
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 144
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_SplitBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 18 | START | 19 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 18 | START | 19 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 18 | START | 19 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 18 | START | 19 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 18 | START | 19 | 314 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 18 | START | 19 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 18 | START | 19 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 18 | START | 19 | 311 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `14` | `14` | 312 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RG | `1` | `1` | 315 | START | 315 | 424 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 315 | START | 341 | 342 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `2` | 315 | START | 315 | 402 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `3` | `3` | 315 | START | 315 | 317 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `5` | 315 | START | 315 | 424 |
| ✅ EXACT | `Action_SplitBlock` | LG | `3` | `3` | 318 | START | 318 | 424 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 319 | END | 312 | 319 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `6` | 330 | START | 330 | 354 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 332 | START | 332 | 539 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 424 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 19–539
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 311 | 293 | inferred_complete_timeline |
| `Action_SnapReceive` | 312 | 319 | 8 | inferred_complete_timeline |
| `Action_None` | 320 | 331 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 332 | 539 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 19–539
- **Visible Samples:** 516

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 329 | 311 | inferred_complete_timeline |
| `Action_BallCarry` | 330 | 354 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 358 | 475 | 118 | inferred_complete_timeline |
| `Action_BallCarry` | 478 | 539 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 19–448
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 141 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 311 | 167 | inferred_complete_timeline |
| `Action_None` | 312 | 338 | 27 | inferred_complete_timeline |
| `Action_None` | 340 | 382 | 43 | inferred_complete_timeline |
| `Action_None` | 444 | 448 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 19–409
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 168 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 314 | 143 | inferred_complete_timeline |
| `Action_ZoneBlock` | 315 | 402 | 88 | inferred_complete_timeline |
| `Action_ZoneBlock` | 404 | 409 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 19–483
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 314 | 296 | inferred_complete_timeline |
| `Action_ZoneBlock` | 315 | 317 | 3 | inferred_complete_timeline |
| `Action_SplitBlock` | 318 | 424 | 107 | inferred_complete_timeline |
| `Action_None` | 425 | 483 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 19–445
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 85 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 122 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 137 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 212 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 301 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 306 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 341 | 342 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 377 | 384 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 391 | 392 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 400 | 424 | 25 | inferred_complete_timeline |
| `Action_None` | 425 | 445 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 19–463
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 128 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 314 | 183 | inferred_complete_timeline |
| `Action_ZoneBlock` | 315 | 424 | 110 | inferred_complete_timeline |
| `Action_None` | 425 | 463 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 19–451
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 112 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 314 | 197 | inferred_complete_timeline |
| `Action_ZoneBlock` | 315 | 424 | 110 | inferred_complete_timeline |
| `Action_None` | 425 | 451 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 19–332
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 311 | 293 | inferred_complete_timeline |
| `Action_None` | 312 | 332 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 19–122
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 111 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 122 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 19–233
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 134 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 233 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 19–354
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 311 | 293 | inferred_complete_timeline |
| `Action_None` | 312 | 354 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 26–539
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 311 | 286 | inferred_complete_timeline |
| `Action_None` | 312 | 489 | 178 | inferred_complete_timeline |
| `Action_None` | 491 | 492 | 2 | inferred_complete_timeline |
| `Action_None` | 496 | 539 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 19–470
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 311 | 293 | inferred_complete_timeline |
| `Action_None` | 312 | 470 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 19–393
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 311 | 293 | inferred_complete_timeline |
| `Action_None` | 312 | 393 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 19–426
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 311 | 293 | inferred_complete_timeline |
| `Action_None` | 312 | 415 | 104 | inferred_complete_timeline |
| `Action_None` | 419 | 426 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 80–81 | 2 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 119–124 | 6 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 125–480 | 281 | 10 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 305–538 | 226 | 5 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 305–465 | 151 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 330–539 | 197 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 361–378 | 18 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 383–537 | 154 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 405–422 | 17 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 405–539 | 128 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 407–498 | 58 | 6 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 413–539 | 126 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 420–539 | 118 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 421–487 | 67 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 448–471 | 7 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 453–475 | 23 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 463–539 | 77 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 475–476 | 2 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 476–482 | 7 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 492–539 | 37 | 3 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 496–498 | 3 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 507–539 | 33 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 529–539 | 11 | 1 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 534–539 | 6 | 1 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 539–539 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `14` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 88 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (RG) duration 110 frames exceeds threshold 90 frames [start=315, end=424].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 95 frames exceeds threshold 90 frames [start=315, end=409].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (RT) duration 110 frames exceeds threshold 90 frames [start=315, end=424].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 110 frames exceeds threshold 90 frames [start=315, end=424].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [312–319], lower_priority='Action_ZoneBlock' annotated_start=315, effective_Action_ZoneBlock_start=320.
- ⚠️ Action 'Action_PreSnap' range [19-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-338] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-382] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-448] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-128] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-463] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-168] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [315-402] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [404-409] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-314] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [318-424] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-483] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-393] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-112] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-451] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [330-354] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [358-475] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-354] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-332] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-415] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-426] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-470] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-134] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-233] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-122] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-212] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-301] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-306] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [341-342] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [377-384] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [391-392] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-445] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-489] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-186] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-197] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-201] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-263] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-311] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-349] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-393] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-480] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-366] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-375] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-529] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-538] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-306] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-316] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-446] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-465] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-388] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-452] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-487] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-539] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-378] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-385] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-537] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-412] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-422] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-441] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-487] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-539] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-420] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-434] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-450] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-498] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-473] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-502] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-487] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-451] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-471] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-475] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-476] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-482] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-503] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-516] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-498] for track '36' has 1 frames without a visible bounding box.
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