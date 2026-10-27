# Play-Annotation-Generator Annotation Review — Counter_117

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_117`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_PlaySideFakeStep` | WR1 | offense | `15` | `14` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `18` | `17` |
| ✅ EXACT | `Action_PullLeadBlock` | WR2 | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `4` | `3` |
| ✅ EXACT | `Action_Handoff` | DE2 | defense | `4` | `3` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `1` | `Group` | 0 | START | 0 | 263 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 265 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 263 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 263 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `15` | `Group` | 0 | START | 0 | 265 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `16` | `Group` | 0 | START | 0 | 263 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 265 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 263 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 265 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 263 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 265 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 264 | START | 264 | 277 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 266 | START | 278 | 329 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 266 | START | 266 | 283 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `9` | `8` | 266 | START | 266 | 309 |
| ✅ EXACT | `Action_PlaySideFakeStep` | WR1 | `15` | `14` | 266 | START | 266 | 309 |
| ✅ EXACT | `Action_PullBlock` | LG | `18` | `17` | 266 | START | 266 | 346 |
| ✅ EXACT | `Action_PullLeadBlock` | WR2 | `11` | `10` | 266 | START | 266 | 367 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `4` | `3` | 277 | END | 264 | 277 |
| ✅ EXACT | `Action_Handoff` | DE2 | `4` | `3` | 288 | START | 288 | 309 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `15` | `14` | 310 | START | 310 | 421 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 367 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–446
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_None` | 264 | 446 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–421
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 266 | 309 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 310 | 421 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–373
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 266 | 367 | 102 | inferred_complete_timeline |
| `Action_None` | 368 | 373 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_None` | 264 | 404 | 141 | inferred_complete_timeline |
| `Action_None` | 409 | 449 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_None` | 264 | 449 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–406
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_None` | 264 | 406 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_None` | 264 | 268 | 5 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |
| `Action_None` | 287 | 449 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–346
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_PullBlock` | 266 | 346 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_BallSnap` | 264 | 277 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 278 | 329 | 52 | inferred_complete_timeline |
| `Action_DownBlock` | 333 | 367 | 35 | inferred_complete_timeline |
| `Action_None` | 368 | 371 | 4 | inferred_complete_timeline |
| `Action_None` | 373 | 391 | 19 | inferred_complete_timeline |
| `Action_None` | 427 | 439 | 13 | inferred_complete_timeline |
| `Action_None` | 443 | 444 | 2 | inferred_complete_timeline |
| `Action_None` | 449 | 449 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–311
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_DownBlock` | 266 | 283 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 303 | 311 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_DownBlock` | 266 | 309 | 44 | inferred_complete_timeline |
| `Action_DownBlock` | 350 | 367 | 18 | inferred_complete_timeline |
| `Action_None` | 368 | 392 | 25 | inferred_complete_timeline |
| `Action_None` | 394 | 449 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–306
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_None` | 264 | 306 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_SnapReceive` | 264 | 277 | 14 | inferred_complete_timeline |
| `Action_None` | 278 | 287 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 288 | 309 | 22 | inferred_complete_timeline |
| `Action_None` | 310 | 314 | 5 | inferred_complete_timeline |
| `Action_None` | 324 | 325 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_None` | 264 | 289 | 26 | inferred_complete_timeline |
| `Action_None` | 291 | 306 | 16 | inferred_complete_timeline |
| `Action_None` | 314 | 317 | 4 | inferred_complete_timeline |
| `Action_None` | 321 | 333 | 13 | inferred_complete_timeline |
| `Action_None` | 344 | 370 | 27 | inferred_complete_timeline |
| `Action_None` | 372 | 373 | 2 | inferred_complete_timeline |
| `Action_None` | 375 | 382 | 8 | inferred_complete_timeline |
| `Action_None` | 384 | 395 | 12 | inferred_complete_timeline |
| `Action_None` | 418 | 419 | 2 | inferred_complete_timeline |
| `Action_None` | 421 | 449 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–344
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_None` | 264 | 304 | 41 | inferred_complete_timeline |
| `Action_None` | 311 | 340 | 30 | inferred_complete_timeline |
| `Action_None` | 343 | 344 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_None` | 264 | 342 | 79 | inferred_complete_timeline |
| `Action_None` | 355 | 369 | 15 | inferred_complete_timeline |
| `Action_None` | 373 | 449 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_None` | 264 | 354 | 91 | inferred_complete_timeline |
| `Action_None` | 358 | 359 | 2 | inferred_complete_timeline |
| `Action_None` | 362 | 371 | 10 | inferred_complete_timeline |
| `Action_None` | 373 | 449 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_None` | 264 | 449 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–341
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_None` | 264 | 341 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_None` | 264 | 401 | 138 | inferred_complete_timeline |
| `Action_None` | 406 | 407 | 2 | inferred_complete_timeline |
| `Action_None` | 409 | 449 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–428
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_None` | 264 | 420 | 157 | inferred_complete_timeline |
| `Action_None` | 422 | 428 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_None` | 264 | 449 | 186 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 159–161 | 3 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 329–437 | 104 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 334–449 | 111 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 353–449 | 51 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 359–409 | 36 | 6 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 368–447 | 27 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 374–449 | 76 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 420–449 | 27 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 438–449 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (RT) duration 102 frames exceeds threshold 90 frames [start=266, end=367].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '11' (C) duration 102 frames exceeds threshold 90 frames [start=266, end=367].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [264–277], lower_priority='Action_DownBlock' annotated_start=266, effective_Action_DownBlock_start=278.
- ⚠️ Action 'Action_None' range [264-406] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-342] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-369] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-449] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-314] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-289] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-306] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-333] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-370] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-382] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-395] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-449] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-420] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-428] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-304] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-340] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [266-309] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-392] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-354] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-371] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-373] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [278-329] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [333-367] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-371] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-391] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-439] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-444] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-401] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-446] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [310-421] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-404] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-449] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-306] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [266-346] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-341] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [266-283] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [303-311] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-161] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-346] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-437] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-351] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-364] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-391] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-449] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-369] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-382] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-391] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-409] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-370] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-391] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-447] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-427] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-434] for track '29' has 2 frames without a visible bounding box.
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

</details>