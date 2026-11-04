# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_32

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_32`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 58
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 160
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 100
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `13` | `13` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `13` | `13` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `21` | `21` |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner1 | defense | `21` | `21` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner2 | defense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `0` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `1` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `13` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `15` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `2` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `3` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `4` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `5` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `6` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `7` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `9` | `Group` | 0 | START | 0 | 40 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `13` | `13` | 41 | START | 41 | 105 |
| ✅ EXACT | `Action_KickBall` | Kicker | `13` | `13` | 106 | START | 106 | 110 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `21` | `21` | 223 | START | 223 | 232 |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner1 | `21` | `21` | 250 | START | 250 | 517 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner2 | `20` | `20` | 626 | START | 626 | 629 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_KickApproach` | 41 | 105 | 65 | inferred_complete_timeline |
| `Action_KickBall` | 106 | 110 | 5 | inferred_complete_timeline |
| `Action_None` | 111 | 629 | 519 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–504
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 504 | 464 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–372
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 190 | 150 | inferred_complete_timeline |
| `Action_None` | 194 | 253 | 60 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 372 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–350
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 350 | 310 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–316
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 295 | 255 | inferred_complete_timeline |
| `Action_None` | 297 | 316 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–595
- **Visible Samples:** 575

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 321 | 281 | inferred_complete_timeline |
| `Action_None` | 323 | 570 | 248 | inferred_complete_timeline |
| `Action_None` | 587 | 588 | 2 | inferred_complete_timeline |
| `Action_None` | 593 | 595 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 277 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 333 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–410
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 410 | 370 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–306
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 306 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–505
- **Visible Samples:** 506

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 505 | 465 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–550
- **Visible Samples:** 551

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 550 | 510 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 308 | 268 | inferred_complete_timeline |
| `Action_None` | 312 | 314 | 3 | inferred_complete_timeline |
| `Action_None` | 316 | 319 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 615

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 249 | 209 | inferred_complete_timeline |
| `Action_None` | 264 | 352 | 89 | inferred_complete_timeline |
| `Action_None` | 354 | 629 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–536
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 536 | 496 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–361
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 361 | 321 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–517
- **Visible Samples:** 518

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |
| `Action_CatchKick` | 223 | 232 | 10 | inferred_complete_timeline |
| `Action_None` | 233 | 249 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 250 | 517 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 625 | 626 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 626 | 629 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–621
- **Visible Samples:** 622

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 621 | 581 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–414
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 387 | 347 | inferred_complete_timeline |
| `Action_None` | 389 | 414 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–357
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 303 | 263 | inferred_complete_timeline |
| `Action_None` | 311 | 357 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–427
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 427 | 387 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `27` | Position_Unknown | Team_Unknown | 136–137 | 2 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 140–143 | 4 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 146–149 | 4 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 193–201 | 9 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 197–204 | 8 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 207–226 | 17 | 2 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 237–280 | 19 | 5 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 280–629 | 344 | 5 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 304–407 | 29 | 2 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 337–412 | 76 | 1 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 358–427 | 70 | 1 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 362–628 | 266 | 2 | Undefined position; Undefined team |
| `35` | `55` | Position_Unknown | Team_Unknown | 387–398 | 8 | 2 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 444–447 | 4 | 1 | Undefined position; Undefined team |
| `37` | `59` | Position_Unknown | Team_Unknown | 461–462 | 2 | 1 | Undefined position; Undefined team |
| `38` | `62` | Position_Unknown | Team_Unknown | 468–609 | 142 | 1 | Undefined position; Undefined team |
| `39` | `65` | Position_Unknown | Team_Unknown | 471–565 | 95 | 1 | Undefined position; Undefined team |
| `40` | `68` | Position_Unknown | Team_Unknown | 479–483 | 5 | 1 | Undefined position; Undefined team |
| `41` | `72` | Position_Unknown | Team_Unknown | 492–494 | 3 | 1 | Undefined position; Undefined team |
| `42` | `73` | Position_Unknown | Team_Unknown | 493–502 | 10 | 1 | Undefined position; Undefined team |
| `43` | `74` | Position_Unknown | Team_Unknown | 498–503 | 5 | 2 | Undefined position; Undefined team |
| `44` | `75` | Position_Unknown | Team_Unknown | 501–513 | 4 | 2 | Undefined position; Undefined team |
| `45` | `76` | Position_Unknown | Team_Unknown | 502–506 | 4 | 2 | Undefined position; Undefined team |
| `46` | `81` | Position_Unknown | Team_Unknown | 537–545 | 9 | 1 | Undefined position; Undefined team |
| `47` | `82` | Position_Unknown | Team_Unknown | 538–540 | 3 | 1 | Undefined position; Undefined team |
| `48` | `83` | Position_Unknown | Team_Unknown | 542–543 | 2 | 1 | Undefined position; Undefined team |
| `49` | `84` | Position_Unknown | Team_Unknown | 555–590 | 11 | 3 | Undefined position; Undefined team |
| `50` | `85` | Position_Unknown | Team_Unknown | 566–571 | 6 | 1 | Undefined position; Undefined team |
| `51` | `87` | Position_Unknown | Team_Unknown | 568–611 | 42 | 2 | Undefined position; Undefined team |
| `52` | `88` | Position_Unknown | Team_Unknown | 577–629 | 53 | 1 | Undefined position; Undefined team |
| `53` | `89` | Position_Unknown | Team_Unknown | 579–580 | 2 | 1 | Undefined position; Undefined team |
| `54` | `91` | Position_Unknown | Team_Unknown | 591–612 | 22 | 1 | Undefined position; Undefined team |
| `55` | `92` | Position_Unknown | Team_Unknown | 593–596 | 4 | 1 | Undefined position; Undefined team |
| `56` | `94` | Position_Unknown | Team_Unknown | 600–602 | 3 | 1 | Undefined position; Undefined team |
| `57` | `96` | Position_Unknown | Team_Unknown | 626–628 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 87 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action 'Action_None' range [41-333] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-410] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-277] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-306] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-190] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-253] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-372] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-350] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-295] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-316] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-504] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-427] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-505] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-308] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-536] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-303] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-357] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-629] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-361] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-321] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-570] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-588] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-595] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-387] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-414] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-249] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-352] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-550] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-621] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-625] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [250-517] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-204] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-226] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-280] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-289] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-357] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-403] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-614] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-308] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-407] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-412] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-427] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-459] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-628] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-391] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-398] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-447] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-462] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-609] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-565] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-483] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-494] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-502] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-499] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-503] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-513] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-506] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-545] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-540] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-543] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-559] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-563] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-590] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-571] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-607] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-611] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-580] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-612] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-596] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-602] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-628] for track '57' has 1 frames without a visible bounding box.
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

</details>