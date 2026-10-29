# Play-Annotation-Generator Annotation Review — Duo_156

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_156`
- **Frame Range:** 0 to 448 (449 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 448
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 157
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | DT2 | defense | `11` | `11` |
| ✅ EXACT | `Action_ComboBlock` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `15` | `15` |
| ✅ EXACT | `Action_ComboBlock` | RT | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 284 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 351 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 213 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 251 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `9` | `Group` | 0 | START | 0 | 12 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | DT2 | `11` | `11` | 214 | START | 214 | 226 |
| ✅ EXACT | `Action_ComboBlock` | QB | `14` | `14` | 214 | START | 214 | 264 |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | `15` | `15` | 214 | START | 214 | 264 |
| ✅ EXACT | `Action_ComboBlock` | RT | `3` | `3` | 214 | START | 214 | 262 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 264 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–319
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_ComboBlock` | 214 | 264 | 51 | inferred_complete_timeline |
| `Action_None` | 265 | 272 | 8 | inferred_complete_timeline |
| `Action_None` | 281 | 319 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–411
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 351 | 352 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 411 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–19
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 19 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–309
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 284 | 285 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 309 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–370
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 351 | 310 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 370 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 282 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 251 | 252 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 255 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–318
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 213 | 128 | inferred_complete_timeline |
| `Action_ComboBlock` | 214 | 262 | 49 | inferred_complete_timeline |
| `Action_None` | 269 | 287 | 19 | inferred_complete_timeline |
| `Action_None` | 290 | 318 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–412
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 351 | 352 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 412 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 257 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 301 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 304 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 276 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 313 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_ComboBlock` | 214 | 226 | 13 | inferred_complete_timeline |
| `Action_ComboBlock` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 244 | 264 | 21 | inferred_complete_timeline |
| `Action_None` | 265 | 292 | 28 | inferred_complete_timeline |
| `Action_None` | 294 | 295 | 2 | inferred_complete_timeline |
| `Action_None` | 303 | 318 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 351 | 352 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 448 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–21
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–300
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 248 | 249 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 274 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 300 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 2–272 | 234 | 7 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 18–314 | 295 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 61–62 | 2 | 1 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 187–245 | 59 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 188–244 | 55 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 200–217 | 4 | 2 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 219–304 | 85 | 2 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 230–347 | 117 | 2 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 255–337 | 83 | 1 | Undefined position; Undefined team |
| `24` | `38` | Position_Unknown | Team_Unknown | 277–289 | 11 | 2 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 279–351 | 73 | 1 | Undefined position; Undefined team |
| `26` | `42` | Position_Unknown | Team_Unknown | 295–425 | 129 | 2 | Undefined position; Undefined team |
| `27` | `44` | Position_Unknown | Team_Unknown | 313–316 | 4 | 1 | Undefined position; Undefined team |
| `28` | `47` | Position_Unknown | Team_Unknown | 339–341 | 3 | 1 | Undefined position; Undefined team |
| `29` | `48` | Position_Unknown | Team_Unknown | 352–354 | 3 | 1 | Undefined position; Undefined team |
| `30` | `49` | Position_Unknown | Team_Unknown | 352–354 | 3 | 1 | Undefined position; Undefined team |
| `31` | `50` | Position_Unknown | Team_Unknown | 352–354 | 3 | 1 | Undefined position; Undefined team |
| `32` | `51` | Position_Unknown | Team_Unknown | 352–354 | 3 | 1 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 352–354 | 3 | 1 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 352–353 | 2 | 1 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 392–445 | 54 | 1 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 398–448 | 50 | 2 | Undefined position; Undefined team |
| `37` | `59` | Position_Unknown | Team_Unknown | 403–410 | 8 | 1 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 403–412 | 10 | 1 | Undefined position; Undefined team |
| `39` | `61` | Position_Unknown | Team_Unknown | 405–406 | 2 | 1 | Undefined position; Undefined team |
| `40` | `62` | Position_Unknown | Team_Unknown | 408–411 | 4 | 1 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 411–412 | 2 | 1 | Undefined position; Undefined team |
| `42` | `64` | Position_Unknown | Team_Unknown | 411–412 | 2 | 1 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 412–413 | 2 | 1 | Undefined position; Undefined team |
| `44` | `66` | Position_Unknown | Team_Unknown | 412–416 | 4 | 2 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 413–414 | 2 | 1 | Undefined position; Undefined team |
| `46` | `71` | Position_Unknown | Team_Unknown | 422–424 | 3 | 1 | Undefined position; Undefined team |
| `47` | `72` | Position_Unknown | Team_Unknown | 423–436 | 14 | 1 | Undefined position; Undefined team |
| `48` | `77` | Position_Unknown | Team_Unknown | 443–444 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `11` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 34 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 34 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 68 |
| Missing visible bounding boxes during action | 88 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 448 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-351] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-284] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-309] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-276] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-313] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [214-262] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-287] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-318] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-248] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-274] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-300] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-351] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-412] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-351] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-370] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-282] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-251] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-19] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-351] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-411] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [214-226] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [228-229] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [233-234] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-292] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-318] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-228] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-257] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-301] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-272] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-319] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-23] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-146] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-213] for track '15' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-272] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-257] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-314] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-62] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-245] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-215] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-244] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-201] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-272] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-304] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-281] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-347] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-337] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-285] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-289] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-351] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-351] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-425] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-316] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-341] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-354] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-354] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-354] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-354] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-354] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-353] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-445] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-445] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-448] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-410] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-412] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-406] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-411] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-412] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-412] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-413] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-413] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-416] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-414] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-424] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-436] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-444] for track '48' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.

</details>