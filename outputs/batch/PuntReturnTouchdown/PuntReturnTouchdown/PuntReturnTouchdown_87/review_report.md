# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_87

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_87`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 70
- **Ball Tracks:** 0
- **Action Segments:** 330
- **Validation Warnings:** 401
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 314
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `18` | `18` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `38` | `29` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `38` | `29` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `38` | `29` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `10` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `11` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `13` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `16` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `17` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `18` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `19` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `7` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `9` | `Group` | 0 | START | 0 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `18` | `18` | 68 | START | 68 | 83 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `7` | `7` | 95 | END | 95 | 95 |
| ✅ EXACT | `Action_PuntBall` | Punter | `7` | `7` | 127 | START | 127 | 140 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `38` | `29` | 229 | START | 229 | 250 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `38` | `29` | 262 | START | 262 | 331 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `38` | `29` | 576 | START | 576 | 580 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–469
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 81 | 14 | inferred_complete_timeline |
| `Action_None` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_None` | 92 | 97 | 6 | inferred_complete_timeline |
| `Action_None` | 101 | 106 | 6 | inferred_complete_timeline |
| `Action_None` | 112 | 121 | 10 | inferred_complete_timeline |
| `Action_None` | 127 | 141 | 15 | inferred_complete_timeline |
| `Action_None` | 144 | 146 | 3 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 250 | 90 | inferred_complete_timeline |
| `Action_None` | 252 | 346 | 95 | inferred_complete_timeline |
| `Action_None` | 348 | 355 | 8 | inferred_complete_timeline |
| `Action_None` | 360 | 370 | 11 | inferred_complete_timeline |
| `Action_None` | 376 | 415 | 40 | inferred_complete_timeline |
| `Action_None` | 417 | 444 | 28 | inferred_complete_timeline |
| `Action_None` | 449 | 458 | 10 | inferred_complete_timeline |
| `Action_None` | 462 | 464 | 3 | inferred_complete_timeline |
| `Action_None` | 466 | 469 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 597

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 385 | 318 | inferred_complete_timeline |
| `Action_None` | 387 | 587 | 201 | inferred_complete_timeline |
| `Action_None` | 589 | 590 | 2 | inferred_complete_timeline |
| `Action_None` | 592 | 599 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 85 | 18 | inferred_complete_timeline |
| `Action_None` | 88 | 98 | 11 | inferred_complete_timeline |
| `Action_None` | 104 | 106 | 3 | inferred_complete_timeline |
| `Action_None` | 114 | 121 | 8 | inferred_complete_timeline |
| `Action_None` | 124 | 141 | 18 | inferred_complete_timeline |
| `Action_None` | 176 | 182 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–461
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_LongSnap` | 68 | 83 | 16 | inferred_complete_timeline |
| `Action_LongSnap` | 89 | 126 | 38 | inferred_complete_timeline |
| `Action_None` | 127 | 234 | 108 | inferred_complete_timeline |
| `Action_None` | 238 | 406 | 169 | inferred_complete_timeline |
| `Action_None` | 435 | 436 | 2 | inferred_complete_timeline |
| `Action_None` | 441 | 442 | 2 | inferred_complete_timeline |
| `Action_None` | 444 | 448 | 5 | inferred_complete_timeline |
| `Action_None` | 450 | 451 | 2 | inferred_complete_timeline |
| `Action_None` | 454 | 461 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 188 | 121 | inferred_complete_timeline |
| `Action_None` | 190 | 241 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 158 | 91 | inferred_complete_timeline |
| `Action_None` | 173 | 176 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–356
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 148 | 81 | inferred_complete_timeline |
| `Action_None` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_None` | 160 | 183 | 24 | inferred_complete_timeline |
| `Action_None` | 187 | 206 | 20 | inferred_complete_timeline |
| `Action_None` | 209 | 356 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_SnapReceive` | 95 | 95 | 1 | inferred_complete_timeline |
| `Action_None` | 96 | 126 | 31 | inferred_complete_timeline |
| `Action_PuntBall` | 127 | 140 | 14 | inferred_complete_timeline |
| `Action_None` | 141 | 215 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 83 | 16 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 117 | 29 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 131 | 4 | inferred_complete_timeline |
| `Action_None` | 134 | 141 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 104 | 37 | inferred_complete_timeline |
| `Action_None` | 109 | 258 | 150 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 83 | 16 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 141 | 53 | inferred_complete_timeline |
| `Action_None` | 156 | 159 | 4 | inferred_complete_timeline |
| `Action_None` | 165 | 198 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–598
- **Visible Samples:** 552

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 78 | 11 | inferred_complete_timeline |
| `Action_None` | 89 | 118 | 30 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 156 | 30 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 171 | 4 | inferred_complete_timeline |
| `Action_None` | 175 | 248 | 74 | inferred_complete_timeline |
| `Action_None` | 254 | 336 | 83 | inferred_complete_timeline |
| `Action_None` | 339 | 372 | 34 | inferred_complete_timeline |
| `Action_None` | 375 | 465 | 91 | inferred_complete_timeline |
| `Action_None` | 468 | 475 | 8 | inferred_complete_timeline |
| `Action_None` | 477 | 503 | 27 | inferred_complete_timeline |
| `Action_None` | 506 | 517 | 12 | inferred_complete_timeline |
| `Action_None` | 521 | 535 | 15 | inferred_complete_timeline |
| `Action_None` | 537 | 540 | 4 | inferred_complete_timeline |
| `Action_None` | 544 | 598 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 83 | 16 | inferred_complete_timeline |
| `Action_None` | 89 | 95 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–373
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 80 | 13 | inferred_complete_timeline |
| `Action_None` | 89 | 326 | 238 | inferred_complete_timeline |
| `Action_None` | 328 | 350 | 23 | inferred_complete_timeline |
| `Action_None` | 352 | 359 | 8 | inferred_complete_timeline |
| `Action_None` | 361 | 373 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 87 | 20 | inferred_complete_timeline |
| `Action_None` | 89 | 117 | 29 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–555
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 104 | 37 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 109 | 555 | 447 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 81 | 14 | inferred_complete_timeline |
| `Action_None` | 89 | 118 | 30 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 131 | 4 | inferred_complete_timeline |
| `Action_None` | 134 | 141 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 104 | 37 | inferred_complete_timeline |
| `Action_None` | 112 | 118 | 7 | inferred_complete_timeline |
| `Action_None` | 128 | 131 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–501
- **Visible Samples:** 501

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 284 | 217 | inferred_complete_timeline |
| `Action_None` | 286 | 501 | 216 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–447 | 406 | 12 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 115–140 | 20 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 138–140 | 3 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 151–153 | 3 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 158–187 | 22 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 159–350 | 154 | 11 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 181–510 | 261 | 15 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 188–215 | 18 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 196–599 | 305 | 10 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 196–278 | 39 | 11 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 202–594 | 307 | 22 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 208–252 | 29 | 3 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 223–229 | 7 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 227–230 | 4 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 245–599 | 354 | 2 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 245–249 | 5 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 259–260 | 2 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 263–413 | 151 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 266–421 | 120 | 6 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 279–409 | 81 | 5 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 280–285 | 5 | 2 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 287–599 | 276 | 7 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 288–545 | 253 | 2 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 302–373 | 72 | 1 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 335–420 | 7 | 2 | Undefined position; Undefined team |
| `45` | `66` | Position_Unknown | Team_Unknown | 346–375 | 24 | 2 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 366–382 | 15 | 3 | Undefined position; Undefined team |
| `47` | `69` | Position_Unknown | Team_Unknown | 379–396 | 6 | 2 | Undefined position; Undefined team |
| `48` | `70` | Position_Unknown | Team_Unknown | 389–599 | 150 | 15 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 390–551 | 104 | 7 | Undefined position; Undefined team |
| `50` | `73` | Position_Unknown | Team_Unknown | 415–456 | 21 | 3 | Undefined position; Undefined team |
| `51` | `74` | Position_Unknown | Team_Unknown | 418–419 | 2 | 1 | Undefined position; Undefined team |
| `52` | `76` | Position_Unknown | Team_Unknown | 422–423 | 2 | 1 | Undefined position; Undefined team |
| `53` | `78` | Position_Unknown | Team_Unknown | 433–599 | 144 | 7 | Undefined position; Undefined team |
| `54` | `79` | Position_Unknown | Team_Unknown | 433–599 | 156 | 3 | Undefined position; Undefined team |
| `55` | `84` | Position_Unknown | Team_Unknown | 443–599 | 149 | 3 | Undefined position; Undefined team |
| `56` | `86` | Position_Unknown | Team_Unknown | 457–579 | 111 | 2 | Undefined position; Undefined team |
| `57` | `89` | Position_Unknown | Team_Unknown | 476–599 | 107 | 4 | Undefined position; Undefined team |
| `58` | `90` | Position_Unknown | Team_Unknown | 480–500 | 21 | 1 | Undefined position; Undefined team |
| `59` | `94` | Position_Unknown | Team_Unknown | 508–599 | 76 | 5 | Undefined position; Undefined team |
| `60` | `95` | Position_Unknown | Team_Unknown | 513–554 | 32 | 4 | Undefined position; Undefined team |
| `61` | `97` | Position_Unknown | Team_Unknown | 526–599 | 66 | 5 | Undefined position; Undefined team |
| `62` | `99` | Position_Unknown | Team_Unknown | 532–533 | 2 | 1 | Undefined position; Undefined team |
| `63` | `100` | Position_Unknown | Team_Unknown | 565–585 | 18 | 2 | Undefined position; Undefined team |
| `64` | `101` | Position_Unknown | Team_Unknown | 573–578 | 6 | 1 | Undefined position; Undefined team |
| `65` | `103` | Position_Unknown | Team_Unknown | 575–599 | 23 | 3 | Undefined position; Undefined team |
| `66` | `104` | Position_Unknown | Team_Unknown | 578–592 | 13 | 2 | Undefined position; Undefined team |
| `67` | `106` | Position_Unknown | Team_Unknown | 581–583 | 3 | 1 | Undefined position; Undefined team |
| `68` | `107` | Position_Unknown | Team_Unknown | 583–584 | 2 | 1 | Undefined position; Undefined team |
| `69` | `110` | Position_Unknown | Team_Unknown | 593–599 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `38` (18 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Guard` position mapped to `offense` team
- ⚠️ 51 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 51 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 102 |
| Missing visible bounding boxes during action | 295 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 176: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [68-385] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-587] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-590] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-599] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-104] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-555] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-104] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-131] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-87] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-117] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-80] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-326] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-350] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-373] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-83] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-95] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-78] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-118] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-156] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-248] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-336] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-372] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-465] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-475] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-503] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-517] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-535] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-540] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-598] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-215] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-190] for track '8' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-408] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-416] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-426] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-439] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-188] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-241] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-98] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-141] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-258] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-284] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-501] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-183] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-356] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-81] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-118] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-83] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-141] for track '15' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-158] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-83] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-117] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-141] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [68-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [89-126] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-234] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-406] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-448] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-451] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-461] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-81] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-106] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-121] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-250] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-346] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-355] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-370] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-415] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-444] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-458] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-464] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-469] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-140] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-172] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-187] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-186] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-199] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-220] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-238] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-279] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-312] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-340] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-350] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-201] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-270] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-306] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-333] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-371] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-412] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-510] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-199] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-342] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-369] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-379] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-428] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-463] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-499] for track '27' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-519] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-599] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-259] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [262-331] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [336-342] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [344-357] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [365-369] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [377-380] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [384-388] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [398-399] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [403-430] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [432-472] for track '29' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [474-475] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [482-487] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [510-517] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [521-522] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [524-525] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [538-539] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [543-554] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [556-575] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [576-580] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [583-594] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-231] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-229] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-250] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-599] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-413] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-276] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-311] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-382] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-388] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-392] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-421] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-320] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-354] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-381] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-409] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-434] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-454] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-501] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-521] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-526] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-464] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-545] for track '42' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-373] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-420] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-366] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-375] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-369] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-377] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-382] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-382] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-392] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-400] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-415] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-463] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-469] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-484] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-488] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-496] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-515] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-538] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-553] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-557] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-586] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-392] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-502] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-517] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-532] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-544] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-551] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-418] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-426] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-456] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-423] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-494] for track '53' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-501] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-522] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-532] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-551] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-557] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-501] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-567] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-505] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-586] for track '55' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-463] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-579] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-520] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-599] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-500] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-512] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-522] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-536] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-549] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-523] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-538] for track '60' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-543] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-554] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-535] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-550] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-561] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-585] for track '61' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-574] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-585] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-578] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-577] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-592] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-585] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-592] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-583] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-584] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>