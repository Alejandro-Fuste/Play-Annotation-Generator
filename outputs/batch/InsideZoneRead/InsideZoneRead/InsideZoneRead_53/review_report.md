# Play-Annotation-Generator Annotation Review — InsideZoneRead_53

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_53`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 539
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | WR5 | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 232 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `19` | `Group` | 0 | START | 0 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 232 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 232 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `21` | `Group` | 0 | START | 0 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 232 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `8` | `Group` | 0 | START | 0 | 280 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 231 | START | 231 | 249 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `9` | 233 | START | 252 | 261 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `15` | `14` | 233 | START | 233 | 260 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `2` | `1` | 233 | START | 233 | 345 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `19` | 233 | START | 233 | 345 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `22` | `21` | 233 | START | 233 | 264 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 250 | END | 231 | 250 |
| ✅ EXACT | `Action_ReadDefender` | QB | `12` | `11` | 255 | START | 255 | 270 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `10` | `9` | 262 | START | 262 | 345 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 271 | START | 271 | 280 |
| ✅ EXACT | `Action_BallCarry` | WR5 | `8` | `7` | 281 | START | 281 | 302 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 345 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–372
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_SnapReceive` | 231 | 250 | 20 | inferred_complete_timeline |
| `Action_None` | 251 | 254 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 255 | 270 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 271 | 280 | 10 | inferred_complete_timeline |
| `Action_None` | 281 | 292 | 12 | inferred_complete_timeline |
| `Action_None` | 298 | 321 | 24 | inferred_complete_timeline |
| `Action_None` | 327 | 372 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–342
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_None` | 231 | 309 | 79 | inferred_complete_timeline |
| `Action_None` | 312 | 342 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–416
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_None` | 231 | 333 | 103 | inferred_complete_timeline |
| `Action_None` | 338 | 416 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–494
- **Visible Samples:** 495

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_None` | 231 | 494 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–377
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_None` | 231 | 334 | 104 | inferred_complete_timeline |
| `Action_None` | 341 | 377 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–302
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 280 | 281 | inferred_complete_timeline |
| `Action_BallCarry` | 281 | 302 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_ZoneBlock` | 233 | 264 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 269 | 270 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–416
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_ZoneBlock` | 233 | 345 | 113 | inferred_complete_timeline |
| `Action_None` | 346 | 416 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–430
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_BallSnap` | 231 | 249 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 252 | 261 | 10 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 262 | 345 | 84 | inferred_complete_timeline |
| `Action_None` | 346 | 414 | 69 | inferred_complete_timeline |
| `Action_None` | 417 | 430 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–417
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_ZoneBlock` | 233 | 345 | 113 | inferred_complete_timeline |
| `Action_None` | 346 | 373 | 28 | inferred_complete_timeline |
| `Action_None` | 375 | 376 | 2 | inferred_complete_timeline |
| `Action_None` | 383 | 417 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–427
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_ZoneBlock` | 233 | 260 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 262 | 345 | 84 | inferred_complete_timeline |
| `Action_None` | 346 | 427 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–414
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_None` | 231 | 353 | 123 | inferred_complete_timeline |
| `Action_None` | 358 | 414 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–425
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_None` | 231 | 425 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–485
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_None` | 231 | 305 | 75 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_None` | 320 | 485 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–423
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_None` | 231 | 423 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–383
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_None` | 231 | 351 | 121 | inferred_complete_timeline |
| `Action_None` | 353 | 383 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–383
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_None` | 231 | 383 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–436
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_None` | 231 | 436 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_None` | 231 | 326 | 96 | inferred_complete_timeline |
| `Action_None` | 333 | 524 | 192 | inferred_complete_timeline |
| `Action_None` | 526 | 539 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–305
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_None` | 231 | 305 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–444
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_None` | 231 | 408 | 178 | inferred_complete_timeline |
| `Action_None` | 412 | 444 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–402 | 403 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 278–279 | 2 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 280–413 | 124 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 306–345 | 40 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 347–539 | 193 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 347–348 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 351–404 | 53 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 356–536 | 174 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 361–375 | 15 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 391–403 | 9 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 401–422 | 22 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 410–418 | 9 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 410–443 | 33 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 430–539 | 108 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 472–517 | 46 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 525–539 | 15 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 538–539 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 233 != Inferred start 252
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 108: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (RG) duration 113 frames exceeds threshold 90 frames [start=233, end=345].
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [231–250], lower_priority='Action_ZoneBlock' annotated_start=233, effective_Action_ZoneBlock_start=251.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RT) duration 113 frames exceeds threshold 90 frames [start=233, end=345].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 113 frames exceeds threshold 90 frames [start=233, end=345].
- ⚠️ Action 'Action_None' range [231-423] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-373] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-417] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-334] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-377] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-383] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-425] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-436] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-494] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [281-302] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-402] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [231-249] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [252-261] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-414] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-430] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-305] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-485] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-292] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-321] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-372] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-305] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-351] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-383] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [233-260] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-427] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-326] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-524] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-353] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-414] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-408] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-444] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-333] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-416] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [233-345] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-416] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-309] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-342] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [233-264] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [269-270] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-328] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-342] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-413] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-345] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-401] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-506] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-521] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-536] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-375] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-397] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-422] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-418] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-440] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-432] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-517] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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