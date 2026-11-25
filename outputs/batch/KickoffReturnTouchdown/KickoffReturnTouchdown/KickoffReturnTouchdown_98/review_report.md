# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_98

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_98`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 84
- **Ball Tracks:** 0
- **Action Segments:** 281
- **Validation Warnings:** 390
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 267
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `7` | `7` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `7` | `7` |
| ❌ MISSING SEGMENT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `45` | `31` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `45` | `31` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `0` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `1` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `10` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `12` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `13` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `14` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `15` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `4` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `5` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `7` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `9` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `7` | `7` | 18 | START | 18 | 66 |
| ✅ EXACT | `Action_KickBall` | Kicker | `7` | `7` | 67 | START | 67 | 71 |
| ❌ MISSING SEGMENT | `Action_CatchKick` | Position_Unknown | `45` | `31` | 194 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `45` | `31` | 215 | START | 235 | 261 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 622

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_KickApproach` | 18 | 66 | 49 | inferred_complete_timeline |
| `Action_KickBall` | 67 | 71 | 5 | inferred_complete_timeline |
| `Action_None` | 72 | 84 | 13 | inferred_complete_timeline |
| `Action_None` | 91 | 450 | 360 | inferred_complete_timeline |
| `Action_None` | 453 | 629 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 358 | 341 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 585

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 153 | 136 | inferred_complete_timeline |
| `Action_None` | 155 | 157 | 3 | inferred_complete_timeline |
| `Action_None` | 159 | 184 | 26 | inferred_complete_timeline |
| `Action_None` | 186 | 214 | 29 | inferred_complete_timeline |
| `Action_None` | 220 | 239 | 20 | inferred_complete_timeline |
| `Action_None` | 241 | 251 | 11 | inferred_complete_timeline |
| `Action_None` | 254 | 283 | 30 | inferred_complete_timeline |
| `Action_None` | 291 | 296 | 6 | inferred_complete_timeline |
| `Action_None` | 299 | 300 | 2 | inferred_complete_timeline |
| `Action_None` | 305 | 315 | 11 | inferred_complete_timeline |
| `Action_None` | 317 | 364 | 48 | inferred_complete_timeline |
| `Action_None` | 369 | 375 | 7 | inferred_complete_timeline |
| `Action_None` | 377 | 401 | 25 | inferred_complete_timeline |
| `Action_None` | 405 | 489 | 85 | inferred_complete_timeline |
| `Action_None` | 497 | 502 | 6 | inferred_complete_timeline |
| `Action_None` | 505 | 512 | 8 | inferred_complete_timeline |
| `Action_None` | 514 | 521 | 8 | inferred_complete_timeline |
| `Action_None` | 524 | 629 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–288
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 92 | 75 | inferred_complete_timeline |
| `Action_None` | 96 | 100 | 5 | inferred_complete_timeline |
| `Action_None` | 103 | 226 | 124 | inferred_complete_timeline |
| `Action_None` | 229 | 243 | 15 | inferred_complete_timeline |
| `Action_None` | 256 | 288 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 70 | 53 | inferred_complete_timeline |
| `Action_None` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_None` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_None` | 79 | 85 | 7 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 111 | 245 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 287 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 215 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–331
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 69 | 52 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_None` | 111 | 131 | 21 | inferred_complete_timeline |
| `Action_None` | 133 | 275 | 143 | inferred_complete_timeline |
| `Action_None` | 278 | 279 | 2 | inferred_complete_timeline |
| `Action_None` | 281 | 290 | 10 | inferred_complete_timeline |
| `Action_None` | 292 | 305 | 14 | inferred_complete_timeline |
| `Action_None` | 307 | 309 | 3 | inferred_complete_timeline |
| `Action_None` | 311 | 331 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 56 | 39 | inferred_complete_timeline |
| `Action_None` | 58 | 62 | 5 | inferred_complete_timeline |
| `Action_None` | 66 | 68 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 62 | 45 | inferred_complete_timeline |
| `Action_None` | 66 | 67 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 60 | 43 | inferred_complete_timeline |
| `Action_None` | 65 | 68 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 128 | 111 | inferred_complete_timeline |
| `Action_None` | 130 | 186 | 57 | inferred_complete_timeline |
| `Action_None` | 194 | 202 | 9 | inferred_complete_timeline |
| `Action_None` | 210 | 224 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 167 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 173 | 156 | inferred_complete_timeline |
| `Action_None` | 179 | 201 | 23 | inferred_complete_timeline |
| `Action_None` | 214 | 334 | 121 | inferred_complete_timeline |
| `Action_None` | 412 | 629 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 72 | 55 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_None` | 88 | 263 | 176 | inferred_complete_timeline |
| `Action_None` | 265 | 267 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 189 | 172 | inferred_complete_timeline |
| `Action_None` | 196 | 217 | 22 | inferred_complete_timeline |
| `Action_None` | 219 | 239 | 21 | inferred_complete_timeline |
| `Action_None` | 241 | 245 | 5 | inferred_complete_timeline |
| `Action_None` | 264 | 265 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 10–74 | 51 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 75–241 | 166 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 80–239 | 155 | 5 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 114–115 | 2 | 1 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 116–118 | 3 | 1 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 119–264 | 145 | 2 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 119–377 | 259 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 119–262 | 128 | 5 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 119–125 | 7 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 138–243 | 106 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 144–230 | 85 | 3 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 153–253 | 97 | 4 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 159–171 | 11 | 2 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 188–226 | 39 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 235–317 | 33 | 3 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 235–300 | 66 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 235–251 | 14 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 242–256 | 15 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 259–261 | 3 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 295–629 | 330 | 4 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 298–629 | 278 | 7 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 303–308 | 6 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 316–512 | 185 | 6 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 316–442 | 97 | 8 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 318–349 | 32 | 1 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 324–352 | 18 | 3 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 329–629 | 301 | 1 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 331–629 | 299 | 1 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 332–629 | 295 | 3 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 334–615 | 208 | 7 | Undefined position; Undefined team |
| `47` | `67` | Position_Unknown | Team_Unknown | 338–629 | 275 | 6 | Undefined position; Undefined team |
| `48` | `68` | Position_Unknown | Team_Unknown | 339–357 | 19 | 1 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 340–629 | 268 | 5 | Undefined position; Undefined team |
| `50` | `70` | Position_Unknown | Team_Unknown | 342–359 | 18 | 1 | Undefined position; Undefined team |
| `51` | `72` | Position_Unknown | Team_Unknown | 360–362 | 3 | 1 | Undefined position; Undefined team |
| `52` | `73` | Position_Unknown | Team_Unknown | 364–629 | 226 | 8 | Undefined position; Undefined team |
| `53` | `75` | Position_Unknown | Team_Unknown | 366–445 | 78 | 2 | Undefined position; Undefined team |
| `54` | `76` | Position_Unknown | Team_Unknown | 368–411 | 8 | 2 | Undefined position; Undefined team |
| `55` | `77` | Position_Unknown | Team_Unknown | 369–373 | 5 | 1 | Undefined position; Undefined team |
| `56` | `79` | Position_Unknown | Team_Unknown | 379–416 | 35 | 2 | Undefined position; Undefined team |
| `57` | `80` | Position_Unknown | Team_Unknown | 383–559 | 89 | 15 | Undefined position; Undefined team |
| `58` | `82` | Position_Unknown | Team_Unknown | 385–439 | 44 | 2 | Undefined position; Undefined team |
| `59` | `83` | Position_Unknown | Team_Unknown | 391–629 | 231 | 2 | Undefined position; Undefined team |
| `60` | `85` | Position_Unknown | Team_Unknown | 395–629 | 235 | 1 | Undefined position; Undefined team |
| `61` | `88` | Position_Unknown | Team_Unknown | 408–409 | 2 | 1 | Undefined position; Undefined team |
| `62` | `90` | Position_Unknown | Team_Unknown | 413–483 | 71 | 1 | Undefined position; Undefined team |
| `63` | `91` | Position_Unknown | Team_Unknown | 413–623 | 211 | 1 | Undefined position; Undefined team |
| `64` | `92` | Position_Unknown | Team_Unknown | 417–629 | 211 | 2 | Undefined position; Undefined team |
| `65` | `94` | Position_Unknown | Team_Unknown | 422–566 | 124 | 7 | Undefined position; Undefined team |
| `66` | `95` | Position_Unknown | Team_Unknown | 425–488 | 57 | 3 | Undefined position; Undefined team |
| `67` | `97` | Position_Unknown | Team_Unknown | 431–629 | 199 | 1 | Undefined position; Undefined team |
| `68` | `98` | Position_Unknown | Team_Unknown | 432–508 | 30 | 6 | Undefined position; Undefined team |
| `69` | `100` | Position_Unknown | Team_Unknown | 445–622 | 135 | 9 | Undefined position; Undefined team |
| `70` | `101` | Position_Unknown | Team_Unknown | 451–629 | 177 | 2 | Undefined position; Undefined team |
| `71` | `102` | Position_Unknown | Team_Unknown | 456–464 | 9 | 1 | Undefined position; Undefined team |
| `72` | `104` | Position_Unknown | Team_Unknown | 485–491 | 7 | 1 | Undefined position; Undefined team |
| `73` | `105` | Position_Unknown | Team_Unknown | 485–629 | 112 | 7 | Undefined position; Undefined team |
| `74` | `107` | Position_Unknown | Team_Unknown | 508–510 | 3 | 1 | Undefined position; Undefined team |
| `75` | `108` | Position_Unknown | Team_Unknown | 515–629 | 112 | 4 | Undefined position; Undefined team |
| `76` | `109` | Position_Unknown | Team_Unknown | 518–520 | 3 | 1 | Undefined position; Undefined team |
| `77` | `111` | Position_Unknown | Team_Unknown | 535–536 | 2 | 1 | Undefined position; Undefined team |
| `78` | `112` | Position_Unknown | Team_Unknown | 540–629 | 71 | 4 | Undefined position; Undefined team |
| `79` | `114` | Position_Unknown | Team_Unknown | 543–578 | 31 | 3 | Undefined position; Undefined team |
| `80` | `115` | Position_Unknown | Team_Unknown | 549–557 | 9 | 1 | Undefined position; Undefined team |
| `81` | `118` | Position_Unknown | Team_Unknown | 563–587 | 25 | 1 | Undefined position; Undefined team |
| `82` | `119` | Position_Unknown | Team_Unknown | 564–629 | 66 | 1 | Undefined position; Undefined team |
| `83` | `122` | Position_Unknown | Team_Unknown | 616–617 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CatchKick` on target `45` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `45` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ 68 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 68 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 100, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '636,642,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 136 |
| Missing visible bounding boxes during action | 251 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Segment 'Action_CatchKick' for track '31' has invalid range: start=235, end=198. Clamping end to start.
- ⚠️ Action 'Action_None' range [18-358] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-92] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-226] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-243] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-288] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-128] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-202] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-224] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-287] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-153] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-184] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-214] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-251] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-283] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-296] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-315] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-364] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-375] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-401] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-489] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-502] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-512] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-521] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-629] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-189] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-217] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-239] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-245] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-450] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-201] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-334] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-629] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-215] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-62] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-263] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-70] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-245] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-68] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-131] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-275] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-290] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-305] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-331] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-56] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-62] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-13] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-68] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-215] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-241] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-150] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-231] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-264] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-377] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-130] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-231] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-249] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-125] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-243] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-151] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-230] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-249] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-171] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [235-261] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [264-267] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [316-317] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-300] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-251] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-256] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-519] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-542] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-553] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-629] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-440] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-512] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-515] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-548] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-566] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-308] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-471] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-488] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-497] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-504] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-325] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-366] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-382] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-394] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-408] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-429] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-349] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-336] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-629] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-409] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-550] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-339] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-371] for track '46' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-502] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-577] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-600] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-606] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-615] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-393] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-416] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-497] for track '47' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-510] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-519] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-357] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-349] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-363] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-507] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-359] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-362] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-435] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-444] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-452] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-519] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-533] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-595] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-409] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-445] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-371] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-411] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-373] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-402] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-416] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-408] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-423] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-430] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-437] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-441] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-453] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-459] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-497] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-507] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-512] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-518] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-546] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-559] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-426] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-515] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-629] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-483] for track '62' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-623] for track '63' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-521] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-629] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-428] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-438] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-457] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-532] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-544] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-562] for track '65' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-566] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-470] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-488] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-438] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-471] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-476] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-481] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-508] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-462] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-508] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-521] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-578] for track '69' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-602] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-610] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-618] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-622] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-542] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-464] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-491] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-515] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-519] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-536] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-571] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-578] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-610] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-510] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-524] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-555] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-567] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-629] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-520] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-550] for track '78' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-564] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-629] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-553] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-571] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-578] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-557] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-587] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-617] for track '83' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_98'; source metadata written as null.

</details>