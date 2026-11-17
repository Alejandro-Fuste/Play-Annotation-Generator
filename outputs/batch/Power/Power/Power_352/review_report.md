# Play-Annotation-Generator Annotation Review — Power_352

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_352`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 28 | START | 28 | 306 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 28 | START | 28 | 306 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 28 | START | 76 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 28 | START | 28 | 341 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 28 | START | 28 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 28 | START | 28 | 373 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 28 | START | 28 | 306 |
| ✅ EXACT | `Action_DownBlock` | RT | `10` | `10` | 307 | START | 307 | 344 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `12` | 307 | START | 307 | 319 |
| ✅ EXACT | `Action_PullBlock` | LG | `9` | `9` | 307 | START | 307 | 344 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 76–77
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 28–373
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 373 | 346 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 28–449
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 341 | 314 | inferred_complete_timeline |
| `Action_PreSnap` | 346 | 391 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 393 | 395 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 398 | 418 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 433 | 449 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 28–425
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 306 | 279 | inferred_complete_timeline |
| `Action_PullBlock` | 307 | 344 | 38 | inferred_complete_timeline |
| `Action_None` | 347 | 348 | 2 | inferred_complete_timeline |
| `Action_None` | 350 | 381 | 32 | inferred_complete_timeline |
| `Action_None` | 384 | 385 | 2 | inferred_complete_timeline |
| `Action_None` | 404 | 425 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 28–380
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 306 | 279 | inferred_complete_timeline |
| `Action_DownBlock` | 307 | 319 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 321 | 344 | 24 | inferred_complete_timeline |
| `Action_None` | 345 | 367 | 23 | inferred_complete_timeline |
| `Action_None` | 371 | 373 | 3 | inferred_complete_timeline |
| `Action_None` | 375 | 376 | 2 | inferred_complete_timeline |
| `Action_None` | 378 | 380 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 28–449
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 449 | 422 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 28–449
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 306 | 279 | inferred_complete_timeline |
| `Action_DownBlock` | 307 | 344 | 38 | inferred_complete_timeline |
| `Action_None` | 345 | 449 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 28–449
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 316 | 289 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 368 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 399 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 406 | 409 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 436 | 449 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 28–449
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 143 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 339 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 350 | 389 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 391 | 431 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 444 | 449 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 28–441
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 54 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 190 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 200 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 243 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 409 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 414 | 421 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 430 | 435 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 438 | 441 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 28–315
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 204 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 309 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 315 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 28–449
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 339 | 312 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 384 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 396 | 449 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 28–449
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 350 | 323 | inferred_complete_timeline |
| `Action_PreSnap` | 352 | 362 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 368 | 438 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 444 | 449 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 28–40 | 13 | 1 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 214–306 | 92 | 2 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 307–369 | 48 | 5 | Undefined position; Undefined team |
| `16` | `22` | Position_Unknown | Team_Unknown | 330–345 | 16 | 1 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 330–449 | 69 | 2 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 360–449 | 55 | 2 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 370–449 | 78 | 3 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 381–449 | 69 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 388–434 | 44 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 394–408 | 14 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 396–444 | 48 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 405–449 | 45 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 430–449 | 20 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 435–449 | 15 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 436–449 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 65 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [28-40] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-339] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-384] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-350] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-362] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-438] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-341] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-391] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-395] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-418] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-143] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-339] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-389] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-431] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-373] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-316] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-368] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-399] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-409] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-204] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-309] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-315] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [307-344] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-381] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-425] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [307-344] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-449] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-54] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-190] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-200] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-243] for track '11' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-409] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-421] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-435] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-441] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [307-319] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-367] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-373] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-301] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-306] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-311] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-317] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-325] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-335] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-369] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-345] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-366] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-449] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-376] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-371] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-443] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [445-449] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-429] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-434] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-405] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-408] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-399] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-444] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.

</details>