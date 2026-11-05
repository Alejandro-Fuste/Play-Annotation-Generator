# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_13`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 689
- **Player Tracks:** 98
- **Ball Tracks:** 0
- **Action Segments:** 395
- **Validation Warnings:** 526
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 383
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `15` | `15` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `51` | `34` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `51` | `34` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `51` | `34` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `1` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `12` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `13` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `15` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `17` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `18` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `7` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `8` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `9` | `Group` | 0 | START | 0 | 63 |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | `13` | `13` | 64 | START | 64 | 127 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `15` | `15` | 93 | END | 93 | 93 |
| ✅ EXACT | `Action_PuntBall` | Punter | `15` | `15` | 128 | START | 128 | 139 |
| ❌ MISSING SEGMENT | `Action_CatchPunt` | Position_Unknown | `51` | `34` | 237 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `51` | `34` | 268 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `51` | `34` | 680 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Gunner — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 128 | 65 | inferred_complete_timeline |
| `Action_None` | 131 | 133 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 81 | 18 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 149 | 45 | inferred_complete_timeline |
| `Action_None` | 151 | 159 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 128 | 65 | inferred_complete_timeline |
| `Action_None` | 132 | 170 | 39 | inferred_complete_timeline |
| `Action_None` | 175 | 214 | 40 | inferred_complete_timeline |
| `Action_None` | 216 | 236 | 21 | inferred_complete_timeline |
| `Action_None` | 239 | 257 | 19 | inferred_complete_timeline |
| `Action_None` | 265 | 268 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–430
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 168 | 105 | inferred_complete_timeline |
| `Action_None` | 170 | 235 | 66 | inferred_complete_timeline |
| `Action_None` | 237 | 318 | 82 | inferred_complete_timeline |
| `Action_None` | 321 | 387 | 67 | inferred_complete_timeline |
| `Action_None` | 392 | 400 | 9 | inferred_complete_timeline |
| `Action_None` | 414 | 417 | 4 | inferred_complete_timeline |
| `Action_None` | 419 | 430 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–316
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_SnapReceive` | 93 | 93 | 1 | inferred_complete_timeline |
| `Action_None` | 94 | 127 | 34 | inferred_complete_timeline |
| `Action_PuntBall` | 128 | 139 | 12 | inferred_complete_timeline |
| `Action_None` | 140 | 312 | 173 | inferred_complete_timeline |
| `Action_None` | 315 | 316 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_LongSnap` | 64 | 127 | 64 | inferred_complete_timeline |
| `Action_None` | 128 | 217 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 268 | 205 | inferred_complete_timeline |
| `Action_None` | 272 | 273 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 147 | 84 | inferred_complete_timeline |
| `Action_None` | 154 | 200 | 47 | inferred_complete_timeline |
| `Action_None` | 204 | 207 | 4 | inferred_complete_timeline |
| `Action_None` | 214 | 261 | 48 | inferred_complete_timeline |
| `Action_None` | 263 | 264 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–453
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 192 | 129 | inferred_complete_timeline |
| `Action_None` | 197 | 202 | 6 | inferred_complete_timeline |
| `Action_None` | 204 | 214 | 11 | inferred_complete_timeline |
| `Action_None` | 226 | 269 | 44 | inferred_complete_timeline |
| `Action_None` | 273 | 279 | 7 | inferred_complete_timeline |
| `Action_None` | 284 | 392 | 109 | inferred_complete_timeline |
| `Action_None` | 394 | 453 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–372
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 112 | 49 | inferred_complete_timeline |
| `Action_None` | 135 | 372 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 97 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 634

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 183 | 120 | inferred_complete_timeline |
| `Action_None` | 186 | 337 | 152 | inferred_complete_timeline |
| `Action_None` | 339 | 343 | 5 | inferred_complete_timeline |
| `Action_None` | 346 | 359 | 14 | inferred_complete_timeline |
| `Action_None` | 361 | 375 | 15 | inferred_complete_timeline |
| `Action_None` | 413 | 427 | 15 | inferred_complete_timeline |
| `Action_None` | 433 | 465 | 33 | inferred_complete_timeline |
| `Action_None` | 468 | 475 | 8 | inferred_complete_timeline |
| `Action_None` | 479 | 486 | 8 | inferred_complete_timeline |
| `Action_None` | 490 | 689 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 109 | 46 | inferred_complete_timeline |
| `Action_None` | 111 | 116 | 6 | inferred_complete_timeline |
| `Action_None` | 118 | 135 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–320
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 221 | 158 | inferred_complete_timeline |
| `Action_None` | 224 | 247 | 24 | inferred_complete_timeline |
| `Action_None` | 263 | 265 | 3 | inferred_complete_timeline |
| `Action_None` | 267 | 271 | 5 | inferred_complete_timeline |
| `Action_None` | 318 | 320 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 127 | 64 | inferred_complete_timeline |
| `Action_None` | 129 | 250 | 122 | inferred_complete_timeline |
| `Action_None` | 322 | 323 | 2 | inferred_complete_timeline |
| `Action_None` | 325 | 329 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 135 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 151 | 88 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 175 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–512
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 182 | 119 | inferred_complete_timeline |
| `Action_None` | 188 | 272 | 85 | inferred_complete_timeline |
| `Action_None` | 275 | 277 | 3 | inferred_complete_timeline |
| `Action_None` | 284 | 286 | 3 | inferred_complete_timeline |
| `Action_None` | 293 | 294 | 2 | inferred_complete_timeline |
| `Action_None` | 299 | 302 | 4 | inferred_complete_timeline |
| `Action_None` | 307 | 311 | 5 | inferred_complete_timeline |
| `Action_None` | 342 | 427 | 86 | inferred_complete_timeline |
| `Action_None` | 429 | 430 | 2 | inferred_complete_timeline |
| `Action_None` | 435 | 441 | 7 | inferred_complete_timeline |
| `Action_None` | 451 | 512 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–334 | 246 | 17 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–78 | 38 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 64–135 | 69 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 87–215 | 126 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 96–201 | 99 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 118–151 | 12 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 155–190 | 36 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 165–359 | 169 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 168–323 | 142 | 5 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 187–189 | 3 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 187–689 | 385 | 15 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 191–270 | 72 | 4 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 198–366 | 169 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 208–401 | 142 | 4 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 209–316 | 108 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 212–236 | 11 | 3 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 222–287 | 4 | 2 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 231–233 | 3 | 1 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 249–297 | 22 | 2 | Undefined position; Undefined team |
| `39` | `60` | Position_Unknown | Team_Unknown | 255–258 | 4 | 1 | Undefined position; Undefined team |
| `40` | `64` | Position_Unknown | Team_Unknown | 262–341 | 54 | 6 | Undefined position; Undefined team |
| `41` | `65` | Position_Unknown | Team_Unknown | 263–267 | 5 | 1 | Undefined position; Undefined team |
| `42` | `66` | Position_Unknown | Team_Unknown | 265–366 | 68 | 6 | Undefined position; Undefined team |
| `43` | `70` | Position_Unknown | Team_Unknown | 276–689 | 347 | 7 | Undefined position; Undefined team |
| `44` | `71` | Position_Unknown | Team_Unknown | 278–372 | 95 | 1 | Undefined position; Undefined team |
| `45` | `72` | Position_Unknown | Team_Unknown | 280–282 | 3 | 1 | Undefined position; Undefined team |
| `46` | `75` | Position_Unknown | Team_Unknown | 289–293 | 5 | 1 | Undefined position; Undefined team |
| `47` | `76` | Position_Unknown | Team_Unknown | 293–344 | 52 | 1 | Undefined position; Undefined team |
| `48` | `78` | Position_Unknown | Team_Unknown | 301–303 | 3 | 1 | Undefined position; Undefined team |
| `49` | `79` | Position_Unknown | Team_Unknown | 302–303 | 2 | 1 | Undefined position; Undefined team |
| `50` | `80` | Position_Unknown | Team_Unknown | 310–312 | 3 | 1 | Undefined position; Undefined team |
| `51` | `81` | Position_Unknown | Team_Unknown | 311–367 | 8 | 3 | Undefined position; Undefined team |
| `52` | `82` | Position_Unknown | Team_Unknown | 313–314 | 2 | 1 | Undefined position; Undefined team |
| `53` | `83` | Position_Unknown | Team_Unknown | 327–330 | 4 | 1 | Undefined position; Undefined team |
| `54` | `84` | Position_Unknown | Team_Unknown | 327–689 | 254 | 17 | Undefined position; Undefined team |
| `55` | `85` | Position_Unknown | Team_Unknown | 331–336 | 6 | 1 | Undefined position; Undefined team |
| `56` | `86` | Position_Unknown | Team_Unknown | 337–339 | 3 | 1 | Undefined position; Undefined team |
| `57` | `88` | Position_Unknown | Team_Unknown | 355–360 | 6 | 1 | Undefined position; Undefined team |
| `58` | `90` | Position_Unknown | Team_Unknown | 361–689 | 316 | 8 | Undefined position; Undefined team |
| `59` | `91` | Position_Unknown | Team_Unknown | 362–689 | 263 | 16 | Undefined position; Undefined team |
| `60` | `94` | Position_Unknown | Team_Unknown | 371–373 | 3 | 1 | Undefined position; Undefined team |
| `61` | `95` | Position_Unknown | Team_Unknown | 372–377 | 6 | 1 | Undefined position; Undefined team |
| `62` | `96` | Position_Unknown | Team_Unknown | 373–689 | 279 | 12 | Undefined position; Undefined team |
| `63` | `97` | Position_Unknown | Team_Unknown | 375–406 | 8 | 2 | Undefined position; Undefined team |
| `64` | `98` | Position_Unknown | Team_Unknown | 377–378 | 2 | 1 | Undefined position; Undefined team |
| `65` | `99` | Position_Unknown | Team_Unknown | 383–689 | 273 | 9 | Undefined position; Undefined team |
| `66` | `101` | Position_Unknown | Team_Unknown | 401–436 | 16 | 3 | Undefined position; Undefined team |
| `67` | `102` | Position_Unknown | Team_Unknown | 401–527 | 49 | 8 | Undefined position; Undefined team |
| `68` | `105` | Position_Unknown | Team_Unknown | 406–535 | 127 | 2 | Undefined position; Undefined team |
| `69` | `106` | Position_Unknown | Team_Unknown | 409–448 | 27 | 3 | Undefined position; Undefined team |
| `70` | `108` | Position_Unknown | Team_Unknown | 413–689 | 264 | 7 | Undefined position; Undefined team |
| `71` | `110` | Position_Unknown | Team_Unknown | 430–432 | 3 | 1 | Undefined position; Undefined team |
| `72` | `111` | Position_Unknown | Team_Unknown | 431–439 | 8 | 2 | Undefined position; Undefined team |
| `73` | `114` | Position_Unknown | Team_Unknown | 435–689 | 221 | 11 | Undefined position; Undefined team |
| `74` | `115` | Position_Unknown | Team_Unknown | 437–569 | 121 | 5 | Undefined position; Undefined team |
| `75` | `117` | Position_Unknown | Team_Unknown | 438–441 | 4 | 1 | Undefined position; Undefined team |
| `76` | `118` | Position_Unknown | Team_Unknown | 438–442 | 5 | 1 | Undefined position; Undefined team |
| `77` | `120` | Position_Unknown | Team_Unknown | 443–668 | 213 | 6 | Undefined position; Undefined team |
| `78` | `122` | Position_Unknown | Team_Unknown | 451–689 | 204 | 10 | Undefined position; Undefined team |
| `79` | `123` | Position_Unknown | Team_Unknown | 451–689 | 219 | 3 | Undefined position; Undefined team |
| `80` | `124` | Position_Unknown | Team_Unknown | 452–689 | 236 | 2 | Undefined position; Undefined team |
| `81` | `126` | Position_Unknown | Team_Unknown | 455–689 | 230 | 4 | Undefined position; Undefined team |
| `82` | `128` | Position_Unknown | Team_Unknown | 455–688 | 216 | 4 | Undefined position; Undefined team |
| `83` | `129` | Position_Unknown | Team_Unknown | 457–459 | 3 | 1 | Undefined position; Undefined team |
| `84` | `130` | Position_Unknown | Team_Unknown | 457–689 | 208 | 4 | Undefined position; Undefined team |
| `85` | `134` | Position_Unknown | Team_Unknown | 480–490 | 8 | 2 | Undefined position; Undefined team |
| `86` | `135` | Position_Unknown | Team_Unknown | 483–503 | 5 | 2 | Undefined position; Undefined team |
| `87` | `136` | Position_Unknown | Team_Unknown | 483–486 | 4 | 1 | Undefined position; Undefined team |
| `88` | `141` | Position_Unknown | Team_Unknown | 494–689 | 189 | 4 | Undefined position; Undefined team |
| `89` | `142` | Position_Unknown | Team_Unknown | 523–645 | 59 | 8 | Undefined position; Undefined team |
| `90` | `143` | Position_Unknown | Team_Unknown | 523–524 | 2 | 1 | Undefined position; Undefined team |
| `91` | `144` | Position_Unknown | Team_Unknown | 547–555 | 7 | 3 | Undefined position; Undefined team |
| `92` | `147` | Position_Unknown | Team_Unknown | 581–689 | 99 | 5 | Undefined position; Undefined team |
| `93` | `148` | Position_Unknown | Team_Unknown | 583–596 | 14 | 1 | Undefined position; Undefined team |
| `94` | `149` | Position_Unknown | Team_Unknown | 597–640 | 34 | 3 | Undefined position; Undefined team |
| `95` | `150` | Position_Unknown | Team_Unknown | 602–689 | 50 | 9 | Undefined position; Undefined team |
| `96` | `152` | Position_Unknown | Team_Unknown | 619–621 | 3 | 1 | Undefined position; Undefined team |
| `97` | `155` | Position_Unknown | Team_Unknown | 685–689 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CatchPunt` on target `51` (Position_Unknown)
- ❌ Missing segment for action `Action_BallCarry` on target `51` (Position_Unknown)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `51` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Jammer3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Wing` position mapped to `offense` team
- ⚠️ 80 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 80 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 160 |
| Missing visible bounding boxes during action | 360 |
| Track-related warning | 3 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_CatchPunt' for track '34' has invalid range: start=237, end=236. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '34' has invalid range: start=268, end=236. Clamping end to start.
- ⚠️ Segment 'Action_CrossGoalLine' for track '34' has invalid range: start=680, end=236. Clamping end to start.
- ⚠️ Action 'Action_None' range [64-221] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-247] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-271] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-128] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-109] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-116] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-135] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-134] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-182] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-196] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-213] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-251] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-135] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-127] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-250] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-128] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-214] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-236] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-257] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-268] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-235] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-318] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-387] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-400] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-417] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-430] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-151] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-175] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-337] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-343] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-375] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-427] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-465] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-475] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-486] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-689] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-147] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-200] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-261] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-217] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-372] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-312] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-182] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-272] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-302] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-311] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-427] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-441] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-512] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-192] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-214] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-269] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-279] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-392] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-453] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-149] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-159] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-74] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-72] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-215] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-141] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-201] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-126] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-198] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-329] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-299] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-304] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-323] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-209] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-312] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-423] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-498] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-503] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-521] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-530] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-539] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-548] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-573] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-587] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-596] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-213] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-270] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-366] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-221] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-319] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-354] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-316] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-213] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-228] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-256] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-297] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-330] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-336] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-341] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-272] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-366] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-444] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-632] for track '43' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-637] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-665] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [669-675] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [683-689] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-372] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-293] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-344] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-367] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-331] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-348] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-421] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-432] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-503] for track '54' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-513] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-521] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-526] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-530] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-538] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-548] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-562] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-576] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-606] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-689] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-336] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-339] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-360] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-400] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-414] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-418] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-689] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-366] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-384] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-397] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-431] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-458] for track '59' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-462] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-491] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-497] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-502] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-517] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-527] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-539] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-548] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-556] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-624] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-373] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-377] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-410] for track '62' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-428] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-448] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-462] for track '62' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-550] for track '62' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-599] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-668] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [670-671] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [680-689] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-406] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-399] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-403] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-430] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-436] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-557] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-563] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-689] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-405] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-412] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-436] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-414] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-423] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-432] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-442] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-501] for track '67' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-417] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-535] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-417] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-423] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-448] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-417] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-439] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-502] for track '70' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-567] for track '70' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-432] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-433] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-439] for track '72' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-439] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-463] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-475] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-497] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-508] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-513] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-517] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-522] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-541] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-689] for track '73' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-464] for track '74' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-519] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-537] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-545] for track '74' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-569] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-441] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-442] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-459] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-470] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-553] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-564] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-573] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-668] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-461] for track '78' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-503] for track '78' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-507] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-530] for track '78' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-539] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-548] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-556] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-618] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-666] for track '79' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [682-689] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-669] for track '80' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-543] for track '81' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-556] for track '81' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-562] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-522] for track '82' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-666] for track '82' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [669-672] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [685-688] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-459] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-545] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-553] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-580] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-484] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-490] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-484] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-503] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-486] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-504] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-539] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-556] for track '88' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-524] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-546] for track '89' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-553] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-587] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-610] for track '89' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-614] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [641-645] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-524] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-548] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-552] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-555] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-586] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-617] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-648] for track '92' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-663] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-596] for track '93' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-599] for track '94' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-629] for track '94' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-640] for track '94' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-624] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-632] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-639] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [642-645] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [655-657] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [662-663] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [667-668] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [674-675] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-621] for track '96' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>