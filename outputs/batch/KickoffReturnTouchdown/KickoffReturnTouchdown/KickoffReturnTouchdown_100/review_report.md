# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_100

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_100`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 449
- **Player Tracks:** 99
- **Ball Tracks:** 0
- **Action Segments:** 267
- **Validation Warnings:** 379
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 253
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `36` | `30` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `36` | `30` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `11` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `12` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `13` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `14` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `2` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `3` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `5` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `6` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `8` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `9` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `5` | `5` | 13 | START | 13 | 71 |
| ✅ EXACT | `Action_KickBall` | Kicker | `5` | `5` | 72 | START | 72 | 76 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `36` | `30` | 184 | START | 184 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `36` | `30` | 198 | START | 198 | 266 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_KickApproach` | 13 | 71 | 59 | inferred_complete_timeline |
| `Action_KickBall` | 72 | 76 | 5 | inferred_complete_timeline |
| `Action_None` | 77 | 141 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 302 | 290 | inferred_complete_timeline |
| `Action_None` | 390 | 414 | 25 | inferred_complete_timeline |
| `Action_None` | 416 | 448 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 42 | 30 | inferred_complete_timeline |
| `Action_None` | 45 | 219 | 175 | inferred_complete_timeline |
| `Action_None` | 221 | 226 | 6 | inferred_complete_timeline |
| `Action_None` | 231 | 256 | 26 | inferred_complete_timeline |
| `Action_None` | 258 | 449 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–45
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 20 | 8 | inferred_complete_timeline |
| `Action_None` | 22 | 32 | 11 | inferred_complete_timeline |
| `Action_None` | 40 | 45 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 261 | 249 | inferred_complete_timeline |
| `Action_None` | 265 | 267 | 3 | inferred_complete_timeline |
| `Action_None` | 270 | 361 | 92 | inferred_complete_timeline |
| `Action_None` | 363 | 381 | 19 | inferred_complete_timeline |
| `Action_None` | 384 | 389 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 293 | 281 | inferred_complete_timeline |
| `Action_None` | 296 | 347 | 52 | inferred_complete_timeline |
| `Action_None` | 350 | 386 | 37 | inferred_complete_timeline |
| `Action_None` | 388 | 449 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 142 | 130 | inferred_complete_timeline |
| `Action_None` | 145 | 232 | 88 | inferred_complete_timeline |
| `Action_None` | 235 | 253 | 19 | inferred_complete_timeline |
| `Action_None` | 255 | 275 | 21 | inferred_complete_timeline |
| `Action_None` | 278 | 279 | 2 | inferred_complete_timeline |
| `Action_None` | 284 | 449 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 150 | 138 | inferred_complete_timeline |
| `Action_None` | 154 | 165 | 12 | inferred_complete_timeline |
| `Action_None` | 167 | 270 | 104 | inferred_complete_timeline |
| `Action_None` | 273 | 277 | 5 | inferred_complete_timeline |
| `Action_None` | 279 | 280 | 2 | inferred_complete_timeline |
| `Action_None` | 285 | 286 | 2 | inferred_complete_timeline |
| `Action_None` | 290 | 449 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 280 | 268 | inferred_complete_timeline |
| `Action_None` | 282 | 295 | 14 | inferred_complete_timeline |
| `Action_None` | 299 | 322 | 24 | inferred_complete_timeline |
| `Action_None` | 328 | 388 | 61 | inferred_complete_timeline |
| `Action_None` | 390 | 403 | 14 | inferred_complete_timeline |
| `Action_None` | 406 | 426 | 21 | inferred_complete_timeline |
| `Action_None` | 429 | 449 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 219 | 207 | inferred_complete_timeline |
| `Action_None` | 221 | 326 | 106 | inferred_complete_timeline |
| `Action_None` | 328 | 342 | 15 | inferred_complete_timeline |
| `Action_None` | 344 | 449 | 106 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 206 | 194 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 347 | 132 | inferred_complete_timeline |
| `Action_None` | 349 | 449 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 208 | 196 | inferred_complete_timeline |
| `Action_None` | 210 | 227 | 18 | inferred_complete_timeline |
| `Action_None` | 240 | 299 | 60 | inferred_complete_timeline |
| `Action_None` | 304 | 449 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–446
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 182 | 170 | inferred_complete_timeline |
| `Action_None` | 186 | 207 | 22 | inferred_complete_timeline |
| `Action_None` | 263 | 269 | 7 | inferred_complete_timeline |
| `Action_None` | 273 | 283 | 11 | inferred_complete_timeline |
| `Action_None` | 290 | 387 | 98 | inferred_complete_timeline |
| `Action_None` | 389 | 398 | 10 | inferred_complete_timeline |
| `Action_None` | 403 | 419 | 17 | inferred_complete_timeline |
| `Action_None` | 422 | 423 | 2 | inferred_complete_timeline |
| `Action_None` | 426 | 429 | 4 | inferred_complete_timeline |
| `Action_None` | 445 | 446 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 254 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 41 | 29 | inferred_complete_timeline |
| `Action_None` | 70 | 72 | 3 | inferred_complete_timeline |
| `Action_None` | 83 | 449 | 367 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 179 | 167 | inferred_complete_timeline |
| `Action_None` | 184 | 188 | 5 | inferred_complete_timeline |
| `Action_None` | 196 | 206 | 11 | inferred_complete_timeline |
| `Action_None` | 213 | 449 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 270 | 258 | inferred_complete_timeline |
| `Action_None` | 281 | 285 | 5 | inferred_complete_timeline |
| `Action_None` | 290 | 292 | 3 | inferred_complete_timeline |
| `Action_None` | 295 | 384 | 90 | inferred_complete_timeline |
| `Action_None` | 387 | 398 | 12 | inferred_complete_timeline |
| `Action_None` | 402 | 449 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–67 | 67 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–43 | 29 | 5 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 5–65 | 37 | 6 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 6–64 | 25 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 10–275 | 261 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 50–305 | 217 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 77–87 | 11 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 79–449 | 371 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 81–393 | 294 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 101–103 | 3 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 115–288 | 156 | 7 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 126–231 | 32 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 129–136 | 5 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 135–449 | 300 | 9 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 150–156 | 7 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 191–192 | 2 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 225–449 | 225 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 243–247 | 5 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 298–449 | 146 | 3 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 306–449 | 94 | 7 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 316–317 | 2 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 320–321 | 2 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 320–449 | 127 | 2 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 330–449 | 113 | 4 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 341–388 | 44 | 3 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 343–344 | 2 | 1 | Undefined position; Undefined team |
| `43` | `63` | Position_Unknown | Team_Unknown | 348–353 | 4 | 2 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 355–449 | 82 | 4 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 374–384 | 6 | 2 | Undefined position; Undefined team |
| `46` | `69` | Position_Unknown | Team_Unknown | 382–387 | 6 | 1 | Undefined position; Undefined team |
| `47` | `74` | Position_Unknown | Team_Unknown | 394–449 | 40 | 6 | Undefined position; Undefined team |
| `48` | `77` | Position_Unknown | Team_Unknown | 409–446 | 36 | 3 | Undefined position; Undefined team |
| `49` | `78` | Position_Unknown | Team_Unknown | 410–448 | 36 | 3 | Undefined position; Undefined team |
| `50` | `79` | Position_Unknown | Team_Unknown | 411–412 | 2 | 1 | Undefined position; Undefined team |
| `51` | `81` | Position_Unknown | Team_Unknown | 414–449 | 25 | 3 | Undefined position; Undefined team |
| `52` | `83` | Position_Unknown | Team_Unknown | 415–448 | 34 | 1 | Undefined position; Undefined team |
| `53` | `84` | Position_Unknown | Team_Unknown | 415–449 | 12 | 2 | Undefined position; Undefined team |
| `54` | `85` | Position_Unknown | Team_Unknown | 417–449 | 33 | 1 | Undefined position; Undefined team |
| `55` | `86` | Position_Unknown | Team_Unknown | 418–428 | 11 | 1 | Undefined position; Undefined team |
| `56` | `87` | Position_Unknown | Team_Unknown | 418–445 | 22 | 2 | Undefined position; Undefined team |
| `57` | `89` | Position_Unknown | Team_Unknown | 420–449 | 29 | 2 | Undefined position; Undefined team |
| `58` | `92` | Position_Unknown | Team_Unknown | 422–449 | 26 | 2 | Undefined position; Undefined team |
| `59` | `94` | Position_Unknown | Team_Unknown | 423–425 | 3 | 1 | Undefined position; Undefined team |
| `60` | `95` | Position_Unknown | Team_Unknown | 423–449 | 24 | 2 | Undefined position; Undefined team |
| `61` | `96` | Position_Unknown | Team_Unknown | 423–449 | 14 | 3 | Undefined position; Undefined team |
| `62` | `97` | Position_Unknown | Team_Unknown | 423–425 | 3 | 1 | Undefined position; Undefined team |
| `63` | `98` | Position_Unknown | Team_Unknown | 423–449 | 25 | 2 | Undefined position; Undefined team |
| `64` | `99` | Position_Unknown | Team_Unknown | 425–448 | 23 | 2 | Undefined position; Undefined team |
| `65` | `103` | Position_Unknown | Team_Unknown | 427–449 | 23 | 1 | Undefined position; Undefined team |
| `66` | `104` | Position_Unknown | Team_Unknown | 427–436 | 10 | 1 | Undefined position; Undefined team |
| `67` | `105` | Position_Unknown | Team_Unknown | 427–438 | 12 | 1 | Undefined position; Undefined team |
| `68` | `106` | Position_Unknown | Team_Unknown | 427–449 | 20 | 2 | Undefined position; Undefined team |
| `69` | `107` | Position_Unknown | Team_Unknown | 427–429 | 3 | 1 | Undefined position; Undefined team |
| `70` | `108` | Position_Unknown | Team_Unknown | 427–429 | 3 | 1 | Undefined position; Undefined team |
| `71` | `109` | Position_Unknown | Team_Unknown | 427–449 | 4 | 2 | Undefined position; Undefined team |
| `72` | `110` | Position_Unknown | Team_Unknown | 429–449 | 21 | 1 | Undefined position; Undefined team |
| `73` | `111` | Position_Unknown | Team_Unknown | 430–432 | 3 | 1 | Undefined position; Undefined team |
| `74` | `112` | Position_Unknown | Team_Unknown | 433–448 | 16 | 1 | Undefined position; Undefined team |
| `75` | `113` | Position_Unknown | Team_Unknown | 433–449 | 13 | 3 | Undefined position; Undefined team |
| `76` | `114` | Position_Unknown | Team_Unknown | 435–436 | 2 | 1 | Undefined position; Undefined team |
| `77` | `115` | Position_Unknown | Team_Unknown | 437–444 | 8 | 1 | Undefined position; Undefined team |
| `78` | `116` | Position_Unknown | Team_Unknown | 437–449 | 8 | 3 | Undefined position; Undefined team |
| `79` | `117` | Position_Unknown | Team_Unknown | 437–443 | 6 | 2 | Undefined position; Undefined team |
| `80` | `118` | Position_Unknown | Team_Unknown | 437–449 | 13 | 1 | Undefined position; Undefined team |
| `81` | `119` | Position_Unknown | Team_Unknown | 439–449 | 11 | 1 | Undefined position; Undefined team |
| `82` | `122` | Position_Unknown | Team_Unknown | 441–445 | 4 | 2 | Undefined position; Undefined team |
| `83` | `123` | Position_Unknown | Team_Unknown | 441–449 | 9 | 1 | Undefined position; Undefined team |
| `84` | `124` | Position_Unknown | Team_Unknown | 441–442 | 2 | 1 | Undefined position; Undefined team |
| `85` | `125` | Position_Unknown | Team_Unknown | 441–449 | 8 | 2 | Undefined position; Undefined team |
| `86` | `126` | Position_Unknown | Team_Unknown | 441–445 | 5 | 1 | Undefined position; Undefined team |
| `87` | `127` | Position_Unknown | Team_Unknown | 441–443 | 3 | 1 | Undefined position; Undefined team |
| `88` | `129` | Position_Unknown | Team_Unknown | 444–449 | 6 | 1 | Undefined position; Undefined team |
| `89` | `130` | Position_Unknown | Team_Unknown | 444–448 | 5 | 1 | Undefined position; Undefined team |
| `90` | `131` | Position_Unknown | Team_Unknown | 444–445 | 2 | 1 | Undefined position; Undefined team |
| `91` | `132` | Position_Unknown | Team_Unknown | 444–445 | 2 | 1 | Undefined position; Undefined team |
| `92` | `133` | Position_Unknown | Team_Unknown | 445–446 | 2 | 1 | Undefined position; Undefined team |
| `93` | `134` | Position_Unknown | Team_Unknown | 445–448 | 4 | 1 | Undefined position; Undefined team |
| `94` | `137` | Position_Unknown | Team_Unknown | 446–449 | 4 | 1 | Undefined position; Undefined team |
| `95` | `138` | Position_Unknown | Team_Unknown | 446–449 | 4 | 1 | Undefined position; Undefined team |
| `96` | `142` | Position_Unknown | Team_Unknown | 449–449 | 1 | 1 | Undefined position; Undefined team |
| `97` | `143` | Position_Unknown | Team_Unknown | 449–449 | 1 | 1 | Undefined position; Undefined team |
| `98` | `144` | Position_Unknown | Team_Unknown | 449–449 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `36` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ 82 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 82 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 102, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '523,530,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 164 |
| Missing visible bounding boxes during action | 213 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_None' range [13-206] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-347] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-208] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-227] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-299] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-261] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-361] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-381] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-389] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-20] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-32] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-45] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-55] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-67] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-141] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-293] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-347] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-386] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-449] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-179] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-206] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-449] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-150] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-165] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-270] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-449] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-142] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-232] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-253] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-275] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-449] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-254] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-302] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-414] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-448] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-280] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-295] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-322] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-388] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-403] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-426] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-219] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-326] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-342] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-449] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-219] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-226] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-256] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-449] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-270] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-384] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-398] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-449] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-182] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-207] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-283] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-387] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-398] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-419] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-423] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-429] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-446] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-20] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-28] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-43] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-17] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-22] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-31] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-65] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-8] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-12] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-18] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-30] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-12] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-236] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-275] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-211] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-246] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-264] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-87] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-449] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-250] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-342] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-393] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-242] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-248] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-256] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-231] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-183] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-266] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [273-281] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [283-289] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [292-346] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [349-359] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-156] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-449] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-352] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-443] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-320] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-393] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-398] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-408] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-414] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-421] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-449] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-449] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-369] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-380] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-343] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-379] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-388] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-358] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-368] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-400] for track '44' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-449] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-376] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-387] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-397] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-409] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-426] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-434] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-446] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-426] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-432] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-446] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-416] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-436] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-448] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-417] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-430] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-448] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-449] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-428] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-432] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-445] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-432] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-440] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-425] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-425] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-430] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-443] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-425] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-429] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-434] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-448] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-436] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-438] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-430] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-429] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-429] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-428] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-432] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-448] for track '74' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-434] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-444] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-444] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-440] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-446] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-440] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-445] for track '85' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-445] for track '86' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-443] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-448] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-446] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-448] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '98' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '98' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_100'; source metadata written as null.

</details>