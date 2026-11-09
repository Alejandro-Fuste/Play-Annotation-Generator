# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_106

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_106`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Tackle`
- **Result Frame:** 509
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 130
- **Validation Warnings:** 154
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 113
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 285 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 307 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 213 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 285 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 418 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 285 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 285 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 285 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 509 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 291 |
| ✅ EXACT | `Action_PressEdge` | RB | `16` | `16` | 214 | START | 214 | 337 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `13` | 286 | START | 286 | 291 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 286 | START | 286 | 291 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `20` | 286 | START | 286 | 291 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 286 | START | 286 | 291 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 286 | START | 286 | 295 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `14` | 308 | START | 308 | 322 |

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
- **Visible Frames:** 0–509
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 307 | 308 | inferred_complete_timeline |
| `Action_Handoff` | 308 | 322 | 15 | inferred_complete_timeline |
| `Action_None` | 323 | 334 | 12 | inferred_complete_timeline |
| `Action_None` | 336 | 509 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–357
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_PressEdge` | 214 | 337 | 124 | inferred_complete_timeline |
| `Action_None` | 338 | 357 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 418 | 419 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 509 | 510 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–295
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 285 | 286 | inferred_complete_timeline |
| `Action_ZoneBlock` | 286 | 295 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 285 | 286 | inferred_complete_timeline |
| `Action_ZoneBlock` | 286 | 291 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 285 | 286 | inferred_complete_timeline |
| `Action_ZoneBlock` | 286 | 291 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 295 | 296 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 301 | 304 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 326 | 336 | 11 | inferred_complete_timeline |
| `Action_None` | 339 | 343 | 5 | inferred_complete_timeline |
| `Action_None` | 384 | 386 | 3 | inferred_complete_timeline |
| `Action_None` | 390 | 397 | 8 | inferred_complete_timeline |
| `Action_None` | 402 | 404 | 3 | inferred_complete_timeline |
| `Action_None` | 406 | 444 | 39 | inferred_complete_timeline |
| `Action_None` | 447 | 497 | 51 | inferred_complete_timeline |
| `Action_None` | 500 | 509 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–394
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 285 | 286 | inferred_complete_timeline |
| `Action_ZoneBlock` | 286 | 291 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 324 | 334 | 11 | inferred_complete_timeline |
| `Action_None` | 342 | 343 | 2 | inferred_complete_timeline |
| `Action_None` | 360 | 363 | 4 | inferred_complete_timeline |
| `Action_None` | 365 | 369 | 5 | inferred_complete_timeline |
| `Action_None` | 372 | 376 | 5 | inferred_complete_timeline |
| `Action_None` | 381 | 384 | 4 | inferred_complete_timeline |
| `Action_None` | 390 | 394 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 285 | 286 | inferred_complete_timeline |
| `Action_ZoneBlock` | 286 | 291 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 315 | 316 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 348 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 363 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 433 | 509 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 317 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 321 | 323 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 334 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 365 | 451 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 453 | 509 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–363
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 353 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 363 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–497
- **Visible Samples:** 486

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 353 | 354 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 358 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 363 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 367 | 371 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 377 | 497 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 473

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 333 | 334 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 365 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 367 | 378 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 380 | 387 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 391 | 409 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 433 | 509 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 496

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 386 | 387 | inferred_complete_timeline |
| `Action_PreSnap` | 393 | 396 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 402 | 404 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 406 | 411 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 414 | 509 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 486

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 315 | 316 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 321 | 322 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 327 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 337 | 345 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 421 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 423 | 425 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 428 | 463 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 467 | 509 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 506

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 418 | 419 | inferred_complete_timeline |
| `Action_PreSnap` | 423 | 509 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 509 | 510 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 509 | 510 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–509 | 510 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 213–216 | 4 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 285–286 | 2 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 327–332 | 5 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 361–404 | 6 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 368–509 | 142 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 382–383 | 2 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 386–441 | 56 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 391–504 | 100 | 6 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 403–407 | 4 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 407–477 | 17 | 4 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 413–475 | 35 | 4 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 420–509 | 62 | 6 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 427–428 | 2 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 434–509 | 76 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 435–509 | 75 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 440–467 | 28 | 1 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 445–466 | 9 | 3 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 455–509 | 52 | 2 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 466–504 | 21 | 5 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 496–509 | 14 | 1 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 497–509 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 108 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 214: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-291] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-317] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-323] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-334] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-451] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-315] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-348] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-363] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-418] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-291] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-353] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-363] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [286-295] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-291] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-418] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-386] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-396] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-404] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-411] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-509] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-291] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-333] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-365] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-378] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-387] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-409] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-353] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-358] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-363] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-371] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-497] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [286-291] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-334] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-509] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-357] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-315] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-322] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-327] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-345] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-421] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-425] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-463] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-509] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [286-291] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [317-318] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [324-334] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-363] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-369] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-376] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-394] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-509] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [286-291] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [295-296] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [301-304] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [326-336] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-343] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-386] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-397] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-404] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-444] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-497] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-509] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [286-291] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-216] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-286] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-332] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-363] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-404] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-383] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-441] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-397] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-404] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-444] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-480] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [488-491] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [493-504] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-404] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-407] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-408] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-414] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-468] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [470-477] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-419] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-423] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-444] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [471-475] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-439] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-467] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [470-477] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [481-482] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [493-495] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-428] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-509] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-467] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [445-446] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [459-463] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [465-466] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [455-471] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-468] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-477] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [480-481] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [486-492] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [498-504] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [497-501] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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