# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_61

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_61`
- **Frame Range:** 0 to 749 (750 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 749
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 174
- **Validation Warnings:** 185
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 157
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `20` | `20` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `20` | `20` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `30` | `26` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `30` | `26` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `49` | `40` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `10` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `11` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `14` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `16` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `18` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `20` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `3` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `4` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `5` | `Group` | 0 | START | 0 | 75 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `4` | `4` | 76 | START | 76 | 129 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `20` | `20` | 100 | END | 100 | 100 |
| ✅ EXACT | `Action_PuntBall` | Punter | `20` | `20` | 130 | START | 130 | 146 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `30` | `26` | 259 | START | 259 | 271 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `30` | `26` | 298 | START | 298 | 404 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `49` | `40` | 725 | START | 725 | 729 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–749
- **Visible Samples:** 738

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 401 | 326 | inferred_complete_timeline |
| `Action_None` | 409 | 539 | 131 | inferred_complete_timeline |
| `Action_None` | 542 | 544 | 3 | inferred_complete_timeline |
| `Action_None` | 548 | 749 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–603
- **Visible Samples:** 603

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 588 | 513 | inferred_complete_timeline |
| `Action_None` | 590 | 603 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–367
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 176 | 101 | inferred_complete_timeline |
| `Action_None` | 178 | 300 | 123 | inferred_complete_timeline |
| `Action_None` | 322 | 326 | 5 | inferred_complete_timeline |
| `Action_None` | 365 | 367 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 211 | 136 | inferred_complete_timeline |
| `Action_None` | 216 | 252 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–749
- **Visible Samples:** 731

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_LongSnap` | 76 | 129 | 54 | inferred_complete_timeline |
| `Action_None` | 130 | 236 | 107 | inferred_complete_timeline |
| `Action_None` | 241 | 507 | 267 | inferred_complete_timeline |
| `Action_None` | 512 | 528 | 17 | inferred_complete_timeline |
| `Action_None` | 538 | 542 | 5 | inferred_complete_timeline |
| `Action_None` | 544 | 557 | 14 | inferred_complete_timeline |
| `Action_None` | 559 | 749 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–749
- **Visible Samples:** 738

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 375 | 300 | inferred_complete_timeline |
| `Action_None` | 388 | 749 | 362 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–749
- **Visible Samples:** 745

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 470 | 395 | inferred_complete_timeline |
| `Action_None` | 476 | 749 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–749
- **Visible Samples:** 734

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_SnapReceive` | 100 | 100 | 1 | inferred_complete_timeline |
| `Action_None` | 101 | 129 | 29 | inferred_complete_timeline |
| `Action_PuntBall` | 130 | 146 | 17 | inferred_complete_timeline |
| `Action_None` | 147 | 270 | 124 | inferred_complete_timeline |
| `Action_None` | 276 | 465 | 190 | inferred_complete_timeline |
| `Action_None` | 470 | 473 | 4 | inferred_complete_timeline |
| `Action_None` | 476 | 477 | 2 | inferred_complete_timeline |
| `Action_None` | 479 | 551 | 73 | inferred_complete_timeline |
| `Action_None` | 553 | 561 | 9 | inferred_complete_timeline |
| `Action_None` | 565 | 749 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–749
- **Visible Samples:** 731

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 147 | 72 | inferred_complete_timeline |
| `Action_None` | 149 | 166 | 18 | inferred_complete_timeline |
| `Action_None` | 169 | 626 | 458 | inferred_complete_timeline |
| `Action_None` | 635 | 640 | 6 | inferred_complete_timeline |
| `Action_None` | 646 | 648 | 3 | inferred_complete_timeline |
| `Action_None` | 652 | 749 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 121 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–721
- **Visible Samples:** 715

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 381 | 306 | inferred_complete_timeline |
| `Action_None` | 385 | 430 | 46 | inferred_complete_timeline |
| `Action_None` | 432 | 569 | 138 | inferred_complete_timeline |
| `Action_None` | 573 | 721 | 149 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 155 | 80 | inferred_complete_timeline |
| `Action_None` | 175 | 185 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–749
- **Visible Samples:** 729

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 174 | 99 | inferred_complete_timeline |
| `Action_None` | 185 | 412 | 228 | inferred_complete_timeline |
| `Action_None` | 423 | 479 | 57 | inferred_complete_timeline |
| `Action_None` | 481 | 749 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–749
- **Visible Samples:** 688

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 105 | 30 | inferred_complete_timeline |
| `Action_None` | 110 | 129 | 20 | inferred_complete_timeline |
| `Action_None` | 159 | 164 | 6 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 186 | 13 | inferred_complete_timeline |
| `Action_None` | 190 | 322 | 133 | inferred_complete_timeline |
| `Action_None` | 332 | 333 | 2 | inferred_complete_timeline |
| `Action_None` | 337 | 340 | 4 | inferred_complete_timeline |
| `Action_None` | 342 | 347 | 6 | inferred_complete_timeline |
| `Action_None` | 350 | 530 | 181 | inferred_complete_timeline |
| `Action_None` | 535 | 749 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–732
- **Visible Samples:** 733

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 732 | 657 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 132 | 57 | inferred_complete_timeline |
| `Action_None` | 134 | 137 | 4 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–749
- **Visible Samples:** 750

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 749 | 674 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–749
- **Visible Samples:** 750

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 749 | 674 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–749
- **Visible Samples:** 739

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 537 | 462 | inferred_complete_timeline |
| `Action_None` | 539 | 542 | 4 | inferred_complete_timeline |
| `Action_None` | 546 | 559 | 14 | inferred_complete_timeline |
| `Action_None` | 562 | 563 | 2 | inferred_complete_timeline |
| `Action_None` | 565 | 624 | 60 | inferred_complete_timeline |
| `Action_None` | 627 | 628 | 2 | inferred_complete_timeline |
| `Action_None` | 630 | 633 | 4 | inferred_complete_timeline |
| `Action_None` | 635 | 749 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–478
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 248 | 173 | inferred_complete_timeline |
| `Action_None` | 250 | 478 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–707
- **Visible Samples:** 695

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 154 | 79 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 316 | 154 | inferred_complete_timeline |
| `Action_None` | 318 | 324 | 7 | inferred_complete_timeline |
| `Action_None` | 329 | 703 | 375 | inferred_complete_timeline |
| `Action_None` | 706 | 707 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 132–155 | 21 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 140–487 | 281 | 9 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 144–749 | 566 | 6 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 193–749 | 536 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 208–215 | 7 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 232–668 | 436 | 5 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 249–260 | 7 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 266–749 | 479 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 354–366 | 9 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 416–417 | 2 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 419–749 | 330 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 425–426 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 449–505 | 37 | 7 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 466–749 | 284 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 480–485 | 6 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 497–749 | 219 | 7 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 569–573 | 5 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 581–618 | 16 | 4 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 610–749 | 140 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 673–749 | 75 | 3 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 707–708 | 2 | 1 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 719–726 | 7 | 2 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 746–749 | 4 | 1 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 748–749 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `30` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Punter` position mapped to `offense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 134 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 749 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [76-588] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-603] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-154] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-316] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-324] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-703] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [706-707] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-749] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-121] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-236] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-507] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-528] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-542] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-557] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-375] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-174] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-412] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-479] for track '6' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-537] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-542] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-559] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-563] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-624] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-628] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [630-633] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-185] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-732] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-381] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-430] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-569] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-721] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-470] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-749] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-105] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-186] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-322] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-340] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-347] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-530] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-749] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-211] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-252] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-401] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-539] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-544] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-749] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-147] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-166] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-626] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-640] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-648] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-248] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-478] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-300] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-326] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-367] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-132] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [130-146] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-270] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-465] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-473] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-551] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-561] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-160] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-178] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-227] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-241] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-283] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-487] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-172] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-457] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-489] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-544] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-741] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [748-749] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-622] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-655] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [659-662] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [667-680] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [686-749] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [298-404] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [406-668] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-534] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-358] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-366] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-422] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-450] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-459] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-468] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-472] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-485] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-496] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-505] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-485] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-600] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-624] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-647] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [649-650] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [674-701] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [706-744] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-573] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-585] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-589] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-600] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-618] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [673-724] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [725-729] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [732-749] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [707-708] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [719-722] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [724-726] for track '42' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>