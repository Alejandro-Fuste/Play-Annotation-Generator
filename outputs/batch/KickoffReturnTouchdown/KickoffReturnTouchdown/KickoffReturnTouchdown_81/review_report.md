# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_81

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_81`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 63
- **Ball Tracks:** 0
- **Action Segments:** 233
- **Validation Warnings:** 271
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 217
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `3` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `19` | `19` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `19` | `19` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner | defense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner | defense | `5` | `5` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner | defense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `10` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `11` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `13` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `15` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `16` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `17` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `18` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `19` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `20` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `21` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `3` | `Group` | 0 | START | 0 | 25 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `19` | `19` | 26 | START | 26 | 69 |
| ✅ EXACT | `Action_KickBall` | Kicker | `19` | `19` | 70 | START | 70 | 74 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner | `5` | `5` | 181 | START | 181 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner | `5` | `5` | 199 | START | 199 | 264 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner | `5` | `5` | 568 | START | 568 | 569 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_KickApproach` | 26 | 69 | 44 | inferred_complete_timeline |
| `Action_KickBall` | 70 | 74 | 5 | inferred_complete_timeline |
| `Action_None` | 75 | 179 | 105 | inferred_complete_timeline |
| `Action_None` | 182 | 458 | 277 | inferred_complete_timeline |
| `Action_None` | 462 | 464 | 3 | inferred_complete_timeline |
| `Action_None` | 467 | 569 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 449 | 424 | inferred_complete_timeline |
| `Action_None` | 451 | 455 | 5 | inferred_complete_timeline |
| `Action_None` | 458 | 535 | 78 | inferred_complete_timeline |
| `Action_None` | 542 | 569 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 207 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–357
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 303 | 278 | inferred_complete_timeline |
| `Action_None` | 313 | 314 | 2 | inferred_complete_timeline |
| `Action_None` | 316 | 318 | 3 | inferred_complete_timeline |
| `Action_None` | 335 | 336 | 2 | inferred_complete_timeline |
| `Action_None` | 338 | 339 | 2 | inferred_complete_timeline |
| `Action_None` | 341 | 342 | 2 | inferred_complete_timeline |
| `Action_None` | 344 | 347 | 4 | inferred_complete_timeline |
| `Action_None` | 351 | 352 | 2 | inferred_complete_timeline |
| `Action_None` | 356 | 357 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 556

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 248 | 223 | inferred_complete_timeline |
| `Action_None` | 252 | 280 | 29 | inferred_complete_timeline |
| `Action_None` | 292 | 569 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 519

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 55 | 30 | inferred_complete_timeline |
| `Action_None` | 57 | 245 | 189 | inferred_complete_timeline |
| `Action_None` | 262 | 267 | 6 | inferred_complete_timeline |
| `Action_None` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_None` | 284 | 291 | 8 | inferred_complete_timeline |
| `Action_None` | 302 | 303 | 2 | inferred_complete_timeline |
| `Action_None` | 308 | 315 | 8 | inferred_complete_timeline |
| `Action_None` | 318 | 344 | 27 | inferred_complete_timeline |
| `Action_None` | 347 | 354 | 8 | inferred_complete_timeline |
| `Action_None` | 357 | 569 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 53 | 28 | inferred_complete_timeline |
| `Action_None` | 55 | 62 | 8 | inferred_complete_timeline |
| `Action_None` | 67 | 74 | 8 | inferred_complete_timeline |
| `Action_None` | 77 | 308 | 232 | inferred_complete_timeline |
| `Action_None` | 310 | 312 | 3 | inferred_complete_timeline |
| `Action_None` | 314 | 347 | 34 | inferred_complete_timeline |
| `Action_None` | 351 | 352 | 2 | inferred_complete_timeline |
| `Action_None` | 354 | 355 | 2 | inferred_complete_timeline |
| `Action_None` | 357 | 473 | 117 | inferred_complete_timeline |
| `Action_None` | 476 | 569 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 44 | 19 | inferred_complete_timeline |
| `Action_None` | 57 | 62 | 6 | inferred_complete_timeline |
| `Action_None` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_None` | 74 | 233 | 160 | inferred_complete_timeline |
| `Action_None` | 237 | 238 | 2 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 264 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 223 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 569 | 544 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 547

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 72 | 47 | inferred_complete_timeline |
| `Action_None` | 77 | 89 | 13 | inferred_complete_timeline |
| `Action_None` | 92 | 301 | 210 | inferred_complete_timeline |
| `Action_None` | 304 | 310 | 7 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 325 | 383 | 59 | inferred_complete_timeline |
| `Action_None` | 387 | 569 | 183 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 557

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 184 | 159 | inferred_complete_timeline |
| `Action_None` | 186 | 193 | 8 | inferred_complete_timeline |
| `Action_None` | 200 | 297 | 98 | inferred_complete_timeline |
| `Action_None` | 302 | 375 | 74 | inferred_complete_timeline |
| `Action_None` | 378 | 569 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 172 | 147 | inferred_complete_timeline |
| `Action_None` | 175 | 207 | 33 | inferred_complete_timeline |
| `Action_None` | 212 | 294 | 83 | inferred_complete_timeline |
| `Action_None` | 296 | 569 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 129 | 104 | inferred_complete_timeline |
| `Action_None` | 132 | 137 | 6 | inferred_complete_timeline |
| `Action_None` | 139 | 263 | 125 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_None` | 357 | 569 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 91 | 66 | inferred_complete_timeline |
| `Action_None` | 95 | 229 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 507

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 99 | 74 | inferred_complete_timeline |
| `Action_None` | 101 | 117 | 17 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 125 | 189 | 65 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 278 | 29 | inferred_complete_timeline |
| `Action_None` | 280 | 569 | 290 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 220 | 195 | inferred_complete_timeline |
| `Action_None` | 222 | 280 | 59 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_None` | 291 | 295 | 5 | inferred_complete_timeline |
| `Action_None` | 297 | 569 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 566

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 180 | 54 | inferred_complete_timeline |
| `Action_CatchKick` | 181 | 187 | 7 | inferred_complete_timeline |
| `Action_None` | 188 | 198 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 199 | 264 | 66 | inferred_complete_timeline |
| `Action_BallCarry` | 268 | 567 | 300 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 568 | 569 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 227 | 202 | inferred_complete_timeline |
| `Action_None` | 233 | 295 | 63 | inferred_complete_timeline |
| `Action_None` | 298 | 311 | 14 | inferred_complete_timeline |
| `Action_None` | 313 | 411 | 99 | inferred_complete_timeline |
| `Action_None` | 416 | 488 | 73 | inferred_complete_timeline |
| `Action_None` | 492 | 493 | 2 | inferred_complete_timeline |
| `Action_None` | 501 | 504 | 4 | inferred_complete_timeline |
| `Action_None` | 506 | 509 | 4 | inferred_complete_timeline |
| `Action_None` | 519 | 569 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 260 | 235 | inferred_complete_timeline |
| `Action_None` | 262 | 269 | 8 | inferred_complete_timeline |
| `Action_None` | 271 | 281 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 251 | 226 | inferred_complete_timeline |
| `Action_None` | 253 | 293 | 41 | inferred_complete_timeline |
| `Action_None` | 295 | 512 | 218 | inferred_complete_timeline |
| `Action_None` | 514 | 569 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 252 | 227 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 3–88 | 86 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 108–114 | 7 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 116–120 | 5 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 128–182 | 33 | 6 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 134–181 | 11 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 159–196 | 23 | 4 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 160–161 | 2 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 160–180 | 14 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 166–180 | 13 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 170–172 | 3 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 201–569 | 357 | 6 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 236–291 | 56 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 258–272 | 15 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 269–326 | 58 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 271–302 | 30 | 3 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 272–569 | 262 | 5 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 286–342 | 38 | 2 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 308–569 | 244 | 2 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 311–569 | 259 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 319–569 | 241 | 5 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 326–569 | 244 | 1 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 342–362 | 10 | 2 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 362–569 | 179 | 6 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 364–386 | 15 | 4 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 366–373 | 8 | 1 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 369–371 | 3 | 1 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 376–387 | 12 | 1 | Undefined position; Undefined team |
| `49` | `73` | Position_Unknown | Team_Unknown | 384–388 | 5 | 1 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 384–392 | 5 | 2 | Undefined position; Undefined team |
| `51` | `75` | Position_Unknown | Team_Unknown | 407–412 | 6 | 1 | Undefined position; Undefined team |
| `52` | `76` | Position_Unknown | Team_Unknown | 435–439 | 4 | 2 | Undefined position; Undefined team |
| `53` | `78` | Position_Unknown | Team_Unknown | 472–519 | 41 | 3 | Undefined position; Undefined team |
| `54` | `79` | Position_Unknown | Team_Unknown | 473–552 | 40 | 4 | Undefined position; Undefined team |
| `55` | `80` | Position_Unknown | Team_Unknown | 473–493 | 19 | 2 | Undefined position; Undefined team |
| `56` | `81` | Position_Unknown | Team_Unknown | 484–567 | 75 | 3 | Undefined position; Undefined team |
| `57` | `83` | Position_Unknown | Team_Unknown | 489–569 | 52 | 6 | Undefined position; Undefined team |
| `58` | `88` | Position_Unknown | Team_Unknown | 527–535 | 8 | 2 | Undefined position; Undefined team |
| `59` | `90` | Position_Unknown | Team_Unknown | 534–551 | 18 | 1 | Undefined position; Undefined team |
| `60` | `92` | Position_Unknown | Team_Unknown | 539–569 | 9 | 3 | Undefined position; Undefined team |
| `61` | `93` | Position_Unknown | Team_Unknown | 550–569 | 14 | 2 | Undefined position; Undefined team |
| `62` | `94` | Position_Unknown | Team_Unknown | 558–567 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ 41 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 41 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 82 |
| Missing visible bounding boxes during action | 188 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action 'Action_None' range [26-251] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-293] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-512] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-569] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-172] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-207] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-294] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-227] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-295] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-311] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-411] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-488] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-493] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-504] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-509] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-72] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-89] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-301] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-310] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-383] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-220] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-280] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-295] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [199-264] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-252] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-260] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-281] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-99] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-117] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-189] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-278] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-129] for track '9' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-137] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-263] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-569] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-53] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-62] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-308] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-347] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-473] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-569] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-303] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-347] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-184] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-193] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-297] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-375] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-207] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-91] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-229] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-223] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-248] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-280] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-449] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-455] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-535] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-458] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-464] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-569] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-245] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-291] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-315] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-344] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-354] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-569] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-44] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-62] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-233] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-264] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-139] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-152] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-173] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-181] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-175] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-275] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-290] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-327] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-331] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-569] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-291] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-272] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-326] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-291] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-302] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-291] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-317] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-569] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-342] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-333] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-446] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-532] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-345] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-362] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-436] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-451] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-467] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-535] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-366] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-374] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-378] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-373] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-371] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-387] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-388] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-386] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-412] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-474] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-478] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-519] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-494] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-511] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-521] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-552] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-489] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-493] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-495] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-523] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-567] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-498] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-519] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-543] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-548] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-532] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-535] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-551] for track '59' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-543] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-549] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-569] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-552] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-567] for track '62' has 1 frames without a visible bounding box.
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

</details>