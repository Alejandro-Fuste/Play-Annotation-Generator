# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_92

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_92`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 148
- **Validation Warnings:** 187
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 134
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `5` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Left_Tackle | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `37` | `30` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `37` | `30` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `42` | `33` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `0` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `1` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `10` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `14` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `2` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `3` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `4` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `5` | `Group` | 0 | START | 0 | 107 |
| ✅ EXACT | `Action_LongSnap` | Left_Tackle | `10` | `10` | 108 | START | 108 | 157 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `2` | `2` | 135 | END | 135 | 135 |
| ✅ EXACT | `Action_PuntBall` | Punter | `2` | `2` | 158 | START | 158 | 170 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `37` | `30` | 262 | START | 262 | 268 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `37` | `30` | 285 | START | 285 | 342 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `42` | `33` | 623 | START | 623 | 629 |

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
- **Visible Frames:** 0–177
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 148 | 41 | inferred_complete_timeline |
| `Action_None` | 156 | 177 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 622

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_LongSnap` | 108 | 157 | 50 | inferred_complete_timeline |
| `Action_None` | 158 | 162 | 5 | inferred_complete_timeline |
| `Action_None` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_None` | 168 | 376 | 209 | inferred_complete_timeline |
| `Action_None` | 379 | 383 | 5 | inferred_complete_timeline |
| `Action_None` | 388 | 629 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 143 | 36 | inferred_complete_timeline |
| `Action_None` | 146 | 173 | 28 | inferred_complete_timeline |
| `Action_None` | 176 | 181 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 624

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 394 | 287 | inferred_complete_timeline |
| `Action_None` | 397 | 399 | 3 | inferred_complete_timeline |
| `Action_None` | 401 | 474 | 74 | inferred_complete_timeline |
| `Action_None` | 478 | 629 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 420 | 313 | inferred_complete_timeline |
| `Action_None` | 422 | 452 | 31 | inferred_complete_timeline |
| `Action_None` | 457 | 476 | 20 | inferred_complete_timeline |
| `Action_None` | 478 | 479 | 2 | inferred_complete_timeline |
| `Action_None` | 484 | 485 | 2 | inferred_complete_timeline |
| `Action_None` | 498 | 500 | 3 | inferred_complete_timeline |
| `Action_None` | 512 | 531 | 20 | inferred_complete_timeline |
| `Action_None` | 534 | 629 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 457 | 350 | inferred_complete_timeline |
| `Action_None` | 460 | 553 | 94 | inferred_complete_timeline |
| `Action_None` | 555 | 629 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–582
- **Visible Samples:** 553

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_SnapReceive` | 135 | 135 | 1 | inferred_complete_timeline |
| `Action_None` | 136 | 157 | 22 | inferred_complete_timeline |
| `Action_PuntBall` | 158 | 170 | 13 | inferred_complete_timeline |
| `Action_None` | 171 | 381 | 211 | inferred_complete_timeline |
| `Action_None` | 384 | 450 | 67 | inferred_complete_timeline |
| `Action_None` | 456 | 556 | 101 | inferred_complete_timeline |
| `Action_None` | 580 | 582 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 320 | 213 | inferred_complete_timeline |
| `Action_None` | 324 | 328 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–415
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 180 | 73 | inferred_complete_timeline |
| `Action_None` | 182 | 198 | 17 | inferred_complete_timeline |
| `Action_None` | 202 | 388 | 187 | inferred_complete_timeline |
| `Action_None` | 413 | 415 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–497
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 141 | 34 | inferred_complete_timeline |
| `Action_None` | 210 | 497 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 168 | 61 | inferred_complete_timeline |
| `Action_None` | 171 | 176 | 6 | inferred_complete_timeline |
| `Action_None` | 181 | 207 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 617

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 168 | 61 | inferred_complete_timeline |
| `Action_None` | 180 | 412 | 233 | inferred_complete_timeline |
| `Action_None` | 415 | 629 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–455
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 129 | 22 | inferred_complete_timeline |
| `Action_None` | 132 | 455 | 324 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 128 | 21 | inferred_complete_timeline |
| `Action_None` | 138 | 141 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 442 | 335 | inferred_complete_timeline |
| `Action_None` | 444 | 629 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 620

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 159 | 52 | inferred_complete_timeline |
| `Action_None` | 164 | 460 | 297 | inferred_complete_timeline |
| `Action_None` | 466 | 467 | 2 | inferred_complete_timeline |
| `Action_None` | 469 | 629 | 161 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–629 | 624 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 133–209 | 77 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 139–142 | 4 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 160–629 | 465 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 160–164 | 5 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 163–620 | 439 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 163–629 | 458 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 171–219 | 49 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 173–204 | 32 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 182–391 | 206 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 205–528 | 320 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 206–233 | 27 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 213–629 | 378 | 6 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 214–629 | 403 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 219–342 | 124 | 4 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 224–629 | 376 | 3 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 292–295 | 4 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 337–629 | 293 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 349–397 | 49 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 361–363 | 3 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 397–401 | 5 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 400–629 | 220 | 5 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 403–629 | 226 | 2 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 426–629 | 195 | 3 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 452–629 | 175 | 2 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 477–478 | 2 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 479–496 | 9 | 2 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 500–629 | 130 | 1 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 543–629 | 86 | 2 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 544–577 | 14 | 3 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 555–573 | 6 | 2 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 574–580 | 6 | 2 | Undefined position; Undefined team |
| `48` | `72` | Position_Unknown | Team_Unknown | 596–629 | 34 | 1 | Undefined position; Undefined team |
| `49` | `73` | Position_Unknown | Team_Unknown | 598–601 | 4 | 1 | Undefined position; Undefined team |
| `50` | `76` | Position_Unknown | Team_Unknown | 602–629 | 28 | 1 | Undefined position; Undefined team |
| `51` | `81` | Position_Unknown | Team_Unknown | 612–613 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 111 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 186: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [108-143] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-173] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-181] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-320] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-328] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-381] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-450] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-556] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-582] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-394] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-399] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-474] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-420] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-452] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-476] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-485] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-500] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-531] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-629] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-148] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-177] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-168] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-412] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-159] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-460] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-467] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-442] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-629] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-376] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-383] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-629] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-141] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-497] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-176] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-273] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-629] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-457] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-553] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-388] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-415] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-455] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-209] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-355] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-629] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-372] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-509] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-609] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-620] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-433] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-629] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-219] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-204] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-330] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-391] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-520] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-528] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-223] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-466] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-482] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-558] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-561] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-581] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-629] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-238] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-465] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [285-342] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-294] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-515] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-397] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-363] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-401] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-427] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-435] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-449] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-456] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-629] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-509] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-433] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-442] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-588] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-485] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-496] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-544] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-629] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-553] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-569] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-577] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-558] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-573] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-577] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-580] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-601] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-629] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-613] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>