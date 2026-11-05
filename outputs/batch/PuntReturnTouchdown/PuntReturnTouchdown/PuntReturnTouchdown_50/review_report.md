# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_50

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_50`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 55
- **Ball Tracks:** 0
- **Action Segments:** 175
- **Validation Warnings:** 209
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
- **Inferred Coverage Segments (Action_None):** 158
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | Interior_Rusher4 | defense | `16` | `16` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `24` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `24` | `22` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `61` | `41` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `0` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `1` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `11` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `2` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `3` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `4` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `5` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `6` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `7` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `8` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `9` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `2` | `2` | 48 | START | 48 | 101 |
| ✅ EXACT | `Action_SnapReceive` | Interior_Rusher4 | `16` | `16` | 78 | END | 78 | 78 |
| ✅ EXACT | `Action_PuntBall` | Punter | `6` | `6` | 102 | START | 102 | 117 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `24` | `22` | 217 | START | 217 | 227 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `24` | `22` | 235 | START | 235 | 301 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `61` | `41` | 560 | START | 560 | 568 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–457
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 100 | 53 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_None` | 116 | 150 | 35 | inferred_complete_timeline |
| `Action_None` | 156 | 325 | 170 | inferred_complete_timeline |
| `Action_None` | 327 | 437 | 111 | inferred_complete_timeline |
| `Action_None` | 440 | 457 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 544

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 302 | 255 | inferred_complete_timeline |
| `Action_None` | 308 | 457 | 150 | inferred_complete_timeline |
| `Action_None` | 459 | 476 | 18 | inferred_complete_timeline |
| `Action_None` | 480 | 485 | 6 | inferred_complete_timeline |
| `Action_None` | 503 | 569 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–484
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 297 | 250 | inferred_complete_timeline |
| `Action_None` | 302 | 315 | 14 | inferred_complete_timeline |
| `Action_None` | 323 | 326 | 4 | inferred_complete_timeline |
| `Action_None` | 332 | 484 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_LongSnap` | 48 | 101 | 54 | inferred_complete_timeline |
| `Action_None` | 102 | 188 | 87 | inferred_complete_timeline |
| `Action_None` | 191 | 209 | 19 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 223 | 240 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–473
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 254 | 207 | inferred_complete_timeline |
| `Action_None` | 257 | 347 | 91 | inferred_complete_timeline |
| `Action_None` | 350 | 415 | 66 | inferred_complete_timeline |
| `Action_None` | 418 | 473 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 252 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 232 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–424
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PuntBall` | 102 | 117 | 16 | inferred_complete_timeline |
| `Action_None` | 118 | 424 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 173 | 126 | inferred_complete_timeline |
| `Action_None` | 176 | 182 | 7 | inferred_complete_timeline |
| `Action_None` | 185 | 222 | 38 | inferred_complete_timeline |
| `Action_None` | 239 | 330 | 92 | inferred_complete_timeline |
| `Action_None` | 333 | 335 | 3 | inferred_complete_timeline |
| `Action_None` | 339 | 379 | 41 | inferred_complete_timeline |
| `Action_None` | 384 | 387 | 4 | inferred_complete_timeline |
| `Action_None` | 389 | 399 | 11 | inferred_complete_timeline |
| `Action_None` | 402 | 569 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 248 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 339 | 292 | inferred_complete_timeline |
| `Action_None` | 342 | 534 | 193 | inferred_complete_timeline |
| `Action_None` | 539 | 543 | 5 | inferred_complete_timeline |
| `Action_None` | 547 | 569 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 191 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–487
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 102 | 55 | inferred_complete_timeline |
| `Action_None` | 105 | 244 | 140 | inferred_complete_timeline |
| `Action_None` | 250 | 398 | 149 | inferred_complete_timeline |
| `Action_None` | 403 | 407 | 5 | inferred_complete_timeline |
| `Action_None` | 411 | 418 | 8 | inferred_complete_timeline |
| `Action_None` | 420 | 432 | 13 | inferred_complete_timeline |
| `Action_None` | 434 | 446 | 13 | inferred_complete_timeline |
| `Action_None` | 451 | 487 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 100 | 53 | inferred_complete_timeline |
| `Action_None` | 102 | 317 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_SnapReceive` | 78 | 78 | 1 | inferred_complete_timeline |
| `Action_None` | 79 | 98 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 250 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–345
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 101 | 54 | inferred_complete_timeline |
| `Action_None` | 104 | 345 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–497
- **Visible Samples:** 488

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 80 | 33 | inferred_complete_timeline |
| `Action_None` | 82 | 86 | 5 | inferred_complete_timeline |
| `Action_None` | 90 | 188 | 99 | inferred_complete_timeline |
| `Action_None` | 190 | 326 | 137 | inferred_complete_timeline |
| `Action_None` | 331 | 332 | 2 | inferred_complete_timeline |
| `Action_None` | 334 | 497 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–395
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 378 | 331 | inferred_complete_timeline |
| `Action_None` | 390 | 395 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 155 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 185 | 138 | inferred_complete_timeline |
| `Action_None` | 206 | 236 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 83–84 | 2 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 97–569 | 460 | 6 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 105–113 | 9 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 106–112 | 7 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 116–216 | 95 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 122–216 | 45 | 8 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 129–326 | 197 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 161–219 | 56 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 183–213 | 15 | 4 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 201–569 | 368 | 2 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 240–245 | 6 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 249–271 | 19 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 251–256 | 6 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 282–324 | 20 | 6 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 378–384 | 5 | 2 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 401–569 | 169 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 406–569 | 160 | 2 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 425–569 | 145 | 3 | Undefined position; Undefined team |
| `42` | `67` | Position_Unknown | Team_Unknown | 457–569 | 113 | 1 | Undefined position; Undefined team |
| `43` | `70` | Position_Unknown | Team_Unknown | 462–569 | 108 | 1 | Undefined position; Undefined team |
| `44` | `71` | Position_Unknown | Team_Unknown | 465–499 | 35 | 1 | Undefined position; Undefined team |
| `45` | `73` | Position_Unknown | Team_Unknown | 467–542 | 21 | 6 | Undefined position; Undefined team |
| `46` | `75` | Position_Unknown | Team_Unknown | 472–481 | 6 | 2 | Undefined position; Undefined team |
| `47` | `76` | Position_Unknown | Team_Unknown | 477–510 | 24 | 4 | Undefined position; Undefined team |
| `48` | `77` | Position_Unknown | Team_Unknown | 488–568 | 26 | 3 | Undefined position; Undefined team |
| `49` | `80` | Position_Unknown | Team_Unknown | 500–549 | 27 | 4 | Undefined position; Undefined team |
| `50` | `82` | Position_Unknown | Team_Unknown | 525–561 | 22 | 5 | Undefined position; Undefined team |
| `51` | `83` | Position_Unknown | Team_Unknown | 529–569 | 37 | 3 | Undefined position; Undefined team |
| `52` | `84` | Position_Unknown | Team_Unknown | 557–558 | 2 | 1 | Undefined position; Undefined team |
| `53` | `85` | Position_Unknown | Team_Unknown | 562–569 | 8 | 1 | Undefined position; Undefined team |
| `54` | `87` | Position_Unknown | Team_Unknown | 566–569 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `24` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ 34 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 34 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 68 |
| Missing visible bounding boxes during action | 137 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 102: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [48-302] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-457] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-476] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-485] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-100] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-325] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-437] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-457] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-209] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-240] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-254] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-347] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-415] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-473] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-297] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-315] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-484] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-232] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-424] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-339] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-534] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-543] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-173] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-182] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-222] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-330] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-379] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-387] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-399] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-248] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-378] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-395] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-252] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-102] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-244] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-398] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-407] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-418] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-432] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-446] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-487] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-155] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-250] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-236] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-86] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-188] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-326] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-497] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-101] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-345] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-100] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-317] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-191] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [235-301] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [303-414] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [427-569] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-112] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-178] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-191] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-216] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-191] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-207] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-303] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-326] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-190] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-219] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-213] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-234] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-569] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-245] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-263] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-271] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-256] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-298] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-324] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-465] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-569] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-569] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-499] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-468] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-481] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-496] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-519] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-522] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-542] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-475] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-481] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-486] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-494] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-502] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-510] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-504] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-546] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-568] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-517] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-524] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-549] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-526] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-533] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-542] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-552] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-561] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-542] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-563] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-558] for track '52' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>