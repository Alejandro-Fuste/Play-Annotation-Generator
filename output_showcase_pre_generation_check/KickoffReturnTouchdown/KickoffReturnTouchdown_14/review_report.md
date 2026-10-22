# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_14

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_14`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 689
- **Player Tracks:** 57
- **Ball Tracks:** 0
- **Action Segments:** 220
- **Validation Warnings:** 253
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
- **Inferred Coverage Segments (Action_None):** 200
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `6` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | defense | `13` | `13` |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner2 | defense | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner2 | defense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `10` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `11` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `14` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `15` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `16` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `17` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `18` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `20` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `21` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `5` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `6` | `Group` | 0 | START | 0 | 65 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `5` | `5` | 66 | START | 66 | 128 |
| ✅ EXACT | `Action_KickBall` | Kicker | `5` | `5` | 129 | START | 129 | 133 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | `13` | `13` | 254 | START | 254 | 259 |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner2 | `13` | `13` | 270 | START | 270 | 375 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner2 | `13` | `13` | 658 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–437
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_KickApproach` | 66 | 128 | 63 | inferred_complete_timeline |
| `Action_KickBall` | 129 | 133 | 5 | inferred_complete_timeline |
| `Action_None` | 134 | 275 | 142 | inferred_complete_timeline |
| `Action_None` | 286 | 288 | 3 | inferred_complete_timeline |
| `Action_None` | 291 | 432 | 142 | inferred_complete_timeline |
| `Action_None` | 434 | 437 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 665

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 139 | 74 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 187 | 34 | inferred_complete_timeline |
| `Action_None` | 189 | 432 | 244 | inferred_complete_timeline |
| `Action_None` | 444 | 616 | 173 | inferred_complete_timeline |
| `Action_None` | 618 | 689 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 684

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 464 | 399 | inferred_complete_timeline |
| `Action_None` | 466 | 584 | 119 | inferred_complete_timeline |
| `Action_None` | 590 | 689 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 674

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 35 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 65 | 29 | inferred_complete_timeline |
| `Action_None` | 66 | 111 | 46 | inferred_complete_timeline |
| `Action_None` | 114 | 287 | 174 | inferred_complete_timeline |
| `Action_None` | 292 | 443 | 152 | inferred_complete_timeline |
| `Action_None` | 445 | 689 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 689

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 456 | 391 | inferred_complete_timeline |
| `Action_None` | 458 | 689 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 687

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 253 | 188 | inferred_complete_timeline |
| `Action_None` | 257 | 689 | 433 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 17 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 56 | 34 | inferred_complete_timeline |
| `Action_None` | 71 | 253 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 685

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 330 | 265 | inferred_complete_timeline |
| `Action_None` | 332 | 380 | 49 | inferred_complete_timeline |
| `Action_None` | 385 | 689 | 305 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–356
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 249 | 184 | inferred_complete_timeline |
| `Action_None` | 252 | 318 | 67 | inferred_complete_timeline |
| `Action_None` | 321 | 328 | 8 | inferred_complete_timeline |
| `Action_None` | 330 | 331 | 2 | inferred_complete_timeline |
| `Action_None` | 355 | 356 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 676

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 371 | 306 | inferred_complete_timeline |
| `Action_None` | 379 | 616 | 238 | inferred_complete_timeline |
| `Action_None` | 621 | 667 | 47 | inferred_complete_timeline |
| `Action_None` | 671 | 689 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 672

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 171 | 106 | inferred_complete_timeline |
| `Action_None` | 181 | 386 | 206 | inferred_complete_timeline |
| `Action_None` | 390 | 411 | 22 | inferred_complete_timeline |
| `Action_None` | 418 | 689 | 272 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 683

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 304 | 239 | inferred_complete_timeline |
| `Action_None` | 306 | 309 | 4 | inferred_complete_timeline |
| `Action_None` | 311 | 312 | 2 | inferred_complete_timeline |
| `Action_None` | 318 | 689 | 372 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 65 | 62 | inferred_complete_timeline |
| `Action_None` | 66 | 145 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–398
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 218 | 153 | inferred_complete_timeline |
| `Action_None` | 221 | 372 | 152 | inferred_complete_timeline |
| `Action_None` | 375 | 398 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–332
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 226 | 161 | inferred_complete_timeline |
| `Action_None` | 228 | 232 | 5 | inferred_complete_timeline |
| `Action_None` | 234 | 332 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–455
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 455 | 390 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–375
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |
| `Action_CatchKick` | 254 | 259 | 6 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 270 | 375 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 689 | 624 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 687

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 424 | 359 | inferred_complete_timeline |
| `Action_None` | 428 | 689 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 183 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 664

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 382 | 317 | inferred_complete_timeline |
| `Action_None` | 386 | 390 | 5 | inferred_complete_timeline |
| `Action_None` | 406 | 604 | 199 | inferred_complete_timeline |
| `Action_None` | 613 | 689 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 688

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 645 | 580 | inferred_complete_timeline |
| `Action_None` | 648 | 689 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–240 | 184 | 9 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 3–63 | 15 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 107–250 | 59 | 8 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 135–339 | 176 | 13 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 164–442 | 260 | 8 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 187–421 | 234 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 196–285 | 82 | 4 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 201–251 | 51 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 211–259 | 37 | 6 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 219–323 | 20 | 5 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 224–269 | 23 | 4 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 240–272 | 22 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 244–253 | 4 | 2 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 340–466 | 121 | 6 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 357–358 | 2 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 363–393 | 31 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 366–689 | 323 | 2 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 371–548 | 168 | 2 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 376–689 | 304 | 3 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 409–689 | 281 | 1 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 428–656 | 228 | 2 | Undefined position; Undefined team |
| `44` | `66` | Position_Unknown | Team_Unknown | 429–594 | 166 | 1 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 431–596 | 48 | 15 | Undefined position; Undefined team |
| `46` | `68` | Position_Unknown | Team_Unknown | 433–689 | 254 | 3 | Undefined position; Undefined team |
| `47` | `69` | Position_Unknown | Team_Unknown | 441–689 | 244 | 3 | Undefined position; Undefined team |
| `48` | `72` | Position_Unknown | Team_Unknown | 478–689 | 211 | 2 | Undefined position; Undefined team |
| `49` | `75` | Position_Unknown | Team_Unknown | 491–689 | 161 | 6 | Undefined position; Undefined team |
| `50` | `77` | Position_Unknown | Team_Unknown | 503–515 | 12 | 2 | Undefined position; Undefined team |
| `51` | `79` | Position_Unknown | Team_Unknown | 527–656 | 127 | 2 | Undefined position; Undefined team |
| `52` | `81` | Position_Unknown | Team_Unknown | 533–540 | 8 | 1 | Undefined position; Undefined team |
| `53` | `87` | Position_Unknown | Team_Unknown | 625–629 | 4 | 2 | Undefined position; Undefined team |
| `54` | `88` | Position_Unknown | Team_Unknown | 627–689 | 44 | 3 | Undefined position; Undefined team |
| `55` | `89` | Position_Unknown | Team_Unknown | 649–650 | 2 | 1 | Undefined position; Undefined team |
| `56` | `91` | Position_Unknown | Team_Unknown | 666–670 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CrossGoalLine` on target `13` (Kick_Returner2)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `22` (actor_track_id `22`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ 35 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 35 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 70 |
| Missing visible bounding boxes during action | 180 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 30: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '13' has invalid range: start=658, end=375. Clamping end to start.
- ⚠️ Action 'Action_None' range [66-645] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-382] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-390] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-604] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-424] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-689] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-183] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-455] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-275] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-432] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-437] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-330] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-380] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-689] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-226] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-332] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-218] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-372] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-398] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-456] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-253] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-689] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-304] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-309] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-689] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [270-375] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-249] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-318] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-328] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-171] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-386] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-411] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-689] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-187] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-432] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-616] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-689] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-464] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-584] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-371] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-616] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-667] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-160] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-287] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-443] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-17] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-21] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-56] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-253] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-145] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-11] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-63] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-178] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-221] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-234] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-144] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-165] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-211] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-219] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-230] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-250] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-273] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-300] for track '25' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-313] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-328] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-285] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-339] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-388] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-442] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-404] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-421] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-268] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-251] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-221] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-251] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-284] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-234] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-250] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-259] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-406] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-433] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-451] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-457] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-461] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-466] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-393] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-659] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-407] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-548] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-395] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-456] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-689] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-470] for track '43' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-656] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-594] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-433] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-444] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-515] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-520] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-523] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-530] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-538] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-553] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-562] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-571] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-579] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-589] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-596] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-622] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-659] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-537] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-543] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-515] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-494] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-513] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-522] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-529] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-505] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-515] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-645] for track '51' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [649-656] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-540] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-626] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-629] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-648] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [665-667] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [649-650] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [666-670] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>