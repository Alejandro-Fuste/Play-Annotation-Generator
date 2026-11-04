# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_30

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_30`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 220
- **Validation Warnings:** 239
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 202
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `6` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | defense | `19` | `19` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `10` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `11` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `12` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `13` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `14` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `15` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `16` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `18` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `6` | `Group` | 0 | START | 0 | 41 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `15` | `15` | 42 | START | 42 | 84 |
| ✅ EXACT | `Action_KickBall` | Kicker | `15` | `15` | 88 | START | 88 | 93 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `19` | `19` | 192 | START | 192 | 205 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | `19` | `19` | 218 | START | 218 | 277 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | `19` | `19` | 555 | START | 555 | 569 |

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
- **Visible Frames:** 0–372
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_KickApproach` | 42 | 84 | 43 | inferred_complete_timeline |
| `Action_KickBall` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_None` | 94 | 164 | 71 | inferred_complete_timeline |
| `Action_None` | 166 | 173 | 8 | inferred_complete_timeline |
| `Action_None` | 178 | 198 | 21 | inferred_complete_timeline |
| `Action_None` | 201 | 372 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 34 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_None` | 42 | 48 | 7 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 85 | 5 | inferred_complete_timeline |
| `Action_None` | 87 | 259 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 166 | 125 | inferred_complete_timeline |
| `Action_None` | 168 | 199 | 32 | inferred_complete_timeline |
| `Action_None` | 204 | 235 | 32 | inferred_complete_timeline |
| `Action_None` | 243 | 258 | 16 | inferred_complete_timeline |
| `Action_None` | 265 | 276 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 467

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_None` | 42 | 46 | 5 | inferred_complete_timeline |
| `Action_None` | 48 | 52 | 5 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |
| `Action_None` | 272 | 509 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 177 | 136 | inferred_complete_timeline |
| `Action_None` | 179 | 187 | 9 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 512

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 43 | 56 | 14 | inferred_complete_timeline |
| `Action_None` | 60 | 83 | 24 | inferred_complete_timeline |
| `Action_None` | 87 | 89 | 3 | inferred_complete_timeline |
| `Action_None` | 92 | 172 | 81 | inferred_complete_timeline |
| `Action_None` | 177 | 190 | 14 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_None` | 200 | 242 | 43 | inferred_complete_timeline |
| `Action_None` | 244 | 288 | 45 | inferred_complete_timeline |
| `Action_None` | 292 | 328 | 37 | inferred_complete_timeline |
| `Action_None` | 330 | 331 | 2 | inferred_complete_timeline |
| `Action_None` | 335 | 456 | 122 | inferred_complete_timeline |
| `Action_None` | 481 | 569 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 60 | 19 | inferred_complete_timeline |
| `Action_None` | 68 | 184 | 117 | inferred_complete_timeline |
| `Action_None` | 187 | 569 | 383 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_None` | 42 | 52 | 11 | inferred_complete_timeline |
| `Action_None` | 58 | 184 | 127 | inferred_complete_timeline |
| `Action_None` | 187 | 569 | 383 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 165 | 124 | inferred_complete_timeline |
| `Action_None` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_None` | 173 | 181 | 9 | inferred_complete_timeline |
| `Action_None` | 187 | 235 | 49 | inferred_complete_timeline |
| `Action_None` | 237 | 439 | 203 | inferred_complete_timeline |
| `Action_None` | 453 | 506 | 54 | inferred_complete_timeline |
| `Action_None` | 521 | 569 | 49 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 530

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 241 | 200 | inferred_complete_timeline |
| `Action_None` | 244 | 245 | 2 | inferred_complete_timeline |
| `Action_None` | 258 | 263 | 6 | inferred_complete_timeline |
| `Action_None` | 271 | 294 | 24 | inferred_complete_timeline |
| `Action_None` | 298 | 359 | 62 | inferred_complete_timeline |
| `Action_None` | 361 | 373 | 13 | inferred_complete_timeline |
| `Action_None` | 378 | 399 | 22 | inferred_complete_timeline |
| `Action_None` | 403 | 439 | 37 | inferred_complete_timeline |
| `Action_None` | 441 | 479 | 39 | inferred_complete_timeline |
| `Action_None` | 483 | 506 | 24 | inferred_complete_timeline |
| `Action_None` | 510 | 517 | 8 | inferred_complete_timeline |
| `Action_None` | 519 | 569 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 359 | 318 | inferred_complete_timeline |
| `Action_None` | 361 | 569 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 163 | 122 | inferred_complete_timeline |
| `Action_None` | 167 | 217 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 103 | 62 | inferred_complete_timeline |
| `Action_None` | 105 | 117 | 13 | inferred_complete_timeline |
| `Action_None` | 143 | 151 | 9 | inferred_complete_timeline |
| `Action_None` | 168 | 197 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–334
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 124 | 83 | inferred_complete_timeline |
| `Action_None` | 127 | 211 | 85 | inferred_complete_timeline |
| `Action_None` | 219 | 226 | 8 | inferred_complete_timeline |
| `Action_None` | 229 | 295 | 67 | inferred_complete_timeline |
| `Action_None` | 332 | 334 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–314
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 124 | 83 | inferred_complete_timeline |
| `Action_None` | 127 | 259 | 133 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_None` | 313 | 314 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 38 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 88 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 113 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 191 | 72 | inferred_complete_timeline |
| `Action_CatchKick` | 192 | 205 | 14 | inferred_complete_timeline |
| `Action_None` | 206 | 217 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 218 | 277 | 60 | inferred_complete_timeline |
| `Action_BallCarry` | 279 | 295 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 301 | 396 | 96 | inferred_complete_timeline |
| `Action_BallCarry` | 401 | 412 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 417 | 439 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 441 | 453 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 464 | 486 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 490 | 495 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 500 | 554 | 55 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 555 | 569 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 41 | 30 | inferred_complete_timeline |
| `Action_None` | 42 | 66 | 25 | inferred_complete_timeline |
| `Action_None` | 74 | 87 | 14 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 95 | 113 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 178 | 137 | inferred_complete_timeline |
| `Action_None` | 184 | 200 | 17 | inferred_complete_timeline |
| `Action_None` | 207 | 276 | 70 | inferred_complete_timeline |
| `Action_None` | 282 | 302 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 144 | 103 | inferred_complete_timeline |
| `Action_None` | 147 | 179 | 33 | inferred_complete_timeline |
| `Action_None` | 187 | 263 | 77 | inferred_complete_timeline |
| `Action_None` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_None` | 272 | 273 | 2 | inferred_complete_timeline |
| `Action_None` | 292 | 569 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–551
- **Visible Samples:** 512

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 109 | 68 | inferred_complete_timeline |
| `Action_None` | 121 | 135 | 15 | inferred_complete_timeline |
| `Action_None` | 144 | 213 | 70 | inferred_complete_timeline |
| `Action_None` | 215 | 221 | 7 | inferred_complete_timeline |
| `Action_None` | 224 | 351 | 128 | inferred_complete_timeline |
| `Action_None` | 365 | 477 | 113 | inferred_complete_timeline |
| `Action_None` | 479 | 482 | 4 | inferred_complete_timeline |
| `Action_None` | 487 | 551 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 33–569 | 456 | 15 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 35–239 | 51 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 71–228 | 156 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 74–101 | 11 | 3 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 121–124 | 4 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 130–569 | 434 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 195–201 | 6 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 217–352 | 136 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 226–380 | 144 | 5 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 280–555 | 242 | 7 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 281–567 | 259 | 5 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 289–569 | 274 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 293–391 | 84 | 5 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 294–295 | 2 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 313–501 | 179 | 7 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 313–569 | 243 | 3 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 373–569 | 197 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 397–421 | 24 | 2 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 399–569 | 165 | 3 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 406–411 | 6 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 431–446 | 16 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 434–569 | 136 | 1 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 492–569 | 73 | 3 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 562–569 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (9 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 190 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action 'Action_None' range [42-124] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-259] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-178] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-276] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-302] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-144] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-179] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-263] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-569] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-241] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-263] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-294] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-373] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-399] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-439] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-479] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-506] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-517] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-359] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-569] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-163] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-217] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-181] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-235] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-439] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-506] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-41] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-66] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-87] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-113] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-124] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-211] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-226] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-295] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-334] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-213] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-351] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-477] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-482] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-551] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-187] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-52] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-184] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-60] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-184] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-166] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-235] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-258] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-276] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-52] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-239] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-509] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [42-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-164] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-372] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-83] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-190] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-242] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-288] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-328] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-456] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-117] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-151] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-197] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-34] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 42, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [42-48] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-259] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-38] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-88] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [218-277] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [279-295] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [301-396] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [401-412] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [417-439] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [441-453] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [464-486] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [490-495] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-34] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-257] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-349] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-362] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-527] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-537] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-546] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-41] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-221] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-101] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-165] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-179] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-390] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-352] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-237] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-355] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-364] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-370] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-380] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-362] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-420] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-434] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-477] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-481] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-521] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-555] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-303] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-377] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-429] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-466] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-567] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-458] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-569] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-298] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-364] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-379] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-391] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-328] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-340] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-377] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-385] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-398] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-501] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-319] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-569] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-418] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-421] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-473] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-479] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-569] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-411] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-446] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-501] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-506] for track '42' has 1 frames without a visible bounding box.
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