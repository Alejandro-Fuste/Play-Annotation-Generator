# Play-Annotation-Generator Annotation Review — SplitZone_224

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_224`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 35
- **Ball Tracks:** 2
- **Action Segments:** 89
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 10
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `3` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `13` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `0` | `0` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `11` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 12 | START | 13 | 303 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 12 | START | 13 | 337 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 12 | START | 13 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 12 | START | 13 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 12 | START | 13 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 12 | START | 13 | 303 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 12 | START | 13 | 300 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 12 | START | 13 | 250 |
| ✅ EXACT | `Action_BallSnap` | C | `6` | `6` | 301 | START | 301 | 305 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `0` | `0` | 304 | START | 304 | 334 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `14` | `14` | 304 | START | 304 | 347 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `15` | `15` | 304 | START | 304 | 359 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `3` | 304 | START | 304 | 390 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `6` | `6` | 304 | START | 306 | 390 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 305 | END | 301 | 305 |
| ✅ EXACT | `Action_SplitBlock` | TE | `13` | `13` | 309 | START | 309 | 390 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 330 | START | 330 | 337 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `0` | `0` | 335 | START | 335 | 390 |
| ✅ EXACT | `Action_BallCarry` | RB | `11` | `11` | 338 | START | 338 | 427 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 390 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 13–432
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 250 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 300 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 301 | 305 | 5 | inferred_complete_timeline |
| `Action_None` | 306 | 329 | 24 | inferred_complete_timeline |
| `Action_Handoff` | 330 | 337 | 8 | inferred_complete_timeline |
| `Action_None` | 338 | 429 | 92 | inferred_complete_timeline |
| `Action_None` | 431 | 432 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 13–427
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 337 | 325 | inferred_complete_timeline |
| `Action_BallCarry` | 338 | 427 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 13–449
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 27 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 308 | 278 | inferred_complete_timeline |
| `Action_SplitBlock` | 309 | 390 | 82 | inferred_complete_timeline |
| `Action_None` | 391 | 416 | 26 | inferred_complete_timeline |
| `Action_None` | 419 | 449 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 13–449
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 303 | 291 | inferred_complete_timeline |
| `Action_ZoneBlock` | 304 | 334 | 31 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 335 | 390 | 56 | inferred_complete_timeline |
| `Action_None` | 391 | 449 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 13–359
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 110 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 303 | 181 | inferred_complete_timeline |
| `Action_ZoneBlock` | 304 | 359 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 13–449
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 300 | 288 | inferred_complete_timeline |
| `Action_BallSnap` | 301 | 305 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 306 | 390 | 85 | inferred_complete_timeline |
| `Action_None` | 391 | 449 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 13–347
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 43 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 48 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 69 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 303 | 233 | inferred_complete_timeline |
| `Action_ZoneBlock` | 304 | 347 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 13–449
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 303 | 291 | inferred_complete_timeline |
| `Action_ZoneBlock` | 304 | 390 | 87 | inferred_complete_timeline |
| `Action_None` | 391 | 449 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 13–399
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 300 | 288 | inferred_complete_timeline |
| `Action_None` | 301 | 362 | 62 | inferred_complete_timeline |
| `Action_None` | 368 | 394 | 27 | inferred_complete_timeline |
| `Action_None` | 397 | 399 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 13–368
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 194 | 182 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 300 | 104 | inferred_complete_timeline |
| `Action_None` | 301 | 363 | 63 | inferred_complete_timeline |
| `Action_None` | 367 | 368 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 13–449
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 300 | 288 | inferred_complete_timeline |
| `Action_None` | 301 | 449 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 13–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 300 | 288 | inferred_complete_timeline |
| `Action_None` | 301 | 349 | 49 | inferred_complete_timeline |
| `Action_None` | 351 | 388 | 38 | inferred_complete_timeline |
| `Action_None` | 390 | 449 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 13–332
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 300 | 288 | inferred_complete_timeline |
| `Action_None` | 301 | 332 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 13–449
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 300 | 288 | inferred_complete_timeline |
| `Action_None` | 301 | 449 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 15–350
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 300 | 286 | inferred_complete_timeline |
| `Action_None` | 301 | 350 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 13–449 | 381 | 7 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 13–134 | 122 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 13–64 | 52 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 148–150 | 3 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 164–449 | 280 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 287–342 | 55 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 350–444 | 95 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 352–363 | 12 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 360–449 | 90 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 362–366 | 5 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 369–449 | 81 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 376–449 | 74 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 378–405 | 27 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 384–449 | 66 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 385–449 | 58 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 403–449 | 47 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 409–439 | 8 | 3 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 424–449 | 26 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 433–449 | 13 | 2 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 442–449 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | 65 | 69 | 2 | 40.0% | 66–68 |
| `21` | `22` | 227 | 295 | 67 | 97.1% | 287, 294 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `6` (C): Annotated start 304 != Inferred start 306

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [301–305], lower_priority='Action_ZoneBlock' annotated_start=304, effective_Action_ZoneBlock_start=306.
- ⚠️ Action 'Action_None' range [301-332] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-99] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-352] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-367] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-378] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-194] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-363] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-134] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-449] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-362] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-394] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-399] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-250] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-300] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [301-305] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-429] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-64] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [338-427] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-449] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-27] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-416] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-43] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [304-347] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-110] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [304-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-349] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-388] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-350] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-300] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-400] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-315] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-342] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-444] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-363] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-366] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-449] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-388] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-405] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-439] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-410] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-423] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-439] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-435] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>