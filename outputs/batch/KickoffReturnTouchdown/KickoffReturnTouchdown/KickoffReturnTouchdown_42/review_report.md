# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_42

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_42`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 69
- **Ball Tracks:** 0
- **Action Segments:** 239
- **Validation Warnings:** 300
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 224
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `21` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `17` | `17` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `17` | `17` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | defense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | defense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner2 | defense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `10` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `12` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `13` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `14` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `15` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `16` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `17` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `18` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `19` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `21` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `17` | `17` | 15 | START | 15 | 99 |
| ✅ EXACT | `Action_KickBall` | Kicker | `17` | `17` | 100 | START | 100 | 103 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | `1` | `1` | 213 | START | 213 | 218 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | `1` | `1` | 241 | START | 241 | 295 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner2 | `1` | `1` | 632 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_KickApproach` | 15 | 99 | 85 | inferred_complete_timeline |
| `Action_KickBall` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_None` | 104 | 407 | 304 | inferred_complete_timeline |
| `Action_None` | 411 | 438 | 28 | inferred_complete_timeline |
| `Action_None` | 440 | 441 | 2 | inferred_complete_timeline |
| `Action_None` | 444 | 449 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–303
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 266 | 252 | inferred_complete_timeline |
| `Action_None` | 272 | 303 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–351
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 247 | 233 | inferred_complete_timeline |
| `Action_None` | 250 | 351 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–395
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 267 | 253 | inferred_complete_timeline |
| `Action_None` | 288 | 296 | 9 | inferred_complete_timeline |
| `Action_None` | 299 | 304 | 6 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 315 | 319 | 5 | inferred_complete_timeline |
| `Action_None` | 321 | 323 | 3 | inferred_complete_timeline |
| `Action_None` | 325 | 327 | 3 | inferred_complete_timeline |
| `Action_None` | 330 | 395 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 14 | 1 | inferred_complete_timeline |
| `Action_None` | 15 | 15 | 1 | inferred_complete_timeline |
| `Action_None` | 67 | 218 | 152 | inferred_complete_timeline |
| `Action_None` | 221 | 233 | 13 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |
| `Action_None` | 254 | 256 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 236 | 222 | inferred_complete_timeline |
| `Action_None` | 241 | 243 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 621

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 116 | 102 | inferred_complete_timeline |
| `Action_None` | 119 | 123 | 5 | inferred_complete_timeline |
| `Action_None` | 127 | 314 | 188 | inferred_complete_timeline |
| `Action_None` | 322 | 338 | 17 | inferred_complete_timeline |
| `Action_None` | 341 | 354 | 14 | inferred_complete_timeline |
| `Action_None` | 360 | 361 | 2 | inferred_complete_timeline |
| `Action_None` | 372 | 375 | 4 | inferred_complete_timeline |
| `Action_None` | 380 | 638 | 259 | inferred_complete_timeline |
| `Action_None` | 645 | 659 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 185 | 171 | inferred_complete_timeline |
| `Action_None` | 189 | 210 | 22 | inferred_complete_timeline |
| `Action_None` | 214 | 229 | 16 | inferred_complete_timeline |
| `Action_None` | 231 | 283 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 256 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–335
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 335 | 321 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–390
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 219 | 205 | inferred_complete_timeline |
| `Action_None` | 223 | 226 | 4 | inferred_complete_timeline |
| `Action_None` | 229 | 280 | 52 | inferred_complete_timeline |
| `Action_None` | 300 | 335 | 36 | inferred_complete_timeline |
| `Action_None` | 338 | 339 | 2 | inferred_complete_timeline |
| `Action_None` | 342 | 355 | 14 | inferred_complete_timeline |
| `Action_None` | 365 | 377 | 13 | inferred_complete_timeline |
| `Action_None` | 384 | 390 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–648
- **Visible Samples:** 576

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 140 | 126 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 147 | 3 | inferred_complete_timeline |
| `Action_None` | 153 | 222 | 70 | inferred_complete_timeline |
| `Action_None` | 233 | 257 | 25 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 273 | 9 | inferred_complete_timeline |
| `Action_None` | 288 | 353 | 66 | inferred_complete_timeline |
| `Action_None` | 355 | 369 | 15 | inferred_complete_timeline |
| `Action_None` | 383 | 386 | 4 | inferred_complete_timeline |
| `Action_None` | 392 | 401 | 10 | inferred_complete_timeline |
| `Action_None` | 408 | 425 | 18 | inferred_complete_timeline |
| `Action_None` | 427 | 451 | 25 | inferred_complete_timeline |
| `Action_None` | 454 | 616 | 163 | inferred_complete_timeline |
| `Action_None` | 625 | 635 | 11 | inferred_complete_timeline |
| `Action_None` | 637 | 648 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 222 | 208 | inferred_complete_timeline |
| `Action_None` | 230 | 388 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 298 | 284 | inferred_complete_timeline |
| `Action_None` | 301 | 347 | 47 | inferred_complete_timeline |
| `Action_None` | 355 | 359 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 637

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 171 | 157 | inferred_complete_timeline |
| `Action_None` | 176 | 189 | 14 | inferred_complete_timeline |
| `Action_None` | 191 | 412 | 222 | inferred_complete_timeline |
| `Action_None` | 415 | 540 | 126 | inferred_complete_timeline |
| `Action_None` | 542 | 543 | 2 | inferred_complete_timeline |
| `Action_None` | 548 | 549 | 2 | inferred_complete_timeline |
| `Action_None` | 561 | 659 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–392
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 238 | 224 | inferred_complete_timeline |
| `Action_None` | 240 | 260 | 21 | inferred_complete_timeline |
| `Action_None` | 270 | 328 | 59 | inferred_complete_timeline |
| `Action_None` | 337 | 338 | 2 | inferred_complete_timeline |
| `Action_None` | 346 | 348 | 3 | inferred_complete_timeline |
| `Action_None` | 352 | 368 | 17 | inferred_complete_timeline |
| `Action_None` | 373 | 376 | 4 | inferred_complete_timeline |
| `Action_None` | 378 | 392 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–392
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 299 | 285 | inferred_complete_timeline |
| `Action_None` | 301 | 309 | 9 | inferred_complete_timeline |
| `Action_None` | 319 | 320 | 2 | inferred_complete_timeline |
| `Action_None` | 329 | 353 | 25 | inferred_complete_timeline |
| `Action_None` | 357 | 362 | 6 | inferred_complete_timeline |
| `Action_None` | 366 | 370 | 5 | inferred_complete_timeline |
| `Action_None` | 372 | 377 | 6 | inferred_complete_timeline |
| `Action_None` | 390 | 392 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–455
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_CatchKick` | 213 | 218 | 6 | inferred_complete_timeline |
| `Action_None` | 219 | 240 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 241 | 295 | 55 | inferred_complete_timeline |
| `Action_BallCarry` | 302 | 366 | 65 | inferred_complete_timeline |
| `Action_BallCarry` | 368 | 455 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 225 | 211 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 278 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–417
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 279 | 265 | inferred_complete_timeline |
| `Action_None` | 281 | 285 | 5 | inferred_complete_timeline |
| `Action_None` | 322 | 329 | 8 | inferred_complete_timeline |
| `Action_None` | 331 | 345 | 15 | inferred_complete_timeline |
| `Action_None` | 347 | 370 | 24 | inferred_complete_timeline |
| `Action_None` | 372 | 375 | 4 | inferred_complete_timeline |
| `Action_None` | 377 | 417 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–365
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 225 | 211 | inferred_complete_timeline |
| `Action_None` | 227 | 235 | 9 | inferred_complete_timeline |
| `Action_None` | 241 | 365 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 100–321 | 207 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 158–192 | 11 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 186–207 | 22 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 249–319 | 11 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 252–253 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 264–341 | 60 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 298–303 | 6 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 307–512 | 141 | 7 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 309–630 | 296 | 7 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 318–404 | 86 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 318–319 | 2 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 327–418 | 91 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 329–578 | 249 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 369–370 | 2 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 369–413 | 43 | 2 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 376–402 | 27 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 388–413 | 14 | 2 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 393–504 | 54 | 4 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 399–656 | 238 | 6 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 407–418 | 12 | 1 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 411–412 | 2 | 1 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 420–589 | 170 | 1 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 423–560 | 126 | 2 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 425–482 | 21 | 3 | Undefined position; Undefined team |
| `46` | `63` | Position_Unknown | Team_Unknown | 432–434 | 3 | 1 | Undefined position; Undefined team |
| `47` | `64` | Position_Unknown | Team_Unknown | 451–485 | 32 | 2 | Undefined position; Undefined team |
| `48` | `66` | Position_Unknown | Team_Unknown | 470–659 | 176 | 4 | Undefined position; Undefined team |
| `49` | `67` | Position_Unknown | Team_Unknown | 503–642 | 116 | 6 | Undefined position; Undefined team |
| `50` | `68` | Position_Unknown | Team_Unknown | 507–659 | 143 | 4 | Undefined position; Undefined team |
| `51` | `70` | Position_Unknown | Team_Unknown | 520–532 | 13 | 1 | Undefined position; Undefined team |
| `52` | `71` | Position_Unknown | Team_Unknown | 524–525 | 2 | 1 | Undefined position; Undefined team |
| `53` | `73` | Position_Unknown | Team_Unknown | 552–624 | 72 | 2 | Undefined position; Undefined team |
| `54` | `74` | Position_Unknown | Team_Unknown | 562–567 | 5 | 2 | Undefined position; Undefined team |
| `55` | `75` | Position_Unknown | Team_Unknown | 577–659 | 72 | 5 | Undefined position; Undefined team |
| `56` | `76` | Position_Unknown | Team_Unknown | 580–659 | 59 | 2 | Undefined position; Undefined team |
| `57` | `77` | Position_Unknown | Team_Unknown | 581–659 | 76 | 2 | Undefined position; Undefined team |
| `58` | `78` | Position_Unknown | Team_Unknown | 590–591 | 2 | 1 | Undefined position; Undefined team |
| `59` | `79` | Position_Unknown | Team_Unknown | 592–648 | 44 | 2 | Undefined position; Undefined team |
| `60` | `80` | Position_Unknown | Team_Unknown | 598–659 | 62 | 1 | Undefined position; Undefined team |
| `61` | `81` | Position_Unknown | Team_Unknown | 605–656 | 52 | 1 | Undefined position; Undefined team |
| `62` | `82` | Position_Unknown | Team_Unknown | 611–659 | 49 | 1 | Undefined position; Undefined team |
| `63` | `84` | Position_Unknown | Team_Unknown | 633–659 | 26 | 2 | Undefined position; Undefined team |
| `64` | `85` | Position_Unknown | Team_Unknown | 646–659 | 14 | 1 | Undefined position; Undefined team |
| `65` | `86` | Position_Unknown | Team_Unknown | 648–659 | 12 | 1 | Undefined position; Undefined team |
| `66` | `87` | Position_Unknown | Team_Unknown | 650–659 | 10 | 1 | Undefined position; Undefined team |
| `67` | `88` | Position_Unknown | Team_Unknown | 655–659 | 5 | 1 | Undefined position; Undefined team |
| `68` | `89` | Position_Unknown | Team_Unknown | 657–659 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (3 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `1` (Kick_Returner2)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ 48 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 48 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 96 |
| Missing visible bounding boxes during action | 202 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '1' has invalid range: start=632, end=455. Clamping end to start.
- ⚠️ Action 'Action_None' range [15-238] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-260] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-328] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-348] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-368] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-392] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [241-295] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [302-366] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [368-455] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-225] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-278] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-219] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-280] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-335] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-355] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-377] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-390] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-299] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-309] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-353] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-362] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-370] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-377] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-392] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-298] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-347] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-171] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-189] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-412] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-540] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-543] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-549] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-222] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-257] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-273] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-353] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-369] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-386] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-401] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-425] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-451] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-616] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-635] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [637-648] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-279] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-345] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-370] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-375] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-417] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-222] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-388] for track '9' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-185] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-229] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-283] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-235] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-365] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-256] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-236] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-335] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-266] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-303] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-314] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-338] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-354] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-375] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-638] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [645-659] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-407] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-438] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-441] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-449] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-247] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-351] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-267] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-296] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-304] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-395] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '21' starts at frame 15, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [15-15] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-218] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-233] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-256] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-272] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-321] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-207] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-256] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-281] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-325] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-341] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-303] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-323] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-356] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-379] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-388] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-403] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-471] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-512] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-313] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-384] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-393] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-552] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-593] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-625] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-630] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-399] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-404] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-410] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-418] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-354] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-578] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-376] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-413] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-402] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-413] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-395] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-462] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-501] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-402] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-422] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-557] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-560] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-652] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [654-656] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-418] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-589] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-509] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-560] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-432] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-436] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-482] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-434] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-478] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-485] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-549] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-645] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-656] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-507] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-515] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-529] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-532] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-636] for track '49' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-642] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-510] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-635] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-639] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-532] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-573] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-624] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-564] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-633] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-636] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-641] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-649] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-584] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-606] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-591] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-625] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-648] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-656] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-645] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-659] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>