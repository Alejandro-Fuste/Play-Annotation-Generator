# Play-Annotation-Generator Annotation Review — Counter_349

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_349`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 127
- **Validation Warnings:** 120
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 102
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `13` | `12` |
| ✅ EXACT | `Action_PullLeadBlock` | CB3 | defense | `4` | `3` |
| ✅ EXACT | `Action_PlaySideFakeStep` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `12` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `17` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 205 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 199 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 200 | START | 200 | 216 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `18` | `17` | 203 | START | 203 | 226 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 203 | START | 203 | 249 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `22` | `21` | 203 | START | 217 | 283 |
| ✅ EXACT | `Action_PullBlock` | LG | `13` | `12` | 203 | START | 203 | 283 |
| ✅ EXACT | `Action_PullLeadBlock` | CB3 | `4` | `3` | 203 | START | 203 | 283 |
| ✅ EXACT | `Action_PlaySideFakeStep` | QB | `20` | `19` | 206 | START | 206 | 224 |
| ✅ EXACT | `Action_SnapReceive` | RB | `6` | `5` | 216 | END | 200 | 216 |
| ✅ EXACT | `Action_Handoff` | RB | `6` | `5` | 223 | START | 223 | 224 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `20` | `19` | 225 | START | 225 | 230 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 283 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 206 | 224 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 225 | 230 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 233 | 325 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–431
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_SnapReceive` | 200 | 216 | 17 | inferred_complete_timeline |
| `Action_None` | 217 | 222 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 225 | 276 | 52 | inferred_complete_timeline |
| `Action_None` | 280 | 347 | 68 | inferred_complete_timeline |
| `Action_None` | 349 | 350 | 2 | inferred_complete_timeline |
| `Action_None` | 352 | 361 | 10 | inferred_complete_timeline |
| `Action_None` | 364 | 403 | 40 | inferred_complete_timeline |
| `Action_None` | 407 | 421 | 15 | inferred_complete_timeline |
| `Action_None` | 426 | 431 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 479 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 479 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 479 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 393 | 194 | inferred_complete_timeline |
| `Action_None` | 434 | 446 | 13 | inferred_complete_timeline |
| `Action_None` | 461 | 479 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–478
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |
| `Action_PullBlock` | 203 | 283 | 81 | inferred_complete_timeline |
| `Action_None` | 284 | 413 | 130 | inferred_complete_timeline |
| `Action_None` | 416 | 435 | 20 | inferred_complete_timeline |
| `Action_None` | 439 | 449 | 11 | inferred_complete_timeline |
| `Action_None` | 452 | 456 | 5 | inferred_complete_timeline |
| `Action_None` | 461 | 463 | 3 | inferred_complete_timeline |
| `Action_None` | 467 | 468 | 2 | inferred_complete_timeline |
| `Action_None` | 470 | 475 | 6 | inferred_complete_timeline |
| `Action_None` | 477 | 478 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–435
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_BallSnap` | 200 | 216 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 217 | 283 | 67 | inferred_complete_timeline |
| `Action_None` | 284 | 435 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–440
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |
| `Action_DownBlock` | 203 | 249 | 47 | inferred_complete_timeline |
| `Action_DownBlock` | 252 | 256 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 277 | 283 | 7 | inferred_complete_timeline |
| `Action_None` | 284 | 289 | 6 | inferred_complete_timeline |
| `Action_None` | 291 | 440 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–474
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |
| `Action_DownBlock` | 203 | 226 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 236 | 283 | 48 | inferred_complete_timeline |
| `Action_None` | 284 | 469 | 186 | inferred_complete_timeline |
| `Action_None` | 472 | 474 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 281 | 82 | inferred_complete_timeline |
| `Action_None` | 285 | 309 | 25 | inferred_complete_timeline |
| `Action_None` | 311 | 403 | 93 | inferred_complete_timeline |
| `Action_None` | 413 | 416 | 4 | inferred_complete_timeline |
| `Action_None` | 423 | 424 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 267 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 479 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–282
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 241 | 42 | inferred_complete_timeline |
| `Action_None` | 243 | 282 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–461
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 432 | 233 | inferred_complete_timeline |
| `Action_None` | 434 | 436 | 3 | inferred_complete_timeline |
| `Action_None` | 438 | 443 | 6 | inferred_complete_timeline |
| `Action_None` | 445 | 451 | 7 | inferred_complete_timeline |
| `Action_None` | 458 | 461 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 309 | 110 | inferred_complete_timeline |
| `Action_None` | 314 | 479 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–356
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 356 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 445 | 246 | inferred_complete_timeline |
| `Action_None` | 447 | 479 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–416
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 203 | 283 | 81 | inferred_complete_timeline |
| `Action_None` | 284 | 416 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–323
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 291 | 92 | inferred_complete_timeline |
| `Action_None` | 299 | 323 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 387 | 188 | inferred_complete_timeline |
| `Action_None` | 401 | 402 | 2 | inferred_complete_timeline |
| `Action_None` | 404 | 479 | 76 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–291 | 292 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–5 | 6 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 263–321 | 7 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 279–479 | 196 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 293–479 | 172 | 6 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 314–330 | 14 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 332–385 | 44 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 333–479 | 129 | 4 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 344–348 | 5 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 345–348 | 4 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 356–359 | 4 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 408–465 | 17 | 4 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 414–479 | 54 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 431–439 | 5 | 2 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 436–479 | 42 | 2 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 455–479 | 25 | 1 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 474–479 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (4 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `22` (C): Annotated start 203 != Inferred start 217
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 700: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [200–216], lower_priority='Action_DownBlock' annotated_start=203, effective_Action_DownBlock_start=217.
- ⚠️ Action 'Action_None' range [200-291] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-432] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-436] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-443] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-451] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-461] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-416] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-393] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-446] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-479] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-276] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-347] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-361] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-403] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-421] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-431] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-309] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-479] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-267] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-445] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-281] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-309] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-403] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-416] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-413] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-435] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-449] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-456] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-463] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-468] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-475] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-387] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-241] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-282] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-291] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-323] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [203-226] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [229-230] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-469] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-474] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-356] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [225-230] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [233-325] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [203-249] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [252-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-289] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-440] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-435] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-287] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-400] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-468] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-312] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-387] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-402] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-469] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-323] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-336] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-368] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-385] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-341] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-357] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-426] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-348] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-415] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-421] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-465] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-427] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-439] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-450] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-479] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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