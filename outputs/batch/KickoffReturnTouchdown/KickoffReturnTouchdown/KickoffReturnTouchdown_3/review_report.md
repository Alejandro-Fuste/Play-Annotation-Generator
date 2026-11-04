# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_3`
- **Frame Range:** 0 to 749 (750 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 749
- **Player Tracks:** 111
- **Ball Tracks:** 0
- **Action Segments:** 486
- **Validation Warnings:** 676
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 1
- **Group Expanded Events:** 2
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 480
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage6 | offense | `3` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Right_Coverage5 | offense | `2` | `2` |
| ✅ EXACT | `Action_KickBall` | Position_Unknown | Team_Unknown | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `41` | `33` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `41` | `33` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `41` | `33` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `2` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage6 | `3` | `Group` | 0 | START | 0 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Right_Coverage5 | `2` | `2` | 107 | START | 107 | 128 |
| ✅ EXACT | `Action_KickBall` | Position_Unknown | `12` | `11` | 164 | START | 164 | 170 |
| ❌ MISSING SEGMENT | `Action_CatchKick` | Position_Unknown | `41` | `33` | 285 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `41` | `33` | 288 | START | 295 | 298 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `41` | `33` | 740 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Coverage6 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 46 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–331
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_KickApproach` | 107 | 128 | 22 | inferred_complete_timeline |
| `Action_KickApproach` | 142 | 147 | 6 | inferred_complete_timeline |
| `Action_KickApproach` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_KickApproach` | 182 | 192 | 11 | inferred_complete_timeline |
| `Action_KickApproach` | 195 | 207 | 13 | inferred_complete_timeline |
| `Action_KickApproach` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 215 | 217 | 3 | inferred_complete_timeline |
| `Action_KickApproach` | 238 | 298 | 61 | inferred_complete_timeline |
| `Action_KickApproach` | 301 | 302 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 304 | 327 | 24 | inferred_complete_timeline |
| `Action_KickApproach` | 330 | 331 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–360
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 194 | 88 | inferred_complete_timeline |
| `Action_None` | 197 | 232 | 36 | inferred_complete_timeline |
| `Action_None` | 234 | 287 | 54 | inferred_complete_timeline |
| `Action_None` | 289 | 337 | 49 | inferred_complete_timeline |
| `Action_None` | 339 | 360 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–749
- **Visible Samples:** 646

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 16 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 26 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 41 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 52 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 74 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 93 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 106 | 12 | inferred_complete_timeline |
| `Action_None` | 107 | 150 | 44 | inferred_complete_timeline |
| `Action_None` | 156 | 168 | 13 | inferred_complete_timeline |
| `Action_None` | 174 | 287 | 114 | inferred_complete_timeline |
| `Action_None` | 295 | 300 | 6 | inferred_complete_timeline |
| `Action_None` | 309 | 490 | 182 | inferred_complete_timeline |
| `Action_None` | 494 | 544 | 51 | inferred_complete_timeline |
| `Action_None` | 559 | 686 | 128 | inferred_complete_timeline |
| `Action_None` | 694 | 711 | 18 | inferred_complete_timeline |
| `Action_None` | 730 | 731 | 2 | inferred_complete_timeline |
| `Action_None` | 736 | 739 | 4 | inferred_complete_timeline |
| `Action_None` | 741 | 749 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–576
- **Visible Samples:** 524

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 28 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 36 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 78 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 89 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 106 | 15 | inferred_complete_timeline |
| `Action_None` | 107 | 159 | 53 | inferred_complete_timeline |
| `Action_None` | 162 | 188 | 27 | inferred_complete_timeline |
| `Action_None` | 195 | 268 | 74 | inferred_complete_timeline |
| `Action_None` | 273 | 316 | 44 | inferred_complete_timeline |
| `Action_None` | 318 | 319 | 2 | inferred_complete_timeline |
| `Action_None` | 322 | 346 | 25 | inferred_complete_timeline |
| `Action_None` | 349 | 562 | 214 | inferred_complete_timeline |
| `Action_None` | 565 | 576 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–507
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 27 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 45 | 17 | inferred_complete_timeline |
| `Action_None` | 111 | 124 | 14 | inferred_complete_timeline |
| `Action_None` | 127 | 130 | 4 | inferred_complete_timeline |
| `Action_None` | 144 | 165 | 22 | inferred_complete_timeline |
| `Action_None` | 171 | 192 | 22 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_None` | 210 | 253 | 44 | inferred_complete_timeline |
| `Action_None` | 260 | 309 | 50 | inferred_complete_timeline |
| `Action_None` | 314 | 317 | 4 | inferred_complete_timeline |
| `Action_None` | 322 | 396 | 75 | inferred_complete_timeline |
| `Action_None` | 398 | 449 | 52 | inferred_complete_timeline |
| `Action_None` | 455 | 459 | 5 | inferred_complete_timeline |
| `Action_None` | 463 | 464 | 2 | inferred_complete_timeline |
| `Action_None` | 466 | 469 | 4 | inferred_complete_timeline |
| `Action_None` | 474 | 507 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–316
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 270 | 164 | inferred_complete_timeline |
| `Action_None` | 273 | 280 | 8 | inferred_complete_timeline |
| `Action_None` | 286 | 305 | 20 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 313 | 316 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–748
- **Visible Samples:** 658

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 71 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 106 | 23 | inferred_complete_timeline |
| `Action_None` | 107 | 174 | 68 | inferred_complete_timeline |
| `Action_None` | 189 | 231 | 43 | inferred_complete_timeline |
| `Action_None` | 234 | 238 | 5 | inferred_complete_timeline |
| `Action_None` | 240 | 398 | 159 | inferred_complete_timeline |
| `Action_None` | 400 | 487 | 88 | inferred_complete_timeline |
| `Action_None` | 498 | 499 | 2 | inferred_complete_timeline |
| `Action_None` | 504 | 601 | 98 | inferred_complete_timeline |
| `Action_None` | 603 | 677 | 75 | inferred_complete_timeline |
| `Action_None` | 679 | 688 | 10 | inferred_complete_timeline |
| `Action_None` | 698 | 699 | 2 | inferred_complete_timeline |
| `Action_None` | 708 | 711 | 4 | inferred_complete_timeline |
| `Action_None` | 735 | 736 | 2 | inferred_complete_timeline |
| `Action_None` | 744 | 748 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 6–749 | 598 | 24 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 13–151 | 65 | 4 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 27–749 | 534 | 15 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 94–145 | 50 | 3 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 105–119 | 15 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 107–110 | 4 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 107–735 | 615 | 7 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 140–158 | 13 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 143–337 | 168 | 7 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 145–622 | 385 | 13 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 188–588 | 388 | 5 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 189–245 | 32 | 6 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 196–198 | 3 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 200–235 | 30 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 203–749 | 527 | 7 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 206–744 | 525 | 7 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 208–553 | 315 | 6 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 217–607 | 380 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 227–255 | 29 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 230–231 | 2 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 230–749 | 508 | 5 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 232–330 | 92 | 4 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 242–327 | 75 | 5 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 246–308 | 61 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 269–301 | 21 | 3 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 310–322 | 13 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 311–315 | 5 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 329–534 | 206 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 331–749 | 358 | 9 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 335–749 | 382 | 8 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 344–387 | 29 | 2 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 352–708 | 291 | 10 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 359–406 | 48 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 374–749 | 355 | 5 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 377–526 | 135 | 7 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 383–398 | 16 | 1 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 408–454 | 45 | 2 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 415–627 | 171 | 4 | Undefined position; Undefined team |
| `47` | `63` | Position_Unknown | Team_Unknown | 434–435 | 2 | 1 | Undefined position; Undefined team |
| `48` | `65` | Position_Unknown | Team_Unknown | 472–749 | 274 | 4 | Undefined position; Undefined team |
| `49` | `66` | Position_Unknown | Team_Unknown | 488–511 | 22 | 2 | Undefined position; Undefined team |
| `50` | `67` | Position_Unknown | Team_Unknown | 492–501 | 9 | 2 | Undefined position; Undefined team |
| `51` | `68` | Position_Unknown | Team_Unknown | 495–498 | 4 | 1 | Undefined position; Undefined team |
| `52` | `69` | Position_Unknown | Team_Unknown | 505–509 | 5 | 1 | Undefined position; Undefined team |
| `53` | `70` | Position_Unknown | Team_Unknown | 505–535 | 20 | 3 | Undefined position; Undefined team |
| `54` | `71` | Position_Unknown | Team_Unknown | 508–631 | 84 | 11 | Undefined position; Undefined team |
| `55` | `74` | Position_Unknown | Team_Unknown | 513–584 | 67 | 2 | Undefined position; Undefined team |
| `56` | `75` | Position_Unknown | Team_Unknown | 514–618 | 103 | 2 | Undefined position; Undefined team |
| `57` | `78` | Position_Unknown | Team_Unknown | 523–526 | 4 | 1 | Undefined position; Undefined team |
| `58` | `79` | Position_Unknown | Team_Unknown | 524–555 | 15 | 3 | Undefined position; Undefined team |
| `59` | `82` | Position_Unknown | Team_Unknown | 527–749 | 174 | 20 | Undefined position; Undefined team |
| `60` | `83` | Position_Unknown | Team_Unknown | 533–593 | 35 | 5 | Undefined position; Undefined team |
| `61` | `84` | Position_Unknown | Team_Unknown | 536–557 | 19 | 2 | Undefined position; Undefined team |
| `62` | `85` | Position_Unknown | Team_Unknown | 545–629 | 85 | 1 | Undefined position; Undefined team |
| `63` | `88` | Position_Unknown | Team_Unknown | 568–663 | 82 | 4 | Undefined position; Undefined team |
| `64` | `90` | Position_Unknown | Team_Unknown | 572–573 | 2 | 1 | Undefined position; Undefined team |
| `65` | `91` | Position_Unknown | Team_Unknown | 586–749 | 124 | 8 | Undefined position; Undefined team |
| `66` | `92` | Position_Unknown | Team_Unknown | 592–744 | 75 | 15 | Undefined position; Undefined team |
| `67` | `93` | Position_Unknown | Team_Unknown | 594–619 | 26 | 1 | Undefined position; Undefined team |
| `68` | `94` | Position_Unknown | Team_Unknown | 606–713 | 83 | 5 | Undefined position; Undefined team |
| `69` | `95` | Position_Unknown | Team_Unknown | 611–631 | 20 | 2 | Undefined position; Undefined team |
| `70` | `96` | Position_Unknown | Team_Unknown | 617–626 | 10 | 1 | Undefined position; Undefined team |
| `71` | `103` | Position_Unknown | Team_Unknown | 632–727 | 78 | 7 | Undefined position; Undefined team |
| `72` | `105` | Position_Unknown | Team_Unknown | 634–637 | 4 | 1 | Undefined position; Undefined team |
| `73` | `106` | Position_Unknown | Team_Unknown | 635–655 | 13 | 2 | Undefined position; Undefined team |
| `74` | `107` | Position_Unknown | Team_Unknown | 635–636 | 2 | 1 | Undefined position; Undefined team |
| `75` | `108` | Position_Unknown | Team_Unknown | 636–747 | 92 | 5 | Undefined position; Undefined team |
| `76` | `110` | Position_Unknown | Team_Unknown | 636–637 | 2 | 1 | Undefined position; Undefined team |
| `77` | `111` | Position_Unknown | Team_Unknown | 647–749 | 82 | 4 | Undefined position; Undefined team |
| `78` | `112` | Position_Unknown | Team_Unknown | 655–749 | 85 | 5 | Undefined position; Undefined team |
| `79` | `113` | Position_Unknown | Team_Unknown | 655–691 | 13 | 4 | Undefined position; Undefined team |
| `80` | `115` | Position_Unknown | Team_Unknown | 664–672 | 9 | 1 | Undefined position; Undefined team |
| `81` | `116` | Position_Unknown | Team_Unknown | 666–698 | 17 | 2 | Undefined position; Undefined team |
| `82` | `120` | Position_Unknown | Team_Unknown | 674–719 | 10 | 2 | Undefined position; Undefined team |
| `83` | `121` | Position_Unknown | Team_Unknown | 675–716 | 26 | 4 | Undefined position; Undefined team |
| `84` | `122` | Position_Unknown | Team_Unknown | 675–677 | 3 | 1 | Undefined position; Undefined team |
| `85` | `123` | Position_Unknown | Team_Unknown | 676–694 | 19 | 1 | Undefined position; Undefined team |
| `86` | `124` | Position_Unknown | Team_Unknown | 677–678 | 2 | 1 | Undefined position; Undefined team |
| `87` | `126` | Position_Unknown | Team_Unknown | 684–708 | 10 | 3 | Undefined position; Undefined team |
| `88` | `133` | Position_Unknown | Team_Unknown | 692–744 | 21 | 5 | Undefined position; Undefined team |
| `89` | `135` | Position_Unknown | Team_Unknown | 693–710 | 16 | 2 | Undefined position; Undefined team |
| `90` | `139` | Position_Unknown | Team_Unknown | 701–726 | 4 | 2 | Undefined position; Undefined team |
| `91` | `141` | Position_Unknown | Team_Unknown | 704–749 | 22 | 6 | Undefined position; Undefined team |
| `92` | `142` | Position_Unknown | Team_Unknown | 706–749 | 38 | 2 | Undefined position; Undefined team |
| `93` | `143` | Position_Unknown | Team_Unknown | 706–745 | 30 | 5 | Undefined position; Undefined team |
| `94` | `144` | Position_Unknown | Team_Unknown | 707–709 | 3 | 1 | Undefined position; Undefined team |
| `95` | `145` | Position_Unknown | Team_Unknown | 707–709 | 3 | 1 | Undefined position; Undefined team |
| `96` | `147` | Position_Unknown | Team_Unknown | 707–749 | 39 | 4 | Undefined position; Undefined team |
| `97` | `148` | Position_Unknown | Team_Unknown | 710–716 | 5 | 2 | Undefined position; Undefined team |
| `98` | `149` | Position_Unknown | Team_Unknown | 710–749 | 12 | 3 | Undefined position; Undefined team |
| `99` | `150` | Position_Unknown | Team_Unknown | 710–744 | 28 | 4 | Undefined position; Undefined team |
| `100` | `152` | Position_Unknown | Team_Unknown | 711–716 | 6 | 1 | Undefined position; Undefined team |
| `101` | `153` | Position_Unknown | Team_Unknown | 711–722 | 11 | 2 | Undefined position; Undefined team |
| `102` | `160` | Position_Unknown | Team_Unknown | 725–731 | 7 | 1 | Undefined position; Undefined team |
| `103` | `161` | Position_Unknown | Team_Unknown | 726–749 | 12 | 3 | Undefined position; Undefined team |
| `104` | `162` | Position_Unknown | Team_Unknown | 726–727 | 2 | 1 | Undefined position; Undefined team |
| `105` | `163` | Position_Unknown | Team_Unknown | 727–749 | 21 | 3 | Undefined position; Undefined team |
| `106` | `166` | Position_Unknown | Team_Unknown | 728–740 | 7 | 2 | Undefined position; Undefined team |
| `107` | `167` | Position_Unknown | Team_Unknown | 729–749 | 14 | 2 | Undefined position; Undefined team |
| `108` | `168` | Position_Unknown | Team_Unknown | 729–730 | 2 | 1 | Undefined position; Undefined team |
| `109` | `170` | Position_Unknown | Team_Unknown | 738–749 | 12 | 1 | Undefined position; Undefined team |
| `110` | `171` | Position_Unknown | Team_Unknown | 739–742 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `2` (11 segments found)
- ❌ Missing segment for action `Action_CatchKick` on target `41` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `41` (2 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `41` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ 103 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 103 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 206 |
| Missing visible bounding boxes during action | 467 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 7: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 749 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '33' has invalid range: start=740, end=301. Clamping end to start.
- ⚠️ Action 'Action_None' range [107-270] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-280] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-305] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-71] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-77] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-174] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-231] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-398] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-487] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-499] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-601] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-677] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [679-688] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [698-699] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [708-711] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [735-736] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [744-748] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [107-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [142-147] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [162-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [182-192] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [195-207] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [212-213] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [215-217] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [238-298] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [301-302] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [304-327] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [330-331] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-27] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-45] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-124] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-165] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-192] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-253] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-309] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-396] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-449] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-459] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-469] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-507] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-28] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-36] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-78] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-85] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-89] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-159] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-188] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-268] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-316] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-346] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-562] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-576] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-21] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-26] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-41] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-52] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-74] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-93] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-150] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-168] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-287] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-300] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-490] for track '7' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-544] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-686] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [694-711] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [730-731] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [736-739] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [741-749] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-194] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-232] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-287] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-337] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-360] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-17] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-22] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-89] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-165] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-220] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-256] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-312] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-629] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-688] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [692-695] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-715] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [725-726] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [728-730] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-18] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-151] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-36] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-110] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-291] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-393] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-405] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-409] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-414] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-452] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-749] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-106] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 107, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [107-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-145] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-119] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-194] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-550] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-735] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-148] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-215] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-337] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-157] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-227] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-493] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-519] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-529] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-543] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-554] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-578] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-599] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-604] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-612] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-622] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-213] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-560] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-571] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-588] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-203] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-229] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-245] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-208] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-224] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-514] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-518] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-574] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-581] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-595] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-633] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-224] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-240] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-676] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [680-686] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [688-715] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [719-726] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [729-744] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-384] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-504] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-507] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-512] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-525] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-553] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-359] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-593] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-598] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-607] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-255] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-607] for track '29' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-654] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [661-662] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [666-745] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-251] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-315] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-330] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-267] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-282] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-290] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-297] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-327] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-308] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-283] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [295-298] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [300-301] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-322] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-315] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-534] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-347] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-376] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-513] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-516] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-580] for track '37' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-655] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-664] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [668-688] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [692-749] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-387] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-579] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-583] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-689] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [694-703] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-710] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-368] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-387] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-376] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-562] for track '40' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-583] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-665] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [667-673] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [675-685] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [688-689] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [693-701] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [707-708] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-406] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-682] for track '42' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [684-707] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [722-729] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [732-743] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [748-749] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-398] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-412] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-483] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-493] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-498] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-526] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-398] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-449] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-454] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-485] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-615] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-622] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-627] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-435] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-491] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-494] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-670] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-493] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-511] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-496] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-501] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-498] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-509] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-508] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-520] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-535] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-511] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-523] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-528] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-547] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-557] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-565] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-570] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-575] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-588] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-598] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-631] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-573] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-584] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-516] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-618] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-526] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-533] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-547] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-555] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-536] for track '59' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-543] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-547] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-556] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-560] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-563] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-592] for track '59' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-598] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-610] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-618] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-627] for track '59' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-640] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-680] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [682-686] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [689-708] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [710-714] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [717-721] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [723-728] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [735-739] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [748-749] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-537] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-559] for track '60' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-565] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-584] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-593] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-557] for track '61' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-629] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-572] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-599] for track '63' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-646] for track '63' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-663] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-573] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-588] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-605] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-652] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [657-694] for track '65' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [698-700] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [721-724] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [726-727] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-603] for track '66' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-609] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-619] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-627] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [630-635] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [640-642] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-653] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [656-662] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [664-670] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [673-677] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [683-685] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [710-711] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [729-732] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [738-740] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [743-744] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-619] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-673] for track '68' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [676-682] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [684-685] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [688-691] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [712-713] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-621] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-631] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-626] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-674] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [677-679] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [688-693] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [695-707] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [710-714] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [719-724] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [726-727] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-637] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-642] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-655] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-636] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [636-656] for track '75' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [667-673] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [677-693] for track '75' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [696-710] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [716-747] for track '75' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [636-637] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-649] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-678] for track '77' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [686-687] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [655-689] for track '78' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [692-698] for track '78' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [703-707] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [711-721] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [655-656] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [675-680] for track '79' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [684-686] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [690-691] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [664-672] for track '80' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [666-676] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [693-698] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [674-678] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [715-719] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [675-676] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [683-689] for track '83' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [691-695] for track '83' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [705-716] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [675-677] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [676-694] for track '85' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [677-678] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [684-687] for track '87' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [691-692] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [705-708] for track '87' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [692-693] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [704-710] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [723-724] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [726-733] for track '88' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [743-744] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [693-694] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [697-710] for track '89' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [701-702] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [725-726] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [704-713] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [716-718] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [720-722] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [730-731] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [741-742] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [706-711] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [718-749] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [706-714] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [717-728] for track '93' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [731-733] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [736-739] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [744-745] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [707-709] for track '94' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [707-709] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [707-726] for track '96' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [728-737] for track '96' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [739-745] for track '96' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [748-749] for track '96' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [710-711] for track '97' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [714-716] for track '97' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [710-711] for track '98' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [713-714] for track '98' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [710-714] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [716-721] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [726-733] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [736-744] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [711-716] for track '100' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [711-715] for track '101' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [717-722] for track '101' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [725-731] for track '102' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [726-731] for track '103' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [743-744] for track '103' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [726-727] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [727-741] for track '105' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [743-745] for track '105' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [747-749] for track '105' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [728-732] for track '106' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [739-740] for track '106' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [729-733] for track '107' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [741-749] for track '107' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [729-730] for track '108' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [738-749] for track '109' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [739-742] for track '110' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '80' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '80' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '81' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '81' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '82' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '82' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '83' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '83' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '84' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '84' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '85' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '85' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '86' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '86' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '87' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '87' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '88' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '88' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '89' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '89' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '90' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '90' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '91' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '91' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '92' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '92' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '93' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '93' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '94' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '94' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '95' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '95' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '96' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '96' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '97' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '97' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '98' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '98' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '99' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '99' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '100' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '100' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '101' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '101' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '102' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '102' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '103' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '103' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '104' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '104' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '105' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '105' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '106' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '106' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '107' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '107' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '108' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '108' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '109' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '109' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '110' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '110' has undefined team_side. Will map to Team_Unknown.

</details>