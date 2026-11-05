# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_80

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_80`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 54
- **Ball Tracks:** 0
- **Action Segments:** 167
- **Validation Warnings:** 214
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 150
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Interior_Rusher3 | defense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `16` | `16` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `16` | `16` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `30` | `26` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `30` | `26` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `30` | `26` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `11` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `12` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `15` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `16` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `2` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `5` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `7` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `8` | `Group` | 0 | START | 0 | 69 |
| ✅ EXACT | `Action_LongSnap` | Interior_Rusher3 | `4` | `4` | 70 | START | 70 | 119 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `16` | `16` | 100 | END | 100 | 100 |
| ✅ EXACT | `Action_PuntBall` | Punter | `16` | `16` | 120 | START | 120 | 134 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `30` | `26` | 242 | START | 242 | 264 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `30` | `26` | 265 | START | 265 | 610 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `30` | `26` | 611 | START | 611 | 616 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 612

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 97 | 28 | inferred_complete_timeline |
| `Action_None` | 106 | 108 | 3 | inferred_complete_timeline |
| `Action_None` | 110 | 138 | 29 | inferred_complete_timeline |
| `Action_None` | 143 | 224 | 82 | inferred_complete_timeline |
| `Action_None` | 227 | 230 | 4 | inferred_complete_timeline |
| `Action_None` | 233 | 347 | 115 | inferred_complete_timeline |
| `Action_None` | 349 | 629 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 90 | 21 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 34 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–525
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 337 | 268 | inferred_complete_timeline |
| `Action_None` | 339 | 525 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 629 | 560 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–308
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 7 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 99 | 84 | inferred_complete_timeline |
| `Action_SnapReceive` | 100 | 100 | 1 | inferred_complete_timeline |
| `Action_None` | 101 | 119 | 19 | inferred_complete_timeline |
| `Action_PuntBall` | 120 | 134 | 15 | inferred_complete_timeline |
| `Action_None` | 135 | 176 | 42 | inferred_complete_timeline |
| `Action_None` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_None` | 184 | 207 | 24 | inferred_complete_timeline |
| `Action_None` | 217 | 245 | 29 | inferred_complete_timeline |
| `Action_None` | 247 | 293 | 47 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 127 | 58 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 610

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 94 | 25 | inferred_complete_timeline |
| `Action_None` | 106 | 120 | 15 | inferred_complete_timeline |
| `Action_None` | 128 | 492 | 365 | inferred_complete_timeline |
| `Action_None` | 495 | 629 | 135 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 223 | 154 | inferred_complete_timeline |
| `Action_None` | 226 | 245 | 20 | inferred_complete_timeline |
| `Action_None` | 248 | 250 | 3 | inferred_complete_timeline |
| `Action_None` | 252 | 327 | 76 | inferred_complete_timeline |
| `Action_None` | 332 | 333 | 2 | inferred_complete_timeline |
| `Action_None` | 340 | 344 | 5 | inferred_complete_timeline |
| `Action_None` | 353 | 365 | 13 | inferred_complete_timeline |
| `Action_None` | 368 | 470 | 103 | inferred_complete_timeline |
| `Action_None` | 473 | 570 | 98 | inferred_complete_timeline |
| `Action_None` | 576 | 578 | 3 | inferred_complete_timeline |
| `Action_None` | 583 | 629 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 581

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 137 | 68 | inferred_complete_timeline |
| `Action_None` | 174 | 187 | 14 | inferred_complete_timeline |
| `Action_None` | 190 | 530 | 341 | inferred_complete_timeline |
| `Action_None` | 542 | 629 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_LongSnap` | 70 | 119 | 50 | inferred_complete_timeline |
| `Action_None` | 120 | 176 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–344
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 109 | 40 | inferred_complete_timeline |
| `Action_None` | 119 | 154 | 36 | inferred_complete_timeline |
| `Action_None` | 159 | 344 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 617

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 189 | 120 | inferred_complete_timeline |
| `Action_None` | 191 | 475 | 285 | inferred_complete_timeline |
| `Action_None` | 480 | 517 | 38 | inferred_complete_timeline |
| `Action_None` | 522 | 579 | 58 | inferred_complete_timeline |
| `Action_None` | 581 | 614 | 34 | inferred_complete_timeline |
| `Action_None` | 618 | 629 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–390
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 390 | 321 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 619

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 132 | 63 | inferred_complete_timeline |
| `Action_None` | 135 | 143 | 9 | inferred_complete_timeline |
| `Action_None` | 145 | 179 | 35 | inferred_complete_timeline |
| `Action_None` | 184 | 303 | 120 | inferred_complete_timeline |
| `Action_None` | 307 | 403 | 97 | inferred_complete_timeline |
| `Action_None` | 405 | 629 | 225 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–629 | 630 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–207 | 199 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 23–275 | 236 | 7 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 105–226 | 119 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 117–141 | 25 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 127–159 | 30 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 135–518 | 381 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 136–362 | 227 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 137–143 | 7 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 145–571 | 412 | 5 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 152–629 | 478 | 5 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 156–629 | 448 | 7 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 158–193 | 26 | 6 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 165–439 | 275 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 171–196 | 19 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 190–422 | 232 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 216–249 | 34 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 246–317 | 72 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 260–629 | 354 | 2 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 280–399 | 118 | 2 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 320–321 | 2 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 344–385 | 42 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 346–488 | 141 | 2 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 351–629 | 267 | 4 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 366–629 | 262 | 2 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 379–544 | 149 | 2 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 394–397 | 4 | 1 | Undefined position; Undefined team |
| `44` | `66` | Position_Unknown | Team_Unknown | 420–430 | 8 | 2 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 424–425 | 2 | 1 | Undefined position; Undefined team |
| `46` | `69` | Position_Unknown | Team_Unknown | 451–452 | 2 | 1 | Undefined position; Undefined team |
| `47` | `70` | Position_Unknown | Team_Unknown | 501–596 | 96 | 1 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 571–590 | 19 | 2 | Undefined position; Undefined team |
| `49` | `72` | Position_Unknown | Team_Unknown | 574–629 | 51 | 2 | Undefined position; Undefined team |
| `50` | `73` | Position_Unknown | Team_Unknown | 575–629 | 55 | 1 | Undefined position; Undefined team |
| `51` | `74` | Position_Unknown | Team_Unknown | 578–629 | 52 | 1 | Undefined position; Undefined team |
| `52` | `75` | Position_Unknown | Team_Unknown | 585–598 | 10 | 2 | Undefined position; Undefined team |
| `53` | `76` | Position_Unknown | Team_Unknown | 590–629 | 35 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `30` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Punter` position mapped to `offense` team
- ⚠️ 39 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 39 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 78 |
| Missing visible bounding boxes during action | 132 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 162: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [70-189] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-475] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-517] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-579] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-614] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-223] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-245] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-327] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-344] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-365] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-470] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-570] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-578] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-127] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-629] for track '3' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-176] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-97] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-138] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-224] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-347] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-629] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-109] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-154] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-344] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-337] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-525] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-90] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-137] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-530] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-179] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-303] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-403] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-94] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-492] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-629] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-390] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-207] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-7] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-176] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-207] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-245] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-293] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-69] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-99] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-120] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-170] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-275] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-182] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-141] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-143] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-518] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-362] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-453] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-500] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-555] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-571] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-183] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-193] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-225] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-254] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-309] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-163] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-177] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-187] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-439] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-216] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-422] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-317] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-418] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-629] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-349] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-399] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-385] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-483] for track '39' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-488] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-511] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-526] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-534] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-629] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-456] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-383] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-544] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-397] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-423] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-430] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-452] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-596] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-572] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-590] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-606] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-590] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-598] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-602] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-617] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>