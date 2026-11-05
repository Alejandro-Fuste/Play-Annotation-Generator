# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_82

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_82`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 74
- **Ball Tracks:** 0
- **Action Segments:** 351
- **Validation Warnings:** 435
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 337
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `3` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_CatchPunt` | Punt_Returner | defense | `2` | `2` |
| ✅ EXACT | `Action_BallCarry` | Punt_Returner | defense | `2` | `2` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `99` | `70` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `10` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `11` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `15` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `16` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `3` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `3` | `3` | 16 | START | 16 | 46 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `10` | `10` | 45 | END | 45 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `10` | `10` | 74 | START | 74 | 86 |
| ⚠️ START CHANGED | `Action_CatchPunt` | Punt_Returner | `2` | `2` | 220 | START | 222 | 224 |
| ✅ EXACT | `Action_BallCarry` | Punt_Returner | `2` | `2` | 248 | START | 248 | 250 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `99` | `70` | 550 | START | 550 | 555 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–351
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 16 | 1 | inferred_complete_timeline |
| `Action_None` | 23 | 24 | 2 | inferred_complete_timeline |
| `Action_None` | 36 | 43 | 8 | inferred_complete_timeline |
| `Action_None` | 64 | 70 | 7 | inferred_complete_timeline |
| `Action_None` | 72 | 103 | 32 | inferred_complete_timeline |
| `Action_None` | 105 | 114 | 10 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_None` | 122 | 243 | 122 | inferred_complete_timeline |
| `Action_None` | 247 | 351 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–517
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 140 | 125 | inferred_complete_timeline |
| `Action_None` | 142 | 164 | 23 | inferred_complete_timeline |
| `Action_None` | 167 | 181 | 15 | inferred_complete_timeline |
| `Action_None` | 184 | 188 | 5 | inferred_complete_timeline |
| `Action_None` | 191 | 208 | 18 | inferred_complete_timeline |
| `Action_None` | 210 | 215 | 6 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 250 | 22 | inferred_complete_timeline |
| `Action_None` | 256 | 263 | 8 | inferred_complete_timeline |
| `Action_None` | 265 | 335 | 71 | inferred_complete_timeline |
| `Action_None` | 337 | 349 | 13 | inferred_complete_timeline |
| `Action_None` | 354 | 374 | 21 | inferred_complete_timeline |
| `Action_None` | 380 | 385 | 6 | inferred_complete_timeline |
| `Action_None` | 387 | 391 | 5 | inferred_complete_timeline |
| `Action_None` | 393 | 422 | 30 | inferred_complete_timeline |
| `Action_None` | 425 | 435 | 11 | inferred_complete_timeline |
| `Action_None` | 438 | 448 | 11 | inferred_complete_timeline |
| `Action_None` | 474 | 475 | 2 | inferred_complete_timeline |
| `Action_None` | 477 | 494 | 18 | inferred_complete_timeline |
| `Action_None` | 496 | 500 | 5 | inferred_complete_timeline |
| `Action_None` | 502 | 508 | 7 | inferred_complete_timeline |
| `Action_None` | 514 | 517 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 41 | 26 | inferred_complete_timeline |
| `Action_None` | 52 | 56 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_LongSnap` | 16 | 46 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 19 | 4 | inferred_complete_timeline |
| `Action_None` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_None` | 58 | 59 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_SnapReceive` | 45 | 45 | 1 | inferred_complete_timeline |
| `Action_None` | 46 | 68 | 23 | inferred_complete_timeline |
| `Action_None` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_PuntBall` | 74 | 86 | 13 | inferred_complete_timeline |
| `Action_PuntBall` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 92 | 96 | 5 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_None` | 44 | 93 | 50 | inferred_complete_timeline |
| `Action_None` | 95 | 103 | 9 | inferred_complete_timeline |
| `Action_None` | 105 | 118 | 14 | inferred_complete_timeline |
| `Action_None` | 121 | 166 | 46 | inferred_complete_timeline |
| `Action_None` | 169 | 172 | 4 | inferred_complete_timeline |
| `Action_None` | 174 | 178 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 63 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 121 | 106 | inferred_complete_timeline |
| `Action_None` | 125 | 245 | 121 | inferred_complete_timeline |
| `Action_None` | 251 | 297 | 47 | inferred_complete_timeline |
| `Action_None` | 301 | 366 | 66 | inferred_complete_timeline |
| `Action_None` | 369 | 372 | 4 | inferred_complete_timeline |
| `Action_None` | 375 | 485 | 111 | inferred_complete_timeline |
| `Action_None` | 490 | 492 | 3 | inferred_complete_timeline |
| `Action_None` | 508 | 509 | 2 | inferred_complete_timeline |
| `Action_None` | 513 | 526 | 14 | inferred_complete_timeline |
| `Action_None` | 529 | 569 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 99 | 84 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–311
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 259 | 244 | inferred_complete_timeline |
| `Action_None` | 266 | 268 | 3 | inferred_complete_timeline |
| `Action_None` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_None` | 293 | 298 | 6 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_None` | 308 | 311 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 55 | 101 | 47 | inferred_complete_timeline |
| `Action_None` | 114 | 128 | 15 | inferred_complete_timeline |
| `Action_None` | 177 | 180 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 111 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 160 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–429
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 156 | 141 | inferred_complete_timeline |
| `Action_None` | 169 | 173 | 5 | inferred_complete_timeline |
| `Action_None` | 175 | 193 | 19 | inferred_complete_timeline |
| `Action_None` | 197 | 238 | 42 | inferred_complete_timeline |
| `Action_None` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_None` | 245 | 256 | 12 | inferred_complete_timeline |
| `Action_None` | 281 | 285 | 5 | inferred_complete_timeline |
| `Action_None` | 287 | 309 | 23 | inferred_complete_timeline |
| `Action_None` | 312 | 322 | 11 | inferred_complete_timeline |
| `Action_None` | 324 | 429 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Returner — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 108 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 165 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 171 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 219 | 38 | inferred_complete_timeline |
| `Action_CatchPunt` | 222 | 224 | 3 | inferred_complete_timeline |
| `Action_None` | 225 | 247 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 248 | 250 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 97 | 82 | inferred_complete_timeline |
| `Action_None` | 109 | 117 | 9 | inferred_complete_timeline |
| `Action_None` | 121 | 129 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 3–57 | 52 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 11–27 | 11 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 38–103 | 54 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 45–58 | 14 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 58–141 | 69 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 81–153 | 45 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 97–265 | 160 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 108–263 | 107 | 10 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 121–375 | 204 | 11 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 122–470 | 303 | 14 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 128–270 | 141 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 131–360 | 193 | 12 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 131–305 | 168 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 144–178 | 28 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 148–301 | 64 | 9 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 154–385 | 163 | 8 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 156–193 | 36 | 3 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 157–569 | 402 | 5 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 164–569 | 383 | 10 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 173–337 | 154 | 2 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 174–181 | 8 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 186–193 | 5 | 2 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 191–420 | 139 | 15 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 192–569 | 284 | 6 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 193–195 | 3 | 1 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 200–322 | 97 | 7 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 235–243 | 4 | 2 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 248–412 | 158 | 6 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 257–367 | 111 | 1 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 268–454 | 152 | 9 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 286–375 | 57 | 3 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 300–499 | 190 | 6 | Undefined position; Undefined team |
| `49` | `70` | Position_Unknown | Team_Unknown | 318–569 | 182 | 4 | Undefined position; Undefined team |
| `50` | `71` | Position_Unknown | Team_Unknown | 320–321 | 2 | 1 | Undefined position; Undefined team |
| `51` | `72` | Position_Unknown | Team_Unknown | 332–569 | 236 | 2 | Undefined position; Undefined team |
| `52` | `74` | Position_Unknown | Team_Unknown | 356–543 | 128 | 5 | Undefined position; Undefined team |
| `53` | `76` | Position_Unknown | Team_Unknown | 365–382 | 17 | 2 | Undefined position; Undefined team |
| `54` | `77` | Position_Unknown | Team_Unknown | 375–377 | 3 | 1 | Undefined position; Undefined team |
| `55` | `78` | Position_Unknown | Team_Unknown | 382–569 | 178 | 4 | Undefined position; Undefined team |
| `56` | `79` | Position_Unknown | Team_Unknown | 385–458 | 74 | 1 | Undefined position; Undefined team |
| `57` | `80` | Position_Unknown | Team_Unknown | 386–446 | 46 | 4 | Undefined position; Undefined team |
| `58` | `81` | Position_Unknown | Team_Unknown | 387–569 | 132 | 11 | Undefined position; Undefined team |
| `59` | `83` | Position_Unknown | Team_Unknown | 405–569 | 91 | 12 | Undefined position; Undefined team |
| `60` | `85` | Position_Unknown | Team_Unknown | 407–569 | 159 | 2 | Undefined position; Undefined team |
| `61` | `86` | Position_Unknown | Team_Unknown | 409–560 | 144 | 2 | Undefined position; Undefined team |
| `62` | `89` | Position_Unknown | Team_Unknown | 439–456 | 13 | 2 | Undefined position; Undefined team |
| `63` | `91` | Position_Unknown | Team_Unknown | 461–526 | 66 | 1 | Undefined position; Undefined team |
| `64` | `92` | Position_Unknown | Team_Unknown | 474–569 | 94 | 2 | Undefined position; Undefined team |
| `65` | `93` | Position_Unknown | Team_Unknown | 491–528 | 38 | 1 | Undefined position; Undefined team |
| `66` | `94` | Position_Unknown | Team_Unknown | 501–569 | 65 | 2 | Undefined position; Undefined team |
| `67` | `95` | Position_Unknown | Team_Unknown | 504–569 | 66 | 1 | Undefined position; Undefined team |
| `68` | `96` | Position_Unknown | Team_Unknown | 507–569 | 63 | 1 | Undefined position; Undefined team |
| `69` | `97` | Position_Unknown | Team_Unknown | 515–569 | 55 | 1 | Undefined position; Undefined team |
| `70` | `99` | Position_Unknown | Team_Unknown | 543–569 | 25 | 4 | Undefined position; Undefined team |
| `71` | `101` | Position_Unknown | Team_Unknown | 559–562 | 4 | 1 | Undefined position; Undefined team |
| `72` | `102` | Position_Unknown | Team_Unknown | 560–569 | 10 | 1 | Undefined position; Undefined team |
| `73` | `107` | Position_Unknown | Team_Unknown | 566–568 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `10` (2 segments found)
- ⚠️ `Action_CatchPunt` for actor_track_id `2` (Punt_Returner): Annotated start 220 != Inferred start 222

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punt_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ 57 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 57 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 114 |
| Missing visible bounding boxes during action | 318 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [16-160] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-41] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-56] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-165] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-219] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchPunt' range [222-224] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [248-250] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [16-46] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-97] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-117] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-129] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-193] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-238] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-256] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-309] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-322] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-429] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-245] for track '6' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-297] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-366] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-372] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-485] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-492] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-509] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-526] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-111] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-63] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-259] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-298] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-311] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [74-86] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-96] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-164] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-181] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-208] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-250] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-263] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-335] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-349] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-374] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-385] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-391] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-422] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-435] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-448] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-494] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-500] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-508] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-517] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-99] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 16, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [16-16] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-24] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-43] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-114] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-243] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-351] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-93] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-118] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-19] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-15] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-29] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-38] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-57] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-17] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-27] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-89] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-58] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-91] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-141] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-153] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-245] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-265] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-184] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-195] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-361] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-375] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-135] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-153] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-182] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-199] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-232] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-330] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-455] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-466] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-258] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-270] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-172] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-185] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-221] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-275] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-332] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-340] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-349] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-360] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-226] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-281] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-305] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-155] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-178] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-160] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-183] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-257] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-289] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-301] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-196] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-243] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-290] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-349] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-371] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-385] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-177] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-193] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-199] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-347] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-363] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-520] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-213] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-306] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-354] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-364] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-374] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-379] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-388] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-435] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-535] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-324] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-181] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-197] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-279] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-288] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-316] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-371] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-381] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-420] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-328] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-358] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-372] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-395] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-211] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-322] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-284] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-298] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-341] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-352] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-359] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-412] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-367] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-275] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-301] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-327] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-339] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-405] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-418] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-435] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-449] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-454] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-326] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-356] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-354] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-366] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-493] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-499] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-404] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-483] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-508] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-416] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-569] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-363] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-372] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-451] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-521] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-543] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-373] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-382] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-377] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-429] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-458] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-413] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-423] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-433] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-446] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-400] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-433] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-443] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-473] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-482] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-504] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-408] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-478] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-510] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-518] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-529] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-558] for track '59' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-561] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-569] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-425] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-569] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-412] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-560] for track '61' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-440] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-456] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-526] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-486] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-569] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-528] for track '65' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-551] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-558] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-562] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-568] for track '73' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>