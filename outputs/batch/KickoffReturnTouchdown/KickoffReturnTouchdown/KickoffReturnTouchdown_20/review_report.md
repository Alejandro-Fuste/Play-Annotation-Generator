# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_20

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_20`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 242
- **Validation Warnings:** 283
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 229
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `9` | `9` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `9` | `9` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | defense | `19` | `19` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `0` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `1` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `10` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `11` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `16` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `2` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `6` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `9` | `Group` | 0 | START | 0 | 34 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `9` | `9` | 35 | START | 35 | 76 |
| ✅ EXACT | `Action_KickBall` | Kicker | `9` | `9` | 77 | START | 77 | 81 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `19` | `19` | 181 | START | 181 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | `19` | `19` | 205 | START | 205 | 298 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | `19` | `19` | 526 | START | 526 | 538 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–371
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_KickApproach` | 35 | 76 | 42 | inferred_complete_timeline |
| `Action_KickBall` | 77 | 81 | 5 | inferred_complete_timeline |
| `Action_None` | 82 | 92 | 11 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 129 | 33 | inferred_complete_timeline |
| `Action_None` | 131 | 143 | 13 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 162 | 371 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–458
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 130 | 96 | inferred_complete_timeline |
| `Action_None` | 135 | 220 | 86 | inferred_complete_timeline |
| `Action_None` | 227 | 256 | 30 | inferred_complete_timeline |
| `Action_None` | 263 | 282 | 20 | inferred_complete_timeline |
| `Action_None` | 288 | 294 | 7 | inferred_complete_timeline |
| `Action_None` | 298 | 300 | 3 | inferred_complete_timeline |
| `Action_None` | 302 | 378 | 77 | inferred_complete_timeline |
| `Action_None` | 382 | 385 | 4 | inferred_complete_timeline |
| `Action_None` | 405 | 458 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 124 | 90 | inferred_complete_timeline |
| `Action_None` | 127 | 149 | 23 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 111 | 77 | inferred_complete_timeline |
| `Action_None` | 123 | 147 | 25 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 160 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 108 | 74 | inferred_complete_timeline |
| `Action_None` | 116 | 118 | 3 | inferred_complete_timeline |
| `Action_None` | 131 | 147 | 17 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_None` | 173 | 210 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 100 | 66 | inferred_complete_timeline |
| `Action_None` | 108 | 118 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–371
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 57 | 23 | inferred_complete_timeline |
| `Action_None` | 59 | 71 | 13 | inferred_complete_timeline |
| `Action_None` | 73 | 127 | 55 | inferred_complete_timeline |
| `Action_None` | 130 | 169 | 40 | inferred_complete_timeline |
| `Action_None` | 188 | 192 | 5 | inferred_complete_timeline |
| `Action_None` | 194 | 345 | 152 | inferred_complete_timeline |
| `Action_None` | 347 | 359 | 13 | inferred_complete_timeline |
| `Action_None` | 361 | 371 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–383
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 282 | 248 | inferred_complete_timeline |
| `Action_None` | 297 | 359 | 63 | inferred_complete_timeline |
| `Action_None` | 364 | 383 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–432
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 154 | 120 | inferred_complete_timeline |
| `Action_None` | 162 | 169 | 8 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_None` | 178 | 204 | 27 | inferred_complete_timeline |
| `Action_None` | 210 | 292 | 83 | inferred_complete_timeline |
| `Action_None` | 303 | 306 | 4 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 312 | 319 | 8 | inferred_complete_timeline |
| `Action_None` | 327 | 331 | 5 | inferred_complete_timeline |
| `Action_None` | 333 | 337 | 5 | inferred_complete_timeline |
| `Action_None` | 339 | 391 | 53 | inferred_complete_timeline |
| `Action_None` | 395 | 432 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 173 | 139 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 204 | 23 | inferred_complete_timeline |
| `Action_None` | 206 | 227 | 22 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 246 | 285 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 160 | 126 | inferred_complete_timeline |
| `Action_None` | 163 | 200 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–489
- **Visible Samples:** 481

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 330 | 296 | inferred_complete_timeline |
| `Action_None` | 340 | 489 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 209 | 175 | inferred_complete_timeline |
| `Action_None` | 212 | 289 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 490

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 24 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 28 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 52 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 180 | 119 | inferred_complete_timeline |
| `Action_CatchKick` | 181 | 193 | 13 | inferred_complete_timeline |
| `Action_None` | 194 | 204 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 205 | 298 | 94 | inferred_complete_timeline |
| `Action_BallCarry` | 302 | 383 | 82 | inferred_complete_timeline |
| `Action_BallCarry` | 385 | 388 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 391 | 392 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 398 | 400 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 408 | 525 | 118 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 526 | 538 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 539 | 539 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–447
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 176 | 142 | inferred_complete_timeline |
| `Action_None` | 179 | 206 | 28 | inferred_complete_timeline |
| `Action_None` | 208 | 234 | 27 | inferred_complete_timeline |
| `Action_None` | 237 | 327 | 91 | inferred_complete_timeline |
| `Action_None` | 336 | 447 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–398
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 398 | 364 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–363
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 158 | 124 | inferred_complete_timeline |
| `Action_None` | 164 | 300 | 137 | inferred_complete_timeline |
| `Action_None` | 305 | 338 | 34 | inferred_complete_timeline |
| `Action_None` | 341 | 358 | 18 | inferred_complete_timeline |
| `Action_None` | 361 | 363 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 271 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 294 | 260 | inferred_complete_timeline |
| `Action_None` | 297 | 318 | 22 | inferred_complete_timeline |
| `Action_None` | 320 | 329 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–483 | 401 | 13 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 57–242 | 145 | 11 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 59–245 | 181 | 4 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 110–143 | 29 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 116–117 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 120–145 | 25 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 158–449 | 254 | 8 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 166–167 | 2 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 173–486 | 273 | 14 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 179–182 | 4 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 183–399 | 160 | 7 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 207–216 | 10 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 208–329 | 100 | 8 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 231–236 | 6 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 239–246 | 8 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 247–400 | 152 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 255–259 | 5 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 260–477 | 195 | 7 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 275–465 | 172 | 3 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 295–476 | 167 | 4 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 299–358 | 48 | 4 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 307–364 | 53 | 3 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 309–310 | 2 | 1 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 332–333 | 2 | 1 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 338–339 | 2 | 1 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 346–486 | 133 | 3 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 348–417 | 66 | 2 | Undefined position; Undefined team |
| `46` | `63` | Position_Unknown | Team_Unknown | 362–369 | 8 | 1 | Undefined position; Undefined team |
| `47` | `64` | Position_Unknown | Team_Unknown | 392–481 | 53 | 5 | Undefined position; Undefined team |
| `48` | `65` | Position_Unknown | Team_Unknown | 397–467 | 70 | 2 | Undefined position; Undefined team |
| `49` | `70` | Position_Unknown | Team_Unknown | 448–539 | 71 | 7 | Undefined position; Undefined team |
| `50` | `71` | Position_Unknown | Team_Unknown | 466–476 | 11 | 1 | Undefined position; Undefined team |
| `51` | `72` | Position_Unknown | Team_Unknown | 470–471 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 215 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 42: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action 'Action_None' range [35-108] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-147] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-111] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-147] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-220] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-256] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-282] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-294] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-300] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-378] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-385] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-458] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-209] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-289] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-76] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-148] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-160] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-254] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-409] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-413] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-479] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-118] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-158] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-300] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-338] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-358] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-363] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-330] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-489] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-143] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-371] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-282] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-359] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-383] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-124] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-149] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-271] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-154] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-204] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-292] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-306] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-319] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-331] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-337] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-391] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-432] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-227] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-285] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-294] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-318] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-329] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-169] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-345] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-359] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-371] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-176] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-206] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-234] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-327] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-447] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-398] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-24] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-28] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-52] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-58] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-180] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [205-298] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [302-383] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [385-388] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [391-392] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [398-400] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-100] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-124] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-156] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-204] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-242] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-197] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-245] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-124] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-141] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-242] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-291] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-328] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-333] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-347] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-388] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-449] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-194] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-249] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-255] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-288] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-302] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-398] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-415] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-428] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-479] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-486] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-194] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-274] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-286] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-330] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-399] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-216] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-221] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-320] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-246] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-349] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-400] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-259] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-277] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-300] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-344] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-463] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-477] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-290] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-299] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-465] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-312] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-450] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-476] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-352] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-334] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-358] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-350] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-458] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-486] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-397] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-417] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-369] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-393] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-400] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-470] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-481] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-409] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-467] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-451] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-464] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-471] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-477] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-505] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-476] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>