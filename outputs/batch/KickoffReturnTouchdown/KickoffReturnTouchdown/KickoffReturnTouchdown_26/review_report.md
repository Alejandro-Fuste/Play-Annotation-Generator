# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_26

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_26`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 48
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 139
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 102
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `14` | `14` |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner1 | defense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `0` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `1` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `10` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `12` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `18` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `2` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `3` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `4` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `5` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `7` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `9` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `12` | `12` | 19 | START | 19 | 104 |
| ✅ EXACT | `Action_KickBall` | Kicker | `12` | `12` | 105 | START | 105 | 108 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `14` | `14` | 233 | START | 233 | 240 |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner1 | `14` | `14` | 241 | START | 241 | 629 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner1 | `14` | `14` | 630 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–565
- **Visible Samples:** 559

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_KickApproach` | 19 | 104 | 86 | inferred_complete_timeline |
| `Action_KickBall` | 105 | 108 | 4 | inferred_complete_timeline |
| `Action_None` | 109 | 472 | 364 | inferred_complete_timeline |
| `Action_None` | 477 | 510 | 34 | inferred_complete_timeline |
| `Action_None` | 514 | 565 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 617

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 572 | 554 | inferred_complete_timeline |
| `Action_None` | 574 | 575 | 2 | inferred_complete_timeline |
| `Action_None` | 581 | 584 | 4 | inferred_complete_timeline |
| `Action_None` | 591 | 594 | 4 | inferred_complete_timeline |
| `Action_None` | 596 | 629 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 148 | 130 | inferred_complete_timeline |
| `Action_None` | 150 | 629 | 480 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–550
- **Visible Samples:** 544

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 148 | 130 | inferred_complete_timeline |
| `Action_None` | 155 | 414 | 260 | inferred_complete_timeline |
| `Action_None` | 416 | 550 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 612

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 598 | 580 | inferred_complete_timeline |
| `Action_None` | 600 | 605 | 6 | inferred_complete_timeline |
| `Action_None` | 608 | 609 | 2 | inferred_complete_timeline |
| `Action_None` | 625 | 629 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 619

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 133 | 115 | inferred_complete_timeline |
| `Action_None` | 137 | 277 | 141 | inferred_complete_timeline |
| `Action_None` | 286 | 629 | 344 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 626

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 176 | 158 | inferred_complete_timeline |
| `Action_None` | 179 | 401 | 223 | inferred_complete_timeline |
| `Action_None` | 404 | 629 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 289 | 271 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 629 | 611 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 629 | 611 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 629 | 611 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–470
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 289 | 271 | inferred_complete_timeline |
| `Action_None` | 294 | 434 | 141 | inferred_complete_timeline |
| `Action_None` | 439 | 470 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 629 | 611 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 629 | 611 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 629 | 611 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–602
- **Visible Samples:** 603

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 602 | 584 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 324 | 306 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_CatchKick` | 233 | 240 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 241 | 629 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–352
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 352 | 334 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 629 | 611 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 335 | 317 | inferred_complete_timeline |
| `Action_None` | 337 | 338 | 2 | inferred_complete_timeline |
| `Action_None` | 341 | 629 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 259 | 241 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 2–153 | 61 | 7 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 26–34 | 9 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 134–182 | 38 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 188–189 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 266–594 | 327 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 285–338 | 26 | 5 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 300–535 | 236 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 319–321 | 3 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 323–324 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 334–629 | 296 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 380–381 | 2 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 381–385 | 5 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 400–454 | 43 | 6 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 442–444 | 3 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 451–452 | 2 | 1 | Undefined position; Undefined team |
| `37` | `59` | Position_Unknown | Team_Unknown | 475–568 | 94 | 1 | Undefined position; Undefined team |
| `38` | `66` | Position_Unknown | Team_Unknown | 496–511 | 10 | 2 | Undefined position; Undefined team |
| `39` | `67` | Position_Unknown | Team_Unknown | 498–500 | 3 | 1 | Undefined position; Undefined team |
| `40` | `71` | Position_Unknown | Team_Unknown | 513–514 | 2 | 1 | Undefined position; Undefined team |
| `41` | `72` | Position_Unknown | Team_Unknown | 519–520 | 2 | 1 | Undefined position; Undefined team |
| `42` | `73` | Position_Unknown | Team_Unknown | 522–523 | 2 | 1 | Undefined position; Undefined team |
| `43` | `74` | Position_Unknown | Team_Unknown | 560–565 | 4 | 2 | Undefined position; Undefined team |
| `44` | `76` | Position_Unknown | Team_Unknown | 572–590 | 18 | 2 | Undefined position; Undefined team |
| `45` | `77` | Position_Unknown | Team_Unknown | 578–587 | 6 | 2 | Undefined position; Undefined team |
| `46` | `78` | Position_Unknown | Team_Unknown | 579–584 | 6 | 1 | Undefined position; Undefined team |
| `47` | `79` | Position_Unknown | Team_Unknown | 587–603 | 12 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CrossGoalLine` on target `14` (Kick_Returner1)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '14' has invalid range: start=630, end=629. Clamping end to start.
- ⚠️ Action 'Action_None' range [19-148] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-629] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-598] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-605] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-609] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-572] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-575] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-584] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-594] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-629] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-289] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-289] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-434] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-470] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-629] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-324] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-133] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-277] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-629] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-176] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-401] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-629] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-472] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-510] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-565] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-602] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-335] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-629] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-148] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-414] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-550] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-259] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-352] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-9] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-29] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-69] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-81] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-153] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-34] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-140] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-182] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-295] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-594] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-295] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-308] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-338] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-535] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-629] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-385] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-402] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-413] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-423] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-443] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-451] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-444] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-452] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-568] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-498] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-511] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-500] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-514] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-520] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-523] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-561] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-574] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-590] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-579] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-587] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-584] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-589] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-596] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-603] for track '47' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 630. Video range is [0, 629].

</details>