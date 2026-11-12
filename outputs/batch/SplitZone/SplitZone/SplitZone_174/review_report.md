# Play-Annotation-Generator Annotation Review — SplitZone_174

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_174`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 599
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `5` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 364 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 361 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 114 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 364 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 324 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `5` | `Group` | 0 | START | 0 | 372 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 404 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 364 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 364 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `16` | `16` | 362 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 365 | END | 362 | 365 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `1` | `1` | 365 | START | 365 | 416 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `16` | `16` | 365 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `2` | 365 | START | 365 | 383 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `7` | `7` | 365 | START | 365 | 438 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `9` | 365 | START | 365 | 496 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `5` | `5` | 373 | START | 373 | 520 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 393 | START | 393 | 404 |
| ✅ EXACT | `Action_BallCarry` | RB | `6` | `6` | 405 | START | 405 | 599 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 528 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–571
- **Visible Samples:** 572

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 361 | 362 | inferred_complete_timeline |
| `Action_SnapReceive` | 362 | 365 | 4 | inferred_complete_timeline |
| `Action_None` | 366 | 392 | 27 | inferred_complete_timeline |
| `Action_Handoff` | 393 | 404 | 12 | inferred_complete_timeline |
| `Action_None` | 405 | 571 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 404 | 405 | inferred_complete_timeline |
| `Action_BallCarry` | 405 | 599 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 324 | 325 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 361 | 36 | inferred_complete_timeline |
| `Action_None` | 362 | 369 | 8 | inferred_complete_timeline |
| `Action_None` | 371 | 599 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–520
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 372 | 373 | inferred_complete_timeline |
| `Action_SplitBlock` | 373 | 520 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–590
- **Visible Samples:** 589

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 364 | 365 | inferred_complete_timeline |
| `Action_ZoneBlock` | 365 | 383 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 385 | 496 | 112 | inferred_complete_timeline |
| `Action_ZoneBlock` | 498 | 528 | 31 | inferred_complete_timeline |
| `Action_None` | 529 | 590 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–450
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 364 | 365 | inferred_complete_timeline |
| `Action_ZoneBlock` | 365 | 438 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 442 | 450 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 114–186
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 114 | 117 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 186 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 364 | 365 | inferred_complete_timeline |
| `Action_ZoneBlock` | 365 | 496 | 132 | inferred_complete_timeline |
| `Action_ZoneBlock` | 503 | 528 | 26 | inferred_complete_timeline |
| `Action_None` | 529 | 599 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–597
- **Visible Samples:** 501

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 364 | 365 | inferred_complete_timeline |
| `Action_ZoneBlock` | 365 | 416 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 431 | 432 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 516 | 528 | 13 | inferred_complete_timeline |
| `Action_None` | 529 | 597 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–426
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 361 | 362 | inferred_complete_timeline |
| `Action_None` | 362 | 426 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 361 | 362 | inferred_complete_timeline |
| `Action_None` | 362 | 599 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–461
- **Visible Samples:** 460

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 361 | 362 | inferred_complete_timeline |
| `Action_None` | 362 | 456 | 95 | inferred_complete_timeline |
| `Action_None` | 459 | 461 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–574
- **Visible Samples:** 575

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 361 | 362 | inferred_complete_timeline |
| `Action_None` | 362 | 574 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 361 | 362 | inferred_complete_timeline |
| `Action_None` | 362 | 599 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–486
- **Visible Samples:** 486

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 361 | 362 | inferred_complete_timeline |
| `Action_None` | 362 | 483 | 122 | inferred_complete_timeline |
| `Action_None` | 485 | 486 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–407
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 361 | 362 | inferred_complete_timeline |
| `Action_None` | 362 | 407 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 192–516 | 253 | 8 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 322–502 | 181 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 370–378 | 8 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 382–599 | 154 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 383–560 | 178 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 396–440 | 45 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 414–599 | 186 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 449–487 | 33 | 4 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 468–599 | 125 | 4 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 470–539 | 70 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 483–576 | 90 | 3 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 488–519 | 31 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 498–511 | 14 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 521–599 | 75 | 2 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 535–536 | 2 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 537–599 | 63 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 539–599 | 61 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 550–551 | 2 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 550–560 | 11 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 583–588 | 6 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 594–595 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `16` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `16` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (RT) duration 164 frames exceeds threshold 90 frames [start=365, end=528].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 164 frames exceeds threshold 90 frames [start=365, end=528].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (RG) duration 164 frames exceeds threshold 90 frames [start=365, end=528].
- ⚠️ Segment 'Action_BallSnap' for track '16' has invalid range: start=362, end=186. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '16' has invalid range: start=365, end=186. Clamping end to start.
- ⚠️ Action 'Action_None' range [362-407] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [365-416] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [431-432] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [516-528] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-597] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [365-383] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [385-496] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-590] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-324] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-369] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-574] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [373-520] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [365-438] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [442-450] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-599] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [365-496] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-571] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-426] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-483] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-456] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-461] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-253] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-186] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-206] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-251] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-261] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-516] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-502] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-378] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-385] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-560] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-440] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-456] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-480] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-484] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-487] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-518] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-530] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-535] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-539] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-558] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-562] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-576] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-516] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-519] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-511] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-594] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-560] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-588] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-595] for track '37' has 1 frames without a visible bounding box.
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

</details>