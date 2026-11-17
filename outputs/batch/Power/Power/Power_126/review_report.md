# Play-Annotation-Generator Annotation Review — Power_126

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_126`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 63
- **Validation Warnings:** 74
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 0
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 15 | START | 15 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 15 | START | 15 | 353 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 15 | START | 15 | 274 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 15 | START | 15 | 274 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 15 | START | 15 | 274 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 15 | START | 15 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 15 | START | 15 | 301 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `12` | 275 | START | 275 | 280 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `2` | `2` | 275 | START | 275 | 305 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `5` | `5` | 275 | START | 275 | 289 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 15–378
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 353 | 339 | inferred_complete_timeline |
| `Action_PreSnap` | 366 | 378 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 15–112
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 112 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 15–389
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 389 | 375 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 15–372
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 274 | 260 | inferred_complete_timeline |
| `Action_PullBlock` | 275 | 289 | 15 | inferred_complete_timeline |
| `Action_PullBlock` | 291 | 347 | 57 | inferred_complete_timeline |
| `Action_None` | 348 | 361 | 14 | inferred_complete_timeline |
| `Action_None` | 368 | 372 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 15–389
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 274 | 260 | inferred_complete_timeline |
| `Action_DownBlock` | 275 | 280 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 305 | 347 | 43 | inferred_complete_timeline |
| `Action_None` | 348 | 358 | 11 | inferred_complete_timeline |
| `Action_None` | 371 | 389 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 15–301
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 301 | 287 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 15–364
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 274 | 260 | inferred_complete_timeline |
| `Action_DownBlock` | 275 | 305 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 310 | 347 | 38 | inferred_complete_timeline |
| `Action_None` | 348 | 364 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 15–343
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 343 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 15–317
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 44 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 278 | 231 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 285 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 317 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 15–331
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 271 | 257 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 323 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 331 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 15–388
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 35 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 48 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 279 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 344 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 346 | 351 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 388 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 15–318
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 291 | 277 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 301 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 313 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 318 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 15–389
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 115 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 389 | 271 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 15–144
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 144 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 15–389 | 339 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 15–383 | 331 | 6 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 295–389 | 78 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 306–389 | 75 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 332–389 | 58 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 334–389 | 56 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 341–383 | 43 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 347–356 | 10 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 351–389 | 39 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 382–385 | 4 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 387–388 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 51 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [15-343] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-274] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [275-305] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-364] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-44] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-278] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-285] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-317] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-115] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [275-289] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-361] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-372] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-90] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-323] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-291] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-301] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-313] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-112] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-301] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-353] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-378] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [275-280] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-358] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-389] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-271] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-323] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-331] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-54] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-135] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-355] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-369] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-378] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-383] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-35] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-48] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-279] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-344] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-351] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-388] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-311] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-349] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-381] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-314] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-317] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-383] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-356] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-385] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-388] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>