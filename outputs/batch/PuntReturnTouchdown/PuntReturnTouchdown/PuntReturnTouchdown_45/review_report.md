# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_45

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_45`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 100
- **Ball Tracks:** 0
- **Action Segments:** 396
- **Validation Warnings:** 528
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 381
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `0` | `0` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `0` | `0` |
| ❌ MISSING SEGMENT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `29` | `26` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `28` | `25` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `54` | `45` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `0` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `10` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `12` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `14` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `17` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `18` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `19` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `3` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `6` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `7` | `Group` | 0 | START | 0 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `12` | `12` | 60 | START | 60 | 76 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `0` | `0` | 84 | END | 84 | 84 |
| ✅ EXACT | `Action_PuntBall` | Punter | `0` | `0` | 111 | START | 111 | 119 |
| ❌ MISSING SEGMENT | `Action_CatchPunt` | Position_Unknown | `29` | `26` | 202 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `28` | `25` | 226 | START | N/A | N/A |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `54` | `45` | 512 | START | 512 | 518 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–538
- **Visible Samples:** 523

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 81 | 22 | inferred_complete_timeline |
| `Action_None` | 89 | 131 | 43 | inferred_complete_timeline |
| `Action_None` | 135 | 287 | 153 | inferred_complete_timeline |
| `Action_None` | 289 | 329 | 41 | inferred_complete_timeline |
| `Action_None` | 331 | 337 | 7 | inferred_complete_timeline |
| `Action_None` | 340 | 481 | 142 | inferred_complete_timeline |
| `Action_None` | 484 | 538 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_None` | 78 | 85 | 8 | inferred_complete_timeline |
| `Action_None` | 88 | 131 | 44 | inferred_complete_timeline |
| `Action_None` | 135 | 155 | 21 | inferred_complete_timeline |
| `Action_None` | 157 | 167 | 11 | inferred_complete_timeline |
| `Action_None` | 169 | 197 | 29 | inferred_complete_timeline |
| `Action_None` | 201 | 206 | 6 | inferred_complete_timeline |
| `Action_None` | 208 | 223 | 16 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 98 | 39 | inferred_complete_timeline |
| `Action_None` | 102 | 172 | 71 | inferred_complete_timeline |
| `Action_None` | 174 | 178 | 5 | inferred_complete_timeline |
| `Action_None` | 181 | 193 | 13 | inferred_complete_timeline |
| `Action_None` | 195 | 201 | 7 | inferred_complete_timeline |
| `Action_None` | 203 | 236 | 34 | inferred_complete_timeline |
| `Action_None` | 239 | 252 | 14 | inferred_complete_timeline |
| `Action_None` | 254 | 286 | 33 | inferred_complete_timeline |
| `Action_None` | 288 | 295 | 8 | inferred_complete_timeline |
| `Action_None` | 300 | 306 | 7 | inferred_complete_timeline |
| `Action_None` | 308 | 309 | 2 | inferred_complete_timeline |
| `Action_None` | 315 | 324 | 10 | inferred_complete_timeline |
| `Action_None` | 327 | 328 | 2 | inferred_complete_timeline |
| `Action_None` | 343 | 344 | 2 | inferred_complete_timeline |
| `Action_None` | 350 | 354 | 5 | inferred_complete_timeline |
| `Action_None` | 359 | 361 | 3 | inferred_complete_timeline |
| `Action_None` | 367 | 375 | 9 | inferred_complete_timeline |
| `Action_None` | 395 | 401 | 7 | inferred_complete_timeline |
| `Action_None` | 409 | 417 | 9 | inferred_complete_timeline |
| `Action_None` | 427 | 434 | 8 | inferred_complete_timeline |
| `Action_None` | 438 | 440 | 3 | inferred_complete_timeline |
| `Action_None` | 447 | 539 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–332
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_LongSnap` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_LongSnap` | 78 | 81 | 4 | inferred_complete_timeline |
| `Action_LongSnap` | 83 | 110 | 28 | inferred_complete_timeline |
| `Action_None` | 111 | 129 | 19 | inferred_complete_timeline |
| `Action_None` | 135 | 164 | 30 | inferred_complete_timeline |
| `Action_None` | 166 | 222 | 57 | inferred_complete_timeline |
| `Action_None` | 230 | 240 | 11 | inferred_complete_timeline |
| `Action_None` | 259 | 272 | 14 | inferred_complete_timeline |
| `Action_None` | 296 | 332 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 287 | 228 | inferred_complete_timeline |
| `Action_None` | 291 | 292 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 132 | 73 | inferred_complete_timeline |
| `Action_None` | 135 | 140 | 6 | inferred_complete_timeline |
| `Action_None` | 142 | 147 | 6 | inferred_complete_timeline |
| `Action_None` | 150 | 167 | 18 | inferred_complete_timeline |
| `Action_None` | 169 | 242 | 74 | inferred_complete_timeline |
| `Action_None` | 244 | 289 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 157 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–477
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_SnapReceive` | 84 | 84 | 1 | inferred_complete_timeline |
| `Action_None` | 85 | 110 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 111 | 119 | 9 | inferred_complete_timeline |
| `Action_None` | 120 | 263 | 144 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_None` | 270 | 377 | 108 | inferred_complete_timeline |
| `Action_None` | 379 | 389 | 11 | inferred_complete_timeline |
| `Action_None` | 396 | 400 | 5 | inferred_complete_timeline |
| `Action_None` | 408 | 418 | 11 | inferred_complete_timeline |
| `Action_None` | 450 | 462 | 13 | inferred_complete_timeline |
| `Action_None` | 476 | 477 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 283 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 130 | 71 | inferred_complete_timeline |
| `Action_None` | 132 | 254 | 123 | inferred_complete_timeline |
| `Action_None` | 257 | 292 | 36 | inferred_complete_timeline |
| `Action_None` | 295 | 296 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 129 | 70 | inferred_complete_timeline |
| `Action_None` | 135 | 206 | 72 | inferred_complete_timeline |
| `Action_None` | 208 | 255 | 48 | inferred_complete_timeline |
| `Action_None` | 257 | 355 | 99 | inferred_complete_timeline |
| `Action_None` | 358 | 361 | 4 | inferred_complete_timeline |
| `Action_None` | 414 | 435 | 22 | inferred_complete_timeline |
| `Action_None` | 439 | 539 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_None` | 79 | 118 | 40 | inferred_complete_timeline |
| `Action_None` | 125 | 130 | 6 | inferred_complete_timeline |
| `Action_None` | 135 | 210 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_None` | 78 | 84 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |
| `Action_None` | 242 | 255 | 14 | inferred_complete_timeline |
| `Action_None` | 260 | 262 | 3 | inferred_complete_timeline |
| `Action_None` | 267 | 272 | 6 | inferred_complete_timeline |
| `Action_None` | 274 | 296 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 129 | 70 | inferred_complete_timeline |
| `Action_None` | 135 | 145 | 11 | inferred_complete_timeline |
| `Action_None` | 147 | 218 | 72 | inferred_complete_timeline |
| `Action_None` | 220 | 227 | 8 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 74 | 15 | inferred_complete_timeline |
| `Action_None` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_None` | 81 | 85 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 59 | 39 | inferred_complete_timeline |
| `Action_None` | 60 | 69 | 10 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_None` | 74 | 106 | 33 | inferred_complete_timeline |
| `Action_None` | 110 | 130 | 21 | inferred_complete_timeline |
| `Action_None` | 135 | 296 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–364
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 344 | 285 | inferred_complete_timeline |
| `Action_None` | 346 | 361 | 16 | inferred_complete_timeline |
| `Action_None` | 363 | 364 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 211 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 129 | 70 | inferred_complete_timeline |
| `Action_None` | 131 | 199 | 69 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 223 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–204 | 202 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 93–124 | 18 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 113–274 | 143 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 140–286 | 135 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 141–155 | 15 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 146–162 | 9 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 151–152 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 170–538 | 348 | 6 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 173–317 | 132 | 5 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 221–224 | 4 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 230–272 | 37 | 3 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 232–539 | 289 | 8 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 236–344 | 53 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 252–416 | 81 | 11 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 263–265 | 3 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 267–438 | 172 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 276–398 | 119 | 2 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 281–528 | 228 | 7 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 282–392 | 56 | 6 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 285–539 | 252 | 2 | Undefined position; Undefined team |
| `41` | `46` | Position_Unknown | Team_Unknown | 287–340 | 54 | 1 | Undefined position; Undefined team |
| `42` | `47` | Position_Unknown | Team_Unknown | 293–330 | 37 | 2 | Undefined position; Undefined team |
| `43` | `48` | Position_Unknown | Team_Unknown | 294–357 | 36 | 5 | Undefined position; Undefined team |
| `44` | `50` | Position_Unknown | Team_Unknown | 297–343 | 47 | 1 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 305–539 | 192 | 7 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 307–308 | 2 | 1 | Undefined position; Undefined team |
| `47` | `56` | Position_Unknown | Team_Unknown | 307–323 | 13 | 4 | Undefined position; Undefined team |
| `48` | `57` | Position_Unknown | Team_Unknown | 308–521 | 173 | 11 | Undefined position; Undefined team |
| `49` | `60` | Position_Unknown | Team_Unknown | 313–314 | 2 | 1 | Undefined position; Undefined team |
| `50` | `61` | Position_Unknown | Team_Unknown | 315–317 | 3 | 1 | Undefined position; Undefined team |
| `51` | `62` | Position_Unknown | Team_Unknown | 318–321 | 4 | 1 | Undefined position; Undefined team |
| `52` | `63` | Position_Unknown | Team_Unknown | 325–539 | 207 | 4 | Undefined position; Undefined team |
| `53` | `64` | Position_Unknown | Team_Unknown | 327–336 | 6 | 2 | Undefined position; Undefined team |
| `54` | `66` | Position_Unknown | Team_Unknown | 344–539 | 184 | 5 | Undefined position; Undefined team |
| `55` | `67` | Position_Unknown | Team_Unknown | 345–539 | 176 | 8 | Undefined position; Undefined team |
| `56` | `71` | Position_Unknown | Team_Unknown | 356–528 | 162 | 5 | Undefined position; Undefined team |
| `57` | `72` | Position_Unknown | Team_Unknown | 380–503 | 74 | 8 | Undefined position; Undefined team |
| `58` | `73` | Position_Unknown | Team_Unknown | 380–531 | 138 | 7 | Undefined position; Undefined team |
| `59` | `74` | Position_Unknown | Team_Unknown | 382–455 | 53 | 5 | Undefined position; Undefined team |
| `60` | `75` | Position_Unknown | Team_Unknown | 387–388 | 2 | 1 | Undefined position; Undefined team |
| `61` | `78` | Position_Unknown | Team_Unknown | 389–464 | 71 | 2 | Undefined position; Undefined team |
| `62` | `79` | Position_Unknown | Team_Unknown | 397–456 | 56 | 4 | Undefined position; Undefined team |
| `63` | `80` | Position_Unknown | Team_Unknown | 398–527 | 71 | 7 | Undefined position; Undefined team |
| `64` | `81` | Position_Unknown | Team_Unknown | 398–521 | 36 | 5 | Undefined position; Undefined team |
| `65` | `83` | Position_Unknown | Team_Unknown | 400–409 | 10 | 1 | Undefined position; Undefined team |
| `66` | `84` | Position_Unknown | Team_Unknown | 404–466 | 52 | 3 | Undefined position; Undefined team |
| `67` | `88` | Position_Unknown | Team_Unknown | 421–455 | 7 | 3 | Undefined position; Undefined team |
| `68` | `89` | Position_Unknown | Team_Unknown | 423–539 | 111 | 4 | Undefined position; Undefined team |
| `69` | `90` | Position_Unknown | Team_Unknown | 424–523 | 99 | 2 | Undefined position; Undefined team |
| `70` | `91` | Position_Unknown | Team_Unknown | 430–434 | 5 | 1 | Undefined position; Undefined team |
| `71` | `93` | Position_Unknown | Team_Unknown | 433–519 | 72 | 9 | Undefined position; Undefined team |
| `72` | `95` | Position_Unknown | Team_Unknown | 438–495 | 54 | 2 | Undefined position; Undefined team |
| `73` | `101` | Position_Unknown | Team_Unknown | 446–452 | 7 | 1 | Undefined position; Undefined team |
| `74` | `102` | Position_Unknown | Team_Unknown | 446–539 | 94 | 1 | Undefined position; Undefined team |
| `75` | `103` | Position_Unknown | Team_Unknown | 446–518 | 41 | 4 | Undefined position; Undefined team |
| `76` | `106` | Position_Unknown | Team_Unknown | 450–539 | 58 | 7 | Undefined position; Undefined team |
| `77` | `108` | Position_Unknown | Team_Unknown | 452–530 | 54 | 4 | Undefined position; Undefined team |
| `78` | `109` | Position_Unknown | Team_Unknown | 453–510 | 11 | 4 | Undefined position; Undefined team |
| `79` | `110` | Position_Unknown | Team_Unknown | 454–536 | 82 | 2 | Undefined position; Undefined team |
| `80` | `112` | Position_Unknown | Team_Unknown | 458–504 | 15 | 3 | Undefined position; Undefined team |
| `81` | `113` | Position_Unknown | Team_Unknown | 458–459 | 2 | 1 | Undefined position; Undefined team |
| `82` | `114` | Position_Unknown | Team_Unknown | 463–526 | 24 | 4 | Undefined position; Undefined team |
| `83` | `119` | Position_Unknown | Team_Unknown | 468–495 | 13 | 3 | Undefined position; Undefined team |
| `84` | `121` | Position_Unknown | Team_Unknown | 469–470 | 2 | 1 | Undefined position; Undefined team |
| `85` | `122` | Position_Unknown | Team_Unknown | 469–521 | 16 | 3 | Undefined position; Undefined team |
| `86` | `124` | Position_Unknown | Team_Unknown | 469–515 | 19 | 2 | Undefined position; Undefined team |
| `87` | `125` | Position_Unknown | Team_Unknown | 469–470 | 2 | 1 | Undefined position; Undefined team |
| `88` | `127` | Position_Unknown | Team_Unknown | 471–539 | 66 | 2 | Undefined position; Undefined team |
| `89` | `129` | Position_Unknown | Team_Unknown | 495–539 | 37 | 4 | Undefined position; Undefined team |
| `90` | `133` | Position_Unknown | Team_Unknown | 498–539 | 37 | 6 | Undefined position; Undefined team |
| `91` | `134` | Position_Unknown | Team_Unknown | 500–539 | 33 | 2 | Undefined position; Undefined team |
| `92` | `135` | Position_Unknown | Team_Unknown | 502–524 | 18 | 3 | Undefined position; Undefined team |
| `93` | `136` | Position_Unknown | Team_Unknown | 502–520 | 4 | 2 | Undefined position; Undefined team |
| `94` | `138` | Position_Unknown | Team_Unknown | 503–504 | 2 | 1 | Undefined position; Undefined team |
| `95` | `140` | Position_Unknown | Team_Unknown | 506–531 | 23 | 3 | Undefined position; Undefined team |
| `96` | `142` | Position_Unknown | Team_Unknown | 508–513 | 6 | 1 | Undefined position; Undefined team |
| `97` | `146` | Position_Unknown | Team_Unknown | 511–539 | 29 | 1 | Undefined position; Undefined team |
| `98` | `150` | Position_Unknown | Team_Unknown | 521–522 | 2 | 1 | Undefined position; Undefined team |
| `99` | `155` | Position_Unknown | Team_Unknown | 537–539 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `12` (3 segments found)
- ❌ Missing segment for action `Action_CatchPunt` on target `29` (Position_Unknown)
- ❌ Missing segment for action `Action_BallCarry` on target `25` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 80 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 80 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 160 |
| Missing visible bounding boxes during action | 362 |
| Track-related warning | 3 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 92: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_BallCarry' for track '25' has invalid range: start=226, end=162. Clamping end to start.
- ⚠️ Segment 'Action_CatchPunt' for track '26' has invalid range: start=202, end=152. Clamping end to start.
- ⚠️ Action 'Action_None' range [120-263] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-377] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-389] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-400] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-418] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-462] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-199] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-223] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-239] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-255] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-272] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-296] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-130] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-254] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-292] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-344] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-361] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-129] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-218] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-227] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-287] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-201] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-236] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-252] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-286] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-295] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-306] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-324] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-354] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-361] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-375] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-401] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-417] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-434] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-440] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-539] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-74] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-76] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-283] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-187] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-204] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [60-76] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [78-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [83-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-164] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-222] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-240] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-272] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-332] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-211] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-132] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-140] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-242] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-289] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-118] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-81] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-131] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-287] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-337] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-481] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-538] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-206] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-255] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-355] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-361] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-435] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-539] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-85] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-155] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-167] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-197] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-223] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-69] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-106] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-296] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-101] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-246] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-274] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-145] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-276] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-155] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-155] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-162] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-152] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-391] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-420] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-434] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-471] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-538] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-236] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-272] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-307] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-240] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-267] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-379] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-391] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-399] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-458] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-467] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-481] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-488] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-286] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-297] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-376] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-381] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-403] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-411] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-438] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-374] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-398] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-347] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-406] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-414] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-440] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-487] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-515] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-528] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-317] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-340] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-377] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-392] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-387] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-539] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-340] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-327] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-331] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-340] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-357] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-343] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-311] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-369] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-511] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-314] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-338] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-356] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-369] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-386] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-398] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-411] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-436] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-510] for track '48' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-521] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-321] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-344] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-528] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-533] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-381] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-393] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-409] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-434] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-374] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-385] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-403] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-432] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-441] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-464] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-428] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-480] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-486] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-522] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-528] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-383] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-387] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-395] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-410] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-415] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-503] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-423] for track '58' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-477] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-480] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-486] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-495] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-531] for track '58' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-400] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-434] for track '59' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-439] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-449] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-455] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-397] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-464] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-403] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-411] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-451] for track '62' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-456] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-402] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-416] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-467] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-472] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-499] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-527] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-402] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-419] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-470] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-510] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-521] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-409] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-413] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-418] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-466] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-423] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-455] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-426] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-436] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-442] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-539] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-426] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-523] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-434] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-434] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-445] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-453] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-456] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-460] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-470] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-486] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-519] for track '71' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-472] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-495] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-452] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-460] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-473] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-510] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-518] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-453] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-473] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-480] for track '76' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-493] for track '76' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-524] for track '76' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-530] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-473] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-510] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-530] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-458] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-466] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-510] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-463] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-536] for track '79' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-461] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-471] for track '80' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-468] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-521] for track '82' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-526] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-471] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-488] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-495] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-510] for track '85' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-521] for track '85' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-515] for track '86' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-488] for track '88' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-521] for track '89' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-528] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-532] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-539] for track '89' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-516] for track '90' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-521] for track '90' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-524] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-532] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-539] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-503] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-539] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-509] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-524] for track '92' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-520] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '94' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-509] for track '95' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-522] for track '95' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-531] for track '95' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-513] for track '96' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-522] for track '98' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-539] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '99' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '99' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>