# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_13`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 71
- **Ball Tracks:** 0
- **Action Segments:** 210
- **Validation Warnings:** 291
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 196
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_KickBall` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | defense | `45` | `33` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | defense | `45` | `33` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner2 | defense | `45` | `33` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `1` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `11` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `12` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `14` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `16` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `6` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `8` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `9` | `Group` | 0 | START | 0 | 49 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `12` | `12` | 50 | START | 50 | 93 |
| ❌ MISSING SEGMENT | `Action_KickBall` | Kicker | `12` | `12` | 116 | START | N/A | N/A |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | `45` | `33` | 243 | START | 243 | 248 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | `45` | `33` | 257 | START | 257 | 645 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner2 | `45` | `33` | 646 | START | 646 | 658 |

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
- **Visible Frames:** 0–659
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_KickApproach` | 50 | 93 | 44 | inferred_complete_timeline |
| `Action_None` | 159 | 172 | 14 | inferred_complete_timeline |
| `Action_None` | 174 | 329 | 156 | inferred_complete_timeline |
| `Action_None` | 331 | 425 | 95 | inferred_complete_timeline |
| `Action_None` | 427 | 523 | 97 | inferred_complete_timeline |
| `Action_None` | 526 | 528 | 3 | inferred_complete_timeline |
| `Action_None` | 530 | 531 | 2 | inferred_complete_timeline |
| `Action_None` | 533 | 615 | 83 | inferred_complete_timeline |
| `Action_None` | 617 | 659 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 49 | 37 | inferred_complete_timeline |
| `Action_None` | 50 | 77 | 28 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 162 | 113 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 387 | 214 | inferred_complete_timeline |
| `Action_None` | 389 | 390 | 2 | inferred_complete_timeline |
| `Action_None` | 400 | 401 | 2 | inferred_complete_timeline |
| `Action_None` | 410 | 429 | 20 | inferred_complete_timeline |
| `Action_None` | 434 | 564 | 131 | inferred_complete_timeline |
| `Action_None` | 566 | 569 | 4 | inferred_complete_timeline |
| `Action_None` | 571 | 659 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 98 | 49 | inferred_complete_timeline |
| `Action_None` | 101 | 130 | 30 | inferred_complete_timeline |
| `Action_None` | 136 | 147 | 12 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–577
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 122 | 73 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 139 | 5 | inferred_complete_timeline |
| `Action_None` | 142 | 149 | 8 | inferred_complete_timeline |
| `Action_None` | 153 | 172 | 20 | inferred_complete_timeline |
| `Action_None` | 174 | 396 | 223 | inferred_complete_timeline |
| `Action_None` | 398 | 404 | 7 | inferred_complete_timeline |
| `Action_None` | 406 | 465 | 60 | inferred_complete_timeline |
| `Action_None` | 468 | 577 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 92 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 49 | 7 | inferred_complete_timeline |
| `Action_None` | 50 | 89 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 92 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–626
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 626 | 577 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 31 | 12 | inferred_complete_timeline |
| `Action_None` | 114 | 120 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–620
- **Visible Samples:** 621

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 620 | 571 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 639

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 120 | 71 | inferred_complete_timeline |
| `Action_None` | 124 | 131 | 8 | inferred_complete_timeline |
| `Action_None` | 133 | 140 | 8 | inferred_complete_timeline |
| `Action_None` | 142 | 148 | 7 | inferred_complete_timeline |
| `Action_None` | 150 | 334 | 185 | inferred_complete_timeline |
| `Action_None` | 337 | 338 | 2 | inferred_complete_timeline |
| `Action_None` | 340 | 341 | 2 | inferred_complete_timeline |
| `Action_None` | 347 | 383 | 37 | inferred_complete_timeline |
| `Action_None` | 386 | 393 | 8 | inferred_complete_timeline |
| `Action_None` | 395 | 548 | 154 | inferred_complete_timeline |
| `Action_None` | 550 | 555 | 6 | inferred_complete_timeline |
| `Action_None` | 557 | 640 | 84 | inferred_complete_timeline |
| `Action_None` | 642 | 643 | 2 | inferred_complete_timeline |
| `Action_None` | 645 | 659 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `45`</summary>

- **xml_track_id:** `33`
- **actor_track_id:** `45`
- **team_side:** `defense`
- **Visible Frames:** 192–659
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 192 | 242 | 51 | inferred_complete_timeline |
| `Action_CatchKick` | 243 | 248 | 6 | inferred_complete_timeline |
| `Action_None` | 249 | 256 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 257 | 645 | 389 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 646 | 658 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 659 | 659 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–631
- **Visible Samples:** 632

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 631 | 582 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–579
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 149 | 100 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 409 | 250 | inferred_complete_timeline |
| `Action_None` | 411 | 429 | 19 | inferred_complete_timeline |
| `Action_None` | 431 | 579 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 659

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 598 | 549 | inferred_complete_timeline |
| `Action_None` | 600 | 659 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–567
- **Visible Samples:** 564

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 357 | 308 | inferred_complete_timeline |
| `Action_None` | 362 | 567 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–382
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 382 | 333 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 66–130 | 33 | 6 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 100–331 | 232 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 104–105 | 2 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 108–249 | 119 | 5 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 125–383 | 196 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 137–601 | 438 | 7 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 142–356 | 206 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 143–145 | 3 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 163–649 | 486 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 175–410 | 211 | 7 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 177–178 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 177–516 | 337 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 177–181 | 5 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 178–418 | 231 | 6 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 185–225 | 33 | 5 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 190–659 | 470 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 195–196 | 2 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 213–214 | 2 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 277–301 | 21 | 2 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 300–302 | 3 | 1 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 313–318 | 6 | 1 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 338–639 | 293 | 3 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 342–369 | 28 | 1 | Undefined position; Undefined team |
| `41` | `64` | Position_Unknown | Team_Unknown | 342–659 | 268 | 6 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 343–659 | 315 | 2 | Undefined position; Undefined team |
| `43` | `66` | Position_Unknown | Team_Unknown | 355–362 | 8 | 1 | Undefined position; Undefined team |
| `44` | `69` | Position_Unknown | Team_Unknown | 366–377 | 11 | 2 | Undefined position; Undefined team |
| `45` | `70` | Position_Unknown | Team_Unknown | 370–659 | 283 | 3 | Undefined position; Undefined team |
| `46` | `71` | Position_Unknown | Team_Unknown | 373–376 | 4 | 1 | Undefined position; Undefined team |
| `47` | `72` | Position_Unknown | Team_Unknown | 373–426 | 43 | 3 | Undefined position; Undefined team |
| `48` | `74` | Position_Unknown | Team_Unknown | 392–631 | 235 | 2 | Undefined position; Undefined team |
| `49` | `78` | Position_Unknown | Team_Unknown | 410–431 | 10 | 3 | Undefined position; Undefined team |
| `50` | `79` | Position_Unknown | Team_Unknown | 412–415 | 4 | 1 | Undefined position; Undefined team |
| `51` | `81` | Position_Unknown | Team_Unknown | 415–659 | 245 | 1 | Undefined position; Undefined team |
| `52` | `82` | Position_Unknown | Team_Unknown | 417–419 | 3 | 1 | Undefined position; Undefined team |
| `53` | `84` | Position_Unknown | Team_Unknown | 433–434 | 2 | 1 | Undefined position; Undefined team |
| `54` | `85` | Position_Unknown | Team_Unknown | 441–443 | 3 | 1 | Undefined position; Undefined team |
| `55` | `88` | Position_Unknown | Team_Unknown | 442–627 | 186 | 1 | Undefined position; Undefined team |
| `56` | `92` | Position_Unknown | Team_Unknown | 457–608 | 150 | 2 | Undefined position; Undefined team |
| `57` | `98` | Position_Unknown | Team_Unknown | 468–625 | 133 | 8 | Undefined position; Undefined team |
| `58` | `100` | Position_Unknown | Team_Unknown | 475–476 | 2 | 1 | Undefined position; Undefined team |
| `59` | `104` | Position_Unknown | Team_Unknown | 488–489 | 2 | 1 | Undefined position; Undefined team |
| `60` | `106` | Position_Unknown | Team_Unknown | 492–494 | 3 | 1 | Undefined position; Undefined team |
| `61` | `110` | Position_Unknown | Team_Unknown | 515–659 | 145 | 1 | Undefined position; Undefined team |
| `62` | `114` | Position_Unknown | Team_Unknown | 542–604 | 56 | 4 | Undefined position; Undefined team |
| `63` | `115` | Position_Unknown | Team_Unknown | 556–557 | 2 | 1 | Undefined position; Undefined team |
| `64` | `117` | Position_Unknown | Team_Unknown | 560–561 | 2 | 1 | Undefined position; Undefined team |
| `65` | `119` | Position_Unknown | Team_Unknown | 564–567 | 4 | 1 | Undefined position; Undefined team |
| `66` | `121` | Position_Unknown | Team_Unknown | 573–641 | 15 | 2 | Undefined position; Undefined team |
| `67` | `128` | Position_Unknown | Team_Unknown | 634–659 | 26 | 1 | Undefined position; Undefined team |
| `68` | `130` | Position_Unknown | Team_Unknown | 642–649 | 7 | 2 | Undefined position; Undefined team |
| `69` | `131` | Position_Unknown | Team_Unknown | 646–658 | 13 | 1 | Undefined position; Undefined team |
| `70` | `132` | Position_Unknown | Team_Unknown | 654–657 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_KickBall` on target `12` (Kicker)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `45` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Second_Level_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `33` (actor_track_id `45`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ 53 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 53 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 106 |
| Missing visible bounding boxes during action | 184 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action 'Action_None' range [50-626] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-122] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-172] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-396] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-404] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-465] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-577] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-631] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-382] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-598] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-659] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-357] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-567] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-130] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-147] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-620] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-92] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-409] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-429] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-579] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-162] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-387] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-429] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-564] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-569] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-659] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [50-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-172] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-425] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-523] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-528] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-531] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-615] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-131] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-140] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-148] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-334] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-383] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-393] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-548] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-555] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-640] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [642-643] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-77] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-89] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-73] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-94] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-331] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-123] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-249] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-145] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-347] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-147] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-230] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-391] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-601] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-344] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-356] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-350] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-649] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-309] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-392] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-399] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-410] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-184] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-516] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-181] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-188] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-311] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-321] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-367] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-399] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-418] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-192] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-222] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-242] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-285] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-301] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-318] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-587] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-593] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-639] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-369] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-385] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-390] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-417] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-646] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-632] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-362] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-374] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-424] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-609] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-659] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-408] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-422] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-414] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-631] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-425] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-431] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-415] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-659] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-419] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-434] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-443] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-627] for track '55' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-599] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-608] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-512] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-545] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-548] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-562] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-567] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-605] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-615] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-625] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-476] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-489] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-494] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-550] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-567] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-585] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-604] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-557] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-561] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-567] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-576] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-641] for track '66' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [642-645] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-649] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-658] for track '69' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [654-657] for track '70' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.

</details>