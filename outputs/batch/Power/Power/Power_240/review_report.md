# Play-Annotation-Generator Annotation Review — Power_240

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_240`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 509
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 164
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `13` | `13` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 318 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 432 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 342 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 355 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 350 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 318 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `13` | `13` | 319 | START | 319 | 342 |
| ✅ EXACT | `Action_DownBlock` | C | `16` | `16` | 319 | START | 319 | 340 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `9` | `9` | 319 | START | 319 | 328 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–476
- **Visible Samples:** 467

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_PreSnap` | 443 | 476 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 342 | 343 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 374 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–350
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 350 | 351 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 355 | 356 | inferred_complete_timeline |
| `Action_PreSnap` | 387 | 455 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 464 | 509 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–346
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 318 | 319 | inferred_complete_timeline |
| `Action_PullBlock` | 319 | 328 | 10 | inferred_complete_timeline |
| `Action_PullBlock` | 338 | 339 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 343 | 346 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–340
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 255 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 318 | 58 | inferred_complete_timeline |
| `Action_DownBlock` | 319 | 340 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–401
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 339 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 380 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 400 | 401 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 318 | 319 | inferred_complete_timeline |
| `Action_DownBlock` | 319 | 342 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 349 | 359 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 509 | 510 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–336
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 336 | 337 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 502

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 411 | 412 | inferred_complete_timeline |
| `Action_PreSnap` | 415 | 418 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 424 | 509 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 500

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 346 | 347 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 374 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 378 | 509 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 481

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 205 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 360 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 410 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 416 | 464 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 473 | 509 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–455
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 414 | 415 | inferred_complete_timeline |
| `Action_PreSnap` | 416 | 417 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 420 | 424 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 429 | 455 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–497 | 485 | 3 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–252 | 242 | 3 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–367 | 368 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–414 | 383 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–143 | 75 | 10 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–349 | 206 | 12 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 160–207 | 30 | 6 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 299–388 | 58 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 330–384 | 55 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 348–379 | 19 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 353–443 | 91 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 358–475 | 107 | 5 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 367–370 | 4 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 388–509 | 117 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 388–423 | 34 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 393–464 | 72 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 401–402 | 2 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 408–507 | 100 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 410–472 | 42 | 4 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 415–416 | 2 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 439–507 | 68 | 2 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 444–509 | 60 | 2 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 448–509 | 62 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 449–471 | 21 | 2 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 495–500 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 111 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 482: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ Row 482: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-411] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-435] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-497] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-234] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-252] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-411] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-418] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-355] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-455] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [464-509] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-414] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-417] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-424] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [429-455] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-367] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-336] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-350] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-509] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [319-328] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [338-339] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [343-346] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-346] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-374] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-509] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-188] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-205] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-360] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-410] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-464] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-349] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-382] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-387] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-392] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-414] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [319-342] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [349-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-432] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-476] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-339] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-380] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-401] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-255] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [319-340] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-342] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-374] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-20] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-32] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-46] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-93] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-109] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-94] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-101] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-247] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-330] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-337] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-349] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-175] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-185] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-201] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-302] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-340] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-346] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-384] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-388] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-384] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-351] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-364] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-374] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-379] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-443] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-383] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-438] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [445-451] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-464] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-475] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-370] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-472] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-480] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-407] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-423] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-464] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-402] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-507] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-416] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-419] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-459] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [465-472] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-416] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-502] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [504-507] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-459] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [449-454] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [457-471] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [495-500] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>