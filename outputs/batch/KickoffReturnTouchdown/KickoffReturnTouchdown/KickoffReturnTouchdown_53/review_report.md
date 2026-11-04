# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_53

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_53`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 166
- **Validation Warnings:** 185
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 151
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `8` | `8` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `8` | `8` |
| ⚠️ START CHANGED | `Action_CatchKick` | Position_Unknown | Team_Unknown | `41` | `29` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `41` | `29` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `41` | `29` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `10` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `13` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `14` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `15` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `16` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `3` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `5` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `6` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `8` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `9` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `8` | `8` | 15 | START | 15 | 85 |
| ✅ EXACT | `Action_KickBall` | Kicker | `8` | `8` | 86 | START | 86 | 92 |
| ⚠️ START CHANGED | `Action_CatchKick` | Position_Unknown | `41` | `29` | 201 | START | 246 | 246 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `41` | `29` | 248 | START | 248 | 368 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `41` | `29` | 621 | START | 621 | 629 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_KickApproach` | 15 | 85 | 71 | inferred_complete_timeline |
| `Action_KickBall` | 86 | 92 | 7 | inferred_complete_timeline |
| `Action_None` | 93 | 105 | 13 | inferred_complete_timeline |
| `Action_None` | 107 | 234 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 607

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 164 | 150 | inferred_complete_timeline |
| `Action_None` | 167 | 454 | 288 | inferred_complete_timeline |
| `Action_None` | 457 | 458 | 2 | inferred_complete_timeline |
| `Action_None` | 468 | 470 | 3 | inferred_complete_timeline |
| `Action_None` | 481 | 629 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 80 | 66 | inferred_complete_timeline |
| `Action_None` | 82 | 89 | 8 | inferred_complete_timeline |
| `Action_None` | 93 | 95 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–625
- **Visible Samples:** 617

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 566 | 552 | inferred_complete_timeline |
| `Action_None` | 569 | 571 | 3 | inferred_complete_timeline |
| `Action_None` | 578 | 579 | 2 | inferred_complete_timeline |
| `Action_None` | 581 | 625 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 629 | 615 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 233 | 219 | inferred_complete_timeline |
| `Action_None` | 240 | 399 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 604

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 56 | 42 | inferred_complete_timeline |
| `Action_None` | 58 | 82 | 25 | inferred_complete_timeline |
| `Action_None` | 84 | 92 | 9 | inferred_complete_timeline |
| `Action_None` | 96 | 100 | 5 | inferred_complete_timeline |
| `Action_None` | 103 | 107 | 5 | inferred_complete_timeline |
| `Action_None` | 109 | 241 | 133 | inferred_complete_timeline |
| `Action_None` | 248 | 266 | 19 | inferred_complete_timeline |
| `Action_None` | 268 | 272 | 5 | inferred_complete_timeline |
| `Action_None` | 275 | 341 | 67 | inferred_complete_timeline |
| `Action_None` | 346 | 371 | 26 | inferred_complete_timeline |
| `Action_None` | 373 | 488 | 116 | inferred_complete_timeline |
| `Action_None` | 492 | 563 | 72 | inferred_complete_timeline |
| `Action_None` | 565 | 629 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 80 | 66 | inferred_complete_timeline |
| `Action_None` | 83 | 88 | 6 | inferred_complete_timeline |
| `Action_None` | 90 | 181 | 92 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 71 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 79 | 65 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_None` | 93 | 174 | 82 | inferred_complete_timeline |
| `Action_None` | 176 | 429 | 254 | inferred_complete_timeline |
| `Action_None` | 432 | 449 | 18 | inferred_complete_timeline |
| `Action_None` | 466 | 471 | 6 | inferred_complete_timeline |
| `Action_None` | 476 | 478 | 3 | inferred_complete_timeline |
| `Action_None` | 481 | 627 | 147 | inferred_complete_timeline |
| `Action_None` | 629 | 629 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 626

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 457 | 443 | inferred_complete_timeline |
| `Action_None` | 462 | 629 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 192 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–627
- **Visible Samples:** 605

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 242 | 228 | inferred_complete_timeline |
| `Action_None` | 253 | 507 | 255 | inferred_complete_timeline |
| `Action_None` | 514 | 563 | 50 | inferred_complete_timeline |
| `Action_None` | 571 | 627 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–375
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 183 | 169 | inferred_complete_timeline |
| `Action_None` | 185 | 224 | 40 | inferred_complete_timeline |
| `Action_None` | 226 | 231 | 6 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_None` | 240 | 249 | 10 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 264 | 268 | 5 | inferred_complete_timeline |
| `Action_None` | 270 | 275 | 6 | inferred_complete_timeline |
| `Action_None` | 277 | 297 | 21 | inferred_complete_timeline |
| `Action_None` | 300 | 375 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 606

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 220 | 206 | inferred_complete_timeline |
| `Action_None` | 224 | 228 | 5 | inferred_complete_timeline |
| `Action_None` | 232 | 403 | 172 | inferred_complete_timeline |
| `Action_None` | 405 | 464 | 60 | inferred_complete_timeline |
| `Action_None` | 466 | 470 | 5 | inferred_complete_timeline |
| `Action_None` | 476 | 482 | 7 | inferred_complete_timeline |
| `Action_None` | 494 | 629 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–627
- **Visible Samples:** 625

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 240 | 226 | inferred_complete_timeline |
| `Action_None` | 243 | 354 | 112 | inferred_complete_timeline |
| `Action_None` | 356 | 627 | 272 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–629 | 611 | 5 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 11–264 | 253 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 33–627 | 552 | 8 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 55–75 | 17 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 85–86 | 2 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 94–416 | 285 | 8 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 103–609 | 481 | 6 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 110–627 | 504 | 3 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 115–116 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 188–189 | 2 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 203–594 | 363 | 4 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 211–279 | 59 | 3 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 213–426 | 175 | 6 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 246–629 | 354 | 8 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 261–262 | 2 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 265–629 | 362 | 4 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 283–629 | 347 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 330–522 | 193 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 431–629 | 192 | 5 | Undefined position; Undefined team |
| `35` | `55` | Position_Unknown | Team_Unknown | 465–629 | 165 | 1 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 504–505 | 2 | 1 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 524–629 | 106 | 1 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 532–629 | 98 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_CatchKick` for actor_track_id `41` (Position_Unknown): Annotated start 201 != Inferred start 246
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `41` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 136 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 108: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Segment 'Action_CatchKick' for track '29' has invalid range: start=246, end=211. Clamping end to start.
- ⚠️ Action 'Action_None' range [15-220] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-403] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-464] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-470] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-482] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-629] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-240] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-354] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-627] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-457] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-71] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-192] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-566] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-571] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-579] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-625] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-79] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-174] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-429] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-449] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-471] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-478] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-627] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-183] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-249] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-275] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-297] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-375] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-105] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-234] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-233] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-399] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-181] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-91] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-198] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-253] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-629] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-242] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-507] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-563] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-627] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-629] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-82] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-92] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-107] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-241] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-266] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-272] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-341] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-371] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-488] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-563] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-629] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-89] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-164] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-454] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-458] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-470] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-629] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-21] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-264] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-309] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-364] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-429] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-491] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-496] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-536] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-621] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-627] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-58] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-67] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-183] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-202] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-218] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-232] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-387] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-330] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-508] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-603] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-609] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-614] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-627] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-223] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-520] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-545] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-594] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-270] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-250] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-288] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-412] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-419] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-426] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [248-368] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [370-441] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [447-454] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [476-477] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [481-620] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-308] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-522] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-453] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-456] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-464] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-474] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-629] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-505] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>