# Play-Annotation-Generator Annotation Review — PuntBlock_42

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_42`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 479
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 125
- **Validation Warnings:** 161
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 119
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_LongSnap` | Left_Guard | offense | `9` | `9` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `9` | `Group` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_BlockPunt` | Right_Edge_Rusher1 | defense | `1` | `1` |
| ✅ EXACT | `Action_SecureRecovery` | Punt_Support1 | defense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_LongSnap` | Left_Guard | `9` | `9` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `10` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `11` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `13` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `2` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `5` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `6` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `8` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `9` | `Group` | 0 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Punter | `6` | `6` | 177 | END | 177 | 177 |
| ✅ EXACT | `Action_PuntBall` | Punter | `6` | `6` | 249 | START | 249 | 479 |
| ✅ EXACT | `Action_BlockPunt` | Right_Edge_Rusher1 | `1` | `1` | 255 | START | 255 | 259 |
| ✅ EXACT | `Action_SecureRecovery` | Punt_Support1 | `0` | `0` | 437 | START | 437 | 440 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–49
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_LongSnap` | 0 | 49 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 479 | 480 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 479 | 480 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–457
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 234 | 235 | inferred_complete_timeline |
| `Action_None` | 236 | 404 | 169 | inferred_complete_timeline |
| `Action_None` | 406 | 407 | 2 | inferred_complete_timeline |
| `Action_None` | 411 | 414 | 4 | inferred_complete_timeline |
| `Action_None` | 418 | 439 | 22 | inferred_complete_timeline |
| `Action_None` | 442 | 450 | 9 | inferred_complete_timeline |
| `Action_None` | 456 | 457 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 434 | 435 | inferred_complete_timeline |
| `Action_None` | 436 | 440 | 5 | inferred_complete_timeline |
| `Action_None` | 442 | 479 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 473

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 93 | 339 | 247 | inferred_complete_timeline |
| `Action_None` | 341 | 462 | 122 | inferred_complete_timeline |
| `Action_None` | 465 | 479 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_SnapReceive` | 177 | 177 | 1 | inferred_complete_timeline |
| `Action_None` | 178 | 248 | 71 | inferred_complete_timeline |
| `Action_PuntBall` | 249 | 479 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 254 | 255 | inferred_complete_timeline |
| `Action_None` | 256 | 448 | 193 | inferred_complete_timeline |
| `Action_None` | 450 | 479 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 53 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–18
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 18 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_None` | 212 | 380 | 169 | inferred_complete_timeline |
| `Action_None` | 389 | 438 | 50 | inferred_complete_timeline |
| `Action_None` | 440 | 479 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 277 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 381 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 383 | 384 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 386 | 416 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 418 | 421 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 424 | 436 | 13 | inferred_complete_timeline |
| `Action_SecureRecovery` | 437 | 440 | 4 | inferred_complete_timeline |
| `Action_None` | 453 | 479 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–477
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 352 | 353 | inferred_complete_timeline |
| `Action_None` | 354 | 358 | 5 | inferred_complete_timeline |
| `Action_None` | 361 | 463 | 103 | inferred_complete_timeline |
| `Action_None` | 475 | 477 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 359 | 360 | inferred_complete_timeline |
| `Action_None` | 361 | 407 | 47 | inferred_complete_timeline |
| `Action_None` | 411 | 422 | 12 | inferred_complete_timeline |
| `Action_None` | 426 | 427 | 2 | inferred_complete_timeline |
| `Action_None` | 430 | 440 | 11 | inferred_complete_timeline |
| `Action_None` | 442 | 479 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–407
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 254 | 255 | inferred_complete_timeline |
| `Action_BlockPunt` | 255 | 259 | 5 | inferred_complete_timeline |
| `Action_None` | 260 | 387 | 128 | inferred_complete_timeline |
| `Action_None` | 390 | 407 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 44–199 | 153 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 55–479 | 419 | 5 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 57–479 | 392 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 59–63 | 5 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 60–145 | 79 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 61–479 | 419 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 86–479 | 389 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 88–152 | 62 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 95–221 | 88 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 141–149 | 9 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 167–479 | 306 | 5 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 213–479 | 257 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 220–479 | 249 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 228–479 | 239 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 236–242 | 7 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 281–370 | 13 | 6 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 317–479 | 158 | 4 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 323–479 | 156 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 325–390 | 50 | 5 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 399–400 | 2 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 403–471 | 39 | 6 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 410–421 | 6 | 2 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 445–479 | 35 | 1 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 465–479 | 13 | 2 | Undefined position; Undefined team |
| `39` | `61` | Position_Unknown | Team_Unknown | 470–471 | 2 | 1 | Undefined position; Undefined team |
| `40` | `65` | Position_Unknown | Team_Unknown | 477–479 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 107 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-268] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-277] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-381] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-384] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-416] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-421] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [437-440] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-387] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-407] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-234] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-404] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-414] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-439] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-450] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-209] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-380] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-438] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-352] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-358] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-463] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-477] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-434] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-440] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-248] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [249-479] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-407] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-422] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-440] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-88] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-339] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-462] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [0-49] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-479] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-479] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-18] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-254] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-448] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-196] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-292] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-455] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-139] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-63] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-102] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-133] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-149] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-370] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-389] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-416] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-479] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-434] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-479] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-240] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-479] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-284] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-302] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-479] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-242] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-370] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-326] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-339] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-464] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-479] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-416] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-336] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-390] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-400] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-412] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-429] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-433] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-452] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-461] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-413] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-421] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-479] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-467] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '39' has 1 frames without a visible bounding box.
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

</details>