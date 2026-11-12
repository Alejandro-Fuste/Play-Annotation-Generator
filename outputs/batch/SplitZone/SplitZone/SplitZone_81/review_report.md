# Play-Annotation-Generator Annotation Review — SplitZone_81

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_81`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 449
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 130
- **Validation Warnings:** 132
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 110
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_SplitBlock` | WR3 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `25` | `22` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `25` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `20` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 8 | START | 9 | 207 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 8 | START | 9 | 207 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 8 | START | 9 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 8 | START | 9 | 207 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 8 | START | 9 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 8 | START | 9 | 213 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 8 | START | 9 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 8 | START | 9 | 207 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 8 | START | 9 | 210 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 208 | START | 208 | 222 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `11` | 211 | START | 211 | 266 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `18` | `18` | 211 | START | 242 | 309 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `20` | 211 | START | 211 | 269 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `6` | 211 | START | 211 | 309 |
| ✅ EXACT | `Action_SplitBlock` | WR3 | `2` | `2` | 214 | START | 214 | 309 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `25` | `22` | 223 | END | 208 | 223 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `25` | `22` | 227 | START | 227 | 234 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `19` | `19` | 235 | START | 235 | 237 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `20` | `20` | 270 | START | 270 | 290 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 309 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 9–449
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 186 | 178 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 234 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 235 | 237 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 240 | 449 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 9–449
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 207 | 199 | inferred_complete_timeline |
| `Action_None` | 208 | 311 | 104 | inferred_complete_timeline |
| `Action_None` | 333 | 398 | 66 | inferred_complete_timeline |
| `Action_None` | 400 | 449 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 9–326
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 207 | 199 | inferred_complete_timeline |
| `Action_None` | 208 | 321 | 114 | inferred_complete_timeline |
| `Action_None` | 323 | 326 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 9–449
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 213 | 205 | inferred_complete_timeline |
| `Action_SplitBlock` | 214 | 309 | 96 | inferred_complete_timeline |
| `Action_None` | 310 | 428 | 119 | inferred_complete_timeline |
| `Action_None` | 430 | 431 | 2 | inferred_complete_timeline |
| `Action_None` | 434 | 449 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 9–348
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 207 | 199 | inferred_complete_timeline |
| `Action_None` | 208 | 279 | 72 | inferred_complete_timeline |
| `Action_None` | 286 | 348 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 9–425
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 210 | 202 | inferred_complete_timeline |
| `Action_ZoneBlock` | 211 | 309 | 99 | inferred_complete_timeline |
| `Action_None` | 310 | 362 | 53 | inferred_complete_timeline |
| `Action_None` | 364 | 371 | 8 | inferred_complete_timeline |
| `Action_None` | 375 | 378 | 4 | inferred_complete_timeline |
| `Action_None` | 392 | 425 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 9–296
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 210 | 202 | inferred_complete_timeline |
| `Action_ZoneBlock` | 211 | 269 | 59 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 270 | 290 | 21 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 293 | 296 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 9–449
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 207 | 199 | inferred_complete_timeline |
| `Action_BallSnap` | 208 | 222 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 242 | 309 | 68 | inferred_complete_timeline |
| `Action_None` | 310 | 370 | 61 | inferred_complete_timeline |
| `Action_None` | 375 | 376 | 2 | inferred_complete_timeline |
| `Action_None` | 379 | 449 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 9–410
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 210 | 202 | inferred_complete_timeline |
| `Action_ZoneBlock` | 211 | 266 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 268 | 309 | 42 | inferred_complete_timeline |
| `Action_None` | 310 | 374 | 65 | inferred_complete_timeline |
| `Action_None` | 379 | 384 | 6 | inferred_complete_timeline |
| `Action_None` | 386 | 387 | 2 | inferred_complete_timeline |
| `Action_None` | 392 | 410 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 9–449
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 207 | 199 | inferred_complete_timeline |
| `Action_None` | 208 | 289 | 82 | inferred_complete_timeline |
| `Action_None` | 298 | 449 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 9–241
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 207 | 199 | inferred_complete_timeline |
| `Action_None` | 208 | 241 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 9–235
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 207 | 199 | inferred_complete_timeline |
| `Action_None` | 208 | 230 | 23 | inferred_complete_timeline |
| `Action_None` | 232 | 235 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 9–293
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 207 | 199 | inferred_complete_timeline |
| `Action_None` | 208 | 293 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 9–311
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 207 | 199 | inferred_complete_timeline |
| `Action_None` | 208 | 311 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 9–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 207 | 199 | inferred_complete_timeline |
| `Action_None` | 208 | 449 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 9–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 207 | 199 | inferred_complete_timeline |
| `Action_None` | 208 | 449 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 207 | 199 | inferred_complete_timeline |
| `Action_None` | 208 | 449 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 9–449
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 207 | 199 | inferred_complete_timeline |
| `Action_None` | 208 | 342 | 135 | inferred_complete_timeline |
| `Action_None` | 355 | 373 | 19 | inferred_complete_timeline |
| `Action_None` | 376 | 377 | 2 | inferred_complete_timeline |
| `Action_None` | 380 | 382 | 3 | inferred_complete_timeline |
| `Action_None` | 386 | 387 | 2 | inferred_complete_timeline |
| `Action_None` | 389 | 390 | 2 | inferred_complete_timeline |
| `Action_None` | 394 | 400 | 7 | inferred_complete_timeline |
| `Action_None` | 404 | 449 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 9–397
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 207 | 199 | inferred_complete_timeline |
| `Action_None` | 208 | 312 | 105 | inferred_complete_timeline |
| `Action_None` | 315 | 350 | 36 | inferred_complete_timeline |
| `Action_None` | 355 | 356 | 2 | inferred_complete_timeline |
| `Action_None` | 359 | 362 | 4 | inferred_complete_timeline |
| `Action_None` | 364 | 370 | 7 | inferred_complete_timeline |
| `Action_None` | 372 | 373 | 2 | inferred_complete_timeline |
| `Action_None` | 375 | 378 | 4 | inferred_complete_timeline |
| `Action_None` | 393 | 397 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 9–448
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 207 | 199 | inferred_complete_timeline |
| `Action_None` | 208 | 436 | 229 | inferred_complete_timeline |
| `Action_None` | 447 | 448 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 9–449 | 372 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 9–55 | 9 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 85–391 | 307 | 5 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 244–331 | 88 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 258–449 | 185 | 3 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 270–449 | 156 | 8 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 290–407 | 91 | 8 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 292–316 | 25 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 319–320 | 2 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 325–371 | 43 | 3 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 355–449 | 80 | 7 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 381–389 | 7 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 394–408 | 15 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 426–436 | 11 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 426–441 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `18` (C): Annotated start 211 != Inferred start 242
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 96 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 164: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (LT) duration 99 frames exceeds threshold 90 frames [start=211, end=309].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (RG) duration 99 frames exceeds threshold 90 frames [start=211, end=309].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 99 frames exceeds threshold 90 frames [start=211, end=309].
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [208–223], lower_priority='Action_ZoneBlock' annotated_start=211, effective_Action_ZoneBlock_start=224.
- ⚠️ Action 'Action_None' range [208-311] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-398] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-449] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-321] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-428] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-449] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-279] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-348] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-311] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-362] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-371] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-425] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-289] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-293] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-449] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [211-266] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [268-309] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-374] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-384] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-410] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-312] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-350] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-362] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-370] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-397] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-241] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-342] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-373] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-382] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-400] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-436] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-230] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-255] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-349] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-449] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [208-222] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-370] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-449] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-186] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [235-237] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [240-449] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [270-290] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [293-296] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-14] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-55] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-207] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-391] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-331] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-370] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-449] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-370] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-410] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-421] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-434] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-440] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-445] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-331] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-350] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-370] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-407] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-316] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-331] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-344] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-371] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-410] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-418] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-425] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-431] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-434] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-389] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-408] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-436] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-441] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>