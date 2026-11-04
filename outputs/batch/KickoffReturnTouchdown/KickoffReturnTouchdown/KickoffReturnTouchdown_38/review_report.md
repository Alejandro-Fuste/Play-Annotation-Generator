# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_38

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_38`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 73
- **Ball Tracks:** 0
- **Action Segments:** 243
- **Validation Warnings:** 321
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 229
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchKick` | Kick_Returner2 | defense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | defense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner2 | defense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `0` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `1` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `10` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `11` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `15` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `2` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `3` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `4` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `5` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `9` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `15` | `15` | 13 | START | 13 | 78 |
| ✅ EXACT | `Action_KickBall` | Kicker | `15` | `15` | 79 | START | 79 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchKick` | Kick_Returner2 | `19` | `19` | 187 | START | 187 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | `19` | `19` | 206 | START | 206 | 215 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner2 | `19` | `19` | 651 | START | N/A | N/A |

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
- **Visible Frames:** 0–659
- **Visible Samples:** 660

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_KickApproach` | 13 | 78 | 66 | inferred_complete_timeline |
| `Action_KickBall` | 79 | 83 | 5 | inferred_complete_timeline |
| `Action_None` | 84 | 659 | 576 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 659

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 102 | 90 | inferred_complete_timeline |
| `Action_None` | 104 | 659 | 556 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–300
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 300 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 223 | 211 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–423
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 241 | 229 | inferred_complete_timeline |
| `Action_None` | 243 | 329 | 87 | inferred_complete_timeline |
| `Action_None` | 359 | 371 | 13 | inferred_complete_timeline |
| `Action_None` | 384 | 423 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–330
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 203 | 191 | inferred_complete_timeline |
| `Action_None` | 205 | 330 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–616
- **Visible Samples:** 606

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 219 | 207 | inferred_complete_timeline |
| `Action_None` | 221 | 289 | 69 | inferred_complete_timeline |
| `Action_None` | 292 | 296 | 5 | inferred_complete_timeline |
| `Action_None` | 301 | 319 | 19 | inferred_complete_timeline |
| `Action_None` | 324 | 616 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 204 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 297 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 246 | 234 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 652

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 199 | 187 | inferred_complete_timeline |
| `Action_None` | 202 | 226 | 25 | inferred_complete_timeline |
| `Action_None` | 230 | 257 | 28 | inferred_complete_timeline |
| `Action_None` | 261 | 659 | 399 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 645

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 221 | 209 | inferred_complete_timeline |
| `Action_None` | 223 | 263 | 41 | inferred_complete_timeline |
| `Action_None` | 267 | 283 | 17 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 293 | 599 | 307 | inferred_complete_timeline |
| `Action_None` | 604 | 659 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 208 | 196 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 243 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 201 | 189 | inferred_complete_timeline |
| `Action_None` | 203 | 205 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–411
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 342 | 330 | inferred_complete_timeline |
| `Action_None` | 350 | 411 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 185 | 173 | inferred_complete_timeline |
| `Action_None` | 194 | 302 | 109 | inferred_complete_timeline |
| `Action_None` | 306 | 313 | 8 | inferred_complete_timeline |
| `Action_None` | 323 | 324 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 93 | 81 | inferred_complete_timeline |
| `Action_None` | 97 | 192 | 96 | inferred_complete_timeline |
| `Action_None` | 198 | 262 | 65 | inferred_complete_timeline |
| `Action_None` | 319 | 325 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–553
- **Visible Samples:** 507

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 33 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 52 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 171 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 186 | 13 | inferred_complete_timeline |
| `Action_CatchKick` | 187 | 194 | 8 | inferred_complete_timeline |
| `Action_CatchKick` | 199 | 199 | 1 | inferred_complete_timeline |
| `Action_None` | 200 | 205 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 206 | 215 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 233 | 293 | 61 | inferred_complete_timeline |
| `Action_BallCarry` | 305 | 553 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 274 | 262 | inferred_complete_timeline |
| `Action_None` | 301 | 318 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–481
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 239 | 227 | inferred_complete_timeline |
| `Action_None` | 245 | 302 | 58 | inferred_complete_timeline |
| `Action_None` | 312 | 372 | 61 | inferred_complete_timeline |
| `Action_None` | 388 | 455 | 68 | inferred_complete_timeline |
| `Action_None` | 458 | 464 | 7 | inferred_complete_timeline |
| `Action_None` | 466 | 469 | 4 | inferred_complete_timeline |
| `Action_None` | 471 | 472 | 2 | inferred_complete_timeline |
| `Action_None` | 474 | 475 | 2 | inferred_complete_timeline |
| `Action_None` | 479 | 481 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–586
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 220 | 208 | inferred_complete_timeline |
| `Action_None` | 222 | 224 | 3 | inferred_complete_timeline |
| `Action_None` | 232 | 298 | 67 | inferred_complete_timeline |
| `Action_None` | 377 | 381 | 5 | inferred_complete_timeline |
| `Action_None` | 384 | 567 | 184 | inferred_complete_timeline |
| `Action_None` | 569 | 586 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–319 | 314 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 100–121 | 22 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 202–206 | 5 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 214–308 | 95 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 235–320 | 85 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 247–649 | 391 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 252–306 | 55 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 253–312 | 47 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 267–659 | 378 | 4 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 285–384 | 76 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 287–306 | 5 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 325–659 | 326 | 3 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 327–652 | 306 | 5 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 336–338 | 3 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 337–568 | 228 | 2 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 341–374 | 34 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 343–378 | 36 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 345–659 | 306 | 3 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 349–367 | 19 | 1 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 370–372 | 3 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 390–606 | 215 | 2 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 397–411 | 13 | 3 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 398–659 | 262 | 1 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 406–417 | 12 | 1 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 415–560 | 146 | 1 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 435–573 | 138 | 2 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 460–533 | 74 | 1 | Undefined position; Undefined team |
| `48` | `70` | Position_Unknown | Team_Unknown | 497–498 | 2 | 1 | Undefined position; Undefined team |
| `49` | `75` | Position_Unknown | Team_Unknown | 501–509 | 9 | 1 | Undefined position; Undefined team |
| `50` | `77` | Position_Unknown | Team_Unknown | 507–556 | 32 | 5 | Undefined position; Undefined team |
| `51` | `78` | Position_Unknown | Team_Unknown | 507–643 | 68 | 16 | Undefined position; Undefined team |
| `52` | `79` | Position_Unknown | Team_Unknown | 513–551 | 26 | 4 | Undefined position; Undefined team |
| `53` | `83` | Position_Unknown | Team_Unknown | 517–634 | 10 | 3 | Undefined position; Undefined team |
| `54` | `85` | Position_Unknown | Team_Unknown | 518–643 | 111 | 6 | Undefined position; Undefined team |
| `55` | `86` | Position_Unknown | Team_Unknown | 518–656 | 50 | 5 | Undefined position; Undefined team |
| `56` | `87` | Position_Unknown | Team_Unknown | 518–525 | 8 | 1 | Undefined position; Undefined team |
| `57` | `88` | Position_Unknown | Team_Unknown | 518–630 | 42 | 12 | Undefined position; Undefined team |
| `58` | `95` | Position_Unknown | Team_Unknown | 526–623 | 28 | 6 | Undefined position; Undefined team |
| `59` | `96` | Position_Unknown | Team_Unknown | 531–544 | 12 | 3 | Undefined position; Undefined team |
| `60` | `97` | Position_Unknown | Team_Unknown | 539–541 | 3 | 1 | Undefined position; Undefined team |
| `61` | `101` | Position_Unknown | Team_Unknown | 548–659 | 105 | 3 | Undefined position; Undefined team |
| `62` | `102` | Position_Unknown | Team_Unknown | 557–637 | 65 | 6 | Undefined position; Undefined team |
| `63` | `106` | Position_Unknown | Team_Unknown | 577–659 | 83 | 1 | Undefined position; Undefined team |
| `64` | `108` | Position_Unknown | Team_Unknown | 583–638 | 53 | 2 | Undefined position; Undefined team |
| `65` | `109` | Position_Unknown | Team_Unknown | 584–652 | 50 | 8 | Undefined position; Undefined team |
| `66` | `110` | Position_Unknown | Team_Unknown | 604–615 | 12 | 1 | Undefined position; Undefined team |
| `67` | `114` | Position_Unknown | Team_Unknown | 616–646 | 31 | 1 | Undefined position; Undefined team |
| `68` | `117` | Position_Unknown | Team_Unknown | 623–624 | 2 | 1 | Undefined position; Undefined team |
| `69` | `118` | Position_Unknown | Team_Unknown | 623–651 | 25 | 3 | Undefined position; Undefined team |
| `70` | `120` | Position_Unknown | Team_Unknown | 624–632 | 4 | 2 | Undefined position; Undefined team |
| `71` | `121` | Position_Unknown | Team_Unknown | 632–633 | 2 | 1 | Undefined position; Undefined team |
| `72` | `122` | Position_Unknown | Team_Unknown | 632–634 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CatchKick` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (4 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `19` (Kick_Returner2)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ 52 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 52 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 104 |
| Missing visible bounding boxes during action | 214 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 78: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '19' has invalid range: start=651, end=553. Clamping end to start.
- ⚠️ Action 'Action_None' range [13-300] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-102] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-659] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-223] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-246] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-219] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-289] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-319] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-616] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-297] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-274] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-318] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-185] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-302] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-313] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-201] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-371] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-423] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-330] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-204] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-305] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-319] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-239] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-302] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-372] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-455] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-464] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-469] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-472] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-481] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-342] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-411] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-659] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-226] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-257] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-263] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-283] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-599] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-208] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-243] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-52] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-171] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-186] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchKick' range [187-194] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 200, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [200-205] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [206-215] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [223-225] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [233-293] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [305-553] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-220] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-298] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-381] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-567] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-586] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-192] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-262] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-325] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-121] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-308] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-317] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-298] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-364] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-540] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-649] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-306] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-287] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-300] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-312] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-290] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-352] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-304] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-384] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-569] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-585] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-384] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-573] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-581] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-588] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-652] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-338] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-386] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-568] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-374] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-378] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-352] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-363] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-659] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-367] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-372] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-499] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-606] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-405] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-408] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-417] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-560] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-512] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-573] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-533] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-498] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-509] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-520] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-525] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-532] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-543] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-556] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-509] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-514] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-519] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-524] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-529] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-534] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-540] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-562] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-572] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-582] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-587] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-590] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-620] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-643] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-529] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-534] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-541] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-518] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-541] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [630-634] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-543] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-556] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-575] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-601] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-643] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-519] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-527] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-620] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-656] for track '55' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-525] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-519] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-545] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-569] for track '57' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-573] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-577] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-585] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-589] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-593] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-596] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-625] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-630] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-529] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-540] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-545] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-554] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-565] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-623] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-533] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-539] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-544] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-541] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-550] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-558] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-659] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-567] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-580] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-588] for track '62' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-596] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-623] for track '62' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-637] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-590] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-638] for track '64' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-589] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-593] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-607] for track '65' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-618] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-626] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-637] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-642] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [645-652] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-615] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-646] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-624] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-636] for track '69' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [640-646] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-651] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-625] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-632] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-633] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-634] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>