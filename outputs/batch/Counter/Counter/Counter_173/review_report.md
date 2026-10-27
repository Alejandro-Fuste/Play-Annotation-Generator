# Play-Annotation-Generator Annotation Review — Counter_173

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_173`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 539
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 158
- **Validation Warnings:** 179
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 129
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | SAF | defense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `23` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF | defense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `22` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `24` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_PullLeadBlock` | DE1 | defense | `16` | `15` |
| ✅ EXACT | `Action_PlaySideFakeStep` | LB2 | defense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `23` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB2 | defense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 10 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 219 |
| ✅ EXACT | `Action_BallSnap` | SAF | `14` | `13` | 220 | START | 220 | 224 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `23` | `21` | 224 | END | 220 | 224 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF | `14` | `13` | 226 | START | 226 | 303 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `22` | `20` | 226 | START | 226 | 242 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `24` | `22` | 226 | START | 226 | 241 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `18` | `17` | 226 | START | 226 | 232 |
| ✅ EXACT | `Action_PullLeadBlock` | DE1 | `16` | `15` | 226 | START | 226 | 290 |
| ✅ EXACT | `Action_PlaySideFakeStep` | LB2 | `7` | `6` | 228 | START | 228 | 272 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `23` | `21` | 260 | START | 260 | 272 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB2 | `7` | `6` | 273 | START | 273 | 305 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 318 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 10–309
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 11 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 14 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 18 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 35 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 60 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 72 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 219 | 143 | inferred_complete_timeline |
| `Action_None` | 220 | 309 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–528
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 237 | 18 | inferred_complete_timeline |
| `Action_None` | 239 | 248 | 10 | inferred_complete_timeline |
| `Action_None` | 265 | 331 | 67 | inferred_complete_timeline |
| `Action_None` | 336 | 389 | 54 | inferred_complete_timeline |
| `Action_None` | 394 | 528 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 506

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 256 | 37 | inferred_complete_timeline |
| `Action_None` | 265 | 294 | 30 | inferred_complete_timeline |
| `Action_None` | 296 | 350 | 55 | inferred_complete_timeline |
| `Action_None` | 352 | 376 | 25 | inferred_complete_timeline |
| `Action_None` | 396 | 398 | 3 | inferred_complete_timeline |
| `Action_None` | 400 | 409 | 10 | inferred_complete_timeline |
| `Action_None` | 414 | 539 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–450
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 328 | 109 | inferred_complete_timeline |
| `Action_None` | 330 | 369 | 40 | inferred_complete_timeline |
| `Action_None` | 372 | 450 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 539 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 523 | 304 | inferred_complete_timeline |
| `Action_None` | 526 | 539 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–378
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 372 | 153 | inferred_complete_timeline |
| `Action_None` | 374 | 378 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 292 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 8–290
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 225 | 218 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 226 | 290 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–486
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 317 | 98 | inferred_complete_timeline |
| `Action_None` | 325 | 486 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–464
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 219 | 128 | inferred_complete_timeline |
| `Action_None` | 220 | 464 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 539 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 381 | 162 | inferred_complete_timeline |
| `Action_None` | 386 | 458 | 73 | inferred_complete_timeline |
| `Action_None` | 461 | 539 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–427
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 228 | 272 | 45 | inferred_complete_timeline |
| `Action_BallCarry` | 273 | 305 | 33 | inferred_complete_timeline |
| `Action_BallCarry` | 311 | 427 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 388 | 169 | inferred_complete_timeline |
| `Action_None` | 401 | 433 | 33 | inferred_complete_timeline |
| `Action_None` | 437 | 539 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–432
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 43 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 219 | 172 | inferred_complete_timeline |
| `Action_None` | 220 | 243 | 24 | inferred_complete_timeline |
| `Action_None` | 245 | 432 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–490
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_BallSnap` | 220 | 224 | 5 | inferred_complete_timeline |
| `Action_None` | 225 | 225 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 226 | 303 | 78 | inferred_complete_timeline |
| `Action_DownBlock` | 305 | 306 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 310 | 317 | 8 | inferred_complete_timeline |
| `Action_None` | 322 | 336 | 15 | inferred_complete_timeline |
| `Action_None` | 338 | 482 | 145 | inferred_complete_timeline |
| `Action_None` | 485 | 490 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 13–291 | 209 | 7 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 13–18 | 4 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 14–266 | 253 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 22–522 | 486 | 5 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 88–419 | 330 | 6 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 89–414 | 218 | 12 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 273–539 | 259 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 288–490 | 199 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 320–425 | 97 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 323–350 | 5 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 331–385 | 37 | 5 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 337–539 | 133 | 7 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 360–364 | 5 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 360–361 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 360–361 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 367–390 | 21 | 4 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 382–469 | 88 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 389–477 | 82 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 397–398 | 2 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 428–483 | 16 | 3 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 456–539 | 62 | 4 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 478–485 | 8 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 496–539 | 37 | 5 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 508–539 | 32 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 510–539 | 30 | 1 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 522–525 | 4 | 1 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 527–539 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (7 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `24` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 121 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (SAF) duration 93 frames exceeds threshold 90 frames [start=226, end=318].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (Unknown) duration 93 frames exceeds threshold 90 frames [start=226, end=318].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '22' (Unknown) duration 93 frames exceeds threshold 90 frames [start=226, end=318].
- ⚠️ Action 'Action_None' range [220-372] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-378] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-328] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-369] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-450] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-523] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-256] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-294] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-350] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-376] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-398] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-409] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-292] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [273-305] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [311-427] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-237] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-248] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-331] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-528] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-317] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-486] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-388] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-433] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-381] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-458] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-539] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-88] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-464] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [226-303] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [305-306] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [310-317] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-336] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-482] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-490] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-243] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-432] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [226-290] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-11] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-14] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-35] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-60] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-72] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-309] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-18] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-43] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [226-232] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [236-264] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [268-282] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [289-291] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-14] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-219] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-266] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-225] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [226-242] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-352] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-522] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [260-272] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-414] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-419] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [226-241] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [256-257] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [261-262] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [302-310] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [312-316] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-352] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-358] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-394] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-414] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-286] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-295] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-490] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-338] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-352] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-376] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-425] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-338] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-369] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-375] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-379] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-349] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-359] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-366] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-376] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-483] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-364] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-369] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-382] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-390] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-469] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-409] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-477] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-443] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-483] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-458] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-477] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-485] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-500] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-509] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-515] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-526] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-539] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-525] for track '42' has 2 frames without a visible bounding box.
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

</details>