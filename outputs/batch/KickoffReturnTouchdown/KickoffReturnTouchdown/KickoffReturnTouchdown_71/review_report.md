# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_71

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_71`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 140
- **Validation Warnings:** 163
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 127
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `3` | `3` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `3` | `3` |
| ⚠️ START CHANGED | `Action_CatchKick` | Kick_Returner1 | defense | `17` | `17` |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner1 | defense | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `1` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `13` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `14` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `18` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `19` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `3` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `6` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `7` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `8` | `Group` | 0 | START | 0 | 13 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `3` | `3` | 14 | START | 14 | 36 |
| ✅ EXACT | `Action_KickBall` | Kicker | `3` | `3` | 55 | START | 55 | 59 |
| ⚠️ START CHANGED | `Action_CatchKick` | Kick_Returner1 | `17` | `17` | 173 | START | 176 | 181 |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner1 | `17` | `17` | 190 | START | 190 | 407 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner1 | `17` | `17` | 540 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 529

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_KickApproach` | 14 | 36 | 23 | inferred_complete_timeline |
| `Action_KickApproach` | 38 | 54 | 17 | inferred_complete_timeline |
| `Action_KickBall` | 55 | 59 | 5 | inferred_complete_timeline |
| `Action_None` | 60 | 71 | 12 | inferred_complete_timeline |
| `Action_None` | 73 | 363 | 291 | inferred_complete_timeline |
| `Action_None` | 366 | 372 | 7 | inferred_complete_timeline |
| `Action_None` | 374 | 396 | 23 | inferred_complete_timeline |
| `Action_None` | 398 | 419 | 22 | inferred_complete_timeline |
| `Action_None` | 422 | 425 | 4 | inferred_complete_timeline |
| `Action_None` | 429 | 539 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 24 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–27
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 19 | 6 | inferred_complete_timeline |
| `Action_None` | 22 | 27 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–27
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 27 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 268 | 255 | inferred_complete_timeline |
| `Action_None` | 273 | 275 | 3 | inferred_complete_timeline |
| `Action_None` | 278 | 284 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 426 | 413 | inferred_complete_timeline |
| `Action_None` | 429 | 539 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 382 | 369 | inferred_complete_timeline |
| `Action_None` | 384 | 539 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 410 | 397 | inferred_complete_timeline |
| `Action_None` | 415 | 417 | 3 | inferred_complete_timeline |
| `Action_None` | 421 | 425 | 5 | inferred_complete_timeline |
| `Action_None` | 427 | 448 | 22 | inferred_complete_timeline |
| `Action_None` | 460 | 465 | 6 | inferred_complete_timeline |
| `Action_None` | 467 | 494 | 28 | inferred_complete_timeline |
| `Action_None` | 501 | 502 | 2 | inferred_complete_timeline |
| `Action_None` | 504 | 509 | 6 | inferred_complete_timeline |
| `Action_None` | 511 | 518 | 8 | inferred_complete_timeline |
| `Action_None` | 522 | 523 | 2 | inferred_complete_timeline |
| `Action_None` | 526 | 527 | 2 | inferred_complete_timeline |
| `Action_None` | 537 | 539 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 539 | 526 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 104 | 91 | inferred_complete_timeline |
| `Action_None` | 106 | 341 | 236 | inferred_complete_timeline |
| `Action_None` | 345 | 539 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 174 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 539 | 526 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 309 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 539 | 526 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–407
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 86 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 164 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 171 | 6 | inferred_complete_timeline |
| `Action_CatchKick` | 176 | 181 | 6 | inferred_complete_timeline |
| `Action_None` | 182 | 189 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 190 | 407 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–500
- **Visible Samples:** 494

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 311 | 298 | inferred_complete_timeline |
| `Action_None` | 316 | 416 | 101 | inferred_complete_timeline |
| `Action_None` | 419 | 421 | 3 | inferred_complete_timeline |
| `Action_None` | 423 | 500 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 294 | 281 | inferred_complete_timeline |
| `Action_None` | 302 | 304 | 3 | inferred_complete_timeline |
| `Action_None` | 306 | 539 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–461
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 280 | 267 | inferred_complete_timeline |
| `Action_None` | 282 | 284 | 3 | inferred_complete_timeline |
| `Action_None` | 288 | 461 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–400
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 391 | 378 | inferred_complete_timeline |
| `Action_None` | 396 | 400 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–290
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 290 | 277 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 43–539 | 478 | 6 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 46–539 | 452 | 7 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 66–97 | 30 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 72–73 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 76–109 | 28 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 83–88 | 6 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 85–98 | 11 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 85–310 | 207 | 5 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 87–88 | 2 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 96–97 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 97–101 | 5 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 101–539 | 434 | 5 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 109–110 | 2 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 110–356 | 247 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 131–154 | 14 | 3 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 198–366 | 168 | 2 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 283–539 | 253 | 2 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 304–539 | 235 | 2 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 307–539 | 226 | 3 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 367–416 | 43 | 3 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 406–407 | 2 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 406–407 | 2 | 1 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 423–442 | 16 | 2 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 432–473 | 17 | 2 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 446–539 | 94 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `3` (2 segments found)
- ⚠️ `Action_CatchKick` for actor_track_id `17` (Kick_Returner1): Annotated start 173 != Inferred start 176
- ❌ Missing segment for action `Action_CrossGoalLine` on target `17` (Kick_Returner1)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 110 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '17' has invalid range: start=540, end=407. Clamping end to start.
- ⚠️ Action 'Action_None' range [14-539] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-268] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-284] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-539] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [14-36] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [38-54] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-71] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-363] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-372] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-396] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-419] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-425] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-294] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-304] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-27] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-426] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-539] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-410] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-417] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-425] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-448] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-465] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-494] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-509] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-518] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-523] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-290] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-391] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-400] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-341] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-309] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-539] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-382] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-311] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-416] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-421] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-500] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-280] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-461] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-78] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-86] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-164] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-189] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [190-407] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-19] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-27] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-24] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-61] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-283] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-302] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-64] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-366] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-419] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-449] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-100] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-88] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-104] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-268] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-292] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-310] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-112] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-352] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-410] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-356] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-154] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-361] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-366] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-290] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-417] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-539] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-539] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-372] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-416] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-435] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-442] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-436] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-473] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-539] for track '44' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 540. Video range is [0, 539].

</details>