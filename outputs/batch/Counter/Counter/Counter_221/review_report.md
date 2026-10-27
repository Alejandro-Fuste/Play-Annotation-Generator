# Play-Annotation-Generator Annotation Review — Counter_221

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_221`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 539
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 150
- **Validation Warnings:** 152
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 126
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_PullBlock` | DT2 | defense | `12` | `11` |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 212 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 213 | START | 213 | 227 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `20` | `19` | 215 | START | 215 | 258 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 215 | START | 215 | 262 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `7` | `6` | 215 | START | 228 | 248 |
| ✅ EXACT | `Action_PullBlock` | DT2 | `12` | `11` | 215 | START | 215 | 298 |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | `10` | `9` | 215 | START | 215 | 298 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 227 | END | 213 | 227 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `13` | `12` | 294 | START | 294 | 355 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 298 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_SnapReceive` | 213 | 227 | 15 | inferred_complete_timeline |
| `Action_None` | 228 | 293 | 66 | inferred_complete_timeline |
| `Action_BallCarry` | 294 | 355 | 62 | inferred_complete_timeline |
| `Action_BallCarry` | 362 | 539 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 539 | 327 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 539 | 327 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 539 | 327 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 539 | 327 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 215 | 298 | 84 | inferred_complete_timeline |
| `Action_None` | 299 | 517 | 219 | inferred_complete_timeline |
| `Action_None` | 522 | 529 | 8 | inferred_complete_timeline |
| `Action_None` | 533 | 537 | 5 | inferred_complete_timeline |
| `Action_None` | 539 | 539 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_DownBlock` | 215 | 258 | 44 | inferred_complete_timeline |
| `Action_DownBlock` | 264 | 266 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 427 | 215 | inferred_complete_timeline |
| `Action_None` | 433 | 539 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 517

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_BallSnap` | 213 | 227 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 228 | 248 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 255 | 298 | 44 | inferred_complete_timeline |
| `Action_None` | 299 | 417 | 119 | inferred_complete_timeline |
| `Action_None` | 419 | 501 | 83 | inferred_complete_timeline |
| `Action_None` | 518 | 539 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–414
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_DownBlock` | 215 | 262 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 268 | 272 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 275 | 298 | 24 | inferred_complete_timeline |
| `Action_None` | 299 | 338 | 40 | inferred_complete_timeline |
| `Action_None` | 344 | 414 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 238 | 26 | inferred_complete_timeline |
| `Action_None` | 240 | 539 | 300 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 539 | 327 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 256 | 44 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 527

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 367 | 155 | inferred_complete_timeline |
| `Action_None` | 369 | 382 | 14 | inferred_complete_timeline |
| `Action_None` | 386 | 388 | 3 | inferred_complete_timeline |
| `Action_None` | 390 | 392 | 3 | inferred_complete_timeline |
| `Action_None` | 399 | 408 | 10 | inferred_complete_timeline |
| `Action_None` | 410 | 508 | 99 | inferred_complete_timeline |
| `Action_None` | 510 | 539 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_PullBlock` | 215 | 298 | 84 | inferred_complete_timeline |
| `Action_None` | 299 | 355 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–362
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 362 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 322 | 110 | inferred_complete_timeline |
| `Action_None` | 327 | 393 | 67 | inferred_complete_timeline |
| `Action_None` | 396 | 539 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 539 | 327 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 539 | 327 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–530
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 530 | 318 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 539 | 327 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 539 | 327 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 241–263 | 9 | 3 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 265–539 | 262 | 5 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 285–286 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 290–539 | 250 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 320–322 | 3 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 326–338 | 13 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 334–336 | 3 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 349–522 | 105 | 14 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 353–354 | 2 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 363–538 | 168 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 363–439 | 38 | 8 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 389–539 | 150 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 406–408 | 3 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 420–539 | 119 | 2 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 429–539 | 48 | 12 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 435–436 | 2 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 438–439 | 2 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 446–464 | 10 | 3 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 457–458 | 2 | 1 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 473–525 | 29 | 8 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 482–538 | 19 | 5 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 483–518 | 20 | 2 | Undefined position; Undefined team |
| `44` | `66` | Position_Unknown | Team_Unknown | 532–536 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 104 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [213–227], lower_priority='Action_DownBlock' annotated_start=215, effective_Action_DownBlock_start=228.
- ⚠️ Action 'Action_None' range [213-256] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-322] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-393] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-362] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [228-248] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-417] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-501] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-517] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-529] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-537] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-427] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-539] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [215-298] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-355] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [294-355] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-367] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-382] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-388] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-392] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-408] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-508] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-530] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [215-258] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [264-266] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [215-262] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [268-272] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-338] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-414] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-238] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-298] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-324] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-369] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-338] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-336] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-361] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-370] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-380] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-399] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-436] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-445] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-454] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-465] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-487] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-503] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-522] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-528] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-538] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-368] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-377] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-388] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-399] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-409] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-419] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-439] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-396] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-539] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-408] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-496] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-432] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-436] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-454] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-463] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-477] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-485] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-494] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-498] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-505] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-521] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-526] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-539] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-448] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-458] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-464] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-458] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-482] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-493] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-507] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-511] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-516] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-485] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-495] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-511] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-523] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-538] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-484] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-518] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-536] for track '44' has 2 frames without a visible bounding box.
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
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>