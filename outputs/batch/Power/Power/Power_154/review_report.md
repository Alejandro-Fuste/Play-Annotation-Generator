# Play-Annotation-Generator Annotation Review — Power_154

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_154`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 148
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `8` | `8` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 32 | START | 32 | 341 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 32 | START | 32 | 267 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 32 | START | 32 | 355 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 32 | START | 32 | 361 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 32 | START | 32 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 32 | START | 32 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 32 | START | 32 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 32 | START | 32 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `7` | `7` | 181 | START | 181 | 204 |
| ✅ EXACT | `Action_DownBlock` | RG | `8` | `8` | 181 | START | 181 | 269 |
| ✅ EXACT | `Action_PullBlock` | LT | `5` | `5` | 181 | START | 181 | 273 |

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
- **Visible Frames:** 32–449
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 267 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 282 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 429 | 145 | inferred_complete_timeline |
| `Action_PreSnap` | 431 | 439 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 447 | 449 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 32–181
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 181 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 32–371
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 355 | 324 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 359 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 361 | 368 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 371 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 32–331
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 180 | 149 | inferred_complete_timeline |
| `Action_PullBlock` | 181 | 273 | 93 | inferred_complete_timeline |
| `Action_None` | 274 | 293 | 20 | inferred_complete_timeline |
| `Action_None` | 295 | 296 | 2 | inferred_complete_timeline |
| `Action_None` | 311 | 321 | 11 | inferred_complete_timeline |
| `Action_None` | 330 | 331 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 32–307
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 180 | 149 | inferred_complete_timeline |
| `Action_DownBlock` | 181 | 204 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 207 | 273 | 67 | inferred_complete_timeline |
| `Action_None` | 274 | 307 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 32–361
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 361 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 32–449
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 180 | 149 | inferred_complete_timeline |
| `Action_DownBlock` | 181 | 269 | 89 | inferred_complete_timeline |
| `Action_None` | 343 | 375 | 33 | inferred_complete_timeline |
| `Action_None` | 432 | 449 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 32–369
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 341 | 310 | inferred_complete_timeline |
| `Action_PreSnap` | 351 | 369 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 32–389
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 287 | 256 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 352 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 356 | 389 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 32–449
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 38 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 269 | 230 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 278 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 411 | 129 | inferred_complete_timeline |
| `Action_PreSnap` | 413 | 419 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 421 | 449 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 32–220
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 96 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 187 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 220 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 32–359
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 178 | 147 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 223 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 253 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 359 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 32–381
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 257 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 330 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 381 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 32–160
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 155 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 160 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 32–266
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 190 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 266 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 32–264 | 113 | 8 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 233–264 | 29 | 2 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 266–336 | 59 | 3 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 276–342 | 63 | 3 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 277–286 | 8 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 279–292 | 9 | 2 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 286–353 | 17 | 3 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 289–373 | 61 | 6 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 290–302 | 11 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 294–449 | 148 | 3 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 294–449 | 154 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 297–345 | 49 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 299–341 | 43 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 303–375 | 68 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 305–368 | 62 | 2 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 331–449 | 118 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 342–449 | 106 | 3 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 362–363 | 2 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 362–366 | 4 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 376–378 | 3 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 389–449 | 61 | 1 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 439–449 | 11 | 1 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 442–444 | 3 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 447–449 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 95 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 310: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '5' (LT) duration 93 frames exceeds threshold 90 frames [start=181, end=273].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '7' (LG) duration 93 frames exceeds threshold 90 frames [start=181, end=273].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (RG) duration 93 frames exceeds threshold 90 frames [start=181, end=273].
- ⚠️ Action 'Action_PreSnap' range [32-341] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-369] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-266] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-257] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-330] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-381] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-155] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-287] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-352] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-293] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-321] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-181] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [181-204] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-307] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [181-269] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-375] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-38] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-269] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-278] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-411] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-419] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-449] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-267] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-282] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-429] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-439] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-449] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-355] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-368] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-371] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-361] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-213] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-223] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-253] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-96] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-187] for track '14' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-220] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-222] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-243] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-264] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-249] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-264] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-285] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-315] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-336] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-300] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-331] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-342] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-278] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-286] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-280] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-292] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-339] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-353] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-297] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-316] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-343] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-353] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-366] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-373] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-294] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-302] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-308] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-379] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-449] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-401] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-345] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-341] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-318] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-359] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-375] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-339] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-368] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-442] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-346] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-419] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-363] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-363] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-366] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-378] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-444] for track '37' has 1 frames without a visible bounding box.
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