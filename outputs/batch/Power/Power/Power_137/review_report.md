# Play-Annotation-Generator Annotation Review — Power_137

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_137`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 479
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 0
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `24` | `23` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 4 | START | 0 | 377 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 4 | START | 0 | 367 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 4 | START | 0 | 253 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 4 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 4 | START | 0 | 373 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 4 | START | 0 | 253 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `24` | `Group` | 4 | START | 12 | 253 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 4 | START | 0 | 479 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `17` | `17` | 254 | START | 254 | 284 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `21` | 254 | START | 254 | 284 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `24` | `23` | 254 | START | 254 | 284 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 373 | 374 | inferred_complete_timeline |
| `Action_PreSnap` | 375 | 479 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_PreSnap` | 369 | 479 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 479 | 480 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–377
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 377 | 378 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |
| `Action_DownBlock` | 254 | 284 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 289 | 293 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 295 | 304 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 308 | 312 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 315 | 347 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 350 | 354 | 5 | inferred_complete_timeline |
| `Action_None` | 355 | 479 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–309
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |
| `Action_DownBlock` | 254 | 284 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 288 | 291 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 296 | 305 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 308 | 309 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 12–479
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 253 | 242 | inferred_complete_timeline |
| `Action_PullBlock` | 254 | 284 | 31 | inferred_complete_timeline |
| `Action_PullBlock` | 288 | 348 | 61 | inferred_complete_timeline |
| `Action_PullBlock` | 350 | 354 | 5 | inferred_complete_timeline |
| `Action_None` | 355 | 362 | 8 | inferred_complete_timeline |
| `Action_None` | 364 | 479 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 62 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 385 | 311 | inferred_complete_timeline |
| `Action_PreSnap` | 388 | 421 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 425 | 479 | 55 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 124 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 264 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 280 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 304 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 309 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 479 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 443 | 444 | inferred_complete_timeline |
| `Action_PreSnap` | 446 | 479 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 284 | 274 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 295 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 350 | 417 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 423 | 479 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 472

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 284 | 285 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 312 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 417 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 419 | 479 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–475
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 356 | 357 | inferred_complete_timeline |
| `Action_PreSnap` | 361 | 362 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 384 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 388 | 452 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 455 | 468 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 471 | 475 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–477
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 477 | 478 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 479 | 480 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 309 | 310 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 362 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 372 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 375 | 389 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 393 | 479 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 479 | 480 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 389 | 390 | inferred_complete_timeline |
| `Action_PreSnap` | 391 | 479 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 479 | 480 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–479 | 473 | 3 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–477 | 473 | 3 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–479 | 438 | 9 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 4–5 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 66–75 | 6 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 179–252 | 8 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 285–349 | 5 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 318–319 | 2 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 322–479 | 158 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 404–408 | 4 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 424–479 | 56 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 476–479 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `24` (3 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 82 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 276: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 276: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 276: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '17' (LG) duration 101 frames exceeds threshold 90 frames [start=254, end=354].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '23' (RG) duration 101 frames exceeds threshold 90 frames [start=254, end=354].
- ⚠️ Action 'Action_PreSnap' range [0-377] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-367] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-479] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-352] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-408] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-428] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-471] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-477] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-309] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-362] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-372] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-389] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-479] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-479] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-124] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-264] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-280] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-304] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-309] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-477] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-443] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-103] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-117] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-139] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-280] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-312] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-347] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-416] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-479] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-284] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-312] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-417] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-479] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-284] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-295] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-417] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-479] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-356] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-362] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-384] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-452] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [455-468] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [471-475] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-253] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [254-284] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [289-293] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [295-304] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [308-312] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [315-347] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-479] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-62] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-385] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-421] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-479] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-373] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-253] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [254-284] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [288-291] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [296-305] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [308-309] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-253] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [254-284] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [288-348] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-362] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-479] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-68] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-75] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-248] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-286] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-349] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-319] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-405] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-408] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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

</details>