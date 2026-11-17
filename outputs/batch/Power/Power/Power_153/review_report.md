# Play-Annotation-Generator Annotation Review — Power_153

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_153`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 129
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
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 24 | START | 29 | 425 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 24 | START | 29 | 207 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 24 | START | 29 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 24 | START | 29 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 24 | START | 29 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 24 | START | 29 | 207 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 24 | START | 29 | 207 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 24 | START | 29 | 412 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 24 | START | 29 | 412 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 24 | START | 29 | 449 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `13` | `13` | 208 | START | 208 | 212 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `21` | `21` | 208 | START | 208 | 232 |
| ✅ EXACT | `Action_PullBlock` | LT | `20` | `20` | 208 | START | 208 | 289 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 29–449
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 299 | 271 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 323 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 337 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 346 | 360 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 449 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 29–449
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 412 | 384 | inferred_complete_timeline |
| `Action_PreSnap` | 415 | 449 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 29–412
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 412 | 384 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 29–449
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 449 | 421 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 29–449
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 449 | 421 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 29–449
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 207 | 179 | inferred_complete_timeline |
| `Action_PullBlock` | 208 | 289 | 82 | inferred_complete_timeline |
| `Action_None` | 290 | 306 | 17 | inferred_complete_timeline |
| `Action_None` | 319 | 339 | 21 | inferred_complete_timeline |
| `Action_None` | 343 | 359 | 17 | inferred_complete_timeline |
| `Action_None` | 363 | 449 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 29–447
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 207 | 179 | inferred_complete_timeline |
| `Action_DownBlock` | 208 | 232 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 239 | 259 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 266 | 268 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 295 | 343 | 49 | inferred_complete_timeline |
| `Action_None` | 351 | 361 | 11 | inferred_complete_timeline |
| `Action_None` | 363 | 427 | 65 | inferred_complete_timeline |
| `Action_None` | 430 | 440 | 11 | inferred_complete_timeline |
| `Action_None` | 442 | 443 | 2 | inferred_complete_timeline |
| `Action_None` | 446 | 447 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 29–449
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 449 | 421 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 29–449
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 207 | 179 | inferred_complete_timeline |
| `Action_DownBlock` | 208 | 212 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 228 | 289 | 62 | inferred_complete_timeline |
| `Action_None` | 290 | 333 | 44 | inferred_complete_timeline |
| `Action_None` | 341 | 359 | 19 | inferred_complete_timeline |
| `Action_None` | 364 | 423 | 60 | inferred_complete_timeline |
| `Action_None` | 427 | 428 | 2 | inferred_complete_timeline |
| `Action_None` | 430 | 444 | 15 | inferred_complete_timeline |
| `Action_None` | 448 | 449 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 29–449
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 425 | 397 | inferred_complete_timeline |
| `Action_PreSnap` | 428 | 447 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 449 | 449 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 29–329
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 329 | 301 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 29–447
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 228 | 200 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 425 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 430 | 444 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 446 | 447 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 29–449
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 241 | 213 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 253 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 267 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 358 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 449 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 29–449
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 240 | 212 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 293 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 363 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 365 | 423 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 427 | 449 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 29–444
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 426 | 398 | inferred_complete_timeline |
| `Action_PreSnap` | 428 | 429 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 431 | 444 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 29–449
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 278 | 250 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 360 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 363 | 384 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 395 | 440 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 442 | 449 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 29–435
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 423 | 395 | inferred_complete_timeline |
| `Action_PreSnap` | 432 | 435 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 29–449
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 434 | 406 | inferred_complete_timeline |
| `Action_PreSnap` | 436 | 449 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 29–223
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 223 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 29–386
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 288 | 260 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 335 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 359 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 386 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 29–439
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 350 | 322 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 359 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 425 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 428 | 429 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 433 | 434 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 438 | 439 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 29–447 | 414 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 222–341 | 120 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 246–356 | 104 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 313–331 | 6 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 355–356 | 2 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 367–449 | 83 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 372–449 | 50 | 7 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 380–393 | 10 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 380–447 | 64 | 3 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 389–447 | 47 | 4 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 400–449 | 21 | 5 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 417–447 | 25 | 3 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 424–425 | 2 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 445–446 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 99 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 308: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [29-425] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-447] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-434] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-423] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-435] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-412] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-288] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-335] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-359] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-386] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-278] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-360] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-384] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-440] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-449] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-386] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-443] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-447] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-412] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-350] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-359] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-425] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-434] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-439] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-240] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-293] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-363] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-423] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-329] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [208-212] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-333] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-359] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-423] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-428] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-444] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-241] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-253] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-267] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-358] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-223] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-323] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-337] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-360] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-426] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-444] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-228] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-425] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-444] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-447] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-449] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 290, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [290-306] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-339] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-359] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [208-232] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [239-259] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [266-268] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [286-287] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-343] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-361] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-427] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-440] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-341] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-303] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-313] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-356] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-316] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-331] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-356] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-449] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-387] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-390] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-405] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-414] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-426] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-433] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-381] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-393] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-426] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-444] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-447] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-407] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-420] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-439] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-447] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-404] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-414] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-424] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-434] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-428] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-440] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-447] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-425] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [445-446] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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