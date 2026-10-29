# Play-Annotation-Generator Annotation Review — Duo_75

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_75`
- **Frame Range:** 0 to 418 (419 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 418
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 59
- **Validation Warnings:** 55
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 36
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `11` | `11` |
| ✅ EXACT | `Action_ComboBlock` | LB2 | defense | `15` | `15` |
| ✅ EXACT | `Action_ComboBlock` | LB1 | defense | `17` | `17` |
| ✅ EXACT | `Action_ComboBlock` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 418 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 418 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 302 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 418 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 302 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 322 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 369 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 339 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 418 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 418 |
| ✅ EXACT | `Action_ComboBlock` | RG | `11` | `11` | 303 | START | 303 | 350 |
| ✅ EXACT | `Action_ComboBlock` | LB2 | `15` | `15` | 303 | START | 303 | 350 |
| ✅ EXACT | `Action_ComboBlock` | LB1 | `17` | `17` | 303 | START | 303 | 350 |
| ✅ EXACT | `Action_ComboBlock` | RT | `18` | `18` | 303 | START | 303 | 350 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `7` | `7` | 318 | START | 318 | 350 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 350 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 322 | 323 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 418 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–412
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 339 | 340 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 353 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 378 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 386 | 399 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 409 | 412 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 418 | 419 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–416
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 369 | 370 | inferred_complete_timeline |
| `Action_PreSnap` | 395 | 403 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 412 | 416 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 418 | 419 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 418 | 419 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 418 | 419 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 418 | 419 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 318 | 350 | 33 | inferred_complete_timeline |
| `Action_None` | 351 | 360 | 10 | inferred_complete_timeline |
| `Action_None` | 363 | 418 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–350
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 302 | 303 | inferred_complete_timeline |
| `Action_ComboBlock` | 303 | 350 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–417
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 302 | 303 | inferred_complete_timeline |
| `Action_ComboBlock` | 303 | 350 | 48 | inferred_complete_timeline |
| `Action_None` | 351 | 374 | 24 | inferred_complete_timeline |
| `Action_None` | 386 | 392 | 7 | inferred_complete_timeline |
| `Action_None` | 395 | 400 | 6 | inferred_complete_timeline |
| `Action_None` | 404 | 417 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 334 | 335 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 418 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 41–418
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 41 | 233 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 418 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–342
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 323 | 324 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 342 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–410
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 302 | 303 | inferred_complete_timeline |
| `Action_ComboBlock` | 303 | 350 | 48 | inferred_complete_timeline |
| `Action_None` | 351 | 410 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 302 | 303 | inferred_complete_timeline |
| `Action_ComboBlock` | 303 | 350 | 48 | inferred_complete_timeline |
| `Action_None` | 351 | 418 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 418 | 419 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–382
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 218 | 171 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 371 | 144 | inferred_complete_timeline |
| `Action_PreSnap` | 380 | 382 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 418 | 419 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 418 | 419 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–353
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 337 | 338 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 353 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–36 | 37 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 59–65 | 7 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 310–387 | 46 | 5 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 314–362 | 49 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 390–399 | 10 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 396–399 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 42 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 418 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-418] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-369] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-403] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-416] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-339] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-353] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-378] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-399] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-412] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-418] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-317] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-360] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-418] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-323] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-342] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [303-350] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-218] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-371] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-382] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-337] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-353] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-334] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-418] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-418] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-410] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-374] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-392] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-400] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-417] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-322] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-233] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-65] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-313] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-327] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-354] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-361] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-387] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-362] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-399] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-399] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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