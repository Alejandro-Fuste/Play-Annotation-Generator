# Play-Annotation-Generator Annotation Review — BootPass_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_19`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 569
- **Player Tracks:** 34
- **Ball Tracks:** 7
- **Action Segments:** 105
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 9
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `15` | `15` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_RunFlatRoute` | TE | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 335 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 243 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 243 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 251 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 251 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 251 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 243 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 243 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 243 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 257 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 244 | START | 244 | 258 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `11` | `11` | 252 | START | 259 | 261 |
| ✅ EXACT | `Action_RunBlock` | RT | `15` | `15` | 252 | START | 252 | 443 |
| ✅ EXACT | `Action_RunBlock` | LG | `16` | `16` | 252 | START | 252 | 419 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `19` | `19` | 252 | START | 252 | 331 |
| ✅ EXACT | `Action_RunFlatRoute` | TE | `8` | `8` | 258 | START | 258 | 342 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 258 | END | 244 | 258 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `13` | `13` | 270 | START | 270 | 282 |
| ✅ EXACT | `Action_BootAway` | QB | `13` | `13` | 288 | START | 288 | 319 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `1` | `1` | 336 | START | 336 | 343 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 336 | START | 336 | 345 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–370
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_SnapReceive` | 244 | 258 | 15 | inferred_complete_timeline |
| `Action_None` | 259 | 269 | 11 | inferred_complete_timeline |
| `Action_FakeHandoff` | 270 | 282 | 13 | inferred_complete_timeline |
| `Action_None` | 283 | 287 | 5 | inferred_complete_timeline |
| `Action_BootAway` | 288 | 319 | 32 | inferred_complete_timeline |
| `Action_None` | 320 | 335 | 16 | inferred_complete_timeline |
| `Action_ThrowPass` | 336 | 345 | 10 | inferred_complete_timeline |
| `Action_None` | 346 | 370 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_None` | 244 | 336 | 93 | inferred_complete_timeline |
| `Action_None` | 342 | 569 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_None` | 244 | 474 | 231 | inferred_complete_timeline |
| `Action_None` | 476 | 479 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 335 | 336 | inferred_complete_timeline |
| `Action_SecureCatch` | 336 | 343 | 8 | inferred_complete_timeline |
| `Action_None` | 344 | 400 | 57 | inferred_complete_timeline |
| `Action_None` | 402 | 569 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–543
- **Visible Samples:** 523

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_None` | 244 | 508 | 265 | inferred_complete_timeline |
| `Action_None` | 518 | 519 | 2 | inferred_complete_timeline |
| `Action_None` | 522 | 523 | 2 | inferred_complete_timeline |
| `Action_None` | 534 | 543 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 257 | 258 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 258 | 342 | 85 | inferred_complete_timeline |
| `Action_None` | 343 | 515 | 173 | inferred_complete_timeline |
| `Action_None` | 517 | 569 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–381
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 251 | 252 | inferred_complete_timeline |
| `Action_RunBlock` | 252 | 331 | 80 | inferred_complete_timeline |
| `Action_RunBlock` | 333 | 381 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 251 | 252 | inferred_complete_timeline |
| `Action_RunBlock` | 252 | 419 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_BallSnap` | 244 | 258 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 259 | 261 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 263 | 272 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–443
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 251 | 252 | inferred_complete_timeline |
| `Action_RunBlock` | 252 | 443 | 192 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–441
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_None` | 244 | 252 | 9 | inferred_complete_timeline |
| `Action_None` | 255 | 277 | 23 | inferred_complete_timeline |
| `Action_None` | 280 | 289 | 10 | inferred_complete_timeline |
| `Action_None` | 292 | 441 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_None` | 244 | 374 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–357
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_None` | 244 | 317 | 74 | inferred_complete_timeline |
| `Action_None` | 319 | 357 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–486
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_None` | 244 | 439 | 196 | inferred_complete_timeline |
| `Action_None` | 441 | 442 | 2 | inferred_complete_timeline |
| `Action_None` | 447 | 464 | 18 | inferred_complete_timeline |
| `Action_None` | 467 | 475 | 9 | inferred_complete_timeline |
| `Action_None` | 477 | 486 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_None` | 244 | 569 | 326 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_None` | 244 | 522 | 279 | inferred_complete_timeline |
| `Action_None` | 561 | 569 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_None` | 244 | 419 | 176 | inferred_complete_timeline |
| `Action_None` | 421 | 537 | 117 | inferred_complete_timeline |
| `Action_None` | 539 | 540 | 2 | inferred_complete_timeline |
| `Action_None` | 548 | 569 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 546

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_None` | 244 | 506 | 263 | inferred_complete_timeline |
| `Action_None` | 508 | 514 | 7 | inferred_complete_timeline |
| `Action_None` | 524 | 529 | 6 | inferred_complete_timeline |
| `Action_None` | 538 | 542 | 5 | inferred_complete_timeline |
| `Action_None` | 549 | 569 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 557

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_None` | 244 | 490 | 247 | inferred_complete_timeline |
| `Action_None` | 492 | 513 | 22 | inferred_complete_timeline |
| `Action_None` | 525 | 545 | 21 | inferred_complete_timeline |
| `Action_None` | 547 | 569 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–464
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_None` | 244 | 461 | 218 | inferred_complete_timeline |
| `Action_None` | 463 | 464 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–292 | 289 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–569 | 570 | 2 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 298–444 | 147 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 299–333 | 35 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 299–300 | 2 | 1 | Undefined position; Undefined team |
| `31` | `52` | Position_Unknown | Team_Unknown | 319–323 | 5 | 1 | Undefined position; Undefined team |
| `32` | `54` | Position_Unknown | Team_Unknown | 337–371 | 35 | 1 | Undefined position; Undefined team |
| `34` | `59` | Position_Unknown | Team_Unknown | 362–363 | 2 | 1 | Undefined position; Undefined team |
| `35` | `60` | Position_Unknown | Team_Unknown | 367–415 | 44 | 4 | Undefined position; Undefined team |
| `36` | `61` | Position_Unknown | Team_Unknown | 372–465 | 94 | 1 | Undefined position; Undefined team |
| `37` | `66` | Position_Unknown | Team_Unknown | 450–482 | 12 | 3 | Undefined position; Undefined team |
| `38` | `68` | Position_Unknown | Team_Unknown | 510–569 | 45 | 5 | Undefined position; Undefined team |
| `39` | `69` | Position_Unknown | Team_Unknown | 557–569 | 13 | 1 | Undefined position; Undefined team |
| `40` | `71` | Position_Unknown | Team_Unknown | 566–569 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | 276 | 278 | 3 | 100.0% | None |
| `23` | `28` | 284 | 284 | 1 | 100.0% | None |
| `24` | `33` | 294 | 294 | 1 | 100.0% | None |
| `28` | `40` | 299 | 299 | 1 | 100.0% | None |
| `29` | `42` | 301 | 301 | 1 | 100.0% | None |
| `30` | `48` | 310 | 310 | 1 | 100.0% | None |
| `33` | `58` | 350 | 355 | 5 | 83.3% | 351 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 40: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ Row 40: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [244–258], lower_priority='Action_RunBlock' annotated_start=252, effective_Action_RunBlock_start=259.
- ⚠️ Action 'Action_None' range [244-506] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-514] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-529] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-542] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-400] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-461] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-474] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-479] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-508] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-519] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-523] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-543] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-374] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-439] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-464] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-475] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-486] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-336] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-515] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-317] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-357] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [259-261] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [263-272] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-419] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-537] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-569] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-370] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-282] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-292] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [252-443] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [252-419] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-252] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-277] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-289] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-441] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-490] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-513] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-545] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [252-331] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [333-381] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-522] for track '20' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-444] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-333] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-323] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-371] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-398] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-407] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-415] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-465] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-453] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-482] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-513] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-520] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-530] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-546] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-569] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-569] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-569] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
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