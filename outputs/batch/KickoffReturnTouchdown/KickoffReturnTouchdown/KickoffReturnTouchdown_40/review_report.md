# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_40

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_40`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 132
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 116
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | defense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | defense | `1` | `1` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner2 | defense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `14` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `15` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `16` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `17` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `18` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `20` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `3` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `5` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `6` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `7` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `9` | `Group` | 0 | START | 0 | 85 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `15` | `15` | 86 | START | 86 | 146 |
| ✅ EXACT | `Action_KickBall` | Kicker | `15` | `15` | 147 | START | 147 | 153 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | `1` | `1` | 252 | START | 252 | 266 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | `1` | `1` | 282 | START | 282 | 607 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner2 | `1` | `1` | 642 | START | 642 | 655 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 656

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_KickApproach` | 86 | 146 | 61 | inferred_complete_timeline |
| `Action_KickBall` | 147 | 153 | 7 | inferred_complete_timeline |
| `Action_None` | 154 | 569 | 416 | inferred_complete_timeline |
| `Action_None` | 574 | 659 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 654

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 246 | 161 | inferred_complete_timeline |
| `Action_None` | 248 | 568 | 321 | inferred_complete_timeline |
| `Action_None` | 570 | 574 | 5 | inferred_complete_timeline |
| `Action_None` | 577 | 585 | 9 | inferred_complete_timeline |
| `Action_None` | 587 | 603 | 17 | inferred_complete_timeline |
| `Action_None` | 605 | 659 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 656

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 640 | 555 | inferred_complete_timeline |
| `Action_None` | 645 | 659 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 651

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 269 | 184 | inferred_complete_timeline |
| `Action_None` | 275 | 335 | 61 | inferred_complete_timeline |
| `Action_None` | 337 | 341 | 5 | inferred_complete_timeline |
| `Action_None` | 345 | 659 | 315 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 287 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–484
- **Visible Samples:** 483

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 354 | 269 | inferred_complete_timeline |
| `Action_None` | 357 | 484 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 657

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 534 | 449 | inferred_complete_timeline |
| `Action_None` | 538 | 659 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–348
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 280 | 195 | inferred_complete_timeline |
| `Action_None` | 300 | 302 | 3 | inferred_complete_timeline |
| `Action_None` | 304 | 315 | 12 | inferred_complete_timeline |
| `Action_None` | 317 | 333 | 17 | inferred_complete_timeline |
| `Action_None` | 335 | 345 | 11 | inferred_complete_timeline |
| `Action_None` | 347 | 348 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 656

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 224 | 139 | inferred_complete_timeline |
| `Action_None` | 228 | 230 | 3 | inferred_complete_timeline |
| `Action_None` | 232 | 659 | 428 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 660

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 659 | 574 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 660

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 659 | 574 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–581
- **Visible Samples:** 580

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 346 | 261 | inferred_complete_timeline |
| `Action_None` | 349 | 581 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–514
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 337 | 252 | inferred_complete_timeline |
| `Action_None` | 340 | 352 | 13 | inferred_complete_timeline |
| `Action_None` | 357 | 514 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 648

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 394 | 309 | inferred_complete_timeline |
| `Action_None` | 398 | 401 | 4 | inferred_complete_timeline |
| `Action_None` | 411 | 659 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–515
- **Visible Samples:** 507

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 304 | 219 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_None` | 316 | 515 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–501
- **Visible Samples:** 502

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 501 | 416 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–480
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 407 | 322 | inferred_complete_timeline |
| `Action_None` | 413 | 480 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 267 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 657

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 251 | 252 | inferred_complete_timeline |
| `Action_CatchKick` | 252 | 266 | 15 | inferred_complete_timeline |
| `Action_None` | 267 | 281 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 282 | 607 | 326 | inferred_complete_timeline |
| `Action_BallCarry` | 610 | 611 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 613 | 641 | 29 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 642 | 655 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 656 | 659 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 649

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 459 | 374 | inferred_complete_timeline |
| `Action_None` | 462 | 535 | 74 | inferred_complete_timeline |
| `Action_None` | 545 | 659 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–494
- **Visible Samples:** 495

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 494 | 409 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–486
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 312 | 227 | inferred_complete_timeline |
| `Action_None` | 314 | 351 | 38 | inferred_complete_timeline |
| `Action_None` | 353 | 370 | 18 | inferred_complete_timeline |
| `Action_None` | 373 | 375 | 3 | inferred_complete_timeline |
| `Action_None` | 389 | 416 | 28 | inferred_complete_timeline |
| `Action_None` | 429 | 453 | 25 | inferred_complete_timeline |
| `Action_None` | 457 | 458 | 2 | inferred_complete_timeline |
| `Action_None` | 462 | 486 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 133–135 | 3 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 185–188 | 4 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 210–217 | 8 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 245–261 | 9 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 276–659 | 371 | 5 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 293–659 | 367 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 329–330 | 2 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 344–349 | 4 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 374–493 | 120 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 459–460 | 2 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 487–659 | 173 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 512–612 | 71 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 553–557 | 5 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 561–581 | 9 | 3 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 568–654 | 38 | 4 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 574–604 | 31 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 612–613 | 2 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 615–659 | 41 | 3 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 618–659 | 25 | 4 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 623–659 | 37 | 1 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 646–659 | 12 | 2 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 652–659 | 5 | 2 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 656–659 | 4 | 1 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 656–659 | 4 | 1 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 658–659 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 88 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action 'Action_None' range [86-501] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [282-607] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [610-611] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [613-641] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-407] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-480] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-354] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-484] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-312] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-351] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-370] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-375] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-416] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-453] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-458] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-486] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-280] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-315] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-333] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-345] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-246] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-568] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-574] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-585] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-603] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-640] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-394] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-401] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-287] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-346] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-581] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-494] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-459] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-535] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-337] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-352] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-514] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-534] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-569] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-335] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-341] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-224] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-659] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-659] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-304] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-515] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-267] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-217] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-294] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-510] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-529] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-631] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-493] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-659] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-514] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-612] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-557] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-562] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-575] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-581] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-579] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-601] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-614] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [653-654] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-604] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-613] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-621] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-627] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-659] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-633] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-637] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-640] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-648] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-659] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-654] for track '43' has 1 frames without a visible bounding box.
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

</details>