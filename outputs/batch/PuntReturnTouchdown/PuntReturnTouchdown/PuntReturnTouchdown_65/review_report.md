# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_65

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_65`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 70
- **Ball Tracks:** 2
- **Action Segments:** 207
- **Validation Warnings:** 284
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 192
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `4` | `4` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `46` | `34` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `57` | `43` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `0` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `10` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing2 | `12` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `15` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `18` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing3 | `2` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector | `3` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `4` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `5` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `9` | `Group` | 0 | START | 0 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `10` | `10` | 29 | START | 29 | 53 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `4` | `4` | 56 | END | 56 | 56 |
| ✅ EXACT | `Action_PuntBall` | Punter | `4` | `4` | 92 | START | 92 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `46` | `34` | 273 | START | 273 | 411 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `57` | `43` | 638 | START | 638 | 643 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 57 | 29 | inferred_complete_timeline |
| `Action_None` | 59 | 110 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 660

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 659 | 631 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–584
- **Visible Samples:** 584

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 57 | 29 | inferred_complete_timeline |
| `Action_None` | 59 | 584 | 526 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_LongSnap` | 29 | 53 | 25 | inferred_complete_timeline |
| `Action_LongSnap` | 59 | 91 | 33 | inferred_complete_timeline |
| `Action_None` | 92 | 183 | 92 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 204 | 13 | inferred_complete_timeline |
| `Action_None` | 208 | 281 | 74 | inferred_complete_timeline |
| `Action_None` | 284 | 321 | 38 | inferred_complete_timeline |
| `Action_None` | 326 | 327 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–548
- **Visible Samples:** 544

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 185 | 157 | inferred_complete_timeline |
| `Action_None` | 188 | 251 | 64 | inferred_complete_timeline |
| `Action_None` | 255 | 548 | 294 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 660

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_SnapReceive` | 56 | 56 | 1 | inferred_complete_timeline |
| `Action_None` | 57 | 91 | 35 | inferred_complete_timeline |
| `Action_PuntBall` | 92 | 107 | 16 | inferred_complete_timeline |
| `Action_None` | 108 | 659 | 552 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–523
- **Visible Samples:** 516

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 87 | 59 | inferred_complete_timeline |
| `Action_None` | 90 | 318 | 229 | inferred_complete_timeline |
| `Action_None` | 325 | 523 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–317
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 57 | 29 | inferred_complete_timeline |
| `Action_None` | 59 | 238 | 180 | inferred_complete_timeline |
| `Action_None` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 254 | 5 | inferred_complete_timeline |
| `Action_None` | 257 | 262 | 6 | inferred_complete_timeline |
| `Action_None` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_None` | 273 | 317 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–656
- **Visible Samples:** 650

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 401 | 373 | inferred_complete_timeline |
| `Action_None` | 407 | 602 | 196 | inferred_complete_timeline |
| `Action_None` | 605 | 656 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–573
- **Visible Samples:** 574

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 573 | 545 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 94 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 43 | 15 | inferred_complete_timeline |
| `Action_None` | 46 | 48 | 3 | inferred_complete_timeline |
| `Action_None` | 51 | 52 | 2 | inferred_complete_timeline |
| `Action_None` | 55 | 97 | 43 | inferred_complete_timeline |
| `Action_None` | 101 | 127 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–646
- **Visible Samples:** 631

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 286 | 258 | inferred_complete_timeline |
| `Action_None` | 290 | 294 | 5 | inferred_complete_timeline |
| `Action_None` | 298 | 329 | 32 | inferred_complete_timeline |
| `Action_None` | 331 | 332 | 2 | inferred_complete_timeline |
| `Action_None` | 334 | 337 | 4 | inferred_complete_timeline |
| `Action_None` | 341 | 347 | 7 | inferred_complete_timeline |
| `Action_None` | 352 | 394 | 43 | inferred_complete_timeline |
| `Action_None` | 396 | 646 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 119 | 91 | inferred_complete_timeline |
| `Action_None` | 121 | 176 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 88 | 60 | inferred_complete_timeline |
| `Action_None` | 119 | 122 | 4 | inferred_complete_timeline |
| `Action_None` | 125 | 173 | 49 | inferred_complete_timeline |
| `Action_None` | 178 | 245 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 44 | 16 | inferred_complete_timeline |
| `Action_None` | 55 | 64 | 10 | inferred_complete_timeline |
| `Action_None` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_None` | 73 | 164 | 92 | inferred_complete_timeline |
| `Action_None` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_None` | 171 | 259 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 42 | 14 | inferred_complete_timeline |
| `Action_None` | 44 | 58 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 104 | 76 | inferred_complete_timeline |
| `Action_None` | 106 | 115 | 10 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 120 | 124 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 44 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 49–178 | 130 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 51–536 | 470 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 69–230 | 139 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 75–118 | 37 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 117–237 | 103 | 7 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 121–573 | 429 | 9 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 145–146 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 173–188 | 16 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 180–182 | 3 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 184–283 | 82 | 5 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 185–330 | 146 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 213–510 | 297 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 258–261 | 4 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 265–305 | 41 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 269–659 | 381 | 6 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 276–279 | 4 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 289–573 | 264 | 3 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 293–632 | 340 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 297–573 | 259 | 4 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 299–313 | 15 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 311–616 | 274 | 11 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 324–607 | 266 | 3 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 334–628 | 277 | 4 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 336–659 | 322 | 5 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 355–573 | 219 | 1 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 373–573 | 200 | 2 | Undefined position; Undefined team |
| `46` | `63` | Position_Unknown | Team_Unknown | 387–407 | 16 | 2 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 412–414 | 3 | 1 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 423–502 | 74 | 2 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 442–483 | 24 | 3 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 445–446 | 2 | 1 | Undefined position; Undefined team |
| `51` | `73` | Position_Unknown | Team_Unknown | 452–483 | 32 | 1 | Undefined position; Undefined team |
| `52` | `75` | Position_Unknown | Team_Unknown | 454–455 | 2 | 1 | Undefined position; Undefined team |
| `54` | `77` | Position_Unknown | Team_Unknown | 460–461 | 2 | 1 | Undefined position; Undefined team |
| `55` | `78` | Position_Unknown | Team_Unknown | 469–472 | 4 | 1 | Undefined position; Undefined team |
| `56` | `84` | Position_Unknown | Team_Unknown | 525–573 | 44 | 3 | Undefined position; Undefined team |
| `57` | `85` | Position_Unknown | Team_Unknown | 537–618 | 74 | 5 | Undefined position; Undefined team |
| `59` | `90` | Position_Unknown | Team_Unknown | 574–659 | 86 | 1 | Undefined position; Undefined team |
| `60` | `91` | Position_Unknown | Team_Unknown | 574–659 | 86 | 1 | Undefined position; Undefined team |
| `61` | `92` | Position_Unknown | Team_Unknown | 574–659 | 86 | 1 | Undefined position; Undefined team |
| `62` | `93` | Position_Unknown | Team_Unknown | 574–659 | 86 | 1 | Undefined position; Undefined team |
| `63` | `97` | Position_Unknown | Team_Unknown | 574–659 | 86 | 1 | Undefined position; Undefined team |
| `64` | `99` | Position_Unknown | Team_Unknown | 574–620 | 42 | 2 | Undefined position; Undefined team |
| `65` | `100` | Position_Unknown | Team_Unknown | 574–616 | 43 | 1 | Undefined position; Undefined team |
| `66` | `101` | Position_Unknown | Team_Unknown | 592–595 | 4 | 1 | Undefined position; Undefined team |
| `67` | `102` | Position_Unknown | Team_Unknown | 594–599 | 6 | 1 | Undefined position; Undefined team |
| `68` | `106` | Position_Unknown | Team_Unknown | 598–638 | 19 | 3 | Undefined position; Undefined team |
| `69` | `108` | Position_Unknown | Team_Unknown | 604–622 | 13 | 3 | Undefined position; Undefined team |
| `70` | `111` | Position_Unknown | Team_Unknown | 633–634 | 2 | 1 | Undefined position; Undefined team |
| `71` | `112` | Position_Unknown | Team_Unknown | 634–647 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `53` | `76` | 458 | 458 | 1 | 100.0% | None |
| `58` | `86` | 560 | 566 | 7 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `46` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Wing3` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Wing2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 51 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 51 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_CatchPunt' at frame 222 targets track ID '?', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 102 |
| Missing visible bounding boxes during action | 179 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [29-57] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-44] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-573] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-185] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-251] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-548] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-659] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-57] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-584] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-87] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-318] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-523] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [29-53] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-204] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-281] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-321] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-286] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-294] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-347] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-394] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-646] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-401] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-602] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-656] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-44] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-64] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-164] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-259] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-659] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-43] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-48] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-97] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-127] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-88] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-173] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-245] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-57] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-238] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-262] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-317] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-178] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-279] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-427] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-536] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-152] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-230] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-118] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-153] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-166] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-194] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-230] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-237] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-229] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-243] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-254] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-261] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-275] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-293] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-350] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-573] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-188] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-283] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-330] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-507] for track '31' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-305] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-271] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [273-411] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [413-427] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [433-443] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [446-447] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [449-659] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-376] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-573] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-632] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-329] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-372] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-409] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-573] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-313] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-316] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-338] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-363] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-367] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-440] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-616] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-341] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-373] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-607] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-338] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-618] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-621] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-628] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-341] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-412] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-637] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-659] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-573] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-387] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-573] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-391] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-407] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-414] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-434] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-502] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-450] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-462] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-483] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-446] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-483] for track '51' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-455] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-472] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-530] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-546] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-573] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-553] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-577] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-590] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-615] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-618] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-659] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-610] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-620] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-616] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-595] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-599] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-605] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-623] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-638] for track '68' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-609] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-618] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-622] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-634] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-647] for track '71' has 2 frames without a visible bounding box.
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
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>