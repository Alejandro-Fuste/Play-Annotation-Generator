# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_22

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_22`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 58
- **Ball Tracks:** 0
- **Action Segments:** 259
- **Validation Warnings:** 306
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
- **Inferred Coverage Segments (Action_None):** 245
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | defense | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `0` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `1` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `10` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `14` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `15` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `19` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `2` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `3` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `5` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `9` | `Group` | 0 | START | 0 | 67 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `15` | `15` | 68 | START | 68 | 93 |
| ✅ EXACT | `Action_KickBall` | Kicker | `15` | `15` | 94 | START | 94 | 101 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `16` | `16` | 205 | START | 205 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | `16` | `16` | 240 | START | 240 | 300 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner1 | `16` | `16` | 591 | START | N/A | N/A |

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
- **Visible Frames:** 0–571
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_KickApproach` | 68 | 93 | 26 | inferred_complete_timeline |
| `Action_KickBall` | 94 | 101 | 8 | inferred_complete_timeline |
| `Action_None` | 102 | 112 | 11 | inferred_complete_timeline |
| `Action_None` | 115 | 325 | 211 | inferred_complete_timeline |
| `Action_None` | 328 | 377 | 50 | inferred_complete_timeline |
| `Action_None` | 379 | 427 | 49 | inferred_complete_timeline |
| `Action_None` | 437 | 457 | 21 | inferred_complete_timeline |
| `Action_None` | 460 | 471 | 12 | inferred_complete_timeline |
| `Action_None` | 474 | 571 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–527
- **Visible Samples:** 507

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 78 | 11 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_None` | 87 | 151 | 65 | inferred_complete_timeline |
| `Action_None` | 157 | 280 | 124 | inferred_complete_timeline |
| `Action_None` | 282 | 335 | 54 | inferred_complete_timeline |
| `Action_None` | 346 | 527 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 79 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 171 | 104 | inferred_complete_timeline |
| `Action_None` | 173 | 201 | 29 | inferred_complete_timeline |
| `Action_None` | 205 | 231 | 27 | inferred_complete_timeline |
| `Action_None` | 234 | 247 | 14 | inferred_complete_timeline |
| `Action_None` | 249 | 251 | 3 | inferred_complete_timeline |
| `Action_None` | 254 | 260 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 124 | 57 | inferred_complete_timeline |
| `Action_None` | 126 | 138 | 13 | inferred_complete_timeline |
| `Action_None` | 144 | 186 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 79 | 12 | inferred_complete_timeline |
| `Action_None` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 133 | 66 | inferred_complete_timeline |
| `Action_None` | 137 | 154 | 18 | inferred_complete_timeline |
| `Action_None` | 156 | 159 | 4 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 236 | 56 | inferred_complete_timeline |
| `Action_None` | 239 | 259 | 21 | inferred_complete_timeline |
| `Action_None` | 291 | 321 | 31 | inferred_complete_timeline |
| `Action_None` | 326 | 359 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 128 | 61 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 134 | 146 | 13 | inferred_complete_timeline |
| `Action_None` | 152 | 157 | 6 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_None` | 179 | 193 | 15 | inferred_complete_timeline |
| `Action_None` | 195 | 229 | 35 | inferred_complete_timeline |
| `Action_None` | 239 | 247 | 9 | inferred_complete_timeline |
| `Action_None` | 249 | 270 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 137 | 70 | inferred_complete_timeline |
| `Action_None` | 142 | 149 | 8 | inferred_complete_timeline |
| `Action_None` | 160 | 164 | 5 | inferred_complete_timeline |
| `Action_None` | 167 | 183 | 17 | inferred_complete_timeline |
| `Action_None` | 185 | 228 | 44 | inferred_complete_timeline |
| `Action_None` | 239 | 244 | 6 | inferred_complete_timeline |
| `Action_None` | 247 | 268 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 237 | 170 | inferred_complete_timeline |
| `Action_None` | 242 | 317 | 76 | inferred_complete_timeline |
| `Action_None` | 322 | 532 | 211 | inferred_complete_timeline |
| `Action_None` | 534 | 599 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–592
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 67 | 8 | inferred_complete_timeline |
| `Action_None` | 68 | 229 | 162 | inferred_complete_timeline |
| `Action_None` | 238 | 270 | 33 | inferred_complete_timeline |
| `Action_None` | 276 | 282 | 7 | inferred_complete_timeline |
| `Action_None` | 287 | 298 | 12 | inferred_complete_timeline |
| `Action_None` | 308 | 323 | 16 | inferred_complete_timeline |
| `Action_None` | 326 | 344 | 19 | inferred_complete_timeline |
| `Action_None` | 385 | 431 | 47 | inferred_complete_timeline |
| `Action_None` | 438 | 441 | 4 | inferred_complete_timeline |
| `Action_None` | 450 | 458 | 9 | inferred_complete_timeline |
| `Action_None` | 478 | 481 | 4 | inferred_complete_timeline |
| `Action_None` | 483 | 486 | 4 | inferred_complete_timeline |
| `Action_None` | 488 | 489 | 2 | inferred_complete_timeline |
| `Action_None` | 495 | 575 | 81 | inferred_complete_timeline |
| `Action_None` | 577 | 592 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–312
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 200 | 133 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_None` | 213 | 242 | 30 | inferred_complete_timeline |
| `Action_None` | 247 | 292 | 46 | inferred_complete_timeline |
| `Action_None` | 297 | 312 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–434
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 434 | 367 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–576
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 290 | 223 | inferred_complete_timeline |
| `Action_None` | 293 | 299 | 7 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_None` | 337 | 371 | 35 | inferred_complete_timeline |
| `Action_None` | 375 | 422 | 48 | inferred_complete_timeline |
| `Action_None` | 428 | 576 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 507

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 244 | 177 | inferred_complete_timeline |
| `Action_None` | 248 | 509 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–312
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_CatchKick` | 205 | 214 | 10 | inferred_complete_timeline |
| `Action_None` | 215 | 239 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 240 | 300 | 61 | inferred_complete_timeline |
| `Action_BallCarry` | 310 | 312 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–446
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 280 | 213 | inferred_complete_timeline |
| `Action_None` | 288 | 292 | 5 | inferred_complete_timeline |
| `Action_None` | 294 | 312 | 19 | inferred_complete_timeline |
| `Action_None` | 314 | 323 | 10 | inferred_complete_timeline |
| `Action_None` | 332 | 446 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 270 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 192 | 125 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 549

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 262 | 195 | inferred_complete_timeline |
| `Action_None` | 286 | 295 | 10 | inferred_complete_timeline |
| `Action_None` | 298 | 303 | 6 | inferred_complete_timeline |
| `Action_None` | 327 | 474 | 148 | inferred_complete_timeline |
| `Action_None` | 477 | 481 | 5 | inferred_complete_timeline |
| `Action_None` | 483 | 599 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 301 | 234 | inferred_complete_timeline |
| `Action_None` | 305 | 339 | 35 | inferred_complete_timeline |
| `Action_None` | 343 | 599 | 257 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 5–210 | 148 | 13 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 47–351 | 198 | 10 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 85–449 | 337 | 7 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 155–163 | 9 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 207–253 | 31 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 207–272 | 63 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 218–241 | 16 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 251–500 | 239 | 7 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 268–587 | 285 | 8 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 300–477 | 172 | 7 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 304–599 | 286 | 6 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 317–554 | 235 | 3 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 328–599 | 268 | 2 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 329–352 | 14 | 5 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 337–339 | 3 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 344–386 | 43 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 367–392 | 24 | 2 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 374–599 | 213 | 7 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 385–599 | 215 | 1 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 391–396 | 6 | 1 | Undefined position; Undefined team |
| `43` | `63` | Position_Unknown | Team_Unknown | 397–573 | 176 | 2 | Undefined position; Undefined team |
| `44` | `67` | Position_Unknown | Team_Unknown | 404–456 | 41 | 4 | Undefined position; Undefined team |
| `45` | `70` | Position_Unknown | Team_Unknown | 416–588 | 170 | 3 | Undefined position; Undefined team |
| `46` | `71` | Position_Unknown | Team_Unknown | 433–481 | 33 | 4 | Undefined position; Undefined team |
| `47` | `74` | Position_Unknown | Team_Unknown | 454–500 | 34 | 3 | Undefined position; Undefined team |
| `48` | `75` | Position_Unknown | Team_Unknown | 465–568 | 89 | 2 | Undefined position; Undefined team |
| `49` | `77` | Position_Unknown | Team_Unknown | 478–525 | 42 | 3 | Undefined position; Undefined team |
| `50` | `78` | Position_Unknown | Team_Unknown | 480–481 | 2 | 1 | Undefined position; Undefined team |
| `51` | `79` | Position_Unknown | Team_Unknown | 483–515 | 10 | 4 | Undefined position; Undefined team |
| `52` | `80` | Position_Unknown | Team_Unknown | 485–598 | 109 | 2 | Undefined position; Undefined team |
| `53` | `81` | Position_Unknown | Team_Unknown | 494–565 | 72 | 1 | Undefined position; Undefined team |
| `54` | `82` | Position_Unknown | Team_Unknown | 500–501 | 2 | 1 | Undefined position; Undefined team |
| `55` | `83` | Position_Unknown | Team_Unknown | 500–523 | 16 | 3 | Undefined position; Undefined team |
| `56` | `87` | Position_Unknown | Team_Unknown | 524–595 | 10 | 4 | Undefined position; Undefined team |
| `57` | `88` | Position_Unknown | Team_Unknown | 545–546 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (2 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `16` (Kick_Returner1)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ 37 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 37 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 74 |
| Missing visible bounding boxes during action | 230 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '16' has invalid range: start=591, end=312. Clamping end to start.
- ⚠️ Action 'Action_None' range [68-124] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-138] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-186] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-237] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-317] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-532] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-133] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-154] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-236] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-259] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-321] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-359] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-137] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-183] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-228] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-268] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-290] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-371] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-422] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-576] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-171] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-201] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-231] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-247] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-260] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-242] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-292] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-312] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-301] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-339] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-434] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-79] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-128] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-193] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-229] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-247] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-270] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-244] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-509] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-229] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-270] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-282] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-298] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-323] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-344] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-431] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-441] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-458] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-481] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-486] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-489] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-575] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-592] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-112] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-325] for track '15' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-377] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-427] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-457] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-471] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-571] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [240-300] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [310-312] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-262] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-295] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-303] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-474] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-481] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-280] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-292] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-312] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-323] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-446] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-78] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-151] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-280] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-335] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-527] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-270] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-11] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-67] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-134] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-152] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-182] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-200] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-60] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-164] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-202] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-224] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-351] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-211] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-282] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-311] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-317] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-449] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-163] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-230] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-253] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-232] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-241] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-272] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-231] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-288] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-301] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-329] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-342] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-443] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-500] for track '30' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-290] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-302] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-337] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-426] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-547] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-587] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-327] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-359] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-406] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-421] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-436] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-451] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-477] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-312] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-327] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-378] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-409] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-599] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-387] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-396] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-554] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-455] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-331] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-337] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-339] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-386] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-386] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-392] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-385] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-396] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-420] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-463] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-476] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-532] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-599] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-396] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-493] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-573] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-432] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-444] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-456] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-481] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-505] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-588] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-443] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-456] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-469] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-481] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-456] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-462] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-500] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-488] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-568] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-504] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-511] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-525] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-481] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-484] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-502] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-507] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-515] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-588] for track '52' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-598] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-565] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-504] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-517] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-523] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-530] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-542] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-595] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-546] for track '57' has 1 frames without a visible bounding box.
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

</details>