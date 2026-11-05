# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_64

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_64`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 61
- **Ball Tracks:** 0
- **Action Segments:** 146
- **Validation Warnings:** 207
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
- **Inferred Coverage Segments (Action_None):** 133
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `10` | `10` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `10` | `10` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `29` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `29` | `23` |
| ✅ EXACT | `Action_CrossGoalLine` | Interior_Rusher3 | defense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `1` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `10` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `14` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `15` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `3` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `7` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `9` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `3` | `3` | 34 | START | 34 | 90 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `10` | `10` | 61 | END | 61 | 61 |
| ✅ EXACT | `Action_PuntBall` | Punter | `10` | `10` | 91 | START | 91 | 106 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `29` | `23` | 218 | START | 218 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `29` | `23` | 238 | START | 238 | 361 |
| ✅ EXACT | `Action_CrossGoalLine` | Interior_Rusher3 | `16` | `16` | 576 | START | 576 | 581 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 107 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–367
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 75 | 42 | inferred_complete_timeline |
| `Action_None` | 77 | 112 | 36 | inferred_complete_timeline |
| `Action_None` | 122 | 140 | 19 | inferred_complete_timeline |
| `Action_None` | 143 | 359 | 217 | inferred_complete_timeline |
| `Action_None` | 364 | 367 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–565
- **Visible Samples:** 559

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 352 | 319 | inferred_complete_timeline |
| `Action_None` | 354 | 401 | 48 | inferred_complete_timeline |
| `Action_None` | 405 | 407 | 3 | inferred_complete_timeline |
| `Action_None` | 409 | 561 | 153 | inferred_complete_timeline |
| `Action_None` | 564 | 565 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–581
- **Visible Samples:** 572

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_LongSnap` | 34 | 90 | 57 | inferred_complete_timeline |
| `Action_None` | 91 | 453 | 363 | inferred_complete_timeline |
| `Action_None` | 458 | 459 | 2 | inferred_complete_timeline |
| `Action_None` | 461 | 464 | 4 | inferred_complete_timeline |
| `Action_None` | 470 | 581 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 205 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 106 | 73 | inferred_complete_timeline |
| `Action_None` | 108 | 268 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_SnapReceive` | 61 | 61 | 1 | inferred_complete_timeline |
| `Action_None` | 62 | 90 | 29 | inferred_complete_timeline |
| `Action_PuntBall` | 91 | 106 | 16 | inferred_complete_timeline |
| `Action_None` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 173 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 59 | 26 | inferred_complete_timeline |
| `Action_None` | 61 | 146 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 285 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 590

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 234 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 410 | 169 | inferred_complete_timeline |
| `Action_PreSnap` | 412 | 575 | 164 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 576 | 581 | 6 | inferred_complete_timeline |
| `Action_None` | 582 | 599 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–364
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 364 | 331 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 599 | 566 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 65 | 32 | inferred_complete_timeline |
| `Action_None` | 67 | 234 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–16
- **Visible Samples:** 17

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–470
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 355 | 322 | inferred_complete_timeline |
| `Action_None` | 362 | 394 | 33 | inferred_complete_timeline |
| `Action_None` | 399 | 401 | 3 | inferred_complete_timeline |
| `Action_None` | 409 | 446 | 38 | inferred_complete_timeline |
| `Action_None` | 448 | 470 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 577

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 141 | 108 | inferred_complete_timeline |
| `Action_None` | 149 | 218 | 70 | inferred_complete_timeline |
| `Action_None` | 221 | 223 | 3 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_None` | 232 | 234 | 3 | inferred_complete_timeline |
| `Action_None` | 243 | 599 | 357 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–370 | 368 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 48–221 | 174 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 90–599 | 508 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 96–99 | 4 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 105–228 | 124 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 120–599 | 480 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 129–343 | 211 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 137–421 | 283 | 6 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 152–218 | 12 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 176–270 | 83 | 5 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 181–307 | 105 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 218–599 | 380 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 242–244 | 3 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 279–364 | 86 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 292–467 | 176 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 309–338 | 26 | 2 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 329–464 | 136 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 353–363 | 8 | 2 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 368–453 | 80 | 2 | Undefined position; Undefined team |
| `35` | `55` | Position_Unknown | Team_Unknown | 370–390 | 6 | 3 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 372–373 | 2 | 1 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 378–384 | 7 | 1 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 378–445 | 68 | 1 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 404–576 | 171 | 3 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 407–599 | 192 | 2 | Undefined position; Undefined team |
| `41` | `64` | Position_Unknown | Team_Unknown | 417–521 | 105 | 1 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 422–539 | 118 | 1 | Undefined position; Undefined team |
| `43` | `66` | Position_Unknown | Team_Unknown | 428–599 | 169 | 2 | Undefined position; Undefined team |
| `44` | `67` | Position_Unknown | Team_Unknown | 432–458 | 26 | 2 | Undefined position; Undefined team |
| `45` | `68` | Position_Unknown | Team_Unknown | 434–437 | 4 | 1 | Undefined position; Undefined team |
| `46` | `70` | Position_Unknown | Team_Unknown | 462–516 | 43 | 2 | Undefined position; Undefined team |
| `47` | `71` | Position_Unknown | Team_Unknown | 467–512 | 46 | 1 | Undefined position; Undefined team |
| `48` | `72` | Position_Unknown | Team_Unknown | 477–599 | 123 | 1 | Undefined position; Undefined team |
| `49` | `74` | Position_Unknown | Team_Unknown | 511–529 | 18 | 2 | Undefined position; Undefined team |
| `50` | `76` | Position_Unknown | Team_Unknown | 515–533 | 18 | 2 | Undefined position; Undefined team |
| `51` | `79` | Position_Unknown | Team_Unknown | 520–528 | 9 | 1 | Undefined position; Undefined team |
| `52` | `81` | Position_Unknown | Team_Unknown | 524–539 | 12 | 2 | Undefined position; Undefined team |
| `53` | `82` | Position_Unknown | Team_Unknown | 545–548 | 4 | 1 | Undefined position; Undefined team |
| `54` | `83` | Position_Unknown | Team_Unknown | 551–564 | 9 | 2 | Undefined position; Undefined team |
| `55` | `84` | Position_Unknown | Team_Unknown | 557–561 | 5 | 1 | Undefined position; Undefined team |
| `56` | `86` | Position_Unknown | Team_Unknown | 561–599 | 36 | 3 | Undefined position; Undefined team |
| `57` | `89` | Position_Unknown | Team_Unknown | 568–599 | 32 | 1 | Undefined position; Undefined team |
| `58` | `90` | Position_Unknown | Team_Unknown | 570–571 | 2 | 1 | Undefined position; Undefined team |
| `59` | `91` | Position_Unknown | Team_Unknown | 576–579 | 4 | 1 | Undefined position; Undefined team |
| `60` | `92` | Position_Unknown | Team_Unknown | 578–593 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `29` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Jammer3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 45 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 45 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 90 |
| Missing visible bounding boxes during action | 113 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 130: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [34-65] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-234] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-205] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-453] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-464] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-581] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-355] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-394] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-401] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-446] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-470] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-363] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-370] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-141] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-218] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-107] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-364] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-112] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-140] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-359] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-367] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-173] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-59] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-146] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-285] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-268] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-352] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-401] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-407] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-561] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-158] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-234] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-410] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-313] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-599] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-228] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-193] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-316] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-343] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [238-361] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [363-395] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [397-421] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-161] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-203] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-220] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-270] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-281] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-307] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-364] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-467] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-332] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-464] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-357] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-363] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-373] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-453] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-384] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-445] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-562] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-569] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-576] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-491] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-521] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-539] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-589] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-435] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-458] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-437] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-516] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-512] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-515] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-529] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-525] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-533] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-528] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-529] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-539] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-548] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-557] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-564] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-561] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-565] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-589] for track '56' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-599] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-571] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-579] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-593] for track '60' has 3 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>