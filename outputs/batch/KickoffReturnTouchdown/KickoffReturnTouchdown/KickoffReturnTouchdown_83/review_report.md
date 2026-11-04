# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_83

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_83`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 326
- **Validation Warnings:** 347
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 307
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | offense | `1` | `1` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | defense | `20` | `20` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `0` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `1` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `10` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `11` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `15` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `18` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `2` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `3` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `4` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `8` | `Group` | 0 | START | 0 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `1` | `1` | 73 | START | 73 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | `1` | `1` | 146 | START | 146 | 149 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `20` | `20` | 258 | START | 258 | 267 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | `20` | `20` | 280 | START | 280 | 357 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | `20` | `20` | 652 | START | 652 | 659 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–638
- **Visible Samples:** 612

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 72 | 1 | inferred_complete_timeline |
| `Action_KickApproach` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_KickApproach` | 76 | 119 | 44 | inferred_complete_timeline |
| `Action_KickApproach` | 121 | 145 | 25 | inferred_complete_timeline |
| `Action_KickBall` | 146 | 149 | 4 | inferred_complete_timeline |
| `Action_KickBall` | 151 | 151 | 1 | inferred_complete_timeline |
| `Action_None` | 152 | 165 | 14 | inferred_complete_timeline |
| `Action_None` | 167 | 182 | 16 | inferred_complete_timeline |
| `Action_None` | 184 | 521 | 338 | inferred_complete_timeline |
| `Action_None` | 523 | 525 | 3 | inferred_complete_timeline |
| `Action_None` | 527 | 544 | 18 | inferred_complete_timeline |
| `Action_None` | 547 | 580 | 34 | inferred_complete_timeline |
| `Action_None` | 585 | 597 | 13 | inferred_complete_timeline |
| `Action_None` | 599 | 614 | 16 | inferred_complete_timeline |
| `Action_None` | 626 | 638 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–377
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 146 | 74 | inferred_complete_timeline |
| `Action_None` | 149 | 171 | 23 | inferred_complete_timeline |
| `Action_None` | 173 | 176 | 4 | inferred_complete_timeline |
| `Action_None` | 179 | 184 | 6 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 204 | 6 | inferred_complete_timeline |
| `Action_None` | 206 | 256 | 51 | inferred_complete_timeline |
| `Action_None` | 264 | 268 | 5 | inferred_complete_timeline |
| `Action_None` | 272 | 273 | 2 | inferred_complete_timeline |
| `Action_None` | 280 | 286 | 7 | inferred_complete_timeline |
| `Action_None` | 289 | 292 | 4 | inferred_complete_timeline |
| `Action_None` | 299 | 301 | 3 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_None` | 321 | 322 | 2 | inferred_complete_timeline |
| `Action_None` | 324 | 372 | 49 | inferred_complete_timeline |
| `Action_None` | 374 | 377 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–372
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 136 | 64 | inferred_complete_timeline |
| `Action_None` | 140 | 300 | 161 | inferred_complete_timeline |
| `Action_None` | 303 | 306 | 4 | inferred_complete_timeline |
| `Action_None` | 310 | 359 | 50 | inferred_complete_timeline |
| `Action_None` | 365 | 372 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 580

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 180 | 108 | inferred_complete_timeline |
| `Action_None` | 185 | 212 | 28 | inferred_complete_timeline |
| `Action_None` | 215 | 247 | 33 | inferred_complete_timeline |
| `Action_None` | 249 | 254 | 6 | inferred_complete_timeline |
| `Action_None` | 257 | 271 | 15 | inferred_complete_timeline |
| `Action_None` | 331 | 375 | 45 | inferred_complete_timeline |
| `Action_None` | 380 | 384 | 5 | inferred_complete_timeline |
| `Action_None` | 387 | 390 | 4 | inferred_complete_timeline |
| `Action_None` | 395 | 396 | 2 | inferred_complete_timeline |
| `Action_None` | 398 | 638 | 241 | inferred_complete_timeline |
| `Action_None` | 640 | 659 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 27 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 60 | 27 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_None` | 95 | 166 | 72 | inferred_complete_timeline |
| `Action_None` | 168 | 189 | 22 | inferred_complete_timeline |
| `Action_None` | 191 | 196 | 6 | inferred_complete_timeline |
| `Action_None` | 199 | 212 | 14 | inferred_complete_timeline |
| `Action_None` | 218 | 239 | 22 | inferred_complete_timeline |
| `Action_None` | 244 | 256 | 13 | inferred_complete_timeline |
| `Action_None` | 260 | 271 | 12 | inferred_complete_timeline |
| `Action_None` | 274 | 277 | 4 | inferred_complete_timeline |
| `Action_None` | 281 | 293 | 13 | inferred_complete_timeline |
| `Action_None` | 310 | 351 | 42 | inferred_complete_timeline |
| `Action_None` | 359 | 365 | 7 | inferred_complete_timeline |
| `Action_None` | 367 | 408 | 42 | inferred_complete_timeline |
| `Action_None` | 410 | 452 | 43 | inferred_complete_timeline |
| `Action_None` | 454 | 475 | 22 | inferred_complete_timeline |
| `Action_None` | 477 | 484 | 8 | inferred_complete_timeline |
| `Action_None` | 490 | 659 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 170 | 98 | inferred_complete_timeline |
| `Action_None` | 176 | 182 | 7 | inferred_complete_timeline |
| `Action_None` | 188 | 198 | 11 | inferred_complete_timeline |
| `Action_None` | 203 | 213 | 11 | inferred_complete_timeline |
| `Action_None` | 219 | 222 | 4 | inferred_complete_timeline |
| `Action_None` | 237 | 238 | 2 | inferred_complete_timeline |
| `Action_None` | 241 | 253 | 13 | inferred_complete_timeline |
| `Action_None` | 258 | 271 | 14 | inferred_complete_timeline |
| `Action_None` | 274 | 276 | 3 | inferred_complete_timeline |
| `Action_None` | 278 | 281 | 4 | inferred_complete_timeline |
| `Action_None` | 297 | 307 | 11 | inferred_complete_timeline |
| `Action_None` | 312 | 320 | 9 | inferred_complete_timeline |
| `Action_None` | 325 | 332 | 8 | inferred_complete_timeline |
| `Action_None` | 339 | 352 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–315
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 184 | 112 | inferred_complete_timeline |
| `Action_None` | 197 | 200 | 4 | inferred_complete_timeline |
| `Action_None` | 202 | 205 | 4 | inferred_complete_timeline |
| `Action_None` | 207 | 260 | 54 | inferred_complete_timeline |
| `Action_None` | 263 | 296 | 34 | inferred_complete_timeline |
| `Action_None` | 298 | 315 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 602

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 180 | 108 | inferred_complete_timeline |
| `Action_None` | 186 | 197 | 12 | inferred_complete_timeline |
| `Action_None` | 199 | 208 | 10 | inferred_complete_timeline |
| `Action_None` | 219 | 223 | 5 | inferred_complete_timeline |
| `Action_None` | 229 | 234 | 6 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 373 | 117 | inferred_complete_timeline |
| `Action_None` | 379 | 462 | 84 | inferred_complete_timeline |
| `Action_None` | 464 | 527 | 64 | inferred_complete_timeline |
| `Action_None` | 533 | 534 | 2 | inferred_complete_timeline |
| `Action_None` | 540 | 648 | 109 | inferred_complete_timeline |
| `Action_None` | 650 | 659 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 608

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 266 | 194 | inferred_complete_timeline |
| `Action_None` | 268 | 286 | 19 | inferred_complete_timeline |
| `Action_None` | 291 | 297 | 7 | inferred_complete_timeline |
| `Action_None` | 299 | 315 | 17 | inferred_complete_timeline |
| `Action_None` | 320 | 368 | 49 | inferred_complete_timeline |
| `Action_None` | 370 | 382 | 13 | inferred_complete_timeline |
| `Action_None` | 384 | 445 | 62 | inferred_complete_timeline |
| `Action_None` | 447 | 476 | 30 | inferred_complete_timeline |
| `Action_None` | 478 | 479 | 2 | inferred_complete_timeline |
| `Action_None` | 484 | 485 | 2 | inferred_complete_timeline |
| `Action_None` | 490 | 593 | 104 | inferred_complete_timeline |
| `Action_None` | 603 | 610 | 8 | inferred_complete_timeline |
| `Action_None` | 612 | 617 | 6 | inferred_complete_timeline |
| `Action_None` | 630 | 638 | 9 | inferred_complete_timeline |
| `Action_None` | 640 | 645 | 6 | inferred_complete_timeline |
| `Action_None` | 653 | 659 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 632

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 334 | 262 | inferred_complete_timeline |
| `Action_None` | 340 | 341 | 2 | inferred_complete_timeline |
| `Action_None` | 347 | 363 | 17 | inferred_complete_timeline |
| `Action_None` | 365 | 373 | 9 | inferred_complete_timeline |
| `Action_None` | 379 | 527 | 149 | inferred_complete_timeline |
| `Action_None` | 535 | 552 | 18 | inferred_complete_timeline |
| `Action_None` | 554 | 557 | 4 | inferred_complete_timeline |
| `Action_None` | 562 | 659 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 249 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–323
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 323 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 649

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 231 | 159 | inferred_complete_timeline |
| `Action_None` | 237 | 273 | 37 | inferred_complete_timeline |
| `Action_None` | 280 | 659 | 380 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–345
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 283 | 211 | inferred_complete_timeline |
| `Action_None` | 291 | 293 | 3 | inferred_complete_timeline |
| `Action_None` | 295 | 303 | 9 | inferred_complete_timeline |
| `Action_None` | 305 | 307 | 3 | inferred_complete_timeline |
| `Action_None` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |
| `Action_None` | 342 | 345 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 548

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 375 | 303 | inferred_complete_timeline |
| `Action_None` | 381 | 444 | 64 | inferred_complete_timeline |
| `Action_None` | 458 | 547 | 90 | inferred_complete_timeline |
| `Action_None` | 550 | 558 | 9 | inferred_complete_timeline |
| `Action_None` | 560 | 568 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 547

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 18 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 44 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 61 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 77 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 166 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 186 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 257 | 70 | inferred_complete_timeline |
| `Action_CatchKick` | 258 | 267 | 10 | inferred_complete_timeline |
| `Action_None` | 268 | 279 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 280 | 357 | 78 | inferred_complete_timeline |
| `Action_BallCarry` | 363 | 433 | 71 | inferred_complete_timeline |
| `Action_BallCarry` | 436 | 651 | 216 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 652 | 659 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–311
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 72 | 27 | inferred_complete_timeline |
| `Action_None` | 73 | 90 | 18 | inferred_complete_timeline |
| `Action_None` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_None` | 107 | 111 | 5 | inferred_complete_timeline |
| `Action_None` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_None` | 122 | 138 | 17 | inferred_complete_timeline |
| `Action_None` | 141 | 227 | 87 | inferred_complete_timeline |
| `Action_None` | 242 | 311 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 618

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 288 | 216 | inferred_complete_timeline |
| `Action_None` | 298 | 308 | 11 | inferred_complete_timeline |
| `Action_None` | 317 | 359 | 43 | inferred_complete_timeline |
| `Action_None` | 367 | 372 | 6 | inferred_complete_timeline |
| `Action_None` | 374 | 467 | 94 | inferred_complete_timeline |
| `Action_None` | 474 | 476 | 3 | inferred_complete_timeline |
| `Action_None` | 480 | 482 | 3 | inferred_complete_timeline |
| `Action_None` | 484 | 525 | 42 | inferred_complete_timeline |
| `Action_None` | 531 | 533 | 3 | inferred_complete_timeline |
| `Action_None` | 536 | 659 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–573
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 310 | 238 | inferred_complete_timeline |
| `Action_None` | 312 | 380 | 69 | inferred_complete_timeline |
| `Action_None` | 389 | 391 | 3 | inferred_complete_timeline |
| `Action_None` | 394 | 395 | 2 | inferred_complete_timeline |
| `Action_None` | 397 | 399 | 3 | inferred_complete_timeline |
| `Action_None` | 404 | 453 | 50 | inferred_complete_timeline |
| `Action_None` | 461 | 475 | 15 | inferred_complete_timeline |
| `Action_None` | 483 | 496 | 14 | inferred_complete_timeline |
| `Action_None` | 506 | 561 | 56 | inferred_complete_timeline |
| `Action_None` | 564 | 573 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–343
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 343 | 271 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–440
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 289 | 217 | inferred_complete_timeline |
| `Action_None` | 292 | 297 | 6 | inferred_complete_timeline |
| `Action_None` | 307 | 373 | 67 | inferred_complete_timeline |
| `Action_None` | 379 | 390 | 12 | inferred_complete_timeline |
| `Action_None` | 393 | 440 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 42–659 | 525 | 29 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 162–184 | 12 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 262–659 | 346 | 15 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 284–337 | 54 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 321–659 | 277 | 6 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 347–378 | 32 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 368–659 | 278 | 4 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 388–441 | 54 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 389–612 | 180 | 10 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 391–659 | 239 | 8 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 399–659 | 257 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 403–603 | 194 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 408–633 | 201 | 5 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 468–659 | 192 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 499–659 | 136 | 7 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 507–508 | 2 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 540–542 | 3 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 549–603 | 23 | 5 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 576–577 | 2 | 1 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 582–600 | 7 | 3 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 592–659 | 64 | 3 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 592–593 | 2 | 1 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 604–614 | 9 | 2 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 609–617 | 9 | 1 | Undefined position; Undefined team |
| `45` | `57` | Position_Unknown | Team_Unknown | 629–630 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_KickBall` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 296 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action 'Action_None' range [73-266] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-286] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-297] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-315] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-368] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-382] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-445] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-476] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-485] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-593] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-610] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-617] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [630-638] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [640-645] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [653-659] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' for track '1' starts at frame 73, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_KickApproach' range [73-73] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [76-119] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [121-145] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [146-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-165] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-182] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-521] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-525] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-544] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-580] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-597] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-614] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-638] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-180] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-197] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-208] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-234] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-373] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-462] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-527] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-534] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-648] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-170] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-182] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-213] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-253] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-271] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-307] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-320] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-332] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-352] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-334] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-363] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-373] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-527] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-552] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-557] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-375] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-444] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-547] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-558] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-568] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-288] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-308] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-372] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-467] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-476] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-482] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-525] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-533] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-659] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-323] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-136] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-300] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-306] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-359] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-372] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-283] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-303] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-345] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-184] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-260] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-296] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-315] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-180] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-212] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-247] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-254] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-271] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-375] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-384] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-390] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-638] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-231] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-273] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-659] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-289] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-297] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-373] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-390] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-440] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-249] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-171] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-204] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-256] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-286] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-372] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-377] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-310] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-380] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-391] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-399] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-453] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-475] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-496] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-561] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-573] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-343] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-27] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-60] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-189] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-212] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-239] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-256] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-271] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-293] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-351] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-365] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-408] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-452] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-475] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-484] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-659] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-227] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-311] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-61] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-67] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-156] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-166] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-174] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-186] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-257] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [280-357] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [363-433] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [436-651] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-117] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-184] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-207] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-357] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-373] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-381] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-388] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-403] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-413] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-433] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-444] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-455] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-469] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-473] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-486] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-498] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-519] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-526] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-659] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-184] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-322] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-341] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-472] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-476] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-504] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-509] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-518] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-543] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-550] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-565] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-570] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-583] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-608] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-659] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-337] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-427] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-432] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-453] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-498] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-378] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-380] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-523] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-659] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-441] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-399] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-449] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-455] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-496] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-558] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-607] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-612] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-393] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-445] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-453] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-460] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-468] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-476] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-494] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-659] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-524] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-462] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-603] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-456] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-470] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-620] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-633] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-659] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-509] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-518] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-533] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-624] for track '35' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-629] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-648] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-508] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-542] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-555] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-572] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-584] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-588] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-603] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-577] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-583] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-593] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-600] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-623] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-631] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-593] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-610] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-614] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-617] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-630] for track '45' has 1 frames without a visible bounding box.
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

</details>