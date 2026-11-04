# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_85

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_85`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 179
- **Validation Warnings:** 209
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
- **Inferred Coverage Segments (Action_None):** 163
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Right_Coverage5 | offense | `15` | `15` |
| ✅ EXACT | `Action_KickBall` | Right_Coverage5 | offense | `15` | `15` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `1` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `11` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `12` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `13` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `14` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `15` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `16` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `5` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `6` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `8` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `9` | `Group` | 0 | START | 0 | 32 |
| ✅ EXACT | `Action_KickApproach` | Right_Coverage5 | `15` | `15` | 33 | START | 33 | 72 |
| ✅ EXACT | `Action_KickBall` | Right_Coverage5 | `15` | `15` | 73 | START | 73 | 77 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `21` | `21` | 196 | START | 196 | 205 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `21` | `21` | 224 | START | 224 | 309 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `21` | `21` | 565 | START | 565 | 569 |

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
- **Visible Frames:** 0–298
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 241 | 209 | inferred_complete_timeline |
| `Action_None` | 245 | 289 | 45 | inferred_complete_timeline |
| `Action_None` | 291 | 298 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 323 | 291 | inferred_complete_timeline |
| `Action_None` | 325 | 569 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 233 | 201 | inferred_complete_timeline |
| `Action_None` | 238 | 272 | 35 | inferred_complete_timeline |
| `Action_None` | 280 | 315 | 36 | inferred_complete_timeline |
| `Action_None` | 319 | 320 | 2 | inferred_complete_timeline |
| `Action_None` | 323 | 326 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 249 | 217 | inferred_complete_timeline |
| `Action_None` | 255 | 569 | 315 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 569 | 537 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 439 | 407 | inferred_complete_timeline |
| `Action_None` | 441 | 569 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 248 | 216 | inferred_complete_timeline |
| `Action_None` | 251 | 280 | 30 | inferred_complete_timeline |
| `Action_None` | 283 | 492 | 210 | inferred_complete_timeline |
| `Action_None` | 495 | 508 | 14 | inferred_complete_timeline |
| `Action_None` | 511 | 569 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 299 | 267 | inferred_complete_timeline |
| `Action_None` | 309 | 312 | 4 | inferred_complete_timeline |
| `Action_None` | 314 | 569 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 312 | 280 | inferred_complete_timeline |
| `Action_None` | 319 | 517 | 199 | inferred_complete_timeline |
| `Action_None` | 520 | 526 | 7 | inferred_complete_timeline |
| `Action_None` | 529 | 560 | 32 | inferred_complete_timeline |
| `Action_None` | 562 | 566 | 5 | inferred_complete_timeline |
| `Action_None` | 568 | 569 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 515

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 409 | 377 | inferred_complete_timeline |
| `Action_None` | 411 | 416 | 6 | inferred_complete_timeline |
| `Action_None` | 425 | 428 | 4 | inferred_complete_timeline |
| `Action_None` | 436 | 437 | 2 | inferred_complete_timeline |
| `Action_None` | 439 | 446 | 8 | inferred_complete_timeline |
| `Action_None` | 449 | 450 | 2 | inferred_complete_timeline |
| `Action_None` | 459 | 468 | 10 | inferred_complete_timeline |
| `Action_None` | 470 | 474 | 5 | inferred_complete_timeline |
| `Action_None` | 488 | 500 | 13 | inferred_complete_timeline |
| `Action_None` | 506 | 507 | 2 | inferred_complete_timeline |
| `Action_None` | 509 | 512 | 4 | inferred_complete_timeline |
| `Action_None` | 514 | 515 | 2 | inferred_complete_timeline |
| `Action_None` | 521 | 538 | 18 | inferred_complete_timeline |
| `Action_None` | 541 | 569 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_KickApproach` | 33 | 72 | 40 | inferred_complete_timeline |
| `Action_KickBall` | 73 | 77 | 5 | inferred_complete_timeline |
| `Action_None` | 78 | 558 | 481 | inferred_complete_timeline |
| `Action_None` | 561 | 567 | 7 | inferred_complete_timeline |
| `Action_None` | 569 | 569 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 566

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 554 | 522 | inferred_complete_timeline |
| `Action_None` | 559 | 569 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 218 | 186 | inferred_complete_timeline |
| `Action_None` | 230 | 265 | 36 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |
| `Action_None` | 275 | 450 | 176 | inferred_complete_timeline |
| `Action_None` | 459 | 480 | 22 | inferred_complete_timeline |
| `Action_None` | 485 | 495 | 11 | inferred_complete_timeline |
| `Action_None` | 499 | 500 | 2 | inferred_complete_timeline |
| `Action_None` | 504 | 508 | 5 | inferred_complete_timeline |
| `Action_None` | 511 | 569 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 549 | 517 | inferred_complete_timeline |
| `Action_None` | 553 | 558 | 6 | inferred_complete_timeline |
| `Action_None` | 563 | 569 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 240 | 208 | inferred_complete_timeline |
| `Action_None` | 248 | 251 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 564

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 151 | 119 | inferred_complete_timeline |
| `Action_None` | 154 | 438 | 285 | inferred_complete_timeline |
| `Action_None` | 443 | 569 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–566
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 566 | 534 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–325 | 326 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–569 | 566 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–569 | 564 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–569 | 554 | 12 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 112–113 | 2 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 127–170 | 12 | 5 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 173–207 | 20 | 3 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 246–247 | 2 | 1 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 264–275 | 7 | 2 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 295–561 | 267 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 297–569 | 264 | 4 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 308–569 | 256 | 4 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 319–569 | 244 | 3 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 339–569 | 230 | 2 | Undefined position; Undefined team |
| `32` | `53` | Position_Unknown | Team_Unknown | 423–439 | 9 | 2 | Undefined position; Undefined team |
| `33` | `54` | Position_Unknown | Team_Unknown | 436–438 | 3 | 1 | Undefined position; Undefined team |
| `34` | `58` | Position_Unknown | Team_Unknown | 489–529 | 41 | 1 | Undefined position; Undefined team |
| `35` | `59` | Position_Unknown | Team_Unknown | 489–540 | 16 | 5 | Undefined position; Undefined team |
| `36` | `60` | Position_Unknown | Team_Unknown | 491–531 | 32 | 3 | Undefined position; Undefined team |
| `37` | `61` | Position_Unknown | Team_Unknown | 508–519 | 6 | 3 | Undefined position; Undefined team |
| `38` | `65` | Position_Unknown | Team_Unknown | 516–562 | 40 | 5 | Undefined position; Undefined team |
| `39` | `68` | Position_Unknown | Team_Unknown | 521–569 | 44 | 2 | Undefined position; Undefined team |
| `40` | `73` | Position_Unknown | Team_Unknown | 526–558 | 31 | 2 | Undefined position; Undefined team |
| `41` | `75` | Position_Unknown | Team_Unknown | 528–556 | 25 | 2 | Undefined position; Undefined team |
| `42` | `78` | Position_Unknown | Team_Unknown | 529–560 | 26 | 3 | Undefined position; Undefined team |
| `43` | `80` | Position_Unknown | Team_Unknown | 530–546 | 14 | 3 | Undefined position; Undefined team |
| `44` | `81` | Position_Unknown | Team_Unknown | 530–537 | 6 | 2 | Undefined position; Undefined team |
| `45` | `83` | Position_Unknown | Team_Unknown | 530–569 | 8 | 3 | Undefined position; Undefined team |
| `46` | `91` | Position_Unknown | Team_Unknown | 545–548 | 4 | 1 | Undefined position; Undefined team |
| `47` | `93` | Position_Unknown | Team_Unknown | 548–550 | 3 | 1 | Undefined position; Undefined team |
| `48` | `94` | Position_Unknown | Team_Unknown | 555–560 | 6 | 1 | Undefined position; Undefined team |
| `49` | `95` | Position_Unknown | Team_Unknown | 555–569 | 11 | 2 | Undefined position; Undefined team |
| `50` | `98` | Position_Unknown | Team_Unknown | 565–569 | 5 | 1 | Undefined position; Undefined team |
| `51` | `99` | Position_Unknown | Team_Unknown | 567–569 | 3 | 1 | Undefined position; Undefined team |
| `52` | `100` | Position_Unknown | Team_Unknown | 569–569 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 136 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action 'Action_None' range [33-554] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-323] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-566] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-218] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-265] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-450] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-480] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-495] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-508] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-569] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-151] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-438] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-233] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-272] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-315] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-249] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-569] for track '6' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-240] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-439] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-248] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-280] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-492] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-508] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-569] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-549] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-558] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-569] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-569] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-312] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-517] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-526] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-560] for track '12' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-566] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-241] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-289] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-298] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-299] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-312] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-558] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-567] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-409] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-416] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-428] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-437] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-446] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-450] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-468] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-474] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-500] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-507] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-512] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-515] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-538] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-325] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-279] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-569] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-291] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-569] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-269] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-118] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [224-309] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [314-323] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [326-393] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [396-405] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-182] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-561] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-316] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-408] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-432] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-569] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-333] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-447] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-450] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-451] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-548] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-569] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-456] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-429] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-438] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-529] for track '34' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-491] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-497] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-514] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-529] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-516] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-531] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-509] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-514] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-519] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-518] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-522] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-535] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-550] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-562] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-562] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-546] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-558] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-550] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-556] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-535] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-550] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-560] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-539] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-542] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-546] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-533] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-531] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-548] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-550] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-560] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-557] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-569] for track '51' has 1 frames without a visible bounding box.
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

</details>