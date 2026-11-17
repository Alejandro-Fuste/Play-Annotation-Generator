# Play-Annotation-Generator Annotation Review — Power_234

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_234`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 25
- **Ball Tracks:** 1
- **Action Segments:** 59
- **Validation Warnings:** 63
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 9 | START | 9 | 256 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 9 | START | 9 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 9 | START | 9 | 256 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 9 | START | 9 | 256 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 9 | START | 9 | 421 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 9 | START | 9 | 256 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 9 | START | 9 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 9 | START | 9 | 389 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `11` | `11` | 257 | START | 257 | 262 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `14` | `14` | 257 | START | 257 | 261 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `3` | `3` | 257 | START | 257 | 271 |
| ✅ EXACT | `Action_PullBlock` | RG | `13` | `13` | 257 | START | 257 | 333 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 9–439
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 389 | 381 | inferred_complete_timeline |
| `Action_PreSnap` | 391 | 404 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 406 | 439 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 9–130
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 130 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 9–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 449 | 441 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 9–449
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 256 | 248 | inferred_complete_timeline |
| `Action_DownBlock` | 257 | 261 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 275 | 287 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 289 | 293 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 295 | 333 | 39 | inferred_complete_timeline |
| `Action_None` | 334 | 351 | 18 | inferred_complete_timeline |
| `Action_None` | 353 | 365 | 13 | inferred_complete_timeline |
| `Action_None` | 367 | 449 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 9–438
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 256 | 248 | inferred_complete_timeline |
| `Action_DownBlock` | 257 | 271 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 284 | 333 | 50 | inferred_complete_timeline |
| `Action_None` | 334 | 438 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 9–449
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 256 | 248 | inferred_complete_timeline |
| `Action_DownBlock` | 257 | 262 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 264 | 333 | 70 | inferred_complete_timeline |
| `Action_None` | 334 | 449 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 9–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 256 | 248 | inferred_complete_timeline |
| `Action_PullBlock` | 257 | 333 | 77 | inferred_complete_timeline |
| `Action_None` | 334 | 449 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 9–421
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 421 | 413 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 9–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 449 | 441 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–193
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 65 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 88 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 112 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 119 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 193 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 9–321
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 321 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 9–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 352 | 344 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 355 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 359 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 9–140
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 140 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 9–425
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 414 | 406 | inferred_complete_timeline |
| `Action_PreSnap` | 416 | 425 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 9–141
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 141 | 133 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 9–65 | 5 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 250–449 | 191 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 252–430 | 179 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 261–264 | 4 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 325–449 | 125 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 348–449 | 98 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 350–449 | 100 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 352–449 | 98 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 366–449 | 75 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 438–449 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `21` | 274 | 274 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 42 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [9-414] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-425] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-352] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-355] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-421] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [257-271] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-438] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-140] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-141] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-321] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-404] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-439] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-119] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-127] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-193] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [257-262] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-130] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-449] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [257-261] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [275-287] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [289-293] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-351] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-365] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-10] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-400] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-430] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-264] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-404] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-427] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-449] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-449] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-404] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-411] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-425] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>