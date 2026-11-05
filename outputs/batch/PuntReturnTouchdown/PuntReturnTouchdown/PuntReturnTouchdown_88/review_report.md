# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_88

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_88`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 58
- **Ball Tracks:** 0
- **Action Segments:** 138
- **Validation Warnings:** 202
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 124
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `23` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `23` | `22` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `23` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `0` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `11` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `12` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `3` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `5` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `8` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `9` | `Group` | 0 | START | 0 | 25 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `0` | `0` | 26 | START | 26 | 85 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `5` | `5` | 58 | END | 58 | 58 |
| ✅ EXACT | `Action_PuntBall` | Punter | `5` | `5` | 86 | START | 86 | 102 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `23` | `22` | 188 | START | 188 | 205 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `23` | `22` | 228 | START | 228 | 279 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `23` | `22` | 531 | START | 531 | 539 |

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
- **Visible Frames:** 0–94
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 43 | 18 | inferred_complete_timeline |
| `Action_None` | 55 | 59 | 5 | inferred_complete_timeline |
| `Action_None` | 89 | 94 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 25 | 16 | inferred_complete_timeline |
| `Action_None` | 26 | 40 | 15 | inferred_complete_timeline |
| `Action_None` | 49 | 55 | 7 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 539 | 455 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_LongSnap` | 26 | 85 | 60 | inferred_complete_timeline |
| `Action_None` | 86 | 539 | 454 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 290 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–507
- **Visible Samples:** 489

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 175 | 150 | inferred_complete_timeline |
| `Action_None` | 177 | 340 | 164 | inferred_complete_timeline |
| `Action_None` | 342 | 360 | 19 | inferred_complete_timeline |
| `Action_None` | 368 | 382 | 15 | inferred_complete_timeline |
| `Action_None` | 393 | 507 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–416
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 58 | 1 | inferred_complete_timeline |
| `Action_None` | 59 | 85 | 27 | inferred_complete_timeline |
| `Action_PuntBall` | 86 | 102 | 17 | inferred_complete_timeline |
| `Action_None` | 103 | 368 | 266 | inferred_complete_timeline |
| `Action_None` | 375 | 405 | 31 | inferred_complete_timeline |
| `Action_None` | 413 | 416 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–533
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 533 | 508 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 79 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 134 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 519

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 268 | 243 | inferred_complete_timeline |
| `Action_None` | 273 | 373 | 101 | inferred_complete_timeline |
| `Action_None` | 385 | 387 | 3 | inferred_complete_timeline |
| `Action_None` | 391 | 423 | 33 | inferred_complete_timeline |
| `Action_None` | 427 | 539 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 539 | 514 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–384
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 72 | 47 | inferred_complete_timeline |
| `Action_None` | 85 | 353 | 269 | inferred_complete_timeline |
| `Action_None` | 362 | 363 | 2 | inferred_complete_timeline |
| `Action_None` | 369 | 384 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–482
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 370 | 345 | inferred_complete_timeline |
| `Action_None` | 372 | 456 | 85 | inferred_complete_timeline |
| `Action_None` | 458 | 459 | 2 | inferred_complete_timeline |
| `Action_None` | 476 | 477 | 2 | inferred_complete_timeline |
| `Action_None` | 481 | 482 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 2–486 | 474 | 4 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 26–42 | 17 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 48–539 | 478 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 76–177 | 67 | 7 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 120–123 | 4 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 136–196 | 61 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 149–351 | 189 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 153–539 | 387 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 164–358 | 195 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 164–539 | 374 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 177–293 | 117 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 183–194 | 12 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 190–206 | 17 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 199–211 | 12 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 204–355 | 141 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 215–419 | 204 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 218–265 | 48 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 224–245 | 22 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 231–539 | 308 | 2 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 260–264 | 5 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 261–268 | 8 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 340–512 | 131 | 6 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 360–539 | 180 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 369–461 | 91 | 2 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 372–373 | 2 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 404–534 | 131 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 418–426 | 9 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 420–435 | 16 | 1 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 420–423 | 4 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 425–464 | 14 | 5 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 428–442 | 15 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 434–448 | 13 | 2 | Undefined position; Undefined team |
| `46` | `59` | Position_Unknown | Team_Unknown | 435–455 | 21 | 1 | Undefined position; Undefined team |
| `47` | `60` | Position_Unknown | Team_Unknown | 436–437 | 2 | 1 | Undefined position; Undefined team |
| `48` | `61` | Position_Unknown | Team_Unknown | 436–437 | 2 | 1 | Undefined position; Undefined team |
| `49` | `62` | Position_Unknown | Team_Unknown | 445–539 | 95 | 1 | Undefined position; Undefined team |
| `50` | `66` | Position_Unknown | Team_Unknown | 455–488 | 31 | 2 | Undefined position; Undefined team |
| `51` | `68` | Position_Unknown | Team_Unknown | 460–497 | 37 | 2 | Undefined position; Undefined team |
| `52` | `69` | Position_Unknown | Team_Unknown | 464–501 | 10 | 3 | Undefined position; Undefined team |
| `53` | `70` | Position_Unknown | Team_Unknown | 466–468 | 3 | 1 | Undefined position; Undefined team |
| `54` | `72` | Position_Unknown | Team_Unknown | 473–539 | 67 | 1 | Undefined position; Undefined team |
| `55` | `74` | Position_Unknown | Team_Unknown | 491–521 | 16 | 3 | Undefined position; Undefined team |
| `56` | `75` | Position_Unknown | Team_Unknown | 508–539 | 15 | 4 | Undefined position; Undefined team |
| `57` | `76` | Position_Unknown | Team_Unknown | 535–537 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `23` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 45 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 45 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 90 |
| Missing visible bounding boxes during action | 108 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 178: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [86-539] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-72] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-353] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-384] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-370] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-456] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-482] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-290] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-79] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-368] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-405] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-416] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-175] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-340] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-360] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-382] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-507] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-43] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-59] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-94] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-268] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-373] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-387] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-423] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-533] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-25] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-40] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-55] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-539] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-74] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-475] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-486] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-109] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-146] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-172] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-196] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-332] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-351] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-358] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [228-279] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [282-530] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-293] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-206] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-206] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-341] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-355] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-296] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-419] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-265] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-245] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-268] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-342] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-461] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-469] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-494] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-504] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-512] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-424] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-461] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-534] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-426] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-435] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-423] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-428] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-433] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-437] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-464] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-442] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-437] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-448] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-455] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-437] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-437] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-482] for track '50' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-488] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-494] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-468] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-501] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-468] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-500] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-518] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-509] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-518] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-530] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-537] for track '57' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>