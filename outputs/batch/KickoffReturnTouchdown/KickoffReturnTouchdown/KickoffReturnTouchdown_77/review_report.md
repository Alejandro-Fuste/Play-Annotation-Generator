# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_77

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_77`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 136
- **Validation Warnings:** 133
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 121
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `21` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `14` | `14` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `14` | `14` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | defense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | defense | `9` | `9` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner2 | defense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `10` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `11` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `12` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `13` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `14` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `15` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `16` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `18` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `19` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `21` | `Group` | 0 | START | 0 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `14` | `14` | 24 | START | 24 | 43 |
| ✅ EXACT | `Action_KickBall` | Kicker | `14` | `14` | 84 | START | 84 | 92 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | `9` | `9` | 189 | START | 189 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | `9` | `9` | 222 | START | 222 | 321 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner2 | `9` | `9` | 575 | START | 575 | 588 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–598
- **Visible Samples:** 592

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_KickApproach` | 24 | 43 | 20 | inferred_complete_timeline |
| `Action_KickApproach` | 45 | 83 | 39 | inferred_complete_timeline |
| `Action_KickBall` | 84 | 92 | 9 | inferred_complete_timeline |
| `Action_None` | 93 | 588 | 496 | inferred_complete_timeline |
| `Action_None` | 595 | 598 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 93 | 70 | inferred_complete_timeline |
| `Action_None` | 97 | 576 | 480 | inferred_complete_timeline |
| `Action_None` | 578 | 591 | 14 | inferred_complete_timeline |
| `Action_None` | 593 | 599 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 522 | 499 | inferred_complete_timeline |
| `Action_None` | 524 | 569 | 46 | inferred_complete_timeline |
| `Action_None` | 574 | 599 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 245 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–500
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 202 | 179 | inferred_complete_timeline |
| `Action_None` | 206 | 500 | 295 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 82 | 59 | inferred_complete_timeline |
| `Action_None` | 87 | 192 | 106 | inferred_complete_timeline |
| `Action_None` | 195 | 294 | 100 | inferred_complete_timeline |
| `Action_None` | 298 | 599 | 302 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 58 | 35 | inferred_complete_timeline |
| `Action_None` | 60 | 155 | 96 | inferred_complete_timeline |
| `Action_None` | 158 | 163 | 6 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 180 | 216 | 37 | inferred_complete_timeline |
| `Action_None` | 220 | 264 | 45 | inferred_complete_timeline |
| `Action_None` | 281 | 292 | 12 | inferred_complete_timeline |
| `Action_None` | 296 | 599 | 304 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 599 | 576 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–592
- **Visible Samples:** 592

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 281 | 258 | inferred_complete_timeline |
| `Action_None` | 283 | 592 | 310 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 571

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 335 | 312 | inferred_complete_timeline |
| `Action_None` | 338 | 456 | 119 | inferred_complete_timeline |
| `Action_None` | 460 | 461 | 2 | inferred_complete_timeline |
| `Action_None` | 465 | 482 | 18 | inferred_complete_timeline |
| `Action_None` | 486 | 489 | 4 | inferred_complete_timeline |
| `Action_None` | 496 | 498 | 3 | inferred_complete_timeline |
| `Action_None` | 503 | 504 | 2 | inferred_complete_timeline |
| `Action_None` | 510 | 561 | 52 | inferred_complete_timeline |
| `Action_None` | 565 | 599 | 35 | inferred_complete_timeline |

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
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 329 | 306 | inferred_complete_timeline |
| `Action_None` | 332 | 599 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–487
- **Visible Samples:** 481

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 350 | 327 | inferred_complete_timeline |
| `Action_None` | 355 | 363 | 9 | inferred_complete_timeline |
| `Action_None` | 365 | 366 | 2 | inferred_complete_timeline |
| `Action_None` | 369 | 487 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 243 | 220 | inferred_complete_timeline |
| `Action_None` | 245 | 312 | 68 | inferred_complete_timeline |
| `Action_None` | 321 | 343 | 23 | inferred_complete_timeline |
| `Action_None` | 364 | 385 | 22 | inferred_complete_timeline |
| `Action_None` | 389 | 599 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 147 | 124 | inferred_complete_timeline |
| `Action_None` | 149 | 599 | 451 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 597

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 221 | 198 | inferred_complete_timeline |
| `Action_None` | 225 | 599 | 375 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–338
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 257 | 234 | inferred_complete_timeline |
| `Action_None` | 261 | 338 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_CatchKick` | 189 | 199 | 11 | inferred_complete_timeline |
| `Action_None` | 200 | 221 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 222 | 321 | 100 | inferred_complete_timeline |
| `Action_BallCarry` | 333 | 341 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 344 | 573 | 230 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 575 | 588 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 589 | 599 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 590

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 272 | 249 | inferred_complete_timeline |
| `Action_None` | 283 | 599 | 317 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 599 | 576 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 590

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 489 | 466 | inferred_complete_timeline |
| `Action_None` | 500 | 599 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 208 | 185 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–99 | 29 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 2–599 | 587 | 6 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 113–141 | 11 | 3 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 136–210 | 67 | 5 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 165–212 | 12 | 4 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 167–168 | 2 | 1 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 215–233 | 15 | 2 | Undefined position; Undefined team |
| `28` | `28` | Position_Unknown | Team_Unknown | 241–321 | 81 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 257–599 | 339 | 3 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 274–281 | 8 | 1 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 286–291 | 6 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 327–354 | 26 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 365–599 | 229 | 4 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 374–409 | 9 | 3 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 416–428 | 13 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 446–599 | 154 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 477–478 | 2 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 503–599 | 97 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 554–562 | 9 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 571–580 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 92 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [24-257] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-338] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-489] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-350] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-363] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-487] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-272] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-221] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-243] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-312] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-343] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-385] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-147] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [222-321] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [333-341] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [344-573] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-335] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-456] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-482] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-489] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-498] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-561] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-202] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-500] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-155] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-163] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-216] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-264] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-292] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-599] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-522] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-569] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [24-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-588] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-598] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-82] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-192] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-294] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-576] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-591] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-208] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-281] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-592] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-245] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-21] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-60] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-99] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-7] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-291] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-527] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-119] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-147] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-186] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-225] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-321] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-356] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-546] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-281] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-291] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-350] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-388] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-397] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-378] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-428] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-599] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-562] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-580] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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