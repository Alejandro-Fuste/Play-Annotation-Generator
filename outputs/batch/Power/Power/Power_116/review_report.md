# Play-Annotation-Generator Annotation Review — Power_116

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_116`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 1
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 9 | START | 9 | 286 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 9 | START | 9 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 9 | START | 9 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 9 | START | 9 | 286 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 9 | START | 9 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 9 | START | 9 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `5` | `5` | 287 | START | 287 | 309 |
| ✅ EXACT | `Action_DownBlock` | C | `7` | `7` | 287 | START | 287 | 291 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `8` | `8` | 287 | START | 287 | 302 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `10` | `10` | 287 | START | 287 | 300 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 9–382
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 44 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 382 | 336 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 9–419
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 179 | 171 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 184 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 326 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 344 | 347 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 351 | 356 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 358 | 359 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 361 | 419 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 9–311
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 286 | 278 | inferred_complete_timeline |
| `Action_PullBlock` | 287 | 300 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 302 | 307 | 6 | inferred_complete_timeline |
| `Action_PullBlock` | 310 | 311 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 9–418
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 168 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 179 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 198 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 230 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 286 | 49 | inferred_complete_timeline |
| `Action_DownBlock` | 287 | 291 | 5 | inferred_complete_timeline |
| `Action_None` | 347 | 359 | 13 | inferred_complete_timeline |
| `Action_None` | 361 | 363 | 3 | inferred_complete_timeline |
| `Action_None` | 383 | 390 | 8 | inferred_complete_timeline |
| `Action_None` | 396 | 418 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 9–335
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 162 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 196 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 204 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 211 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 286 | 58 | inferred_complete_timeline |
| `Action_DownBlock` | 287 | 302 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 318 | 335 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 9–401
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 286 | 278 | inferred_complete_timeline |
| `Action_DownBlock` | 287 | 309 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 311 | 337 | 27 | inferred_complete_timeline |
| `Action_None` | 338 | 401 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 9–419
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 405 | 397 | inferred_complete_timeline |
| `Action_PreSnap` | 407 | 419 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 9–303
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 303 | 295 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 9–320
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 284 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 308 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 320 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 9–401
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 260 | 252 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 285 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 337 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 401 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 9–316
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 308 | 300 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 316 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 9–375
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 301 | 293 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 360 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 375 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 9–419
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 382 | 374 | inferred_complete_timeline |
| `Action_PreSnap` | 402 | 414 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 416 | 419 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 138–159 | 22 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 208–361 | 150 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 284–419 | 124 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 309–357 | 49 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 314–419 | 68 | 4 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 330–396 | 66 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 331–375 | 45 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 366–419 | 54 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 368–376 | 9 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 373–376 | 4 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 383–401 | 17 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 387–419 | 33 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 387–419 | 33 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 388–408 | 21 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 400–419 | 20 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 410–419 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 234: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [9-301] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-360] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-375] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-308] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-316] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-382] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-414] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-405] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-179] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-184] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-194] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-326] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-347] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-356] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [287-309] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-401] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-303] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-168] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-179] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-198] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-218] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [287-291] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-363] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-390] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-418] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-162] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-196] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-204] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-211] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [287-302] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [314-315] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [318-335] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-260] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-263] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-285] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-337] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-401] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [287-300] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [302-307] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [310-311] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-284] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-308] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-320] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-44] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-382] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-322] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-330] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-361] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-296] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-419] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-357] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-337] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-386] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-390] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-364] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-396] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-375] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-376] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-376] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-384] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-387] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-401] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-408] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.

</details>