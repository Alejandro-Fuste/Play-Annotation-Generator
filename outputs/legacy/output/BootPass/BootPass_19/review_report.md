# Play-Annotation-Generator Annotation Review — BootPass_19

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_19`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 569
- **Player Tracks:** 34
- **Ball Tracks:** 7
- **Action Segments:** 85
- **Validation Warnings:** 135
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 6
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `13` | `13` |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `13` | `13` |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | Team_Unknown | `13` | `13` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `8` | `8` | 258 | START | 258 | 342 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `13` | `13` | 258 | END | 258 | 258 |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | `13` | `13` | 270 | START | 270 | 282 |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | `13` | `13` | 288 | START | 288 | 319 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `1` | `1` | 336 | START | 336 | 343 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `13` | `13` | 336 | START | 336 | 345 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

*(No offensive player tracks)*

</details>

<details>
<summary><strong>Defense</strong></summary>

*(No defensive player tracks)*

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–569 | 546 | 5 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–569 | 569 | 4 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–464 | 464 | 2 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–479 | 479 | 2 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–543 | 523 | 4 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–374 | 375 | 1 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–486 | 479 | 5 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–569 | 565 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–569 | 569 | 4 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–569 | 570 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–357 | 357 | 2 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–272 | 272 | 2 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–569 | 561 | 4 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–370 | 371 | 9 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–292 | 289 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–443 | 444 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–419 | 420 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–441 | 436 | 4 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–569 | 557 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–381 | 381 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–569 | 532 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–569 | 570 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 298–444 | 147 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 299–333 | 35 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 299–300 | 2 | 1 | Undefined position; Undefined team |
| `31` | `52` | Position_Unknown | Team_Unknown | 319–323 | 5 | 1 | Undefined position; Undefined team |
| `32` | `54` | Position_Unknown | Team_Unknown | 337–371 | 35 | 1 | Undefined position; Undefined team |
| `34` | `59` | Position_Unknown | Team_Unknown | 362–363 | 2 | 1 | Undefined position; Undefined team |
| `35` | `60` | Position_Unknown | Team_Unknown | 367–415 | 44 | 4 | Undefined position; Undefined team |
| `36` | `61` | Position_Unknown | Team_Unknown | 372–465 | 94 | 1 | Undefined position; Undefined team |
| `37` | `66` | Position_Unknown | Team_Unknown | 450–482 | 12 | 3 | Undefined position; Undefined team |
| `38` | `68` | Position_Unknown | Team_Unknown | 510–569 | 45 | 5 | Undefined position; Undefined team |
| `39` | `69` | Position_Unknown | Team_Unknown | 557–569 | 13 | 1 | Undefined position; Undefined team |
| `40` | `71` | Position_Unknown | Team_Unknown | 566–569 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | 276 | 278 | 3 | 100.0% | None |
| `23` | `28` | 284 | 284 | 1 | 100.0% | None |
| `24` | `33` | 294 | 294 | 1 | 100.0% | None |
| `28` | `40` | 299 | 299 | 1 | 100.0% | None |
| `29` | `42` | 301 | 301 | 1 | 100.0% | None |
| `30` | `48` | 310 | 310 | 1 | 100.0% | None |
| `33` | `58` | 350 | 355 | 5 | 83.3% | 351 |

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 34 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 34 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 252 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 68 |
| Missing visible bounding boxes during action | 65 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-506] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [508-514] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [524-529] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [538-542] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-400] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-461] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-464] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-474] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-479] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-508] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [518-519] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [522-523] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [534-543] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-374] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-439] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-442] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-464] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-475] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-486] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-336] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-515] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-317] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-357] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-261] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-272] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-419] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-537] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [539-540] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [548-569] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-370] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-282] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-292] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-443] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-419] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-252] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-277] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-289] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-441] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-490] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [492-513] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [525-545] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-331] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-381] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-522] for track '20' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-444] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-333] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-300] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-323] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-371] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-363] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-398] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-402] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-407] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-415] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-465] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-453] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [459-460] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-482] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [510-513] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [516-520] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [522-530] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [542-546] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [548-569] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [557-569] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [566-569] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
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

</details>