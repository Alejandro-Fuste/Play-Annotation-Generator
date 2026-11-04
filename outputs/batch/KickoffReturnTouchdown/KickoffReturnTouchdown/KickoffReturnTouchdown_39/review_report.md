# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_39

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_39`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 76
- **Ball Tracks:** 0
- **Action Segments:** 269
- **Validation Warnings:** 359
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 258
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_KickBall` | Kicker | offense | `8` | `8` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | defense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | defense | `13` | `13` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner2 | defense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `0` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `10` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `12` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `14` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `15` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `4` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `8` | `Group` | 0 | START | 0 | 45 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `8` | `8` | 46 | START | 46 | 95 |
| ❌ MISSING SEGMENT | `Action_KickBall` | Kicker | `8` | `8` | 127 | START | N/A | N/A |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | `13` | `13` | 245 | START | 245 | 256 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | `13` | `13` | 266 | START | 266 | 295 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner2 | `13` | `13` | 623 | START | 623 | 629 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_KickApproach` | 46 | 95 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–568
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 568 | 523 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 96 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 619

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 106 | 61 | inferred_complete_timeline |
| `Action_None` | 113 | 115 | 3 | inferred_complete_timeline |
| `Action_None` | 117 | 138 | 22 | inferred_complete_timeline |
| `Action_None` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_None` | 145 | 174 | 30 | inferred_complete_timeline |
| `Action_None` | 176 | 629 | 454 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–626
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 106 | 61 | inferred_complete_timeline |
| `Action_None` | 109 | 115 | 7 | inferred_complete_timeline |
| `Action_None` | 117 | 144 | 28 | inferred_complete_timeline |
| `Action_None` | 147 | 306 | 160 | inferred_complete_timeline |
| `Action_None` | 308 | 311 | 4 | inferred_complete_timeline |
| `Action_None` | 347 | 626 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 92 | 47 | inferred_complete_timeline |
| `Action_None` | 105 | 110 | 6 | inferred_complete_timeline |
| `Action_None` | 114 | 124 | 11 | inferred_complete_timeline |
| `Action_None` | 143 | 507 | 365 | inferred_complete_timeline |
| `Action_None` | 516 | 608 | 93 | inferred_complete_timeline |
| `Action_None` | 611 | 629 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 65 | 20 | inferred_complete_timeline |
| `Action_None` | 68 | 72 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–622
- **Visible Samples:** 581

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 228 | 183 | inferred_complete_timeline |
| `Action_None` | 230 | 238 | 9 | inferred_complete_timeline |
| `Action_None` | 240 | 243 | 4 | inferred_complete_timeline |
| `Action_None` | 245 | 251 | 7 | inferred_complete_timeline |
| `Action_None` | 258 | 274 | 17 | inferred_complete_timeline |
| `Action_None` | 282 | 590 | 309 | inferred_complete_timeline |
| `Action_None` | 601 | 602 | 2 | inferred_complete_timeline |
| `Action_None` | 613 | 614 | 2 | inferred_complete_timeline |
| `Action_None` | 621 | 622 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 626

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 230 | 185 | inferred_complete_timeline |
| `Action_None` | 235 | 629 | 395 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 624

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 258 | 213 | inferred_complete_timeline |
| `Action_None` | 264 | 266 | 3 | inferred_complete_timeline |
| `Action_None` | 268 | 629 | 362 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 224 | 179 | inferred_complete_timeline |
| `Action_None` | 234 | 281 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 629 | 584 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 588

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 29 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 167 | 136 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 244 | 56 | inferred_complete_timeline |
| `Action_CatchKick` | 245 | 256 | 12 | inferred_complete_timeline |
| `Action_None` | 257 | 265 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 266 | 295 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 309 | 594 | 286 | inferred_complete_timeline |
| `Action_BallCarry` | 597 | 606 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 617 | 622 | 6 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 623 | 629 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 616

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 336 | 291 | inferred_complete_timeline |
| `Action_None` | 346 | 588 | 243 | inferred_complete_timeline |
| `Action_None` | 593 | 622 | 30 | inferred_complete_timeline |
| `Action_None` | 624 | 629 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–598
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 201 | 156 | inferred_complete_timeline |
| `Action_None` | 203 | 206 | 4 | inferred_complete_timeline |
| `Action_None` | 209 | 320 | 112 | inferred_complete_timeline |
| `Action_None` | 323 | 598 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–344
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 150 | 105 | inferred_complete_timeline |
| `Action_None` | 153 | 235 | 83 | inferred_complete_timeline |
| `Action_None` | 237 | 341 | 105 | inferred_complete_timeline |
| `Action_None` | 343 | 344 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 4–228 | 161 | 7 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 119–629 | 480 | 10 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 143–629 | 468 | 7 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 146–629 | 473 | 7 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 147–284 | 125 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 152–154 | 3 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 153–154 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 159–629 | 469 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 159–629 | 455 | 5 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 168–170 | 3 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 177–216 | 23 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 182–203 | 8 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 184–629 | 420 | 8 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 190–258 | 39 | 5 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 200–203 | 4 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 210–629 | 420 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 217–226 | 6 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 217–219 | 3 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 250–251 | 2 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 253–290 | 13 | 3 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 282–624 | 342 | 2 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 289–292 | 4 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 294–363 | 70 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 296–629 | 322 | 6 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 332–333 | 2 | 1 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 340–629 | 263 | 3 | Undefined position; Undefined team |
| `43` | `63` | Position_Unknown | Team_Unknown | 362–371 | 7 | 2 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 367–629 | 260 | 3 | Undefined position; Undefined team |
| `45` | `66` | Position_Unknown | Team_Unknown | 377–378 | 2 | 1 | Undefined position; Undefined team |
| `46` | `68` | Position_Unknown | Team_Unknown | 398–401 | 4 | 1 | Undefined position; Undefined team |
| `47` | `70` | Position_Unknown | Team_Unknown | 416–417 | 2 | 1 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 417–423 | 6 | 2 | Undefined position; Undefined team |
| `49` | `76` | Position_Unknown | Team_Unknown | 459–536 | 49 | 8 | Undefined position; Undefined team |
| `50` | `78` | Position_Unknown | Team_Unknown | 468–611 | 79 | 13 | Undefined position; Undefined team |
| `51` | `82` | Position_Unknown | Team_Unknown | 478–537 | 44 | 6 | Undefined position; Undefined team |
| `52` | `83` | Position_Unknown | Team_Unknown | 486–629 | 118 | 8 | Undefined position; Undefined team |
| `53` | `85` | Position_Unknown | Team_Unknown | 489–490 | 2 | 1 | Undefined position; Undefined team |
| `54` | `87` | Position_Unknown | Team_Unknown | 503–586 | 30 | 7 | Undefined position; Undefined team |
| `55` | `90` | Position_Unknown | Team_Unknown | 527–572 | 25 | 4 | Undefined position; Undefined team |
| `56` | `91` | Position_Unknown | Team_Unknown | 528–582 | 40 | 3 | Undefined position; Undefined team |
| `57` | `97` | Position_Unknown | Team_Unknown | 543–589 | 7 | 2 | Undefined position; Undefined team |
| `58` | `98` | Position_Unknown | Team_Unknown | 547–591 | 44 | 2 | Undefined position; Undefined team |
| `59` | `99` | Position_Unknown | Team_Unknown | 550–580 | 16 | 3 | Undefined position; Undefined team |
| `60` | `100` | Position_Unknown | Team_Unknown | 563–628 | 38 | 7 | Undefined position; Undefined team |
| `61` | `103` | Position_Unknown | Team_Unknown | 571–573 | 3 | 1 | Undefined position; Undefined team |
| `62` | `107` | Position_Unknown | Team_Unknown | 581–629 | 25 | 3 | Undefined position; Undefined team |
| `63` | `109` | Position_Unknown | Team_Unknown | 600–627 | 19 | 4 | Undefined position; Undefined team |
| `64` | `112` | Position_Unknown | Team_Unknown | 603–617 | 15 | 1 | Undefined position; Undefined team |
| `65` | `116` | Position_Unknown | Team_Unknown | 606–629 | 11 | 3 | Undefined position; Undefined team |
| `66` | `120` | Position_Unknown | Team_Unknown | 609–628 | 17 | 3 | Undefined position; Undefined team |
| `67` | `121` | Position_Unknown | Team_Unknown | 610–620 | 6 | 2 | Undefined position; Undefined team |
| `68` | `123` | Position_Unknown | Team_Unknown | 610–611 | 2 | 1 | Undefined position; Undefined team |
| `69` | `124` | Position_Unknown | Team_Unknown | 611–612 | 2 | 1 | Undefined position; Undefined team |
| `70` | `126` | Position_Unknown | Team_Unknown | 616–626 | 10 | 2 | Undefined position; Undefined team |
| `71` | `129` | Position_Unknown | Team_Unknown | 619–623 | 5 | 1 | Undefined position; Undefined team |
| `72` | `132` | Position_Unknown | Team_Unknown | 621–624 | 4 | 1 | Undefined position; Undefined team |
| `73` | `134` | Position_Unknown | Team_Unknown | 622–623 | 2 | 1 | Undefined position; Undefined team |
| `74` | `135` | Position_Unknown | Team_Unknown | 623–629 | 6 | 2 | Undefined position; Undefined team |
| `75` | `138` | Position_Unknown | Team_Unknown | 628–629 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_KickBall` on target `8` (Kicker)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ 60 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 60 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 120 |
| Missing visible bounding boxes during action | 237 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Segment 'Action_KickBall' for track '8' has invalid range: start=127, end=95. Clamping end to start.
- ⚠️ Action 'Action_None' range [46-568] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-228] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-238] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-251] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-274] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-590] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-602] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-614] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-622] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-336] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-588] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-622] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-629] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-124] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-507] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-608] for track '4' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-320] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-598] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-224] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-281] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-629] for track '7' has 10 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [46-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-258] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-629] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-106] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-144] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-306] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-311] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-626] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-235] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-341] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-138] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-174] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-629] for track '12' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-29] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-167] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [266-295] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [309-594] for track '13' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [597-606] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-7] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-25] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-118] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-162] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-228] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-138] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-189] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-414] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-588] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-595] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-606] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-613] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-619] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-152] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-168] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-241] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-352] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-613] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-156] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-232] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-318] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-564] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-605] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-156] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-171] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-284] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-170] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-219] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-241] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-629] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-187] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-203] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-191] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-321] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-395] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-466] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-594] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-598] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-200] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-219] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-237] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-265] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-314] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-624] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-363] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-317] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-323] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-551] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-583] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-588] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-629] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-362] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-365] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-371] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-477] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-401] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-420] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-423] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-467] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-473] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-480] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-488] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-498] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-508] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-522] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-536] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-470] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-474] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-494] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-517] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-538] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-542] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-546] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-556] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-568] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-583] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-590] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-596] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-611] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-495] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-518] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-532] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-537] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-519] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-587] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-594] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-597] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-603] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-613] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-622] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-629] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-490] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-505] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-508] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-526] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-534] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-548] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-569] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-586] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-536] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-550] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-558] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-572] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-532] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-550] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-582] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-546] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-589] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-561] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-591] for track '58' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-554] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-580] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-565] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-572] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-576] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-588] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-613] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-621] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-628] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-573] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-585] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-601] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-629] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-601] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-605] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-611] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-627] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-617] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-609] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-616] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-617] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-622] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-628] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-611] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-620] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-611] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-612] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-623] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-626] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-623] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-624] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-623] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-625] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-629] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.

</details>