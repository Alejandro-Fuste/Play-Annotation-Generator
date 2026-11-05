# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_90

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_90`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 72
- **Ball Tracks:** 1
- **Action Segments:** 214
- **Validation Warnings:** 302
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 201
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `26` | `24` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `26` | `24` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `64` | `45` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `0` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `1` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `2` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `4` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `5` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `6` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `7` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `9` | `Group` | 0 | START | 0 | 49 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `6` | `6` | 50 | START | 50 | 100 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `7` | `7` | 74 | END | 74 | 74 |
| ✅ EXACT | `Action_PuntBall` | Punter | `7` | `7` | 101 | START | 101 | 115 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `26` | `24` | 215 | START | 215 | 224 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `26` | `24` | 242 | START | 242 | 270 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `64` | `45` | 645 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–643
- **Visible Samples:** 637

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 217 | 168 | inferred_complete_timeline |
| `Action_None` | 222 | 354 | 133 | inferred_complete_timeline |
| `Action_None` | 358 | 643 | 286 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 282 | 233 | inferred_complete_timeline |
| `Action_None` | 294 | 307 | 14 | inferred_complete_timeline |
| `Action_None` | 309 | 319 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–471
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_LongSnap` | 50 | 100 | 51 | inferred_complete_timeline |
| `Action_None` | 101 | 282 | 182 | inferred_complete_timeline |
| `Action_None` | 296 | 301 | 6 | inferred_complete_timeline |
| `Action_None` | 307 | 471 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–649
- **Visible Samples:** 637

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 321 | 272 | inferred_complete_timeline |
| `Action_None` | 327 | 328 | 2 | inferred_complete_timeline |
| `Action_None` | 337 | 649 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 648

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 302 | 253 | inferred_complete_timeline |
| `Action_None` | 305 | 311 | 7 | inferred_complete_timeline |
| `Action_None` | 314 | 319 | 6 | inferred_complete_timeline |
| `Action_None` | 322 | 337 | 16 | inferred_complete_timeline |
| `Action_None` | 343 | 346 | 4 | inferred_complete_timeline |
| `Action_None` | 348 | 659 | 312 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–633
- **Visible Samples:** 633

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SnapReceive` | 74 | 74 | 1 | inferred_complete_timeline |
| `Action_None` | 75 | 100 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 101 | 115 | 15 | inferred_complete_timeline |
| `Action_None` | 116 | 621 | 506 | inferred_complete_timeline |
| `Action_None` | 623 | 633 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 649

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 150 | 101 | inferred_complete_timeline |
| `Action_None` | 160 | 192 | 33 | inferred_complete_timeline |
| `Action_None` | 195 | 659 | 465 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 283 | 234 | inferred_complete_timeline |
| `Action_None` | 287 | 302 | 16 | inferred_complete_timeline |
| `Action_None` | 305 | 311 | 7 | inferred_complete_timeline |
| `Action_None` | 314 | 324 | 11 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 634

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 76 | 27 | inferred_complete_timeline |
| `Action_None` | 82 | 90 | 9 | inferred_complete_timeline |
| `Action_None` | 95 | 222 | 128 | inferred_complete_timeline |
| `Action_None` | 224 | 291 | 68 | inferred_complete_timeline |
| `Action_None` | 294 | 300 | 7 | inferred_complete_timeline |
| `Action_None` | 302 | 558 | 257 | inferred_complete_timeline |
| `Action_None` | 560 | 561 | 2 | inferred_complete_timeline |
| `Action_None` | 566 | 606 | 41 | inferred_complete_timeline |
| `Action_None` | 615 | 659 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–492
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 288 | 239 | inferred_complete_timeline |
| `Action_None` | 290 | 302 | 13 | inferred_complete_timeline |
| `Action_None` | 304 | 344 | 41 | inferred_complete_timeline |
| `Action_None` | 361 | 365 | 5 | inferred_complete_timeline |
| `Action_None` | 371 | 492 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 133 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–648
- **Visible Samples:** 619

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 65 | 16 | inferred_complete_timeline |
| `Action_None` | 68 | 73 | 6 | inferred_complete_timeline |
| `Action_None` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_None` | 81 | 284 | 204 | inferred_complete_timeline |
| `Action_None` | 286 | 318 | 33 | inferred_complete_timeline |
| `Action_None` | 321 | 326 | 6 | inferred_complete_timeline |
| `Action_None` | 339 | 341 | 3 | inferred_complete_timeline |
| `Action_None` | 345 | 354 | 10 | inferred_complete_timeline |
| `Action_None` | 361 | 648 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 653

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 310 | 261 | inferred_complete_timeline |
| `Action_None` | 315 | 323 | 9 | inferred_complete_timeline |
| `Action_None` | 326 | 333 | 8 | inferred_complete_timeline |
| `Action_None` | 335 | 659 | 325 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–628
- **Visible Samples:** 622

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 275 | 226 | inferred_complete_timeline |
| `Action_None` | 277 | 281 | 5 | inferred_complete_timeline |
| `Action_None` | 284 | 503 | 220 | inferred_complete_timeline |
| `Action_None` | 508 | 628 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–645
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 177 | 128 | inferred_complete_timeline |
| `Action_None` | 183 | 186 | 4 | inferred_complete_timeline |
| `Action_None` | 189 | 282 | 94 | inferred_complete_timeline |
| `Action_None` | 295 | 297 | 3 | inferred_complete_timeline |
| `Action_None` | 305 | 310 | 6 | inferred_complete_timeline |
| `Action_None` | 314 | 319 | 6 | inferred_complete_timeline |
| `Action_None` | 364 | 367 | 4 | inferred_complete_timeline |
| `Action_None` | 376 | 645 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–641
- **Visible Samples:** 642

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 641 | 592 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–266 | 259 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 91–325 | 231 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 99–659 | 540 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 141–165 | 25 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 164–390 | 227 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 169–481 | 313 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 172–203 | 18 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 178–362 | 95 | 5 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 184–189 | 6 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 190–192 | 3 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 191–209 | 19 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 200–330 | 130 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 209–296 | 64 | 6 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 210–215 | 4 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 235–244 | 7 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 253–276 | 22 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 271–278 | 8 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 275–659 | 377 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 277–278 | 2 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 289–659 | 370 | 2 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 337–352 | 16 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 343–344 | 2 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 346–488 | 136 | 4 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 349–501 | 126 | 4 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 353–463 | 98 | 4 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 372–631 | 260 | 1 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 379–385 | 7 | 1 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 408–409 | 2 | 1 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 452–480 | 23 | 2 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 481–502 | 13 | 2 | Undefined position; Undefined team |
| `47` | `67` | Position_Unknown | Team_Unknown | 491–654 | 146 | 4 | Undefined position; Undefined team |
| `48` | `68` | Position_Unknown | Team_Unknown | 493–659 | 167 | 1 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 509–516 | 7 | 2 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 518–524 | 7 | 1 | Undefined position; Undefined team |
| `51` | `74` | Position_Unknown | Team_Unknown | 532–533 | 2 | 1 | Undefined position; Undefined team |
| `52` | `79` | Position_Unknown | Team_Unknown | 542–611 | 38 | 5 | Undefined position; Undefined team |
| `53` | `80` | Position_Unknown | Team_Unknown | 543–552 | 10 | 1 | Undefined position; Undefined team |
| `54` | `84` | Position_Unknown | Team_Unknown | 545–553 | 9 | 1 | Undefined position; Undefined team |
| `55` | `85` | Position_Unknown | Team_Unknown | 545–628 | 76 | 6 | Undefined position; Undefined team |
| `56` | `88` | Position_Unknown | Team_Unknown | 551–595 | 16 | 4 | Undefined position; Undefined team |
| `57` | `90` | Position_Unknown | Team_Unknown | 553–622 | 69 | 2 | Undefined position; Undefined team |
| `58` | `92` | Position_Unknown | Team_Unknown | 562–631 | 70 | 1 | Undefined position; Undefined team |
| `59` | `93` | Position_Unknown | Team_Unknown | 562–603 | 20 | 6 | Undefined position; Undefined team |
| `60` | `94` | Position_Unknown | Team_Unknown | 562–579 | 15 | 2 | Undefined position; Undefined team |
| `61` | `97` | Position_Unknown | Team_Unknown | 569–591 | 19 | 2 | Undefined position; Undefined team |
| `62` | `100` | Position_Unknown | Team_Unknown | 577–621 | 18 | 5 | Undefined position; Undefined team |
| `63` | `101` | Position_Unknown | Team_Unknown | 577–592 | 10 | 3 | Undefined position; Undefined team |
| `64` | `102` | Position_Unknown | Team_Unknown | 581–582 | 2 | 1 | Undefined position; Undefined team |
| `65` | `103` | Position_Unknown | Team_Unknown | 584–651 | 13 | 2 | Undefined position; Undefined team |
| `66` | `106` | Position_Unknown | Team_Unknown | 594–598 | 5 | 1 | Undefined position; Undefined team |
| `67` | `107` | Position_Unknown | Team_Unknown | 599–653 | 55 | 1 | Undefined position; Undefined team |
| `68` | `108` | Position_Unknown | Team_Unknown | 607–621 | 14 | 2 | Undefined position; Undefined team |
| `69` | `109` | Position_Unknown | Team_Unknown | 610–611 | 2 | 1 | Undefined position; Undefined team |
| `70` | `110` | Position_Unknown | Team_Unknown | 617–618 | 2 | 1 | Undefined position; Undefined team |
| `71` | `112` | Position_Unknown | Team_Unknown | 642–659 | 9 | 2 | Undefined position; Undefined team |
| `72` | `114` | Position_Unknown | Team_Unknown | 650–658 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | 68 | 68 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `26` (2 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `45` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ 56 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 56 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 112 |
| Missing visible bounding boxes during action | 185 |
| Track-related warning | 2 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 182: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_CrossGoalLine' for track '45' has invalid range: start=645, end=480. Clamping end to start.
- ⚠️ Action 'Action_None' range [50-302] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-311] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-319] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-337] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-346] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-659] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-321] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-649] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-217] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-354] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-643] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-275] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-503] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-628] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-282] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-307] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-319] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-282] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-301] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-471] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-621] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-633] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-641] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-283] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-302] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-311] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-324] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-310] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-323] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-333] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-177] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-282] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-310] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-319] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-367] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-645] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-76] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-222] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-291] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-300] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-558] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-561] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-606] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-122] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-266] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-288] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-302] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-344] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-365] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-492] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-284] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-318] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-326] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-341] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-354] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-648] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-302] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-312] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-321] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-324] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-334] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-165] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-390] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-481] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-189] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [242-270] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [361-362] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-209] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-248] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-330] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-232] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-247] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-280] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-276] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-278] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-330] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-659] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-300] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-659] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-352] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-355] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-408] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-482] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-488] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-353] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-475] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-480] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-380] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-438] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-463] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-631] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-385] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-455] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [462-480] for track '45' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-486] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-502] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-534] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-543] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-566] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-654] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-659] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-511] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-516] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-524] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-543] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-571] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-580] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-606] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-611] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-552] for track '53' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-553] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-550] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-554] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-560] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-563] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-593] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-628] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-552] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-558] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-575] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-595] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-618] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-622] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-631] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-563] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-572] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-577] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-592] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-596] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-603] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-572] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-579] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-585] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-591] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-583] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-586] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-612] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-618] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-621] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-580] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-587] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-592] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-582] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-592] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-651] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-598] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-653] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-611] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-621] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-611] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-618] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [642-645] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-658] for track '72' has 2 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>