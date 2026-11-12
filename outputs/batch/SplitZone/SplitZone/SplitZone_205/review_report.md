# Play-Annotation-Generator Annotation Review — SplitZone_205

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_205`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | offense | `19` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 14 | START | 15 | 272 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 14 | START | 15 | 272 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 14 | START | 15 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 14 | START | 15 | 297 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 14 | START | 15 | 272 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 14 | START | 15 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 14 | START | 15 | 272 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 14 | START | 15 | 272 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 14 | START | 15 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 14 | START | 15 | 278 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 14 | START | 15 | 275 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 273 | START | 273 | 284 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `12` | 276 | START | 276 | 296 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `19` | `19` | 276 | START | 276 | 306 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `20` | 276 | START | 285 | 287 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 276 | START | 276 | 353 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `7` | `7` | 276 | START | 276 | 297 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `6` | `6` | 279 | START | 279 | 339 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 284 | END | 273 | 284 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `17` | 286 | START | 286 | 297 |
| ✅ EXACT | `Action_BallCarry` | RB | `15` | `15` | 298 | START | 298 | 302 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | `19` | `19` | 307 | START | 307 | 350 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 353 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 15–449
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 272 | 258 | inferred_complete_timeline |
| `Action_SnapReceive` | 273 | 284 | 12 | inferred_complete_timeline |
| `Action_None` | 285 | 285 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 286 | 297 | 12 | inferred_complete_timeline |
| `Action_None` | 298 | 407 | 110 | inferred_complete_timeline |
| `Action_None` | 409 | 412 | 4 | inferred_complete_timeline |
| `Action_None` | 414 | 440 | 27 | inferred_complete_timeline |
| `Action_None` | 442 | 449 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 15–302
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 297 | 283 | inferred_complete_timeline |
| `Action_BallCarry` | 298 | 302 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 15–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 272 | 258 | inferred_complete_timeline |
| `Action_None` | 273 | 449 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 15–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 272 | 258 | inferred_complete_timeline |
| `Action_None` | 273 | 392 | 120 | inferred_complete_timeline |
| `Action_None` | 394 | 449 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 15–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 272 | 258 | inferred_complete_timeline |
| `Action_None` | 273 | 449 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 15–361
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 278 | 264 | inferred_complete_timeline |
| `Action_SplitBlock` | 279 | 339 | 61 | inferred_complete_timeline |
| `Action_SplitBlock` | 346 | 353 | 8 | inferred_complete_timeline |
| `Action_None` | 354 | 361 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 15–449
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 275 | 261 | inferred_complete_timeline |
| `Action_ZoneBlock` | 276 | 297 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 305 | 353 | 49 | inferred_complete_timeline |
| `Action_None` | 354 | 449 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 15–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 275 | 261 | inferred_complete_timeline |
| `Action_ZoneBlock` | 276 | 353 | 78 | inferred_complete_timeline |
| `Action_None` | 354 | 449 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 15–449
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 272 | 258 | inferred_complete_timeline |
| `Action_BallSnap` | 273 | 284 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 285 | 287 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 291 | 327 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 329 | 353 | 25 | inferred_complete_timeline |
| `Action_None` | 354 | 412 | 59 | inferred_complete_timeline |
| `Action_None` | 419 | 449 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 15–449
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 275 | 261 | inferred_complete_timeline |
| `Action_ZoneBlock` | 276 | 296 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 298 | 330 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 348 | 353 | 6 | inferred_complete_timeline |
| `Action_None` | 356 | 366 | 11 | inferred_complete_timeline |
| `Action_None` | 369 | 378 | 10 | inferred_complete_timeline |
| `Action_None` | 380 | 381 | 2 | inferred_complete_timeline |
| `Action_None` | 383 | 399 | 17 | inferred_complete_timeline |
| `Action_None` | 404 | 449 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 15–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 275 | 261 | inferred_complete_timeline |
| `Action_ZoneBlock` | 276 | 306 | 31 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 307 | 350 | 44 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 352 | 353 | 2 | inferred_complete_timeline |
| `Action_None` | 354 | 449 | 96 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 15–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 272 | 258 | inferred_complete_timeline |
| `Action_None` | 273 | 449 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 15–319
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 272 | 258 | inferred_complete_timeline |
| `Action_None` | 273 | 319 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 15–449
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 272 | 258 | inferred_complete_timeline |
| `Action_None` | 273 | 297 | 25 | inferred_complete_timeline |
| `Action_None` | 308 | 309 | 2 | inferred_complete_timeline |
| `Action_None` | 311 | 322 | 12 | inferred_complete_timeline |
| `Action_None` | 327 | 449 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 15–442
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 272 | 258 | inferred_complete_timeline |
| `Action_None` | 273 | 384 | 112 | inferred_complete_timeline |
| `Action_None` | 388 | 393 | 6 | inferred_complete_timeline |
| `Action_None` | 395 | 398 | 4 | inferred_complete_timeline |
| `Action_None` | 409 | 442 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 15–449
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 272 | 258 | inferred_complete_timeline |
| `Action_None` | 273 | 341 | 69 | inferred_complete_timeline |
| `Action_None` | 344 | 346 | 3 | inferred_complete_timeline |
| `Action_None` | 348 | 386 | 39 | inferred_complete_timeline |
| `Action_None` | 396 | 429 | 34 | inferred_complete_timeline |
| `Action_None` | 435 | 449 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 15–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 272 | 258 | inferred_complete_timeline |
| `Action_None` | 273 | 449 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 15–449
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 272 | 258 | inferred_complete_timeline |
| `Action_None` | 273 | 390 | 118 | inferred_complete_timeline |
| `Action_None` | 396 | 430 | 35 | inferred_complete_timeline |
| `Action_None` | 436 | 449 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 15–449
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 272 | 258 | inferred_complete_timeline |
| `Action_None` | 273 | 392 | 120 | inferred_complete_timeline |
| `Action_None` | 396 | 449 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 15–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 272 | 258 | inferred_complete_timeline |
| `Action_None` | 273 | 386 | 114 | inferred_complete_timeline |
| `Action_None` | 388 | 449 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 15–448
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 272 | 258 | inferred_complete_timeline |
| `Action_None` | 273 | 448 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 15–431
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 272 | 258 | inferred_complete_timeline |
| `Action_None` | 273 | 384 | 112 | inferred_complete_timeline |
| `Action_None` | 430 | 431 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 310–377 | 66 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 321–449 | 119 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 361–369 | 8 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 369–393 | 23 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 396–449 | 54 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 420–448 | 27 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 422–449 | 18 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 447–449 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [273–284], lower_priority='Action_ZoneBlock' annotated_start=276, effective_Action_ZoneBlock_start=285.
- ⚠️ Action 'Action_None' range [273-392] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-390] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-430] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [279-339] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-361] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [276-297] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-448] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-386] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-341] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-346] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-386] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-429] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-297] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-322] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [276-296] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [298-330] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [348-353] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-366] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-378] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-399] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-449] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-392] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-384] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [298-302] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-319] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-407] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-412] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-440] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-384] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-393] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-398] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-442] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [276-306] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [307-350] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-449] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [285-287] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [291-327] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-412] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-449] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-373] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-354] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-394] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-364] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-369] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-377] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-393] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-449] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-433] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-448] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-427] for track '28' has 1 frames without a visible bounding box.
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

</details>