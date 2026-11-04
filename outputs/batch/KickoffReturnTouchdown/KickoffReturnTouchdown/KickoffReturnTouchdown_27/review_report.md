# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_27

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_27`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 182
- **Validation Warnings:** 212
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 170
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `5` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `5` | `5` |
| ❌ MISSING SEGMENT | `Action_KickBall` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | defense | `6` | `6` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `12` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `13` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `15` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `16` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `4` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `5` | `Group` | 0 | START | 0 | 38 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `5` | `5` | 39 | START | 39 | 97 |
| ❌ MISSING SEGMENT | `Action_KickBall` | Kicker | `5` | `5` | 98 | START | N/A | N/A |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `6` | `6` | 211 | START | 211 | 225 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | `6` | `6` | 236 | START | 236 | 323 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | `6` | `6` | 595 | START | 595 | 599 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_KickApproach` | 39 | 97 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 138 | 100 | inferred_complete_timeline |
| `Action_None` | 140 | 599 | 460 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 19 | 2 | inferred_complete_timeline |
| `Action_None` | 54 | 58 | 5 | inferred_complete_timeline |
| `Action_None` | 60 | 64 | 5 | inferred_complete_timeline |
| `Action_None` | 72 | 229 | 158 | inferred_complete_timeline |
| `Action_None` | 235 | 299 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 38 | 30 | inferred_complete_timeline |
| `Action_None` | 39 | 47 | 9 | inferred_complete_timeline |
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_None` | 53 | 77 | 25 | inferred_complete_timeline |
| `Action_None` | 81 | 97 | 17 | inferred_complete_timeline |
| `Action_None` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_None` | 118 | 360 | 243 | inferred_complete_timeline |
| `Action_None` | 363 | 364 | 2 | inferred_complete_timeline |
| `Action_None` | 367 | 427 | 61 | inferred_complete_timeline |
| `Action_None` | 429 | 599 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 579

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 79 | 41 | inferred_complete_timeline |
| `Action_None` | 81 | 101 | 21 | inferred_complete_timeline |
| `Action_None` | 107 | 182 | 76 | inferred_complete_timeline |
| `Action_None` | 184 | 222 | 39 | inferred_complete_timeline |
| `Action_None` | 224 | 238 | 15 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 288 | 40 | inferred_complete_timeline |
| `Action_None` | 293 | 295 | 3 | inferred_complete_timeline |
| `Action_None` | 297 | 599 | 303 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 46 | 8 | inferred_complete_timeline |
| `Action_None` | 48 | 66 | 19 | inferred_complete_timeline |
| `Action_None` | 76 | 101 | 26 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 592

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 119 | 81 | inferred_complete_timeline |
| `Action_None` | 128 | 599 | 472 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 219 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 38 | 20 | inferred_complete_timeline |
| `Action_None` | 39 | 220 | 182 | inferred_complete_timeline |
| `Action_None` | 223 | 599 | 377 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 556

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 208 | 170 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 599 | 343 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 559

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 186 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 196 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 203 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 210 | 5 | inferred_complete_timeline |
| `Action_CatchKick` | 211 | 225 | 15 | inferred_complete_timeline |
| `Action_None` | 226 | 235 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 236 | 323 | 88 | inferred_complete_timeline |
| `Action_BallCarry` | 325 | 395 | 71 | inferred_complete_timeline |
| `Action_BallCarry` | 397 | 440 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 443 | 448 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 451 | 453 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 458 | 462 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 467 | 470 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 472 | 477 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 483 | 492 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 495 | 499 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 501 | 507 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 511 | 514 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 517 | 519 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 521 | 522 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 527 | 594 | 68 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 595 | 599 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 592

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 21 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 38 | 16 | inferred_complete_timeline |
| `Action_None` | 39 | 99 | 61 | inferred_complete_timeline |
| `Action_None` | 102 | 300 | 199 | inferred_complete_timeline |
| `Action_None` | 303 | 599 | 297 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 597

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 275 | 237 | inferred_complete_timeline |
| `Action_None` | 279 | 599 | 321 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 589

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 225 | 187 | inferred_complete_timeline |
| `Action_None` | 227 | 231 | 5 | inferred_complete_timeline |
| `Action_None` | 234 | 236 | 3 | inferred_complete_timeline |
| `Action_None` | 238 | 268 | 31 | inferred_complete_timeline |
| `Action_None` | 274 | 362 | 89 | inferred_complete_timeline |
| `Action_None` | 364 | 397 | 34 | inferred_complete_timeline |
| `Action_None` | 399 | 599 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 127 | 89 | inferred_complete_timeline |
| `Action_None` | 129 | 243 | 115 | inferred_complete_timeline |
| `Action_None` | 246 | 283 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 488 | 450 | inferred_complete_timeline |
| `Action_None` | 510 | 511 | 2 | inferred_complete_timeline |
| `Action_None` | 518 | 525 | 8 | inferred_complete_timeline |
| `Action_None` | 528 | 534 | 7 | inferred_complete_timeline |
| `Action_None` | 539 | 564 | 26 | inferred_complete_timeline |
| `Action_None` | 566 | 569 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–119 | 35 | 5 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 8–599 | 481 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 15–599 | 537 | 11 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 20–81 | 51 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 45–46 | 2 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 77–361 | 280 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 91–599 | 472 | 11 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 92–580 | 469 | 7 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 118–599 | 478 | 4 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 144–599 | 456 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 149–224 | 26 | 7 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 168–312 | 141 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 180–203 | 21 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 180–182 | 3 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 257–328 | 71 | 2 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 293–599 | 303 | 2 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 317–599 | 283 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 324–570 | 247 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 336–599 | 261 | 2 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 355–358 | 4 | 1 | Undefined position; Undefined team |
| `37` | `57` | Position_Unknown | Team_Unknown | 382–599 | 217 | 2 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 391–394 | 4 | 1 | Undefined position; Undefined team |
| `39` | `64` | Position_Unknown | Team_Unknown | 415–416 | 2 | 1 | Undefined position; Undefined team |
| `40` | `73` | Position_Unknown | Team_Unknown | 507–508 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_KickBall` on target `5` (Kicker)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (15 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 158 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 56: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 56: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Segment 'Action_KickBall' for track '5' has invalid range: start=98, end=97. Clamping end to start.
- ⚠️ Action 'Action_None' range [39-225] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-231] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-268] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-362] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-397] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-599] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-488] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-511] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-525] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-534] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-564] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-569] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-127] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-243] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-283] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-79] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-101] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-182] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-238] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-288] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [39-97] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-164] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-186] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-196] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-203] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [236-323] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [325-395] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [397-440] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [443-448] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [451-453] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [458-462] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [467-470] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [472-477] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [483-492] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [495-499] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [501-507] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [511-514] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [517-519] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [521-522] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [527-594] for track '6' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-208] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-599] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-275] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-16] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-108] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-21] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-99] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-300] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-138] for track '12' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-19] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-58] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-229] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-299] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-220] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-599] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-38] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-47] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-77] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-360] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-427] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-599] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-46] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-66] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-101] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-18] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-102] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-349] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-27] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-62] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-293] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-578] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-596] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-27] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-34] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-81] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-237] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-343] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-361] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-159] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-571] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-130] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-164] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-198] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-573] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-580] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-194] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-382] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-568] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-599] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-161] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-220] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-266] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-312] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-324] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-310] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-599] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-599] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-570] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-357] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-599] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-358] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-392] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-394] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-508] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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