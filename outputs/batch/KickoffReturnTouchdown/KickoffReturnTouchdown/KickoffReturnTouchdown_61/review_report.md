# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_61

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_61`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 68
- **Ball Tracks:** 0
- **Action Segments:** 306
- **Validation Warnings:** 376
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 291
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `7` | `7` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `7` | `7` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `27` | `25` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `27` | `25` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `27` | `25` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `11` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `12` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `14` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `15` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `16` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `2` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `5` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `6` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `7` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `8` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `9` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `7` | `7` | 15 | START | 15 | 107 |
| ✅ EXACT | `Action_KickBall` | Kicker | `7` | `7` | 108 | START | 108 | 113 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `27` | `25` | 227 | START | 227 | 234 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `27` | `25` | 248 | START | 248 | 317 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `27` | `25` | 600 | START | N/A | N/A |

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
- **Visible Frames:** 0–395
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_KickApproach` | 15 | 107 | 93 | inferred_complete_timeline |
| `Action_KickBall` | 108 | 113 | 6 | inferred_complete_timeline |
| `Action_None` | 114 | 169 | 56 | inferred_complete_timeline |
| `Action_None` | 171 | 384 | 214 | inferred_complete_timeline |
| `Action_None` | 394 | 395 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–377
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 326 | 312 | inferred_complete_timeline |
| `Action_None` | 331 | 351 | 21 | inferred_complete_timeline |
| `Action_None` | 360 | 367 | 8 | inferred_complete_timeline |
| `Action_None` | 369 | 377 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 258 | 244 | inferred_complete_timeline |
| `Action_None` | 268 | 277 | 10 | inferred_complete_timeline |
| `Action_None` | 282 | 291 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 254 | 240 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 266 | 7 | inferred_complete_timeline |
| `Action_None` | 324 | 325 | 2 | inferred_complete_timeline |
| `Action_None` | 327 | 599 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 260 | 246 | inferred_complete_timeline |
| `Action_None` | 262 | 273 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 195 | 181 | inferred_complete_timeline |
| `Action_None` | 197 | 203 | 7 | inferred_complete_timeline |
| `Action_None` | 205 | 218 | 14 | inferred_complete_timeline |
| `Action_None` | 222 | 227 | 6 | inferred_complete_timeline |
| `Action_None` | 239 | 242 | 4 | inferred_complete_timeline |
| `Action_None` | 245 | 255 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 166 | 152 | inferred_complete_timeline |
| `Action_None` | 171 | 178 | 8 | inferred_complete_timeline |
| `Action_None` | 187 | 190 | 4 | inferred_complete_timeline |
| `Action_None` | 194 | 232 | 39 | inferred_complete_timeline |
| `Action_None` | 234 | 237 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 163 | 149 | inferred_complete_timeline |
| `Action_None` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 175 | 4 | inferred_complete_timeline |
| `Action_None` | 188 | 192 | 5 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_None` | 206 | 273 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–295
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 229 | 215 | inferred_complete_timeline |
| `Action_None` | 233 | 281 | 49 | inferred_complete_timeline |
| `Action_None` | 284 | 292 | 9 | inferred_complete_timeline |
| `Action_None` | 294 | 295 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–303
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 195 | 181 | inferred_complete_timeline |
| `Action_None` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 219 | 303 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–524
- **Visible Samples:** 488

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 19 | 5 | inferred_complete_timeline |
| `Action_None` | 22 | 50 | 29 | inferred_complete_timeline |
| `Action_None` | 52 | 125 | 74 | inferred_complete_timeline |
| `Action_None` | 127 | 147 | 21 | inferred_complete_timeline |
| `Action_None` | 150 | 189 | 40 | inferred_complete_timeline |
| `Action_None` | 195 | 385 | 191 | inferred_complete_timeline |
| `Action_None` | 387 | 394 | 8 | inferred_complete_timeline |
| `Action_None` | 396 | 401 | 6 | inferred_complete_timeline |
| `Action_None` | 404 | 407 | 4 | inferred_complete_timeline |
| `Action_None` | 410 | 416 | 7 | inferred_complete_timeline |
| `Action_None` | 418 | 421 | 4 | inferred_complete_timeline |
| `Action_None` | 424 | 429 | 6 | inferred_complete_timeline |
| `Action_None` | 435 | 436 | 2 | inferred_complete_timeline |
| `Action_None` | 440 | 450 | 11 | inferred_complete_timeline |
| `Action_None` | 454 | 488 | 35 | inferred_complete_timeline |
| `Action_None` | 490 | 506 | 17 | inferred_complete_timeline |
| `Action_None` | 511 | 517 | 7 | inferred_complete_timeline |
| `Action_None` | 519 | 524 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 267 | 253 | inferred_complete_timeline |
| `Action_None` | 269 | 280 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 256 | 242 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |
| `Action_None` | 338 | 599 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 140 | 126 | inferred_complete_timeline |
| `Action_None` | 143 | 241 | 99 | inferred_complete_timeline |
| `Action_None` | 247 | 389 | 143 | inferred_complete_timeline |
| `Action_None` | 391 | 516 | 126 | inferred_complete_timeline |
| `Action_None` | 518 | 548 | 31 | inferred_complete_timeline |
| `Action_None` | 551 | 561 | 11 | inferred_complete_timeline |
| `Action_None` | 572 | 576 | 5 | inferred_complete_timeline |
| `Action_None` | 581 | 582 | 2 | inferred_complete_timeline |
| `Action_None` | 589 | 592 | 4 | inferred_complete_timeline |
| `Action_None` | 597 | 599 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 581

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 559 | 545 | inferred_complete_timeline |
| `Action_None` | 573 | 576 | 4 | inferred_complete_timeline |
| `Action_None` | 578 | 584 | 7 | inferred_complete_timeline |
| `Action_None` | 588 | 593 | 6 | inferred_complete_timeline |
| `Action_None` | 596 | 599 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 257 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 255 | 241 | inferred_complete_timeline |
| `Action_None` | 263 | 270 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 118–599 | 423 | 8 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 137–142 | 4 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 138–599 | 322 | 12 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 140–198 | 49 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 142–197 | 56 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 154–190 | 33 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 156–325 | 152 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 170–261 | 89 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 188–599 | 396 | 11 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 206–218 | 11 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 207–306 | 93 | 4 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 210–325 | 100 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 212–217 | 6 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 238–246 | 7 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 249–250 | 2 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 255–257 | 3 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 282–283 | 2 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 288–290 | 3 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 308–587 | 228 | 16 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 313–599 | 244 | 10 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 314–599 | 247 | 6 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 325–524 | 180 | 8 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 325–547 | 213 | 4 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 332–599 | 260 | 6 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 333–599 | 260 | 2 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 334–599 | 252 | 8 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 335–599 | 264 | 2 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 337–390 | 53 | 2 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 338–599 | 262 | 1 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 340–599 | 239 | 7 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 392–599 | 200 | 5 | Undefined position; Undefined team |
| `48` | `70` | Position_Unknown | Team_Unknown | 397–400 | 4 | 1 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 400–511 | 96 | 9 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 404–405 | 2 | 1 | Undefined position; Undefined team |
| `51` | `73` | Position_Unknown | Team_Unknown | 408–454 | 13 | 4 | Undefined position; Undefined team |
| `52` | `77` | Position_Unknown | Team_Unknown | 412–599 | 180 | 5 | Undefined position; Undefined team |
| `53` | `78` | Position_Unknown | Team_Unknown | 412–599 | 167 | 7 | Undefined position; Undefined team |
| `54` | `82` | Position_Unknown | Team_Unknown | 441–599 | 158 | 2 | Undefined position; Undefined team |
| `55` | `83` | Position_Unknown | Team_Unknown | 441–445 | 5 | 1 | Undefined position; Undefined team |
| `56` | `85` | Position_Unknown | Team_Unknown | 451–599 | 107 | 6 | Undefined position; Undefined team |
| `57` | `86` | Position_Unknown | Team_Unknown | 474–512 | 25 | 4 | Undefined position; Undefined team |
| `58` | `90` | Position_Unknown | Team_Unknown | 520–523 | 4 | 1 | Undefined position; Undefined team |
| `59` | `92` | Position_Unknown | Team_Unknown | 525–587 | 54 | 7 | Undefined position; Undefined team |
| `60` | `93` | Position_Unknown | Team_Unknown | 532–536 | 4 | 2 | Undefined position; Undefined team |
| `61` | `94` | Position_Unknown | Team_Unknown | 537–598 | 59 | 3 | Undefined position; Undefined team |
| `62` | `95` | Position_Unknown | Team_Unknown | 538–539 | 2 | 1 | Undefined position; Undefined team |
| `63` | `96` | Position_Unknown | Team_Unknown | 540–563 | 13 | 3 | Undefined position; Undefined team |
| `64` | `102` | Position_Unknown | Team_Unknown | 598–599 | 2 | 1 | Undefined position; Undefined team |
| `65` | `103` | Position_Unknown | Team_Unknown | 599–599 | 1 | 1 | Undefined position; Undefined team |
| `66` | `104` | Position_Unknown | Team_Unknown | 599–599 | 1 | 1 | Undefined position; Undefined team |
| `67` | `105` | Position_Unknown | Team_Unknown | 599–599 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `27` (8 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `27` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ 51 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 51 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 102 |
| Missing visible bounding boxes during action | 271 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '25' has invalid range: start=600, end=599. Clamping end to start.
- ⚠️ Action 'Action_None' range [15-267] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-280] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-256] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-599] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-195] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-203] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-218] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-255] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-140] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-241] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-389] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-516] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-548] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-561] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-576] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-582] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-592] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-257] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-260] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-273] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-166] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-178] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-232] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-169] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-384] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-254] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-266] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-258] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-277] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-291] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-255] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-270] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-229] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-281] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-292] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-326] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-351] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-367] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-377] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-559] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-576] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-584] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-593] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-273] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-19] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-125] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-147] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-189] for track '15' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-385] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-394] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-401] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-407] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-416] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-421] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-429] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-450] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-488] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-506] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-517] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-524] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-195] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-303] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-153] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-253] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-448] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-599] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-203] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-228] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-286] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-380] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-444] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-508] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-512] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-599] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-165] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-179] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-198] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-197] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-160] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-185] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-199] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-221] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-308] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-178] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-257] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [248-317] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [323-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [334-354] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [356-571] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [573-585] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [588-589] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [591-592] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-260] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-296] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-306] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-295] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-325] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-217] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-359] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-392] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-437] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-464] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-470] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-486] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-492] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-506] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-526] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-535] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-539] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-549] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-566] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-583] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-587] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-351] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-384] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-490] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-496] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-541] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-552] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-576] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-586] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-593] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-599] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-518] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-525] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-548] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-582] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-589] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-353] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-388] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-429] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-502] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-524] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-533] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-541] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-547] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-536] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-545] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-562] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-567] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-599] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-353] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-497] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-502] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-559] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-564] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-571] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-580] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-599] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-387] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-358] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-390] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-599] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-506] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-548] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-561] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-567] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-576] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-593] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-421] for track '47' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-481] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-511] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-515] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-599] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-400] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-405] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-410] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-440] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-468] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-484] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-487] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-504] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-511] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-410] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-418] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-431] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-483] for track '52' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-490] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-504] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-599] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-451] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-456] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-470] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-493] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-580] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-545] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-599] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-445] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-454] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-483] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-526] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-529] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-599] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-481] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-484] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-500] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-512] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-523] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-539] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-547] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-552] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-557] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-561] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-569] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-587] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-540] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-553] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-598] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-547] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-553] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-563] for track '63' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 600. Video range is [0, 599].

</details>