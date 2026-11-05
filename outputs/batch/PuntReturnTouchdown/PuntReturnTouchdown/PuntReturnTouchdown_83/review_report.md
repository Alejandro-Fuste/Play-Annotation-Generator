# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_83

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_83`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 689
- **Player Tracks:** 57
- **Ball Tracks:** 0
- **Action Segments:** 225
- **Validation Warnings:** 267
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
- **Inferred Coverage Segments (Action_None):** 209
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `16` | `16` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `16` | `16` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `36` | `28` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `36` | `28` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `36` | `28` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `1` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `10` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `11` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `12` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `13` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `16` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `18` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `20` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `6` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `8` | `Group` | 0 | START | 0 | 44 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `12` | `12` | 45 | START | 45 | 100 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `16` | `16` | 70 | END | 70 | 70 |
| ✅ EXACT | `Action_PuntBall` | Punter | `16` | `16` | 101 | START | 101 | 116 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `36` | `28` | 233 | START | 233 | 246 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `36` | `28` | 247 | START | 247 | 300 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `36` | `28` | 662 | START | 662 | 668 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 134 | 90 | inferred_complete_timeline |
| `Action_None` | 137 | 142 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–486
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 141 | 97 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 198 | 38 | inferred_complete_timeline |
| `Action_None` | 200 | 206 | 7 | inferred_complete_timeline |
| `Action_None` | 208 | 423 | 216 | inferred_complete_timeline |
| `Action_None` | 427 | 448 | 22 | inferred_complete_timeline |
| `Action_None` | 459 | 460 | 2 | inferred_complete_timeline |
| `Action_None` | 462 | 463 | 2 | inferred_complete_timeline |
| `Action_None` | 485 | 486 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–688
- **Visible Samples:** 664

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 128 | 84 | inferred_complete_timeline |
| `Action_None` | 133 | 148 | 16 | inferred_complete_timeline |
| `Action_None` | 150 | 232 | 83 | inferred_complete_timeline |
| `Action_None` | 236 | 240 | 5 | inferred_complete_timeline |
| `Action_None` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 355 | 108 | inferred_complete_timeline |
| `Action_None` | 361 | 362 | 2 | inferred_complete_timeline |
| `Action_None` | 365 | 410 | 46 | inferred_complete_timeline |
| `Action_None` | 416 | 688 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 680

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_LongSnap` | 45 | 100 | 56 | inferred_complete_timeline |
| `Action_None` | 101 | 237 | 137 | inferred_complete_timeline |
| `Action_None` | 239 | 265 | 27 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |
| `Action_None` | 271 | 399 | 129 | inferred_complete_timeline |
| `Action_None` | 401 | 503 | 103 | inferred_complete_timeline |
| `Action_None` | 507 | 509 | 3 | inferred_complete_timeline |
| `Action_None` | 512 | 647 | 136 | inferred_complete_timeline |
| `Action_None` | 649 | 689 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 683

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 396 | 352 | inferred_complete_timeline |
| `Action_None` | 400 | 404 | 5 | inferred_complete_timeline |
| `Action_None` | 406 | 413 | 8 | inferred_complete_timeline |
| `Action_None` | 416 | 495 | 80 | inferred_complete_timeline |
| `Action_None` | 497 | 689 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 105 | 61 | inferred_complete_timeline |
| `Action_None` | 109 | 202 | 94 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |
| `Action_None` | 214 | 216 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–489
- **Visible Samples:** 490

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 489 | 445 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 665

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_SnapReceive` | 70 | 70 | 1 | inferred_complete_timeline |
| `Action_None` | 71 | 100 | 30 | inferred_complete_timeline |
| `Action_PuntBall` | 101 | 116 | 16 | inferred_complete_timeline |
| `Action_None` | 117 | 153 | 37 | inferred_complete_timeline |
| `Action_None` | 158 | 263 | 106 | inferred_complete_timeline |
| `Action_None` | 265 | 613 | 349 | inferred_complete_timeline |
| `Action_None` | 615 | 646 | 32 | inferred_complete_timeline |
| `Action_None` | 656 | 659 | 4 | inferred_complete_timeline |
| `Action_None` | 662 | 663 | 2 | inferred_complete_timeline |
| `Action_None` | 672 | 689 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 85 | 41 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_None` | 93 | 165 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–635
- **Visible Samples:** 602

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 321 | 277 | inferred_complete_timeline |
| `Action_None` | 323 | 350 | 28 | inferred_complete_timeline |
| `Action_None` | 352 | 355 | 4 | inferred_complete_timeline |
| `Action_None` | 359 | 363 | 5 | inferred_complete_timeline |
| `Action_None` | 370 | 484 | 115 | inferred_complete_timeline |
| `Action_None` | 486 | 597 | 112 | inferred_complete_timeline |
| `Action_None` | 600 | 601 | 2 | inferred_complete_timeline |
| `Action_None` | 611 | 613 | 3 | inferred_complete_timeline |
| `Action_None` | 619 | 623 | 5 | inferred_complete_timeline |
| `Action_None` | 630 | 635 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–570
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 214 | 170 | inferred_complete_timeline |
| `Action_None` | 217 | 570 | 354 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 597

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 237 | 193 | inferred_complete_timeline |
| `Action_None` | 240 | 242 | 3 | inferred_complete_timeline |
| `Action_None` | 246 | 252 | 7 | inferred_complete_timeline |
| `Action_None` | 334 | 440 | 107 | inferred_complete_timeline |
| `Action_None` | 443 | 446 | 4 | inferred_complete_timeline |
| `Action_None` | 448 | 664 | 217 | inferred_complete_timeline |
| `Action_None` | 668 | 672 | 5 | inferred_complete_timeline |
| `Action_None` | 674 | 689 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–619
- **Visible Samples:** 618

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 246 | 202 | inferred_complete_timeline |
| `Action_None` | 248 | 268 | 21 | inferred_complete_timeline |
| `Action_None` | 270 | 619 | 350 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 683

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 160 | 116 | inferred_complete_timeline |
| `Action_None` | 163 | 495 | 333 | inferred_complete_timeline |
| `Action_None` | 497 | 518 | 22 | inferred_complete_timeline |
| `Action_None` | 522 | 545 | 24 | inferred_complete_timeline |
| `Action_None` | 547 | 689 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 689 | 645 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 167 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–608
- **Visible Samples:** 606

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 214 | 170 | inferred_complete_timeline |
| `Action_None` | 216 | 262 | 47 | inferred_complete_timeline |
| `Action_None` | 264 | 604 | 341 | inferred_complete_timeline |
| `Action_None` | 606 | 608 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 122 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 687

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 103 | 59 | inferred_complete_timeline |
| `Action_None` | 106 | 204 | 99 | inferred_complete_timeline |
| `Action_None` | 206 | 689 | 484 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 685

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 253 | 209 | inferred_complete_timeline |
| `Action_None` | 256 | 279 | 24 | inferred_complete_timeline |
| `Action_None` | 281 | 578 | 298 | inferred_complete_timeline |
| `Action_None` | 580 | 626 | 47 | inferred_complete_timeline |
| `Action_None` | 628 | 689 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–518 | 515 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 75–76 | 2 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 135–689 | 550 | 3 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 162–163 | 2 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 175–519 | 253 | 10 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 179–568 | 362 | 6 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 190–191 | 2 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 192–194 | 3 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 195–689 | 494 | 6 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 195–197 | 3 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 219–689 | 441 | 11 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 265–266 | 2 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 272–327 | 56 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 296–366 | 69 | 2 | Undefined position; Undefined team |
| `35` | `55` | Position_Unknown | Team_Unknown | 310–314 | 5 | 1 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 318–325 | 8 | 1 | Undefined position; Undefined team |
| `37` | `57` | Position_Unknown | Team_Unknown | 341–396 | 43 | 4 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 366–689 | 320 | 5 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 396–400 | 5 | 1 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 442–444 | 3 | 1 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 452–687 | 213 | 9 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 486–677 | 129 | 10 | Undefined position; Undefined team |
| `43` | `68` | Position_Unknown | Team_Unknown | 503–504 | 2 | 1 | Undefined position; Undefined team |
| `44` | `69` | Position_Unknown | Team_Unknown | 506–509 | 4 | 1 | Undefined position; Undefined team |
| `45` | `70` | Position_Unknown | Team_Unknown | 507–689 | 152 | 10 | Undefined position; Undefined team |
| `46` | `74` | Position_Unknown | Team_Unknown | 521–525 | 5 | 1 | Undefined position; Undefined team |
| `47` | `82` | Position_Unknown | Team_Unknown | 573–574 | 2 | 1 | Undefined position; Undefined team |
| `48` | `85` | Position_Unknown | Team_Unknown | 575–576 | 2 | 1 | Undefined position; Undefined team |
| `49` | `88` | Position_Unknown | Team_Unknown | 581–584 | 4 | 1 | Undefined position; Undefined team |
| `50` | `89` | Position_Unknown | Team_Unknown | 591–593 | 3 | 1 | Undefined position; Undefined team |
| `51` | `90` | Position_Unknown | Team_Unknown | 616–689 | 62 | 5 | Undefined position; Undefined team |
| `52` | `91` | Position_Unknown | Team_Unknown | 619–689 | 70 | 2 | Undefined position; Undefined team |
| `53` | `94` | Position_Unknown | Team_Unknown | 649–689 | 41 | 1 | Undefined position; Undefined team |
| `54` | `95` | Position_Unknown | Team_Unknown | 649–689 | 41 | 1 | Undefined position; Undefined team |
| `55` | `96` | Position_Unknown | Team_Unknown | 684–686 | 3 | 1 | Undefined position; Undefined team |
| `56` | `97` | Position_Unknown | Team_Unknown | 684–689 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `36` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ 37 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 37 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 74 |
| Missing visible bounding boxes during action | 189 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 168: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [45-689] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-141] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-198] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-423] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-448] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-122] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-214] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-570] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-252] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-440] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-446] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-664] for track '4' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [668-672] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-160] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-495] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-518] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-545] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-321] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-350] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-355] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-363] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-484] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-597] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-601] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-613] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-623] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [630-635] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-246] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-268] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-619] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-85] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-165] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-253] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-279] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-578] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-626] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-689] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-128] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-148] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-232] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-355] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-410] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-688] for track '11' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [45-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-237] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-265] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-399] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-503] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-509] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-647] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [649-689] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-396] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-404] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-413] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-495] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-204] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-218] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-518] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-214] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-262] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-604] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-608] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-153] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-263] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-613] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-646] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [656-659] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [662-663] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [672-689] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-167] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-105] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-202] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-204] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-689] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-489] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-483] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-489] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-248] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-261] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-280] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-289] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-310] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-519] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-245] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-259] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-568] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [247-300] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [302-661] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-231] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-254] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-290] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-612] for track '30' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-622] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-633] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-640] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-669] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-327] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-333] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-366] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-314] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-325] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-346] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-375] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-380] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-396] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-395] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-403] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-520] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-576] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-689] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-400] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-444] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-554] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-564] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-591] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-604] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-609] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-622] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-629] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-644] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-687] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-488] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-499] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-589] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-606] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-612] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-621] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-633] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-652] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [669-670] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [676-677] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-509] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-601] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-612] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-623] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-633] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-641] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-645] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-652] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [654-659] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [672-680] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-525] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-576] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-584] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-593] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-619] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-641] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-652] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [657-664] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-632] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [649-689] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [649-689] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [684-686] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [684-689] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>