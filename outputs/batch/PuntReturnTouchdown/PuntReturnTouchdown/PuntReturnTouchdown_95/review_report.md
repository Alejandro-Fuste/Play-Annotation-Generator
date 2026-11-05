# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_95

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_95`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 56
- **Ball Tracks:** 0
- **Action Segments:** 189
- **Validation Warnings:** 227
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 173
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `48` | `29` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `48` | `29` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `48` | `29` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `15` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `16` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `17` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `18` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `19` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `20` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `6` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `7` | `Group` | 0 | START | 0 | 65 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `17` | `17` | 39 | START | 39 | 93 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `7` | `7` | 66 | END | 66 | 66 |
| ✅ EXACT | `Action_PuntBall` | Punter | `7` | `7` | 94 | START | 94 | 107 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `48` | `29` | 213 | START | 213 | 223 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `48` | `29` | 230 | START | 230 | 521 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `48` | `29` | 522 | START | 522 | 527 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 67 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 147 | 109 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 519

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 423 | 385 | inferred_complete_timeline |
| `Action_None` | 425 | 462 | 38 | inferred_complete_timeline |
| `Action_None` | 470 | 474 | 5 | inferred_complete_timeline |
| `Action_None` | 477 | 491 | 15 | inferred_complete_timeline |
| `Action_None` | 497 | 499 | 3 | inferred_complete_timeline |
| `Action_None` | 504 | 509 | 6 | inferred_complete_timeline |
| `Action_None` | 512 | 539 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 514

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_LongSnap` | 39 | 93 | 55 | inferred_complete_timeline |
| `Action_None` | 94 | 464 | 371 | inferred_complete_timeline |
| `Action_None` | 468 | 474 | 7 | inferred_complete_timeline |
| `Action_None` | 497 | 531 | 35 | inferred_complete_timeline |
| `Action_None` | 533 | 539 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 150 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–452
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 76 | 38 | inferred_complete_timeline |
| `Action_None` | 94 | 432 | 339 | inferred_complete_timeline |
| `Action_None` | 434 | 437 | 4 | inferred_complete_timeline |
| `Action_None` | 442 | 443 | 2 | inferred_complete_timeline |
| `Action_None` | 451 | 452 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 96 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_SnapReceive` | 66 | 66 | 1 | inferred_complete_timeline |
| `Action_None` | 67 | 93 | 27 | inferred_complete_timeline |
| `Action_PuntBall` | 94 | 107 | 14 | inferred_complete_timeline |
| `Action_None` | 108 | 140 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 144 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 61 | 23 | inferred_complete_timeline |
| `Action_None` | 66 | 204 | 139 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–438
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 438 | 400 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 438 | 400 | inferred_complete_timeline |
| `Action_None` | 440 | 442 | 3 | inferred_complete_timeline |
| `Action_None` | 447 | 448 | 2 | inferred_complete_timeline |
| `Action_None` | 450 | 462 | 13 | inferred_complete_timeline |
| `Action_None` | 465 | 467 | 3 | inferred_complete_timeline |
| `Action_None` | 469 | 539 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 153 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–425
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 425 | 387 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 68 | 30 | inferred_complete_timeline |
| `Action_None` | 81 | 91 | 11 | inferred_complete_timeline |
| `Action_None` | 96 | 98 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 90 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–423
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 423 | 385 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–428
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 106 | 68 | inferred_complete_timeline |
| `Action_None` | 108 | 428 | 321 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–539 | 517 | 12 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–539 | 504 | 8 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–539 | 523 | 8 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 36–76 | 15 | 4 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 77–122 | 11 | 3 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 78–82 | 5 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 87–88 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 95–149 | 54 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 101–539 | 432 | 5 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 130–439 | 306 | 5 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 131–195 | 37 | 6 | Undefined position; Undefined team |
| `29` | `48` | Position_Unknown | Team_Unknown | 147–539 | 393 | 6 | Undefined position; Undefined team |
| `30` | `49` | Position_Unknown | Team_Unknown | 147–539 | 337 | 2 | Undefined position; Undefined team |
| `31` | `51` | Position_Unknown | Team_Unknown | 167–526 | 356 | 4 | Undefined position; Undefined team |
| `32` | `54` | Position_Unknown | Team_Unknown | 223–539 | 317 | 1 | Undefined position; Undefined team |
| `33` | `59` | Position_Unknown | Team_Unknown | 262–263 | 2 | 1 | Undefined position; Undefined team |
| `34` | `60` | Position_Unknown | Team_Unknown | 270–539 | 262 | 3 | Undefined position; Undefined team |
| `35` | `62` | Position_Unknown | Team_Unknown | 295–313 | 8 | 3 | Undefined position; Undefined team |
| `36` | `63` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `37` | `65` | Position_Unknown | Team_Unknown | 314–526 | 158 | 11 | Undefined position; Undefined team |
| `38` | `68` | Position_Unknown | Team_Unknown | 340–421 | 75 | 4 | Undefined position; Undefined team |
| `39` | `69` | Position_Unknown | Team_Unknown | 344–347 | 4 | 1 | Undefined position; Undefined team |
| `40` | `72` | Position_Unknown | Team_Unknown | 347–539 | 144 | 7 | Undefined position; Undefined team |
| `41` | `73` | Position_Unknown | Team_Unknown | 347–414 | 68 | 1 | Undefined position; Undefined team |
| `42` | `74` | Position_Unknown | Team_Unknown | 347–388 | 6 | 3 | Undefined position; Undefined team |
| `43` | `80` | Position_Unknown | Team_Unknown | 423–424 | 2 | 1 | Undefined position; Undefined team |
| `44` | `81` | Position_Unknown | Team_Unknown | 424–429 | 6 | 1 | Undefined position; Undefined team |
| `45` | `83` | Position_Unknown | Team_Unknown | 430–431 | 2 | 1 | Undefined position; Undefined team |
| `46` | `84` | Position_Unknown | Team_Unknown | 438–539 | 100 | 2 | Undefined position; Undefined team |
| `47` | `86` | Position_Unknown | Team_Unknown | 444–463 | 20 | 1 | Undefined position; Undefined team |
| `48` | `89` | Position_Unknown | Team_Unknown | 467–468 | 2 | 1 | Undefined position; Undefined team |
| `49` | `91` | Position_Unknown | Team_Unknown | 483–539 | 54 | 3 | Undefined position; Undefined team |
| `50` | `95` | Position_Unknown | Team_Unknown | 498–539 | 40 | 3 | Undefined position; Undefined team |
| `51` | `96` | Position_Unknown | Team_Unknown | 499–539 | 28 | 3 | Undefined position; Undefined team |
| `52` | `98` | Position_Unknown | Team_Unknown | 506–507 | 2 | 1 | Undefined position; Undefined team |
| `53` | `103` | Position_Unknown | Team_Unknown | 516–539 | 24 | 1 | Undefined position; Undefined team |
| `54` | `104` | Position_Unknown | Team_Unknown | 516–522 | 7 | 1 | Undefined position; Undefined team |
| `55` | `106` | Position_Unknown | Team_Unknown | 521–539 | 17 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `48` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Guard` position mapped to `offense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 147 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 192: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [39-147] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-83] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-404] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-439] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-446] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-452] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-458] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-469] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-494] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-511] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-517] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-89] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-97] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-105] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-447] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-502] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-423] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-100] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-187] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-440] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-510] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-519] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-530] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-438] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-442] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-462] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-467] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-539] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-96] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-438] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-153] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-91] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-106] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-428] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-425] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-67] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-423] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-462] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-474] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-491] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-499] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-509] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-539] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [39-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-464] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-474] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-531] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-204] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-432] for track '19' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-437] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-452] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-144] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-49] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-82] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-149] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-452] for track '26' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-459] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-468] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-503] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-225] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-402] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-411] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-439] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-146] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-195] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [230-521] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-438] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-231] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-509] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-513] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-526] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-510] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-516] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-539] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-298] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-423] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-430] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-435] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-438] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-454] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-458] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-485] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-511] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-518] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-526] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-400] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-410] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-421] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-347] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-368] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-445] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-452] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-485] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-531] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-414] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-429] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-516] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-463] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-468] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-496] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-510] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-539] for track '49' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-523] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-533] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-526] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-507] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-522] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-527] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>