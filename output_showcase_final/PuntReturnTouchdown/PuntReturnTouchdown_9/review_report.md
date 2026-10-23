# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_9`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 163
- **Validation Warnings:** 181
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 147
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `1` | `1` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `1` | `1` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `27` | `26` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `27` | `26` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `27` | `26` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner3 | `0` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `1` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner1 | `10` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `11` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `16` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `17` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `18` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `19` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner2 | `4` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `9` | `Group` | 0 | START | 0 | 96 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `19` | `19` | 97 | START | 97 | 153 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `1` | `1` | 128 | END | 128 | 128 |
| ✅ EXACT | `Action_PuntBall` | Punter | `1` | `1` | 154 | START | 154 | 166 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `27` | `26` | 276 | START | 276 | 283 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `27` | `26` | 299 | START | 300 | 301 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `27` | `26` | 649 | START | 649 | 655 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–653
- **Visible Samples:** 636

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 423 | 327 | inferred_complete_timeline |
| `Action_None` | 426 | 450 | 25 | inferred_complete_timeline |
| `Action_None` | 453 | 485 | 33 | inferred_complete_timeline |
| `Action_None` | 490 | 491 | 2 | inferred_complete_timeline |
| `Action_None` | 498 | 499 | 2 | inferred_complete_timeline |
| `Action_None` | 504 | 653 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–491
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 146 | 50 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 164 | 11 | inferred_complete_timeline |
| `Action_None` | 166 | 212 | 47 | inferred_complete_timeline |
| `Action_None` | 221 | 491 | 271 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 175 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–414
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_LongSnap` | 97 | 153 | 57 | inferred_complete_timeline |
| `Action_None` | 154 | 166 | 13 | inferred_complete_timeline |
| `Action_None` | 171 | 256 | 86 | inferred_complete_timeline |
| `Action_None` | 260 | 283 | 24 | inferred_complete_timeline |
| `Action_None` | 288 | 414 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 216 | 120 | inferred_complete_timeline |
| `Action_None` | 220 | 244 | 25 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 656

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 340 | 244 | inferred_complete_timeline |
| `Action_None` | 344 | 505 | 162 | inferred_complete_timeline |
| `Action_None` | 507 | 659 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_SnapReceive` | 128 | 128 | 1 | inferred_complete_timeline |
| `Action_None` | 129 | 153 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 154 | 166 | 13 | inferred_complete_timeline |
| `Action_None` | 167 | 221 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–573
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 272 | 176 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 293 | 6 | inferred_complete_timeline |
| `Action_None` | 296 | 310 | 15 | inferred_complete_timeline |
| `Action_None` | 313 | 396 | 84 | inferred_complete_timeline |
| `Action_None` | 399 | 407 | 9 | inferred_complete_timeline |
| `Action_None` | 410 | 414 | 5 | inferred_complete_timeline |
| `Action_None` | 418 | 419 | 2 | inferred_complete_timeline |
| `Action_None` | 425 | 426 | 2 | inferred_complete_timeline |
| `Action_None` | 430 | 432 | 3 | inferred_complete_timeline |
| `Action_None` | 438 | 439 | 2 | inferred_complete_timeline |
| `Action_None` | 441 | 445 | 5 | inferred_complete_timeline |
| `Action_None` | 449 | 573 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 217 | 121 | inferred_complete_timeline |
| `Action_None` | 219 | 222 | 4 | inferred_complete_timeline |
| `Action_None` | 231 | 267 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–573
- **Visible Samples:** 572

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 219 | 123 | inferred_complete_timeline |
| `Action_None` | 222 | 573 | 352 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–454
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 245 | 149 | inferred_complete_timeline |
| `Action_None` | 247 | 454 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–541
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 403 | 307 | inferred_complete_timeline |
| `Action_None` | 413 | 414 | 2 | inferred_complete_timeline |
| `Action_None` | 444 | 541 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 637

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 136 | 40 | inferred_complete_timeline |
| `Action_None` | 138 | 245 | 108 | inferred_complete_timeline |
| `Action_None` | 248 | 256 | 9 | inferred_complete_timeline |
| `Action_None` | 267 | 480 | 214 | inferred_complete_timeline |
| `Action_None` | 482 | 489 | 8 | inferred_complete_timeline |
| `Action_None` | 491 | 492 | 2 | inferred_complete_timeline |
| `Action_None` | 500 | 505 | 6 | inferred_complete_timeline |
| `Action_None` | 507 | 659 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 646

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 214 | 118 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 393 | 170 | inferred_complete_timeline |
| `Action_None` | 395 | 480 | 86 | inferred_complete_timeline |
| `Action_None` | 482 | 494 | 13 | inferred_complete_timeline |
| `Action_None` | 496 | 504 | 9 | inferred_complete_timeline |
| `Action_None` | 509 | 659 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 186 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 649

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 297 | 201 | inferred_complete_timeline |
| `Action_None` | 299 | 474 | 176 | inferred_complete_timeline |
| `Action_None` | 476 | 487 | 12 | inferred_complete_timeline |
| `Action_None` | 497 | 659 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 660

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 659 | 563 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–649
- **Visible Samples:** 649

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 233 | 137 | inferred_complete_timeline |
| `Action_None` | 235 | 649 | 415 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 623

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 210 | 114 | inferred_complete_timeline |
| `Action_None` | 216 | 252 | 37 | inferred_complete_timeline |
| `Action_None` | 258 | 263 | 6 | inferred_complete_timeline |
| `Action_None` | 267 | 297 | 31 | inferred_complete_timeline |
| `Action_None` | 299 | 427 | 129 | inferred_complete_timeline |
| `Action_None` | 432 | 485 | 54 | inferred_complete_timeline |
| `Action_None` | 500 | 502 | 3 | inferred_complete_timeline |
| `Action_None` | 507 | 508 | 2 | inferred_complete_timeline |
| `Action_None` | 510 | 659 | 150 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–406 | 405 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 3–340 | 333 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 179–644 | 461 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 195–196 | 2 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 208–232 | 19 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 217–235 | 19 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 225–659 | 427 | 10 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 256–262 | 7 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 273–637 | 349 | 3 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 286–381 | 95 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 319–351 | 16 | 5 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 330–399 | 60 | 2 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 337–364 | 10 | 2 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 352–659 | 305 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 374–375 | 2 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 377–406 | 29 | 2 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 390–652 | 254 | 3 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 430–659 | 228 | 3 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 433–577 | 145 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 442–563 | 122 | 1 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 443–659 | 207 | 4 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 497–498 | 2 | 1 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 502–649 | 148 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `27` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Jammer5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Jammer4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Jammer3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 129 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 17: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [97-219] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-573] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-252] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-263] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-297] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-427] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-485] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-502] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-508] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-233] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-649] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-217] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-267] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-214] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-393] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-480] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-494] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-504] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-659] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-297] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-474] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-487] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-216] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-244] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-272] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-293] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-310] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-396] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-407] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-414] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-432] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-445] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-573] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-340] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-505] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-659] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-256] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-480] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-489] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-505] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-659] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-403] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-414] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-541] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-402] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-245] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-454] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-212] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-491] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-423] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-450] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-485] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-499] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-653] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-256] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-283] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-414] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-30] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-192] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-268] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-340] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-248] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-258] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-439] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-644] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-214] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-223] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-235] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-297] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [300-301] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [303-304] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [306-311] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [313-401] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [405-648] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-262] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-414] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-494] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-637] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-290] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-381] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-376] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-399] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-364] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-648] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-403] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-572] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-604] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-652] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-447] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-517] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-577] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-563] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-445] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-451] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-459] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-498] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-649] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>