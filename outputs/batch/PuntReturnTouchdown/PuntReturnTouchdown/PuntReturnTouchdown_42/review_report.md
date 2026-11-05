# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_42

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_42`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 80
- **Ball Tracks:** 0
- **Action Segments:** 267
- **Validation Warnings:** 392
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 2
- **Group Expanded Events:** 3
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 259
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `11` | `11` |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_CatchPunt` | Punt_Returner | defense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Punt_Returner | defense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `11` | `Group` | 16 | START | 16 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `3` | `Group` | 16 | START | 16 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `7` | `Group` | 16 | START | 16 | 22 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `11` | `11` | 23 | START | 23 | 44 |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | `20` | `19` | 54 | END | 55 | 55 |
| ✅ EXACT | `Action_CatchPunt` | Punt_Returner | `0` | `0` | 211 | START | 211 | 230 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Punt_Returner | `0` | `0` | 238 | START | 238 | 309 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Long_Snapper — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 16–317
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 19 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 22 | 1 | inferred_complete_timeline |
| `Action_LongSnap` | 23 | 44 | 22 | inferred_complete_timeline |
| `Action_None` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_None` | 75 | 144 | 70 | inferred_complete_timeline |
| `Action_None` | 159 | 163 | 5 | inferred_complete_timeline |
| `Action_None` | 168 | 174 | 7 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 317 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 16–124
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 22 | 7 | inferred_complete_timeline |
| `Action_None` | 23 | 52 | 30 | inferred_complete_timeline |
| `Action_None` | 54 | 65 | 12 | inferred_complete_timeline |
| `Action_None` | 67 | 120 | 54 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 16–74
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 22 | 7 | inferred_complete_timeline |
| `Action_None` | 23 | 74 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 16–442
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 20 | 5 | inferred_complete_timeline |
| `Action_None` | 35 | 79 | 45 | inferred_complete_timeline |
| `Action_None` | 83 | 260 | 178 | inferred_complete_timeline |
| `Action_None` | 264 | 341 | 78 | inferred_complete_timeline |
| `Action_None` | 355 | 413 | 59 | inferred_complete_timeline |
| `Action_None` | 441 | 442 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 16–237
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 22 | 7 | inferred_complete_timeline |
| `Action_None` | 23 | 237 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 16–374
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 22 | 7 | inferred_complete_timeline |
| `Action_None` | 23 | 107 | 85 | inferred_complete_timeline |
| `Action_None` | 109 | 113 | 5 | inferred_complete_timeline |
| `Action_None` | 148 | 188 | 41 | inferred_complete_timeline |
| `Action_None` | 198 | 374 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 16–599
- **Visible Samples:** 580

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 22 | 7 | inferred_complete_timeline |
| `Action_None` | 23 | 61 | 39 | inferred_complete_timeline |
| `Action_None` | 63 | 405 | 343 | inferred_complete_timeline |
| `Action_None` | 409 | 599 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 16–112
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 22 | 7 | inferred_complete_timeline |
| `Action_None` | 23 | 66 | 44 | inferred_complete_timeline |
| `Action_None` | 74 | 86 | 13 | inferred_complete_timeline |
| `Action_None` | 91 | 104 | 14 | inferred_complete_timeline |
| `Action_None` | 106 | 112 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 16–74
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 22 | 7 | inferred_complete_timeline |
| `Action_None` | 23 | 74 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 16–407
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 22 | 7 | inferred_complete_timeline |
| `Action_None` | 23 | 201 | 179 | inferred_complete_timeline |
| `Action_None` | 205 | 214 | 10 | inferred_complete_timeline |
| `Action_None` | 218 | 398 | 181 | inferred_complete_timeline |
| `Action_None` | 405 | 407 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Returner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 16–599
- **Visible Samples:** 528

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 210 | 195 | inferred_complete_timeline |
| `Action_CatchPunt` | 211 | 230 | 20 | inferred_complete_timeline |
| `Action_None` | 231 | 237 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 238 | 309 | 72 | inferred_complete_timeline |
| `Action_BallCarry` | 343 | 357 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 359 | 387 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 401 | 404 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 407 | 474 | 68 | inferred_complete_timeline |
| `Action_BallCarry` | 482 | 599 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 16–130
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 22 | 7 | inferred_complete_timeline |
| `Action_None` | 23 | 91 | 69 | inferred_complete_timeline |
| `Action_None` | 94 | 108 | 15 | inferred_complete_timeline |
| `Action_None` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_None` | 121 | 130 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 26–70 | 29 | 5 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 38–142 | 100 | 4 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 40–599 | 536 | 6 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 41–87 | 43 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 43–292 | 159 | 4 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 44–68 | 25 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 49–59 | 11 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 55–66 | 12 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 72–108 | 34 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 75–331 | 240 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 75–432 | 300 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 81–364 | 279 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 91–121 | 31 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 98–331 | 194 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 108–179 | 68 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 121–205 | 77 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 127–442 | 248 | 7 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 134–487 | 303 | 12 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 138–599 | 404 | 12 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 144–319 | 169 | 5 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 151–158 | 8 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 159–350 | 173 | 3 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 181–393 | 196 | 5 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 188–325 | 138 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 199–393 | 195 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 220–354 | 135 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 254–592 | 329 | 4 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 309–374 | 66 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 314–315 | 2 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 316–361 | 42 | 3 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 327–360 | 34 | 1 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 334–445 | 112 | 1 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 336–588 | 212 | 8 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 355–423 | 63 | 3 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 365–434 | 61 | 3 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 379–587 | 148 | 10 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 381–568 | 142 | 4 | Undefined position; Undefined team |
| `49` | `68` | Position_Unknown | Team_Unknown | 384–439 | 56 | 1 | Undefined position; Undefined team |
| `50` | `69` | Position_Unknown | Team_Unknown | 395–599 | 124 | 5 | Undefined position; Undefined team |
| `51` | `70` | Position_Unknown | Team_Unknown | 398–401 | 4 | 1 | Undefined position; Undefined team |
| `52` | `71` | Position_Unknown | Team_Unknown | 398–463 | 51 | 4 | Undefined position; Undefined team |
| `53` | `72` | Position_Unknown | Team_Unknown | 402–404 | 3 | 1 | Undefined position; Undefined team |
| `54` | `73` | Position_Unknown | Team_Unknown | 406–414 | 9 | 1 | Undefined position; Undefined team |
| `55` | `74` | Position_Unknown | Team_Unknown | 408–425 | 13 | 2 | Undefined position; Undefined team |
| `56` | `77` | Position_Unknown | Team_Unknown | 423–548 | 93 | 6 | Undefined position; Undefined team |
| `57` | `78` | Position_Unknown | Team_Unknown | 424–494 | 57 | 2 | Undefined position; Undefined team |
| `58` | `79` | Position_Unknown | Team_Unknown | 424–574 | 119 | 5 | Undefined position; Undefined team |
| `59` | `81` | Position_Unknown | Team_Unknown | 432–532 | 83 | 4 | Undefined position; Undefined team |
| `60` | `82` | Position_Unknown | Team_Unknown | 436–593 | 127 | 6 | Undefined position; Undefined team |
| `61` | `83` | Position_Unknown | Team_Unknown | 444–481 | 38 | 1 | Undefined position; Undefined team |
| `62` | `84` | Position_Unknown | Team_Unknown | 447–481 | 35 | 1 | Undefined position; Undefined team |
| `63` | `85` | Position_Unknown | Team_Unknown | 456–588 | 106 | 7 | Undefined position; Undefined team |
| `64` | `87` | Position_Unknown | Team_Unknown | 469–592 | 109 | 2 | Undefined position; Undefined team |
| `65` | `88` | Position_Unknown | Team_Unknown | 481–592 | 104 | 2 | Undefined position; Undefined team |
| `66` | `89` | Position_Unknown | Team_Unknown | 482–599 | 118 | 1 | Undefined position; Undefined team |
| `67` | `91` | Position_Unknown | Team_Unknown | 489–512 | 9 | 3 | Undefined position; Undefined team |
| `68` | `92` | Position_Unknown | Team_Unknown | 489–597 | 21 | 3 | Undefined position; Undefined team |
| `69` | `93` | Position_Unknown | Team_Unknown | 496–599 | 101 | 2 | Undefined position; Undefined team |
| `70` | `94` | Position_Unknown | Team_Unknown | 500–587 | 73 | 4 | Undefined position; Undefined team |
| `71` | `95` | Position_Unknown | Team_Unknown | 512–597 | 86 | 1 | Undefined position; Undefined team |
| `72` | `98` | Position_Unknown | Team_Unknown | 534–545 | 8 | 3 | Undefined position; Undefined team |
| `73` | `100` | Position_Unknown | Team_Unknown | 549–587 | 39 | 1 | Undefined position; Undefined team |
| `74` | `102` | Position_Unknown | Team_Unknown | 550–553 | 4 | 1 | Undefined position; Undefined team |
| `75` | `104` | Position_Unknown | Team_Unknown | 556–557 | 2 | 1 | Undefined position; Undefined team |
| `76` | `105` | Position_Unknown | Team_Unknown | 556–581 | 26 | 1 | Undefined position; Undefined team |
| `77` | `106` | Position_Unknown | Team_Unknown | 560–561 | 2 | 1 | Undefined position; Undefined team |
| `78` | `107` | Position_Unknown | Team_Unknown | 565–566 | 2 | 1 | Undefined position; Undefined team |
| `79` | `108` | Position_Unknown | Team_Unknown | 593–597 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punt_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 68 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 68 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_PuntBall' at frame 78 targets track ID '?', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 136 |
| Missing visible bounding boxes during action | 250 |
| Track-related warning | 3 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 85: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 86: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SnapReceive' for track '19' has invalid range: start=55, end=54. Clamping end to start.
- ⚠️ Action 'Action_BallCarry' range [238-309] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [343-357] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [359-387] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [401-404] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [407-474] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [482-599] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-91] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-108] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-66] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-86] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-104] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-112] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-74] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-214] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-398] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-407] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-74] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-52] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-65] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-120] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-107] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-188] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-374] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-61] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-405] for track '9' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-599] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-20] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-79] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-260] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-341] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-413] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-19] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [23-44] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-51] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-144] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-163] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-317] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-27] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-48] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-67] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-44] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-49] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-134] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-69] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-287] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-414] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-421] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-50] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-125] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-158] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-292] for track '16' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-68] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-59] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-92] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-117] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-141] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-152] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-331] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-260] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-363] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-390] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-237] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-364] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-121] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-133] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-230] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-331] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-170] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-194] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-226] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-379] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-442] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-161] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-188] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-295] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-351] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-399] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-439] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-487] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-145] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-161] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-220] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-293] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-321] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-339] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-369] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-423] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-443] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-492] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-599] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-153] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-163] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-319] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-158] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-229] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-285] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-350] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-221] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-276] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-356] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-393] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-325] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-393] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-354] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-391] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-530] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-548] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-592] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-374] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-345] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-361] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-360] for track '42' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-445] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-381] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-437] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-466] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-471] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-536] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-543] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-547] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-588] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-381] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-392] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-423] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-406] for track '46' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-434] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-434] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-446] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-461] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-491] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-526] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-562] for track '47' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-567] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-587] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-412] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-526] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-559] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-568] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-439] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-397] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-416] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-401] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-402] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-457] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-463] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-404] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-414] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-417] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-425] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-480] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-499] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-513] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-529] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-548] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-470] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-494] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-508] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-532] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-559] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-564] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-574] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-469] for track '59' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-487] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-523] for track '59' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-532] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-466] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-482] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-569] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-593] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-481] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-481] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-481] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-512] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-521] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-525] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-533] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-548] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-588] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-532] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-592] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-516] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-592] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-492] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-512] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-493] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-507] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-597] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-551] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-599] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-546] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-562] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-582] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-587] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-597] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-536] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-545] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-587] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-553] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-557] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-581] for track '76' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-561] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-566] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-597] for track '79' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>