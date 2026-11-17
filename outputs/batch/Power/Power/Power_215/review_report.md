# Play-Annotation-Generator Annotation Review — Power_215

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_215`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE1 | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `24` | `23` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 30 | START | 30 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 30 | START | 30 | 420 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `13` | `Group` | 30 | START | 30 | 290 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 30 | START | 30 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 30 | START | 30 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 30 | START | 30 | 260 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 30 | START | 30 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 30 | START | 35 | 196 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 30 | START | 30 | 285 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 30 | START | 30 | 260 |
| ✅ EXACT | `Action_DownBlock` | C | `18` | `18` | 261 | START | 261 | 309 |
| ✅ EXACT | `Action_DownBlock` | LG | `19` | `19` | 261 | START | 261 | 309 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE1 | `8` | `8` | 261 | START | 261 | 279 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `24` | `23` | 261 | START | 262 | 264 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 30–348
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 183 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 348 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 30–441
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 420 | 391 | inferred_complete_timeline |
| `Action_PreSnap` | 422 | 423 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 425 | 441 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 30–449
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 449 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 30–449
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 285 | 256 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 449 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 30–331
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 260 | 231 | inferred_complete_timeline |
| `Action_DownBlock` | 261 | 279 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 283 | 309 | 27 | inferred_complete_timeline |
| `Action_None` | 310 | 316 | 7 | inferred_complete_timeline |
| `Action_None` | 324 | 328 | 5 | inferred_complete_timeline |
| `Action_None` | 330 | 331 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 30–290
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 290 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 35–196
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 35 | 196 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 30–388
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 57 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 260 | 199 | inferred_complete_timeline |
| `Action_DownBlock` | 261 | 309 | 49 | inferred_complete_timeline |
| `Action_None` | 310 | 329 | 20 | inferred_complete_timeline |
| `Action_None` | 332 | 342 | 11 | inferred_complete_timeline |
| `Action_None` | 354 | 360 | 7 | inferred_complete_timeline |
| `Action_None` | 375 | 379 | 5 | inferred_complete_timeline |
| `Action_None` | 387 | 388 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 30–449
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 260 | 231 | inferred_complete_timeline |
| `Action_DownBlock` | 261 | 309 | 49 | inferred_complete_timeline |
| `Action_None` | 310 | 328 | 19 | inferred_complete_timeline |
| `Action_None` | 350 | 439 | 90 | inferred_complete_timeline |
| `Action_None` | 443 | 449 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 30–293
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 174 | 145 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 293 | 117 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 30–449
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 286 | 257 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 407 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 413 | 414 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 418 | 449 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 30–449
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 277 | 248 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 283 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 449 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 30–294
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 294 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 30–449
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 280 | 251 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 285 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 306 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 320 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 333 | 366 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 368 | 449 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 30–350
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 350 | 321 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 30–325
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 310 | 281 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 325 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 30–449
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 416 | 387 | inferred_complete_timeline |
| `Action_PreSnap` | 420 | 449 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 30–449
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 449 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 30–449
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 449 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 30–423
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 423 | 394 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 30–447 | 413 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 182–188 | 7 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 216–303 | 9 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 262–449 | 183 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 292–325 | 32 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 305–449 | 145 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 318–408 | 89 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 318–449 | 114 | 5 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 327–449 | 122 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 337–449 | 113 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 338–401 | 23 | 5 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 353–449 | 97 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 365–449 | 85 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `24` (2 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 65 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [30-416] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-350] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-285] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-286] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-407] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-414] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-422] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-427] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-447] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-423] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-260] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [261-279] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-316] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-328] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-310] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-325] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-280] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-285] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-306] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-320] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-366] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-420] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-423] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-441] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-294] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-290] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-277] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-283] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-449] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-183] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-348] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-293] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-328] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-439] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-57] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-260] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-342] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-360] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-379] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-188] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-303] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [262-264] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-337] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-319] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-325] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-449] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-322] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-408] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-319] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-354] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-372] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-375] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-370] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-449] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-340] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-343] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-349] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-357] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-401] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>