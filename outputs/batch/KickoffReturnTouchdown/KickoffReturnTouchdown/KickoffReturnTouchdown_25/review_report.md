# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_25`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 689
- **Player Tracks:** 56
- **Ball Tracks:** 0
- **Action Segments:** 159
- **Validation Warnings:** 213
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 144
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `29` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `29` | `23` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `29` | `23` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `11` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `12` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `14` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `15` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `16` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `4` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `5` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `6` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `7` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `8` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `9` | `Group` | 0 | START | 0 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `12` | `12` | 79 | START | 79 | 151 |
| ✅ EXACT | `Action_KickBall` | Kicker | `12` | `12` | 168 | START | 168 | 173 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `29` | `23` | 295 | START | 295 | 300 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `29` | `23` | 311 | START | 311 | 381 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `29` | `23` | 690 | START | N/A | N/A |

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
- **Visible Frames:** 0–341
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_KickApproach` | 79 | 151 | 73 | inferred_complete_timeline |
| `Action_KickApproach` | 154 | 158 | 5 | inferred_complete_timeline |
| `Action_KickApproach` | 160 | 167 | 8 | inferred_complete_timeline |
| `Action_KickBall` | 168 | 173 | 6 | inferred_complete_timeline |
| `Action_None` | 174 | 341 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–661
- **Visible Samples:** 662

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 661 | 583 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 358 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–367
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 270 | 192 | inferred_complete_timeline |
| `Action_None` | 275 | 286 | 12 | inferred_complete_timeline |
| `Action_None` | 288 | 367 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 320 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 292 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 326 | 248 | inferred_complete_timeline |
| `Action_None` | 330 | 333 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 602

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 310 | 232 | inferred_complete_timeline |
| `Action_None` | 313 | 318 | 6 | inferred_complete_timeline |
| `Action_None` | 381 | 385 | 5 | inferred_complete_timeline |
| `Action_None` | 387 | 390 | 4 | inferred_complete_timeline |
| `Action_None` | 396 | 409 | 14 | inferred_complete_timeline |
| `Action_None` | 412 | 557 | 146 | inferred_complete_timeline |
| `Action_None` | 561 | 622 | 62 | inferred_complete_timeline |
| `Action_None` | 636 | 689 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–481
- **Visible Samples:** 473

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 412 | 334 | inferred_complete_timeline |
| `Action_None` | 419 | 474 | 56 | inferred_complete_timeline |
| `Action_None` | 476 | 477 | 2 | inferred_complete_timeline |
| `Action_None` | 480 | 481 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–496
- **Visible Samples:** 496

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 186 | 108 | inferred_complete_timeline |
| `Action_None` | 188 | 496 | 309 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–451
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 194 | 116 | inferred_complete_timeline |
| `Action_None` | 196 | 201 | 6 | inferred_complete_timeline |
| `Action_None` | 203 | 407 | 205 | inferred_complete_timeline |
| `Action_None` | 409 | 451 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–588
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 553 | 475 | inferred_complete_timeline |
| `Action_None` | 556 | 588 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 668

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 310 | 232 | inferred_complete_timeline |
| `Action_None` | 322 | 573 | 252 | inferred_complete_timeline |
| `Action_None` | 580 | 585 | 6 | inferred_complete_timeline |
| `Action_None` | 587 | 603 | 17 | inferred_complete_timeline |
| `Action_None` | 608 | 689 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 292 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 300 | 222 | inferred_complete_timeline |
| `Action_None` | 357 | 358 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–605
- **Visible Samples:** 530

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 310 | 232 | inferred_complete_timeline |
| `Action_None` | 323 | 337 | 15 | inferred_complete_timeline |
| `Action_None` | 341 | 343 | 3 | inferred_complete_timeline |
| `Action_None` | 345 | 346 | 2 | inferred_complete_timeline |
| `Action_None` | 380 | 385 | 6 | inferred_complete_timeline |
| `Action_None` | 387 | 388 | 2 | inferred_complete_timeline |
| `Action_None` | 394 | 409 | 16 | inferred_complete_timeline |
| `Action_None` | 412 | 478 | 67 | inferred_complete_timeline |
| `Action_None` | 493 | 539 | 47 | inferred_complete_timeline |
| `Action_None` | 541 | 543 | 3 | inferred_complete_timeline |
| `Action_None` | 546 | 547 | 2 | inferred_complete_timeline |
| `Action_None` | 550 | 605 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 688

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 308 | 230 | inferred_complete_timeline |
| `Action_None` | 310 | 587 | 278 | inferred_complete_timeline |
| `Action_None` | 589 | 689 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 180–185 | 6 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 223–226 | 4 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 241–413 | 142 | 5 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 245–675 | 404 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 251–446 | 196 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 262–343 | 47 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 270–385 | 115 | 5 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 347–689 | 304 | 4 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 351–521 | 171 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 376–387 | 9 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 384–385 | 2 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 390–689 | 299 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 393–566 | 163 | 4 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 393–582 | 190 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 397–689 | 275 | 7 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 397–398 | 2 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 403–573 | 171 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 403–525 | 120 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 405–449 | 36 | 3 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 406–665 | 212 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 413–689 | 274 | 2 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 420–599 | 166 | 5 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 452–453 | 2 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 454–494 | 41 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 471–642 | 165 | 3 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 485–486 | 2 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 495–689 | 195 | 1 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 496–540 | 42 | 2 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 500–501 | 2 | 1 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 504–507 | 4 | 1 | Undefined position; Undefined team |
| `47` | `63` | Position_Unknown | Team_Unknown | 516–689 | 174 | 1 | Undefined position; Undefined team |
| `48` | `65` | Position_Unknown | Team_Unknown | 527–594 | 63 | 2 | Undefined position; Undefined team |
| `49` | `66` | Position_Unknown | Team_Unknown | 529–681 | 146 | 3 | Undefined position; Undefined team |
| `50` | `67` | Position_Unknown | Team_Unknown | 531–535 | 5 | 1 | Undefined position; Undefined team |
| `51` | `69` | Position_Unknown | Team_Unknown | 543–561 | 19 | 1 | Undefined position; Undefined team |
| `52` | `73` | Position_Unknown | Team_Unknown | 577–578 | 2 | 1 | Undefined position; Undefined team |
| `53` | `74` | Position_Unknown | Team_Unknown | 586–676 | 71 | 5 | Undefined position; Undefined team |
| `54` | `80` | Position_Unknown | Team_Unknown | 655–658 | 4 | 1 | Undefined position; Undefined team |
| `55` | `81` | Position_Unknown | Team_Unknown | 669–689 | 9 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `29` (2 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `29` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ 39 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 39 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 78 |
| Missing visible bounding boxes during action | 132 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '23' has invalid range: start=690, end=385. Clamping end to start.
- ⚠️ Action 'Action_None' range [79-553] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-588] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-292] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-300] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-310] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-337] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-343] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-385] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-409] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-478] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-539] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-543] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-547] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-605] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-320] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-310] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-318] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-385] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-390] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-409] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-557] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-622] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-326] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-333] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-412] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-474] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-481] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-292] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-661] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-308] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-587] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-689] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-496] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [79-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [154-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-341] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-310] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-573] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-585] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-603] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-689] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-194] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-407] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-451] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-358] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-270] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-286] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-367] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-349] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-356] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-398] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-409] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-359] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-675] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-446] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-303] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-343] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [311-381] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [383-385] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-350] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-647] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-521] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-379] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-387] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-392] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-689] for track '28' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-433] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-480] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-563] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-566] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-582] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-407] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-573] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-579] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-618] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-627] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-573] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-490] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-525] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-407] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-449] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-665] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-415] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-689] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-422] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-579] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-583] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-595] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-599] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-494] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-473] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-579] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-642] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-532] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-540] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-507] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-689] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-573] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-594] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-539] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-643] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-681] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-535] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-561] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-588] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-599] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-606] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-663] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [667-676] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [655-658] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [669-670] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [681-682] for track '55' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 690. Video range is [0, 689].

</details>