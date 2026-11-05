# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_20

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_20`
- **Frame Range:** 0 to 719 (720 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 719
- **Player Tracks:** 69
- **Ball Tracks:** 0
- **Action Segments:** 259
- **Validation Warnings:** 356
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 2
- **Group Expanded Events:** 4
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 244
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Personal_Protector2 | offense | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `37` | `31` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `37` | `31` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `37` | `31` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `11` | `Group` | 0 | START | 2 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `2` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `7` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `9` | `Group` | 0 | START | 0 | 14 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Personal_Protector2 | `11` | `11` | 211 | START | 211 | 239 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Punter | `9` | `9` | 241 | END | N/A | N/A |
| ✅ EXACT | `Action_PuntBall` | Punter | `9` | `9` | 268 | START | 268 | 277 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `37` | `31` | 391 | START | 391 | 401 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `37` | `31` | 417 | START | 417 | 419 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `37` | `31` | 711 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Personal_Protector1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–541
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 506 | 296 | inferred_complete_timeline |
| `Action_None` | 510 | 536 | 27 | inferred_complete_timeline |
| `Action_None` | 540 | 541 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 2–577
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 47 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 210 | 156 | inferred_complete_timeline |
| `Action_LongSnap` | 211 | 239 | 29 | inferred_complete_timeline |
| `Action_LongSnap` | 246 | 267 | 22 | inferred_complete_timeline |
| `Action_None` | 268 | 396 | 129 | inferred_complete_timeline |
| `Action_None` | 402 | 577 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–300
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 300 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 22 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 36 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 162 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 226 | 42 | inferred_complete_timeline |
| `Action_None` | 246 | 267 | 22 | inferred_complete_timeline |
| `Action_PuntBall` | 268 | 277 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 269 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–686
- **Visible Samples:** 645

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 357 | 147 | inferred_complete_timeline |
| `Action_None` | 359 | 417 | 59 | inferred_complete_timeline |
| `Action_None` | 424 | 428 | 5 | inferred_complete_timeline |
| `Action_None` | 430 | 431 | 2 | inferred_complete_timeline |
| `Action_None` | 435 | 536 | 102 | inferred_complete_timeline |
| `Action_None` | 555 | 562 | 8 | inferred_complete_timeline |
| `Action_None` | 564 | 568 | 5 | inferred_complete_timeline |
| `Action_None` | 581 | 686 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–349
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 282 | 72 | inferred_complete_timeline |
| `Action_None` | 288 | 309 | 22 | inferred_complete_timeline |
| `Action_None` | 342 | 345 | 4 | inferred_complete_timeline |
| `Action_None` | 348 | 349 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–719
- **Visible Samples:** 680

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 300 | 90 | inferred_complete_timeline |
| `Action_None` | 304 | 318 | 15 | inferred_complete_timeline |
| `Action_None` | 320 | 327 | 8 | inferred_complete_timeline |
| `Action_None` | 335 | 336 | 2 | inferred_complete_timeline |
| `Action_None` | 338 | 341 | 4 | inferred_complete_timeline |
| `Action_None` | 345 | 431 | 87 | inferred_complete_timeline |
| `Action_None` | 435 | 437 | 3 | inferred_complete_timeline |
| `Action_None` | 447 | 450 | 4 | inferred_complete_timeline |
| `Action_None` | 455 | 457 | 3 | inferred_complete_timeline |
| `Action_None` | 461 | 539 | 79 | inferred_complete_timeline |
| `Action_None` | 545 | 693 | 149 | inferred_complete_timeline |
| `Action_None` | 695 | 719 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–375
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 210 | 53 | inferred_complete_timeline |
| `Action_None` | 211 | 277 | 67 | inferred_complete_timeline |
| `Action_None` | 309 | 320 | 12 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |
| `Action_None` | 340 | 344 | 5 | inferred_complete_timeline |
| `Action_None` | 349 | 353 | 5 | inferred_complete_timeline |
| `Action_None` | 374 | 375 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–377
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 107 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 126 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 137 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 210 | 71 | inferred_complete_timeline |
| `Action_None` | 211 | 283 | 73 | inferred_complete_timeline |
| `Action_None` | 285 | 371 | 87 | inferred_complete_timeline |
| `Action_None` | 374 | 377 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–572 | 556 | 9 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–255 | 241 | 6 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 10–30 | 21 | 1 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 11–114 | 38 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 18–22 | 5 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 31–100 | 70 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 38–434 | 391 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 41–252 | 212 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 160–271 | 53 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 227–231 | 5 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 237–259 | 23 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 240–266 | 27 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 241–243 | 3 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 249–250 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 257–267 | 11 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 270–273 | 4 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 272–716 | 429 | 7 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 274–719 | 316 | 16 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 278–444 | 154 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 286–305 | 13 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 286–674 | 345 | 10 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 295–537 | 242 | 5 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 299–599 | 264 | 10 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 306–351 | 41 | 4 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 306–315 | 10 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 306–316 | 7 | 2 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 311–719 | 393 | 5 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 324–346 | 10 | 4 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 326–386 | 60 | 2 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 328–348 | 21 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 331–578 | 242 | 3 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 331–438 | 108 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 355–538 | 175 | 4 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 355–364 | 10 | 1 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 356–405 | 44 | 3 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 357–361 | 5 | 1 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 376–645 | 242 | 4 | Undefined position; Undefined team |
| `47` | `56` | Position_Unknown | Team_Unknown | 381–719 | 305 | 5 | Undefined position; Undefined team |
| `48` | `59` | Position_Unknown | Team_Unknown | 393–472 | 80 | 1 | Undefined position; Undefined team |
| `49` | `60` | Position_Unknown | Team_Unknown | 403–556 | 152 | 3 | Undefined position; Undefined team |
| `50` | `61` | Position_Unknown | Team_Unknown | 417–719 | 293 | 4 | Undefined position; Undefined team |
| `51` | `62` | Position_Unknown | Team_Unknown | 435–689 | 162 | 6 | Undefined position; Undefined team |
| `52` | `63` | Position_Unknown | Team_Unknown | 445–717 | 266 | 5 | Undefined position; Undefined team |
| `53` | `64` | Position_Unknown | Team_Unknown | 464–719 | 249 | 3 | Undefined position; Undefined team |
| `54` | `65` | Position_Unknown | Team_Unknown | 470–719 | 235 | 7 | Undefined position; Undefined team |
| `55` | `69` | Position_Unknown | Team_Unknown | 493–719 | 195 | 9 | Undefined position; Undefined team |
| `56` | `70` | Position_Unknown | Team_Unknown | 506–719 | 171 | 6 | Undefined position; Undefined team |
| `57` | `72` | Position_Unknown | Team_Unknown | 550–634 | 85 | 1 | Undefined position; Undefined team |
| `58` | `73` | Position_Unknown | Team_Unknown | 558–622 | 65 | 1 | Undefined position; Undefined team |
| `59` | `74` | Position_Unknown | Team_Unknown | 576–624 | 49 | 1 | Undefined position; Undefined team |
| `60` | `77` | Position_Unknown | Team_Unknown | 597–682 | 86 | 1 | Undefined position; Undefined team |
| `61` | `78` | Position_Unknown | Team_Unknown | 616–690 | 68 | 4 | Undefined position; Undefined team |
| `62` | `80` | Position_Unknown | Team_Unknown | 669–682 | 13 | 2 | Undefined position; Undefined team |
| `63` | `83` | Position_Unknown | Team_Unknown | 688–719 | 26 | 4 | Undefined position; Undefined team |
| `64` | `84` | Position_Unknown | Team_Unknown | 700–703 | 4 | 1 | Undefined position; Undefined team |
| `65` | `86` | Position_Unknown | Team_Unknown | 703–717 | 15 | 1 | Undefined position; Undefined team |
| `66` | `87` | Position_Unknown | Team_Unknown | 706–709 | 4 | 1 | Undefined position; Undefined team |
| `67` | `88` | Position_Unknown | Team_Unknown | 707–715 | 9 | 1 | Undefined position; Undefined team |
| `68` | `89` | Position_Unknown | Team_Unknown | 711–719 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `11` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `9` (Punter)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `37` (2 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `37` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Edge_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Edge_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ 59 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 59 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 118 |
| Missing visible bounding boxes during action | 233 |
| Track-related warning | 2 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 41: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 719 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_CrossGoalLine' for track '31' has invalid range: start=711, end=537. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-277] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-320] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-344] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-353] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-305] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-369] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-385] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-404] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-505] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-550] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-572] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-506] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-536] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-541] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-357] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-417] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-428] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-536] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-562] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-568] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-686] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-282] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-309] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-345] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-300] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-318] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-327] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-341] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-431] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-437] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-450] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-457] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-539] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-693] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-99] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-105] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-255] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-300] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-22] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-26] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-36] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-226] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [268-277] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-107] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-126] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-283] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-371] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-377] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [211-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-396] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-577] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-30] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-29] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-22] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-422] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-434] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-252] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-271] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-231] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-259] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-266] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-267] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-287] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-336] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-449] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-458] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-463] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-709] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [711-716] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-320] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-343] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-371] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-405] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-430] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-441] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-450] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-541] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-564] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-572] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-701] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [704-713] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-305] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-409] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-444] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-291] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-296] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-290] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-296] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-348] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-402] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-548] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-552] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-605] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-623] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-630] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [636-674] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [417-419] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [421-537] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-356] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-366] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-376] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-425] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-443] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-539] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-548] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-599] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-325] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-341] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-315] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-310] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-345] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-506] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-582] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-334] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-341] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-362] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-386] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-348] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-493] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-499] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-578] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-438] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-388] for track '42' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-419] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-538] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-364] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-360] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-375] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-405] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-361] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-542] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-556] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-629] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [640-645] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-417] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-525] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-566] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-632] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-719] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-472] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-417] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-543] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-556] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-466] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-491] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-682] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-450] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-483] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-565] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-573] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-614] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-689] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-453] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-466] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-570] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-577] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-717] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-563] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-507] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-525] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-532] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-572] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-579] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-698] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-495] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-526] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-544] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-560] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-578] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-626] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-630] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-713] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-534] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-556] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-579] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-606] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-649] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-634] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-622] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-624] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-682] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-623] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-640] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [645-682] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [685-690] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [669-671] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [673-682] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [688-693] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [696-697] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [700-701] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [700-703] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [703-717] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [706-709] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [707-715] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>