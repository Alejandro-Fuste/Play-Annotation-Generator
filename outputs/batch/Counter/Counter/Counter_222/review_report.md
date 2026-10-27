# Play-Annotation-Generator Annotation Review — Counter_222

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_222`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 569
- **Player Tracks:** 58
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 179
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | Team_Unknown | `19` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `2` | `1` |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `17` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 258 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 258 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 258 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 262 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 258 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 262 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 258 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 259 | START | 259 | 276 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 263 | START | 277 | 308 |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | `19` | `17` | 263 | START | 270 | 271 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `2` | `1` | 263 | START | 263 | 305 |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | `8` | `7` | 263 | START | 263 | 326 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 276 | END | 259 | 276 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 326 | BOUNDARY | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `17` | `16` | 341 | START | 341 | 415 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 566

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |
| `Action_SnapReceive` | 259 | 276 | 18 | inferred_complete_timeline |
| `Action_None` | 277 | 340 | 64 | inferred_complete_timeline |
| `Action_BallCarry` | 341 | 415 | 75 | inferred_complete_timeline |
| `Action_BallCarry` | 420 | 569 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–469
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 262 | 263 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 263 | 326 | 64 | inferred_complete_timeline |
| `Action_None` | 327 | 399 | 73 | inferred_complete_timeline |
| `Action_None` | 402 | 469 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–494
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |
| `Action_None` | 259 | 312 | 54 | inferred_complete_timeline |
| `Action_None` | 376 | 494 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–420
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 262 | 263 | inferred_complete_timeline |
| `Action_PullBlock` | 263 | 305 | 43 | inferred_complete_timeline |
| `Action_PullBlock` | 308 | 326 | 19 | inferred_complete_timeline |
| `Action_None` | 327 | 408 | 82 | inferred_complete_timeline |
| `Action_None` | 415 | 420 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–337
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |
| `Action_BallSnap` | 259 | 276 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 277 | 308 | 32 | inferred_complete_timeline |
| `Action_DownBlock` | 310 | 326 | 17 | inferred_complete_timeline |
| `Action_None` | 327 | 337 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |
| `Action_None` | 259 | 324 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–343
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |
| `Action_None` | 259 | 320 | 62 | inferred_complete_timeline |
| `Action_None` | 324 | 343 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–346
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |
| `Action_None` | 259 | 323 | 65 | inferred_complete_timeline |
| `Action_None` | 328 | 346 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |
| `Action_None` | 259 | 308 | 50 | inferred_complete_timeline |
| `Action_None` | 310 | 324 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–340
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |
| `Action_None` | 259 | 284 | 26 | inferred_complete_timeline |
| `Action_None` | 286 | 304 | 19 | inferred_complete_timeline |
| `Action_None` | 324 | 326 | 3 | inferred_complete_timeline |
| `Action_None` | 334 | 340 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–453
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |
| `Action_None` | 259 | 453 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–457
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |
| `Action_None` | 259 | 397 | 139 | inferred_complete_timeline |
| `Action_None` | 430 | 433 | 4 | inferred_complete_timeline |
| `Action_None` | 435 | 440 | 6 | inferred_complete_timeline |
| `Action_None` | 444 | 457 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–327
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |
| `Action_None` | 259 | 327 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–331
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |
| `Action_None` | 259 | 331 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–324 | 325 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–335 | 336 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–329 | 330 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 270–271 | 2 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 309–328 | 15 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 309–337 | 29 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 309–312 | 4 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 313–457 | 145 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 316–425 | 110 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 318–345 | 26 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 325–407 | 83 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 327–379 | 53 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 328–569 | 242 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 329–569 | 241 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 366–496 | 110 | 4 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 367–569 | 201 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 367–479 | 113 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 368–505 | 138 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 371–486 | 110 | 4 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 372–569 | 198 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 374–443 | 61 | 2 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 377–569 | 167 | 2 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 381–532 | 152 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 385–529 | 145 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 408–541 | 131 | 2 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 438–524 | 87 | 1 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 438–442 | 5 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 445–468 | 23 | 2 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 456–512 | 57 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 466–569 | 104 | 1 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 467–494 | 28 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 478–479 | 2 | 1 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 533–564 | 22 | 2 | Undefined position; Undefined team |
| `47` | `65` | Position_Unknown | Team_Unknown | 537–564 | 19 | 2 | Undefined position; Undefined team |
| `48` | `66` | Position_Unknown | Team_Unknown | 538–539 | 2 | 1 | Undefined position; Undefined team |
| `49` | `67` | Position_Unknown | Team_Unknown | 538–539 | 2 | 1 | Undefined position; Undefined team |
| `50` | `69` | Position_Unknown | Team_Unknown | 542–569 | 28 | 1 | Undefined position; Undefined team |
| `51` | `70` | Position_Unknown | Team_Unknown | 542–545 | 4 | 1 | Undefined position; Undefined team |
| `52` | `71` | Position_Unknown | Team_Unknown | 548–564 | 17 | 1 | Undefined position; Undefined team |
| `53` | `72` | Position_Unknown | Team_Unknown | 553–569 | 17 | 1 | Undefined position; Undefined team |
| `54` | `73` | Position_Unknown | Team_Unknown | 554–564 | 9 | 2 | Undefined position; Undefined team |
| `55` | `74` | Position_Unknown | Team_Unknown | 555–557 | 3 | 1 | Undefined position; Undefined team |
| `56` | `77` | Position_Unknown | Team_Unknown | 559–562 | 4 | 1 | Undefined position; Undefined team |
| `57` | `79` | Position_Unknown | Team_Unknown | 563–569 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `19` (Position_Unknown): Annotated start 263 != Inferred start 270
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 44 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 44 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 88 |
| Missing visible bounding boxes during action | 86 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 446: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 446: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 446: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [259–276], lower_priority='Action_DownBlock' annotated_start=263, effective_Action_DownBlock_start=277.
- ⚠️ Action 'Action_None' range [259-312] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-494] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [263-305] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-408] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-420] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-324] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-324] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-323] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-346] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-331] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-453] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [263-326] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '7' starts at frame 327, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [327-399] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-469] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-320] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-343] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-327] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-397] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-433] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-440] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-457] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [277-308] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-337] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-308] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-324] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-284] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-304] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-340] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-335] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [341-415] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [270-271] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-312] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-328] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-337] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-312] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-457] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-425] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-324] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-345] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-407] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-379] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-569] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-569] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-399] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-476] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-496] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-399] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-479] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-505] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-397] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-417] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-451] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-486] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-432] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-466] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-532] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-529] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-462] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-541] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-524] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-442] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-451] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-468] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-512] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-494] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-541] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-564] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-541] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-564] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-569] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-545] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-564] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-557] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-564] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-557] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-562] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-564] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-569] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.

</details>