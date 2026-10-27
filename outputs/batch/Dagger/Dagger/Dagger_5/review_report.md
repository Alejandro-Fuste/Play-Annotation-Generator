# Play-Annotation-Generator Annotation Review — Dagger_5

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_5`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Checkdown`
- **Result Frame:** 539
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 96
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_BreakInside` | WR2 | offense | `7` | `7` |
| ✅ EXACT | `Action_ClearToEdge` | WR1 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `13` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 231 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 231 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 217 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 215 | START | 215 | 232 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `12` | `12` | 218 | START | 233 | 282 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `18` | `18` | 218 | START | 218 | 306 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `5` | `5` | 218 | START | 218 | 308 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `9` | `9` | 218 | START | 218 | 323 |
| ✅ EXACT | `Action_BreakInside` | WR2 | `7` | `7` | 232 | START | 232 | 308 |
| ✅ EXACT | `Action_ClearToEdge` | WR1 | `2` | `2` | 232 | START | 232 | 308 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 232 | END | 215 | 232 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 300 | START | 300 | 308 |

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
- **Visible Frames:** 0–435
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_SnapReceive` | 215 | 232 | 18 | inferred_complete_timeline |
| `Action_None` | 233 | 299 | 67 | inferred_complete_timeline |
| `Action_ThrowPass` | 300 | 308 | 9 | inferred_complete_timeline |
| `Action_None` | 309 | 435 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–536
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 463 | 249 | inferred_complete_timeline |
| `Action_None` | 475 | 496 | 22 | inferred_complete_timeline |
| `Action_None` | 504 | 513 | 10 | inferred_complete_timeline |
| `Action_None` | 515 | 521 | 7 | inferred_complete_timeline |
| `Action_None` | 535 | 536 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–421
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_ClearToEdge` | 232 | 308 | 77 | inferred_complete_timeline |
| `Action_None` | 309 | 421 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–529
- **Visible Samples:** 529

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_BreakInside` | 232 | 308 | 77 | inferred_complete_timeline |
| `Action_None` | 309 | 501 | 193 | inferred_complete_timeline |
| `Action_None` | 503 | 529 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 539 | 325 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–483
- **Visible Samples:** 484

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 483 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–317
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 217 | 218 | inferred_complete_timeline |
| `Action_PassBlock` | 218 | 306 | 89 | inferred_complete_timeline |
| `Action_PassBlock` | 308 | 310 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 312 | 317 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–483
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_BallSnap` | 215 | 232 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 233 | 282 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 285 | 474 | 190 | inferred_complete_timeline |
| `Action_PassBlock` | 477 | 483 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–504
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 217 | 218 | inferred_complete_timeline |
| `Action_PassBlock` | 218 | 323 | 106 | inferred_complete_timeline |
| `Action_PassBlock` | 325 | 504 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–468
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 217 | 218 | inferred_complete_timeline |
| `Action_PassBlock` | 218 | 308 | 91 | inferred_complete_timeline |
| `Action_PassBlock` | 311 | 314 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 316 | 372 | 57 | inferred_complete_timeline |
| `Action_PassBlock` | 376 | 468 | 93 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–351
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 305 | 91 | inferred_complete_timeline |
| `Action_None` | 321 | 323 | 3 | inferred_complete_timeline |
| `Action_None` | 325 | 351 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 530

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 273 | 59 | inferred_complete_timeline |
| `Action_None` | 275 | 281 | 7 | inferred_complete_timeline |
| `Action_None` | 286 | 289 | 4 | inferred_complete_timeline |
| `Action_None` | 295 | 539 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–476
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 244 | 30 | inferred_complete_timeline |
| `Action_None` | 246 | 248 | 3 | inferred_complete_timeline |
| `Action_None` | 251 | 259 | 9 | inferred_complete_timeline |
| `Action_None` | 262 | 268 | 7 | inferred_complete_timeline |
| `Action_None` | 272 | 312 | 41 | inferred_complete_timeline |
| `Action_None` | 317 | 322 | 6 | inferred_complete_timeline |
| `Action_None` | 327 | 341 | 15 | inferred_complete_timeline |
| `Action_None` | 343 | 355 | 13 | inferred_complete_timeline |
| `Action_None` | 364 | 371 | 8 | inferred_complete_timeline |
| `Action_None` | 374 | 387 | 14 | inferred_complete_timeline |
| `Action_None` | 409 | 421 | 13 | inferred_complete_timeline |
| `Action_None` | 424 | 428 | 5 | inferred_complete_timeline |
| `Action_None` | 430 | 435 | 6 | inferred_complete_timeline |
| `Action_None` | 437 | 440 | 4 | inferred_complete_timeline |
| `Action_None` | 451 | 454 | 4 | inferred_complete_timeline |
| `Action_None` | 458 | 463 | 6 | inferred_complete_timeline |
| `Action_None` | 471 | 476 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 492 | 278 | inferred_complete_timeline |
| `Action_None` | 498 | 539 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 291 | 77 | inferred_complete_timeline |
| `Action_None` | 297 | 539 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 529

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 243 | 29 | inferred_complete_timeline |
| `Action_None` | 248 | 254 | 7 | inferred_complete_timeline |
| `Action_None` | 259 | 263 | 5 | inferred_complete_timeline |
| `Action_None` | 265 | 375 | 111 | inferred_complete_timeline |
| `Action_None` | 377 | 406 | 30 | inferred_complete_timeline |
| `Action_None` | 408 | 539 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 539 | 325 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–362
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 362 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 500

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 485 | 271 | inferred_complete_timeline |
| `Action_None` | 526 | 539 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 411 | 197 | inferred_complete_timeline |
| `Action_None` | 419 | 539 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–527
- **Visible Samples:** 523

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 366 | 152 | inferred_complete_timeline |
| `Action_None` | 369 | 412 | 44 | inferred_complete_timeline |
| `Action_None` | 414 | 510 | 97 | inferred_complete_timeline |
| `Action_None` | 513 | 527 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 2–255 | 250 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 300–322 | 23 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 319–526 | 208 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 353–539 | 172 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 383–539 | 144 | 5 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 419–495 | 62 | 3 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 457–496 | 40 | 1 | Undefined position; Undefined team |
| `29` | `47` | Position_Unknown | Team_Unknown | 527–539 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [215–232], lower_priority='Action_PassBlock' annotated_start=218, effective_Action_PassBlock_start=233.
- ⚠️ Action 'Action_None' range [215-273] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-281] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-289] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-362] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-421] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-244] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-259] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-312] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-322] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-341] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-355] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-371] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-387] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-421] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-428] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-435] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-440] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-454] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-463] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-476] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [218-308] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [311-314] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [316-372] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [376-468] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-485] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-539] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-501] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-529] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-366] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-412] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-510] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-527] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [218-323] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [325-504] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-492] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-539] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [233-282] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [285-474] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [477-483] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-483] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-463] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-496] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-513] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-521] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-305] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-351] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-291] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-539] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-411] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [218-306] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [308-310] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [312-317] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-435] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-243] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-254] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-375] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-406] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-235] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-255] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-322] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-526] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-391] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-503] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-518] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-524] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-532] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-539] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-473] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-479] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-496] for track '28' has 1 frames without a visible bounding box.
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

</details>