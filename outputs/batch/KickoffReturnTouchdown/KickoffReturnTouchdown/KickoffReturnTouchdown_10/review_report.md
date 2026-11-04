# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_10

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_10`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 65
- **Ball Tracks:** 0
- **Action Segments:** 269
- **Validation Warnings:** 324
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 254
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchKick` | Kick_Returner1 | defense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | defense | `21` | `21` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `10` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `11` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `12` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `13` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `15` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `16` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `3` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `6` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `7` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `8` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `15` | `15` | 18 | START | 18 | 84 |
| ✅ EXACT | `Action_KickBall` | Kicker | `15` | `15` | 85 | START | 85 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchKick` | Kick_Returner1 | `21` | `21` | 190 | START | 190 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | `21` | `21` | 210 | START | 210 | 282 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner1 | `21` | `21` | 540 | START | N/A | N/A |

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
- **Visible Frames:** 0–416
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_KickApproach` | 18 | 84 | 67 | inferred_complete_timeline |
| `Action_KickBall` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_None` | 89 | 409 | 321 | inferred_complete_timeline |
| `Action_None` | 411 | 416 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_None` | 63 | 91 | 29 | inferred_complete_timeline |
| `Action_None` | 101 | 320 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 539 | 522 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 503

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 117 | 100 | inferred_complete_timeline |
| `Action_None` | 119 | 178 | 60 | inferred_complete_timeline |
| `Action_None` | 182 | 390 | 209 | inferred_complete_timeline |
| `Action_None` | 395 | 396 | 2 | inferred_complete_timeline |
| `Action_None` | 404 | 408 | 5 | inferred_complete_timeline |
| `Action_None` | 410 | 416 | 7 | inferred_complete_timeline |
| `Action_None` | 420 | 436 | 17 | inferred_complete_timeline |
| `Action_None` | 447 | 448 | 2 | inferred_complete_timeline |
| `Action_None` | 457 | 539 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 198 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 203 | 186 | inferred_complete_timeline |
| `Action_None` | 207 | 268 | 62 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 286 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–306
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 147 | 130 | inferred_complete_timeline |
| `Action_None` | 149 | 264 | 116 | inferred_complete_timeline |
| `Action_None` | 270 | 287 | 18 | inferred_complete_timeline |
| `Action_None` | 290 | 306 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–538
- **Visible Samples:** 524

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 141 | 124 | inferred_complete_timeline |
| `Action_None` | 143 | 305 | 163 | inferred_complete_timeline |
| `Action_None` | 320 | 538 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 284 | 267 | inferred_complete_timeline |
| `Action_None` | 314 | 320 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 539 | 522 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 296 | 279 | inferred_complete_timeline |
| `Action_None` | 298 | 314 | 17 | inferred_complete_timeline |
| `Action_None` | 320 | 357 | 38 | inferred_complete_timeline |
| `Action_None` | 395 | 396 | 2 | inferred_complete_timeline |
| `Action_None` | 401 | 539 | 139 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 173 | 156 | inferred_complete_timeline |
| `Action_None` | 177 | 261 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–430
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 146 | 129 | inferred_complete_timeline |
| `Action_None` | 152 | 159 | 8 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 173 | 8 | inferred_complete_timeline |
| `Action_None` | 175 | 204 | 30 | inferred_complete_timeline |
| `Action_None` | 207 | 212 | 6 | inferred_complete_timeline |
| `Action_None` | 218 | 357 | 140 | inferred_complete_timeline |
| `Action_None` | 364 | 392 | 29 | inferred_complete_timeline |
| `Action_None` | 397 | 400 | 4 | inferred_complete_timeline |
| `Action_None` | 403 | 422 | 20 | inferred_complete_timeline |
| `Action_None` | 427 | 430 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 104 | 87 | inferred_complete_timeline |
| `Action_None` | 119 | 132 | 14 | inferred_complete_timeline |
| `Action_None` | 136 | 154 | 19 | inferred_complete_timeline |
| `Action_None` | 157 | 173 | 17 | inferred_complete_timeline |
| `Action_None` | 181 | 188 | 8 | inferred_complete_timeline |
| `Action_None` | 190 | 206 | 17 | inferred_complete_timeline |
| `Action_None` | 220 | 223 | 4 | inferred_complete_timeline |
| `Action_None` | 226 | 230 | 5 | inferred_complete_timeline |
| `Action_None` | 232 | 272 | 41 | inferred_complete_timeline |
| `Action_None` | 294 | 539 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–377
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 271 | 254 | inferred_complete_timeline |
| `Action_None` | 283 | 346 | 64 | inferred_complete_timeline |
| `Action_None` | 352 | 377 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 70 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 115 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 189 | 71 | inferred_complete_timeline |
| `Action_CatchKick` | 190 | 193 | 4 | inferred_complete_timeline |
| `Action_CatchKick` | 195 | 195 | 1 | inferred_complete_timeline |
| `Action_None` | 196 | 209 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 210 | 282 | 73 | inferred_complete_timeline |
| `Action_BallCarry` | 288 | 306 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 308 | 321 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 323 | 327 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 331 | 333 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 461

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 142 | 125 | inferred_complete_timeline |
| `Action_None` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 168 | 12 | inferred_complete_timeline |
| `Action_None` | 172 | 195 | 24 | inferred_complete_timeline |
| `Action_None` | 197 | 201 | 5 | inferred_complete_timeline |
| `Action_None` | 204 | 230 | 27 | inferred_complete_timeline |
| `Action_None` | 232 | 422 | 191 | inferred_complete_timeline |
| `Action_None` | 424 | 435 | 12 | inferred_complete_timeline |
| `Action_None` | 440 | 445 | 6 | inferred_complete_timeline |
| `Action_None` | 448 | 449 | 2 | inferred_complete_timeline |
| `Action_None` | 455 | 459 | 5 | inferred_complete_timeline |
| `Action_None` | 464 | 468 | 5 | inferred_complete_timeline |
| `Action_None` | 473 | 474 | 2 | inferred_complete_timeline |
| `Action_None` | 500 | 501 | 2 | inferred_complete_timeline |
| `Action_None` | 511 | 514 | 4 | inferred_complete_timeline |
| `Action_None` | 520 | 522 | 3 | inferred_complete_timeline |
| `Action_None` | 524 | 532 | 9 | inferred_complete_timeline |
| `Action_None` | 537 | 539 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 151 | 134 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 167 | 11 | inferred_complete_timeline |
| `Action_None` | 170 | 278 | 109 | inferred_complete_timeline |
| `Action_None` | 280 | 375 | 96 | inferred_complete_timeline |
| `Action_None` | 385 | 539 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 15 | 4 | inferred_complete_timeline |
| `Action_None` | 25 | 208 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–538
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 171 | 154 | inferred_complete_timeline |
| `Action_None` | 174 | 210 | 37 | inferred_complete_timeline |
| `Action_None` | 217 | 538 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 294 | 277 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker5 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 514

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 137 | 120 | inferred_complete_timeline |
| `Action_None` | 139 | 398 | 260 | inferred_complete_timeline |
| `Action_None` | 404 | 406 | 3 | inferred_complete_timeline |
| `Action_None` | 419 | 422 | 4 | inferred_complete_timeline |
| `Action_None` | 424 | 428 | 5 | inferred_complete_timeline |
| `Action_None` | 432 | 436 | 5 | inferred_complete_timeline |
| `Action_None` | 438 | 449 | 12 | inferred_complete_timeline |
| `Action_None` | 453 | 539 | 87 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 96–99 | 4 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 122–187 | 22 | 5 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 126–130 | 5 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 231–249 | 19 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 256–539 | 250 | 9 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 286–370 | 79 | 4 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 306–329 | 22 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 310–539 | 229 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 315–539 | 222 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 321–539 | 165 | 12 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 321–539 | 202 | 8 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 331–389 | 55 | 3 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 336–539 | 188 | 4 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 352–539 | 179 | 6 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 366–370 | 5 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 371–539 | 143 | 7 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 371–380 | 8 | 2 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 372–385 | 10 | 2 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 373–380 | 7 | 2 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 373–383 | 5 | 2 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 373–374 | 2 | 1 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 373–380 | 5 | 2 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 373–374 | 2 | 1 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 386–387 | 2 | 1 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 393–531 | 74 | 14 | Undefined position; Undefined team |
| `47` | `64` | Position_Unknown | Team_Unknown | 410–411 | 2 | 1 | Undefined position; Undefined team |
| `48` | `66` | Position_Unknown | Team_Unknown | 414–415 | 2 | 1 | Undefined position; Undefined team |
| `49` | `67` | Position_Unknown | Team_Unknown | 418–459 | 31 | 3 | Undefined position; Undefined team |
| `50` | `68` | Position_Unknown | Team_Unknown | 421–500 | 64 | 3 | Undefined position; Undefined team |
| `51` | `69` | Position_Unknown | Team_Unknown | 423–433 | 11 | 1 | Undefined position; Undefined team |
| `52` | `70` | Position_Unknown | Team_Unknown | 425–473 | 8 | 2 | Undefined position; Undefined team |
| `53` | `74` | Position_Unknown | Team_Unknown | 439–539 | 99 | 2 | Undefined position; Undefined team |
| `54` | `78` | Position_Unknown | Team_Unknown | 456–474 | 14 | 4 | Undefined position; Undefined team |
| `55` | `79` | Position_Unknown | Team_Unknown | 456–494 | 28 | 5 | Undefined position; Undefined team |
| `56` | `80` | Position_Unknown | Team_Unknown | 462–539 | 63 | 4 | Undefined position; Undefined team |
| `57` | `81` | Position_Unknown | Team_Unknown | 469–477 | 9 | 1 | Undefined position; Undefined team |
| `58` | `82` | Position_Unknown | Team_Unknown | 470–477 | 7 | 2 | Undefined position; Undefined team |
| `59` | `83` | Position_Unknown | Team_Unknown | 470–477 | 8 | 1 | Undefined position; Undefined team |
| `60` | `84` | Position_Unknown | Team_Unknown | 470–474 | 5 | 1 | Undefined position; Undefined team |
| `61` | `86` | Position_Unknown | Team_Unknown | 474–475 | 2 | 1 | Undefined position; Undefined team |
| `62` | `97` | Position_Unknown | Team_Unknown | 518–539 | 20 | 2 | Undefined position; Undefined team |
| `63` | `98` | Position_Unknown | Team_Unknown | 521–526 | 5 | 2 | Undefined position; Undefined team |
| `64` | `99` | Position_Unknown | Team_Unknown | 539–539 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CatchKick` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (5 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `21` (Kick_Returner1)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Second_Level_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ 43 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 43 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 86 |
| Missing visible bounding boxes during action | 235 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '21' has invalid range: start=540, end=333. Clamping end to start.
- ⚠️ Action 'Action_None' range [18-151] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-167] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-278] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-375] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-294] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-146] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-173] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-357] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-392] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-400] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-422] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-430] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-538] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-271] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-346] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-377] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-296] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-314] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-357] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-178] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-390] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-408] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-416] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-436] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-147] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-264] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-287] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-306] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-173] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-261] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-539] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-141] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-305] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-538] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-284] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-320] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-198] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-154] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-188] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-206] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-272] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-539] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [18-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [85-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-409] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-416] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-203] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-268] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-286] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-137] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-398] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-406] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-422] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-428] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-436] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-449] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-142] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-168] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-195] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-230] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-422] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-435] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-445] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-459] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-468] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-514] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-522] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-532] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-15] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-208] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-91] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-320] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchKick' range [190-193] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-209] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [210-282] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [288-306] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [308-321] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [323-327] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [331-333] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-137] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-249] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-422] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-434] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-437] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-443] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-512] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-531] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-359] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-364] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-370] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-325] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-368] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-539] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-362] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-434] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-382] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-404] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-410] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-419] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-435] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-440] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-444] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-476] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-494] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-539] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-362] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-403] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-480] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-488] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-506] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-527] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-536] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-355] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-384] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-339] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-357] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-368] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-401] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-413] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-452] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-482] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-506] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-370] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-380] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-390] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-413] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-422] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-430] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-374] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-380] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-375] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-385] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-375] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-380] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-375] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-411] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-430] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-445] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-461] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-466] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-471] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-487] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-501] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-506] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-520] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-526] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-531] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-420] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-442] for track '49' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-459] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-440] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-445] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-500] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-433] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-428] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-473] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-511] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-539] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-459] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-462] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-466] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-474] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-461] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-472] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-485] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-488] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-494] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-479] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-497] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-539] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-477] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-474] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-477] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-474] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-535] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-523] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-526] for track '63' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 540. Video range is [0, 539].

</details>