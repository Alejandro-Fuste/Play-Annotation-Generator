# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_97

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_97`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 83
- **Ball Tracks:** 0
- **Action Segments:** 251
- **Validation Warnings:** 349
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 235
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `3` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `11` | `11` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `40` | `30` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `70` | `49` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `11` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `13` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `14` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `15` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `17` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `18` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `19` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `20` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `3` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `14` | `14` | 13 | START | 13 | 66 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `11` | `11` | 40 | END | 40 | 40 |
| ✅ EXACT | `Action_PuntBall` | Punter | `11` | `11` | 67 | START | 67 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `40` | `30` | 228 | START | 228 | 266 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `70` | `49` | 613 | START | 613 | 624 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–43
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 35 | 23 | inferred_complete_timeline |
| `Action_None` | 37 | 43 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–21
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 21 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_LongSnap` | 13 | 66 | 54 | inferred_complete_timeline |
| `Action_None` | 67 | 266 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 95 | 83 | inferred_complete_timeline |
| `Action_None` | 114 | 125 | 12 | inferred_complete_timeline |
| `Action_None` | 129 | 133 | 5 | inferred_complete_timeline |
| `Action_None` | 137 | 140 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 43 | 31 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 63 | 67 | 5 | inferred_complete_timeline |
| `Action_None` | 105 | 354 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 12 | 3 | inferred_complete_timeline |
| `Action_None` | 13 | 15 | 3 | inferred_complete_timeline |
| `Action_None` | 17 | 18 | 2 | inferred_complete_timeline |
| `Action_None` | 21 | 88 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_None` | 41 | 66 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 67 | 80 | 14 | inferred_complete_timeline |
| `Action_None` | 81 | 135 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 50 | 38 | inferred_complete_timeline |
| `Action_None` | 54 | 107 | 54 | inferred_complete_timeline |
| `Action_None` | 112 | 261 | 150 | inferred_complete_timeline |
| `Action_None` | 264 | 265 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 50 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 236 | 224 | inferred_complete_timeline |
| `Action_None` | 240 | 266 | 27 | inferred_complete_timeline |
| `Action_None` | 268 | 272 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 118 | 106 | inferred_complete_timeline |
| `Action_None` | 125 | 139 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 149 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 98 | 86 | inferred_complete_timeline |
| `Action_None` | 100 | 121 | 22 | inferred_complete_timeline |
| `Action_None` | 123 | 154 | 32 | inferred_complete_timeline |
| `Action_None` | 156 | 255 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 612

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 287 | 275 | inferred_complete_timeline |
| `Action_None` | 292 | 298 | 7 | inferred_complete_timeline |
| `Action_None` | 304 | 465 | 162 | inferred_complete_timeline |
| `Action_None` | 470 | 592 | 123 | inferred_complete_timeline |
| `Action_None` | 594 | 597 | 4 | inferred_complete_timeline |
| `Action_None` | 602 | 629 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 197 | 185 | inferred_complete_timeline |
| `Action_None` | 201 | 212 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 238 | 226 | inferred_complete_timeline |
| `Action_None` | 240 | 319 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 38 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 33 | 21 | inferred_complete_timeline |
| `Action_None` | 40 | 291 | 252 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |
| `Action_None` | 316 | 320 | 5 | inferred_complete_timeline |
| `Action_None` | 322 | 326 | 5 | inferred_complete_timeline |
| `Action_None` | 329 | 592 | 264 | inferred_complete_timeline |
| `Action_None` | 594 | 629 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–472
- **Visible Samples:** 460

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 173 | 161 | inferred_complete_timeline |
| `Action_None` | 176 | 208 | 33 | inferred_complete_timeline |
| `Action_None` | 210 | 437 | 228 | inferred_complete_timeline |
| `Action_None` | 442 | 448 | 7 | inferred_complete_timeline |
| `Action_None` | 454 | 468 | 15 | inferred_complete_timeline |
| `Action_None` | 470 | 472 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–582 | 561 | 9 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–118 | 118 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–176 | 177 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 15–38 | 24 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 49–177 | 125 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 53–299 | 244 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 53–56 | 4 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 81–157 | 69 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 113–629 | 492 | 10 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 124–211 | 88 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 152–153 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 176–307 | 112 | 4 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 187–199 | 13 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 207–319 | 113 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 211–213 | 3 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 218–219 | 2 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 222–310 | 88 | 2 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 236–276 | 33 | 3 | Undefined position; Undefined team |
| `37` | `57` | Position_Unknown | Team_Unknown | 237–251 | 15 | 1 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 250–565 | 310 | 5 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 251–254 | 4 | 1 | Undefined position; Undefined team |
| `40` | `60` | Position_Unknown | Team_Unknown | 253–314 | 41 | 2 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 256–440 | 185 | 1 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 263–343 | 39 | 2 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 277–326 | 49 | 2 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 277–629 | 350 | 3 | Undefined position; Undefined team |
| `45` | `66` | Position_Unknown | Team_Unknown | 282–598 | 314 | 2 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 283–629 | 340 | 4 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 293–629 | 323 | 5 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |
| `49` | `70` | Position_Unknown | Team_Unknown | 314–629 | 304 | 7 | Undefined position; Undefined team |
| `50` | `71` | Position_Unknown | Team_Unknown | 315–629 | 298 | 7 | Undefined position; Undefined team |
| `51` | `72` | Position_Unknown | Team_Unknown | 318–454 | 117 | 5 | Undefined position; Undefined team |
| `52` | `73` | Position_Unknown | Team_Unknown | 318–604 | 258 | 6 | Undefined position; Undefined team |
| `53` | `74` | Position_Unknown | Team_Unknown | 328–629 | 264 | 9 | Undefined position; Undefined team |
| `54` | `75` | Position_Unknown | Team_Unknown | 340–629 | 263 | 5 | Undefined position; Undefined team |
| `55` | `76` | Position_Unknown | Team_Unknown | 358–629 | 272 | 1 | Undefined position; Undefined team |
| `56` | `77` | Position_Unknown | Team_Unknown | 358–383 | 26 | 1 | Undefined position; Undefined team |
| `57` | `79` | Position_Unknown | Team_Unknown | 362–363 | 2 | 1 | Undefined position; Undefined team |
| `58` | `81` | Position_Unknown | Team_Unknown | 372–398 | 24 | 2 | Undefined position; Undefined team |
| `59` | `82` | Position_Unknown | Team_Unknown | 382–393 | 12 | 1 | Undefined position; Undefined team |
| `60` | `84` | Position_Unknown | Team_Unknown | 395–629 | 208 | 4 | Undefined position; Undefined team |
| `61` | `85` | Position_Unknown | Team_Unknown | 404–596 | 182 | 7 | Undefined position; Undefined team |
| `62` | `86` | Position_Unknown | Team_Unknown | 428–447 | 17 | 2 | Undefined position; Undefined team |
| `63` | `88` | Position_Unknown | Team_Unknown | 450–452 | 3 | 1 | Undefined position; Undefined team |
| `64` | `89` | Position_Unknown | Team_Unknown | 461–629 | 162 | 2 | Undefined position; Undefined team |
| `65` | `92` | Position_Unknown | Team_Unknown | 485–628 | 144 | 1 | Undefined position; Undefined team |
| `66` | `95` | Position_Unknown | Team_Unknown | 491–629 | 139 | 1 | Undefined position; Undefined team |
| `67` | `97` | Position_Unknown | Team_Unknown | 499–518 | 7 | 3 | Undefined position; Undefined team |
| `68` | `98` | Position_Unknown | Team_Unknown | 500–510 | 7 | 2 | Undefined position; Undefined team |
| `69` | `100` | Position_Unknown | Team_Unknown | 510–629 | 116 | 4 | Undefined position; Undefined team |
| `70` | `101` | Position_Unknown | Team_Unknown | 513–548 | 36 | 1 | Undefined position; Undefined team |
| `71` | `103` | Position_Unknown | Team_Unknown | 520–525 | 4 | 2 | Undefined position; Undefined team |
| `72` | `105` | Position_Unknown | Team_Unknown | 522–523 | 2 | 1 | Undefined position; Undefined team |
| `73` | `106` | Position_Unknown | Team_Unknown | 535–537 | 3 | 1 | Undefined position; Undefined team |
| `74` | `108` | Position_Unknown | Team_Unknown | 557–558 | 2 | 1 | Undefined position; Undefined team |
| `75` | `111` | Position_Unknown | Team_Unknown | 568–573 | 6 | 1 | Undefined position; Undefined team |
| `76` | `112` | Position_Unknown | Team_Unknown | 569–571 | 3 | 1 | Undefined position; Undefined team |
| `77` | `116` | Position_Unknown | Team_Unknown | 591–615 | 7 | 3 | Undefined position; Undefined team |
| `78` | `117` | Position_Unknown | Team_Unknown | 593–611 | 17 | 2 | Undefined position; Undefined team |
| `79` | `118` | Position_Unknown | Team_Unknown | 612–618 | 7 | 1 | Undefined position; Undefined team |
| `80` | `120` | Position_Unknown | Team_Unknown | 616–629 | 10 | 3 | Undefined position; Undefined team |
| `81` | `121` | Position_Unknown | Team_Unknown | 622–625 | 4 | 1 | Undefined position; Undefined team |
| `82` | `122` | Position_Unknown | Team_Unknown | 628–629 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `40` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ 64 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 64 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 128 |
| Missing visible bounding boxes during action | 214 |
| Track-related warning | 4 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 195: Duplicate assignment for track ID '20' in grid. Overwriting previous assignment.
- ⚠️ Row 196: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 196: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 196: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [13-238] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-319] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-38] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-98] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-121] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-255] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-43] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-67] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-354] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-33] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-291] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-320] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-326] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-592] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-149] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-287] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-298] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-465] for track '6' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-592] for track '6' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-597] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-629] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-208] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-437] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-448] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-468] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-472] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-197] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-212] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-310] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-334] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-442] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-448] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-537] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-582] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-118] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-118] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [13-66] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-266] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-236] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-266] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-272] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-35] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-43] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-50] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-261] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-50] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-21] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-15] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-18] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-88] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-38] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-158] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-250] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-267] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-273] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-127] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-157] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-137] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-167] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-481] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-525] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-592] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-603] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-211] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-182] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-227] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [228-266] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [270-307] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-199] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-319] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-273] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-310] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-244] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-267] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-251] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-469] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-474] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-507] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-559] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-565] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-267] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-314] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-440] for track '41' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-271] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-343] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-321] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-566] for track '44' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-588] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-629] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-310] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-598] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-304] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-444] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-506] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-629] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-441] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-492] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-579] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-585] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-557] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [559-572] for track '49' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [576-582] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [585-587] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-564] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-578] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-588] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-600] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-336] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-418] for track '51' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-454] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-334] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-469] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-578] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-604] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-426] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-494] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-499] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-556] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-585] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-592] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-599] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-583] for track '54' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-588] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-597] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-616] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-629] for track '55' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-383] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-375] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-398] for track '58' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-393] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-432] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-457] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-552] for track '60' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-409] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-425] for track '61' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-575] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-580] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-592] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-596] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-434] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-447] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-452] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-606] for track '64' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-628] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-629] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-518] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-503] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-510] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-573] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-576] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-626] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-629] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-548] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-523] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-537] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-558] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-573] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-571] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-592] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-597] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-615] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-599] for track '78' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-611] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-618] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-618] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-625] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-625] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-629] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>