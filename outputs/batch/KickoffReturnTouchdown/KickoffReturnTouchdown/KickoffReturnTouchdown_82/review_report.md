# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_82

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_82`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 302
- **Validation Warnings:** 327
- **Validation Errors:** 0
- **Overall Status:** WARNING

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
- **Inferred Coverage Segments (Action_None):** 281
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `38` | `28` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `38` | `28` |
| ✅ EXACT | `Action_CrossGoalLine` | Right_Coverage3 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `0` | `Group` | 0 | START | 0 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `10` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `11` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `12` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `15` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `16` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `2` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `6` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `8` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `9` | `Group` | 0 | START | 0 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `15` | `15` | 19 | START | 24 | 26 |
| ✅ EXACT | `Action_KickBall` | Kicker | `15` | `15` | 101 | START | 101 | 105 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `38` | `28` | 212 | START | 212 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `38` | `28` | 239 | START | 239 | 537 |
| ✅ EXACT | `Action_CrossGoalLine` | Right_Coverage3 | `0` | `0` | 610 | START | 610 | 629 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 459

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_KickApproach` | 24 | 26 | 3 | inferred_complete_timeline |
| `Action_KickApproach` | 34 | 100 | 67 | inferred_complete_timeline |
| `Action_KickBall` | 101 | 105 | 5 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 168 | 59 | inferred_complete_timeline |
| `Action_None` | 171 | 173 | 3 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 237 | 4 | inferred_complete_timeline |
| `Action_None` | 254 | 316 | 63 | inferred_complete_timeline |
| `Action_None` | 326 | 457 | 132 | inferred_complete_timeline |
| `Action_None` | 465 | 467 | 3 | inferred_complete_timeline |
| `Action_None` | 471 | 504 | 34 | inferred_complete_timeline |
| `Action_None` | 509 | 521 | 13 | inferred_complete_timeline |
| `Action_None` | 524 | 530 | 7 | inferred_complete_timeline |
| `Action_None` | 565 | 566 | 2 | inferred_complete_timeline |
| `Action_None` | 573 | 585 | 13 | inferred_complete_timeline |
| `Action_None` | 591 | 608 | 18 | inferred_complete_timeline |
| `Action_None` | 611 | 629 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 30 | 12 | inferred_complete_timeline |
| `Action_None` | 32 | 49 | 18 | inferred_complete_timeline |
| `Action_None` | 75 | 82 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–621
- **Visible Samples:** 550

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 136 | 118 | inferred_complete_timeline |
| `Action_None` | 138 | 152 | 15 | inferred_complete_timeline |
| `Action_None` | 154 | 167 | 14 | inferred_complete_timeline |
| `Action_None` | 170 | 183 | 14 | inferred_complete_timeline |
| `Action_None` | 185 | 201 | 17 | inferred_complete_timeline |
| `Action_None` | 203 | 215 | 13 | inferred_complete_timeline |
| `Action_None` | 218 | 271 | 54 | inferred_complete_timeline |
| `Action_None` | 276 | 279 | 4 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_None` | 293 | 423 | 131 | inferred_complete_timeline |
| `Action_None` | 427 | 449 | 23 | inferred_complete_timeline |
| `Action_None` | 451 | 456 | 6 | inferred_complete_timeline |
| `Action_None` | 459 | 522 | 64 | inferred_complete_timeline |
| `Action_None` | 527 | 529 | 3 | inferred_complete_timeline |
| `Action_None` | 536 | 537 | 2 | inferred_complete_timeline |
| `Action_None` | 539 | 550 | 12 | inferred_complete_timeline |
| `Action_None` | 556 | 557 | 2 | inferred_complete_timeline |
| `Action_None` | 559 | 560 | 2 | inferred_complete_timeline |
| `Action_None` | 573 | 576 | 4 | inferred_complete_timeline |
| `Action_None` | 579 | 582 | 4 | inferred_complete_timeline |
| `Action_None` | 585 | 601 | 17 | inferred_complete_timeline |
| `Action_None` | 604 | 608 | 5 | inferred_complete_timeline |
| `Action_None` | 611 | 612 | 2 | inferred_complete_timeline |
| `Action_None` | 619 | 621 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 588

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 171 | 153 | inferred_complete_timeline |
| `Action_None` | 173 | 200 | 28 | inferred_complete_timeline |
| `Action_None` | 203 | 217 | 15 | inferred_complete_timeline |
| `Action_None` | 219 | 246 | 28 | inferred_complete_timeline |
| `Action_None` | 250 | 335 | 86 | inferred_complete_timeline |
| `Action_None` | 344 | 402 | 59 | inferred_complete_timeline |
| `Action_None` | 405 | 409 | 5 | inferred_complete_timeline |
| `Action_None` | 411 | 415 | 5 | inferred_complete_timeline |
| `Action_None` | 417 | 422 | 6 | inferred_complete_timeline |
| `Action_None` | 424 | 521 | 98 | inferred_complete_timeline |
| `Action_None` | 529 | 539 | 11 | inferred_complete_timeline |
| `Action_None` | 543 | 544 | 2 | inferred_complete_timeline |
| `Action_None` | 546 | 559 | 14 | inferred_complete_timeline |
| `Action_None` | 562 | 619 | 58 | inferred_complete_timeline |
| `Action_None` | 629 | 629 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 76 | 58 | inferred_complete_timeline |
| `Action_None` | 78 | 151 | 74 | inferred_complete_timeline |
| `Action_None` | 153 | 166 | 14 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 177 | 182 | 6 | inferred_complete_timeline |
| `Action_None` | 184 | 190 | 7 | inferred_complete_timeline |
| `Action_None` | 193 | 197 | 5 | inferred_complete_timeline |
| `Action_None` | 200 | 242 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 146 | 128 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 158 | 5 | inferred_complete_timeline |
| `Action_None` | 169 | 175 | 7 | inferred_complete_timeline |
| `Action_None` | 181 | 194 | 14 | inferred_complete_timeline |
| `Action_None` | 197 | 208 | 12 | inferred_complete_timeline |
| `Action_None` | 210 | 215 | 6 | inferred_complete_timeline |
| `Action_None` | 218 | 223 | 6 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_None` | 251 | 256 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 146 | 128 | inferred_complete_timeline |
| `Action_None` | 149 | 162 | 14 | inferred_complete_timeline |
| `Action_None` | 165 | 171 | 7 | inferred_complete_timeline |
| `Action_None` | 175 | 178 | 4 | inferred_complete_timeline |
| `Action_None` | 181 | 185 | 5 | inferred_complete_timeline |
| `Action_None` | 188 | 199 | 12 | inferred_complete_timeline |
| `Action_None` | 201 | 206 | 6 | inferred_complete_timeline |
| `Action_None` | 211 | 214 | 4 | inferred_complete_timeline |
| `Action_None` | 218 | 220 | 3 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_None` | 236 | 238 | 3 | inferred_complete_timeline |
| `Action_None` | 243 | 245 | 3 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 251 | 330 | 80 | inferred_complete_timeline |
| `Action_None` | 334 | 335 | 2 | inferred_complete_timeline |
| `Action_None` | 337 | 414 | 78 | inferred_complete_timeline |
| `Action_None` | 416 | 453 | 38 | inferred_complete_timeline |
| `Action_None` | 456 | 458 | 3 | inferred_complete_timeline |
| `Action_None` | 464 | 477 | 14 | inferred_complete_timeline |
| `Action_None` | 485 | 486 | 2 | inferred_complete_timeline |
| `Action_None` | 488 | 499 | 12 | inferred_complete_timeline |
| `Action_None` | 502 | 629 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 579

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 206 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 211 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 255 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 302 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 609 | 306 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 610 | 629 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 91 | 73 | inferred_complete_timeline |
| `Action_None` | 95 | 193 | 99 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 207 | 6 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |
| `Action_None` | 232 | 233 | 2 | inferred_complete_timeline |
| `Action_None` | 245 | 253 | 9 | inferred_complete_timeline |
| `Action_None` | 255 | 257 | 3 | inferred_complete_timeline |
| `Action_None` | 259 | 277 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 610

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 402 | 384 | inferred_complete_timeline |
| `Action_None` | 404 | 591 | 188 | inferred_complete_timeline |
| `Action_None` | 599 | 600 | 2 | inferred_complete_timeline |
| `Action_None` | 608 | 609 | 2 | inferred_complete_timeline |
| `Action_None` | 612 | 615 | 4 | inferred_complete_timeline |
| `Action_None` | 617 | 618 | 2 | inferred_complete_timeline |
| `Action_None` | 621 | 629 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–556
- **Visible Samples:** 514

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 168 | 150 | inferred_complete_timeline |
| `Action_None` | 171 | 243 | 73 | inferred_complete_timeline |
| `Action_None` | 246 | 252 | 7 | inferred_complete_timeline |
| `Action_None` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 361 | 96 | inferred_complete_timeline |
| `Action_None` | 365 | 367 | 3 | inferred_complete_timeline |
| `Action_None` | 371 | 412 | 42 | inferred_complete_timeline |
| `Action_None` | 418 | 429 | 12 | inferred_complete_timeline |
| `Action_None` | 434 | 458 | 25 | inferred_complete_timeline |
| `Action_None` | 460 | 535 | 76 | inferred_complete_timeline |
| `Action_None` | 538 | 542 | 5 | inferred_complete_timeline |
| `Action_None` | 547 | 548 | 2 | inferred_complete_timeline |
| `Action_None` | 555 | 556 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 629 | 611 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 593 | 575 | inferred_complete_timeline |
| `Action_None` | 597 | 629 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 624

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 347 | 329 | inferred_complete_timeline |
| `Action_None` | 349 | 384 | 36 | inferred_complete_timeline |
| `Action_None` | 390 | 629 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–573
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 312 | 294 | inferred_complete_timeline |
| `Action_None` | 314 | 385 | 72 | inferred_complete_timeline |
| `Action_None` | 387 | 510 | 124 | inferred_complete_timeline |
| `Action_None` | 513 | 517 | 5 | inferred_complete_timeline |
| `Action_None` | 521 | 533 | 13 | inferred_complete_timeline |
| `Action_None` | 536 | 573 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 626

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 557 | 539 | inferred_complete_timeline |
| `Action_None` | 562 | 629 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–111 | 112 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 86–303 | 218 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 99–140 | 32 | 5 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 116–629 | 514 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 138–629 | 469 | 6 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 139–629 | 466 | 10 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 158–247 | 55 | 7 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 160–629 | 448 | 6 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 161–164 | 4 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 162–165 | 4 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 168–378 | 204 | 4 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 179–629 | 440 | 6 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 270–277 | 6 | 2 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 273–629 | 356 | 2 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 294–538 | 239 | 6 | Undefined position; Undefined team |
| `32` | `51` | Position_Unknown | Team_Unknown | 316–629 | 313 | 2 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 316–629 | 245 | 9 | Undefined position; Undefined team |
| `34` | `55` | Position_Unknown | Team_Unknown | 368–568 | 195 | 3 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 382–629 | 224 | 14 | Undefined position; Undefined team |
| `36` | `60` | Position_Unknown | Team_Unknown | 411–569 | 126 | 13 | Undefined position; Undefined team |
| `37` | `61` | Position_Unknown | Team_Unknown | 413–606 | 135 | 18 | Undefined position; Undefined team |
| `38` | `63` | Position_Unknown | Team_Unknown | 419–421 | 3 | 1 | Undefined position; Undefined team |
| `39` | `67` | Position_Unknown | Team_Unknown | 432–508 | 64 | 4 | Undefined position; Undefined team |
| `40` | `75` | Position_Unknown | Team_Unknown | 554–556 | 3 | 1 | Undefined position; Undefined team |
| `41` | `76` | Position_Unknown | Team_Unknown | 561–629 | 56 | 5 | Undefined position; Undefined team |
| `42` | `77` | Position_Unknown | Team_Unknown | 607–624 | 18 | 1 | Undefined position; Undefined team |
| `43` | `79` | Position_Unknown | Team_Unknown | 613–629 | 14 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `38` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 269 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 165: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-198] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-206] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-211] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-218] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-255] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-302] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-312] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-385] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-510] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-517] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-533] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-573] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-402] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-591] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-600] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-609] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-615] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-618] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-629] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-347] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-384] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-168] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-243] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-252] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-361] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-367] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-412] for track '4' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-429] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-458] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-535] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-542] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-548] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-556] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-111] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-76] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-166] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-182] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-190] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-242] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-593] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-146] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-162] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-199] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-330] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-414] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-453] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-458] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-477] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-499] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-629] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-136] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-167] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-183] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-201] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-215] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-271] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-423] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-449] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-456] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-522] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-529] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-550] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-557] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-560] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-576] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-582] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-601] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-608] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-612] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-621] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-91] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-193] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-253] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-277] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-171] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-200] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-217] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-246] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-335] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-402] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-409] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-415] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-422] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-521] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-539] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-544] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-559] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-619] for track '11' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-146] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-175] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-194] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-208] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-223] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-256] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-557] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [24-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [34-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-168] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-316] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-457] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-467] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-504] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-521] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-530] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-566] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-585] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-608] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-629] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-49] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-82] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-303] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-105] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-119] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-135] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-629] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-518] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-590] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-604] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-617] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-620] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-183] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-200] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-499] for track '21' has 9 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-538] for track '21' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-582] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-621] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-208] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-220] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-304] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-372] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-485] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-502] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-623] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-327] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-367] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-373] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-211] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '28' starts at frame 222, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [222-222] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-238] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [239-537] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-334] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-387] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-394] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-399] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-407] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-413] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-538] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-476] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-489] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-508] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-523] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-533] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-573] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-583] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-620] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-510] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-561] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-568] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-391] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-399] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-405] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-420] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-426] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-437] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-442] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-583] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-592] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-601] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-610] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-614] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-427] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-433] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-446] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-467] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-479] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-511] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-537] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-544] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-547] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-553] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-561] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-569] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-417] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-426] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-433] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-446] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-451] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-466] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-477] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-481] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-505] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-512] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-523] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-568] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-571] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-590] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-594] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-600] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-606] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-421] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-437] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-451] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-501] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-508] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-556] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-569] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-585] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-599] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-615] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-624] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-618] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>