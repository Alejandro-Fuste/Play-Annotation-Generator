# Play-Annotation-Generator Annotation Review — Power_319

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_319`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 509
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 509 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 263 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 509 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 218 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 218 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 281 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 392 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 354 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `16` | `16` | 219 | START | 219 | 229 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `17` | `17` | 219 | START | 219 | 233 |
| ✅ EXACT | `Action_PullBlock` | LG | `20` | `20` | 219 | START | 219 | 295 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–350
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 281 | 282 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 293 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 300 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 309 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 346 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 350 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 409 | 142 | inferred_complete_timeline |
| `Action_PreSnap` | 411 | 509 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 509 | 510 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–468
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 354 | 355 | inferred_complete_timeline |
| `Action_PreSnap` | 358 | 468 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 392 | 393 | inferred_complete_timeline |
| `Action_PreSnap` | 394 | 509 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–456
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 456 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–474
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 93 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 218 | 113 | inferred_complete_timeline |
| `Action_PullBlock` | 219 | 295 | 77 | inferred_complete_timeline |
| `Action_None` | 296 | 474 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 218 | 219 | inferred_complete_timeline |
| `Action_DownBlock` | 219 | 233 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 247 | 295 | 49 | inferred_complete_timeline |
| `Action_None` | 296 | 353 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–428
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 218 | 219 | inferred_complete_timeline |
| `Action_DownBlock` | 219 | 229 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 233 | 295 | 63 | inferred_complete_timeline |
| `Action_None` | 296 | 318 | 23 | inferred_complete_timeline |
| `Action_None` | 321 | 428 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 509 | 510 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 487

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 305 | 306 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 334 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 336 | 339 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 344 | 346 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 357 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 362 | 509 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 509 | 510 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 4–61
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 16 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 47 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 61 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 508

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 275 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 509 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–435
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 261 | 262 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 321 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 409 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 411 | 435 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–301
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 301 | 302 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 375 | 376 | inferred_complete_timeline |
| `Action_PreSnap` | 380 | 418 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 420 | 509 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 509 | 510 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 294 | 295 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 499

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 428 | 429 | inferred_complete_timeline |
| `Action_PreSnap` | 432 | 434 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 437 | 438 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 443 | 500 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 503 | 509 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 499

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 322 | 323 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 509 | 176 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–334 | 335 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 59–243 | 166 | 5 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 256–509 | 252 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 287–509 | 220 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 324–412 | 89 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 341–441 | 91 | 5 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 355–364 | 6 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 358–382 | 21 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 368–400 | 31 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 378–438 | 43 | 5 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 389–452 | 64 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 426–427 | 2 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 439–443 | 5 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 442–443 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 638: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-375] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-418] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-281] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-293] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-300] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-309] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-346] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-350] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-305] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-334] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-339] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-346] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-357] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-509] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-392] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-354] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-468] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-322] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-294] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-428] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-434] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-438] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-500] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [503-509] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-263] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-409] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-261] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-321] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-409] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-435] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-247] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-456] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-301] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [219-229] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [233-295] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-318] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-428] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [219-233] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-353] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-275] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-509] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-334] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-93] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-474] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-16] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-64] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-234] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-497] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-290] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-412] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-346] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-379] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-390] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-394] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-441] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-358] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-364] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-374] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-382] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-370] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-400] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-379] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-404] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-409] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-414] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-438] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-452] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-427] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-443] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-443] for track '34' has 1 frames without a visible bounding box.
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

</details>