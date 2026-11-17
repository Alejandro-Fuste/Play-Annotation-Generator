# Play-Annotation-Generator Annotation Review — Power_247

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_247`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 449
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 15 | START | 15 | 250 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 15 | START | 15 | 274 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `16` | `Group` | 15 | START | 15 | 279 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 15 | START | 15 | 252 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 15 | START | 15 | 252 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 15 | START | 15 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 15 | START | 15 | 422 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 15 | START | 15 | 289 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 15 | START | 15 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 15 | START | 15 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 15 | START | 15 | 449 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `19` | `19` | 253 | START | 253 | 263 |
| ✅ EXACT | `Action_PullBlock` | LG | `18` | `18` | 253 | START | 253 | 297 |

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
- **Visible Frames:** 15–449
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 422 | 408 | inferred_complete_timeline |
| `Action_PreSnap` | 428 | 449 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 15–413
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 289 | 275 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 295 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 307 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 400 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 403 | 413 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 15–449
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 279 | 265 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 436 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 444 | 449 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 15–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 449 | 435 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 15–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 449 | 435 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 15–449
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 250 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 258 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 449 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 15–395
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 275 | 261 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 280 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 301 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 395 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 15–449
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 252 | 238 | inferred_complete_timeline |
| `Action_PullBlock` | 253 | 297 | 45 | inferred_complete_timeline |
| `Action_None` | 298 | 312 | 15 | inferred_complete_timeline |
| `Action_None` | 319 | 449 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 15–449
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 252 | 238 | inferred_complete_timeline |
| `Action_DownBlock` | 253 | 263 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 268 | 274 | 7 | inferred_complete_timeline |
| `Action_None` | 317 | 352 | 36 | inferred_complete_timeline |
| `Action_None` | 355 | 449 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 15–449
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 274 | 260 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 325 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 411 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 416 | 444 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 446 | 449 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 15–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 449 | 435 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 15–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 449 | 435 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 15–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 449 | 435 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 15–257
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 257 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 15–278
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 275 | 261 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 278 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 15–318
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 287 | 273 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 304 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 318 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 15–334
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 330 | 316 | inferred_complete_timeline |
| `Action_PreSnap` | 333 | 334 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 15–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 449 | 435 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 15–449
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 414 | 400 | inferred_complete_timeline |
| `Action_PreSnap` | 425 | 434 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 439 | 449 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 15–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 449 | 435 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 15–449
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 434 | 420 | inferred_complete_timeline |
| `Action_PreSnap` | 442 | 444 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 447 | 449 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 15–449 | 427 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 132–336 | 58 | 7 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 259–269 | 4 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 270–292 | 23 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 273–306 | 23 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 314–449 | 131 | 4 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 317–449 | 123 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 324–449 | 117 | 3 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 332–334 | 3 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 346–449 | 97 | 3 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 351–355 | 5 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 376–439 | 19 | 3 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 398–446 | 29 | 4 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 399–401 | 3 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 402–449 | 47 | 2 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 421–449 | 23 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (3 segments found)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 496: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [15-250] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-258] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-275] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-280] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-301] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-395] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-449] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-275] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-278] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-330] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-334] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-434] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-444] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-449] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-287] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-304] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-318] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-414] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-434] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-257] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-274] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-325] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-411] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-444] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-279] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-436] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-333] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-346] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-312] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [253-263] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [265-266] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [268-274] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-352] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-449] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-422] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-289] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-295] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-307] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-400] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-413] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-209] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-250] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-330] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-336] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-260] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-292] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-280] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-300] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-306] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-316] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-320] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-330] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-364] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-326] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-354] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-334] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-367] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-355] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-390] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-402] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-439] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-404] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-413] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [429-431] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-446] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-401] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-404] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-423] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-429] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-437] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-449] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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