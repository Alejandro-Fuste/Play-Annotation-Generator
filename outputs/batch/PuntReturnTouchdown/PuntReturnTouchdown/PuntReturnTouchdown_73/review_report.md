# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_73

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_73`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 79
- **Ball Tracks:** 0
- **Action Segments:** 344
- **Validation Warnings:** 432
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 328
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `56` | `41` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `56` | `41` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `56` | `41` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner1 | `0` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner2 | `1` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `10` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | `12` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `15` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | `17` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `18` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `2` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `9` | `Group` | 0 | START | 0 | 42 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `15` | `15` | 43 | START | 43 | 66 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `2` | `2` | 75 | END | 75 | 75 |
| ✅ EXACT | `Action_PuntBall` | Punter | `2` | `2` | 84 | START | 84 | 114 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `56` | `41` | 227 | START | 227 | 238 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `56` | `41` | 270 | START | 270 | 491 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `56` | `41` | 627 | START | 627 | 629 |

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
- **Visible Frames:** 0–629
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 79 | 37 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 139 | 51 | inferred_complete_timeline |
| `Action_None` | 192 | 235 | 44 | inferred_complete_timeline |
| `Action_None` | 240 | 268 | 29 | inferred_complete_timeline |
| `Action_None` | 270 | 309 | 40 | inferred_complete_timeline |
| `Action_None` | 311 | 353 | 43 | inferred_complete_timeline |
| `Action_None` | 357 | 358 | 2 | inferred_complete_timeline |
| `Action_None` | 362 | 629 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–337
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 124 | 82 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 139 | 5 | inferred_complete_timeline |
| `Action_None` | 143 | 157 | 15 | inferred_complete_timeline |
| `Action_None` | 161 | 163 | 3 | inferred_complete_timeline |
| `Action_None` | 199 | 203 | 5 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_None` | 209 | 280 | 72 | inferred_complete_timeline |
| `Action_None` | 289 | 337 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 57 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_LongSnap` | 43 | 66 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 67 | 25 | inferred_complete_timeline |
| `Action_None` | 72 | 77 | 6 | inferred_complete_timeline |
| `Action_None` | 103 | 123 | 21 | inferred_complete_timeline |
| `Action_None` | 126 | 132 | 7 | inferred_complete_timeline |
| `Action_None` | 135 | 154 | 20 | inferred_complete_timeline |
| `Action_None` | 156 | 167 | 12 | inferred_complete_timeline |
| `Action_None` | 173 | 176 | 4 | inferred_complete_timeline |
| `Action_None` | 184 | 253 | 70 | inferred_complete_timeline |
| `Action_None` | 259 | 267 | 9 | inferred_complete_timeline |
| `Action_None` | 274 | 294 | 21 | inferred_complete_timeline |
| `Action_None` | 299 | 303 | 5 | inferred_complete_timeline |
| `Action_None` | 308 | 342 | 35 | inferred_complete_timeline |
| `Action_None` | 345 | 427 | 83 | inferred_complete_timeline |
| `Action_None` | 429 | 480 | 52 | inferred_complete_timeline |
| `Action_None` | 484 | 611 | 128 | inferred_complete_timeline |
| `Action_None` | 613 | 629 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 123 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–463
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_SnapReceive` | 75 | 75 | 1 | inferred_complete_timeline |
| `Action_None` | 76 | 83 | 8 | inferred_complete_timeline |
| `Action_PuntBall` | 84 | 114 | 31 | inferred_complete_timeline |
| `Action_None` | 115 | 157 | 43 | inferred_complete_timeline |
| `Action_None` | 159 | 251 | 93 | inferred_complete_timeline |
| `Action_None` | 256 | 274 | 19 | inferred_complete_timeline |
| `Action_None` | 278 | 279 | 2 | inferred_complete_timeline |
| `Action_None` | 283 | 307 | 25 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 318 | 348 | 31 | inferred_complete_timeline |
| `Action_None` | 354 | 360 | 7 | inferred_complete_timeline |
| `Action_None` | 363 | 364 | 2 | inferred_complete_timeline |
| `Action_None` | 369 | 379 | 11 | inferred_complete_timeline |
| `Action_None` | 381 | 388 | 8 | inferred_complete_timeline |
| `Action_None` | 393 | 403 | 11 | inferred_complete_timeline |
| `Action_None` | 406 | 409 | 4 | inferred_complete_timeline |
| `Action_None` | 412 | 463 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 75 | 33 | inferred_complete_timeline |
| `Action_None` | 79 | 100 | 22 | inferred_complete_timeline |
| `Action_None` | 106 | 159 | 54 | inferred_complete_timeline |
| `Action_None` | 184 | 189 | 6 | inferred_complete_timeline |
| `Action_None` | 199 | 219 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 166 | 124 | inferred_complete_timeline |
| `Action_None` | 169 | 172 | 4 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 199 | 5 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 287 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–347
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 141 | 99 | inferred_complete_timeline |
| `Action_None` | 143 | 150 | 8 | inferred_complete_timeline |
| `Action_None` | 152 | 159 | 8 | inferred_complete_timeline |
| `Action_None` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 175 | 4 | inferred_complete_timeline |
| `Action_None` | 204 | 209 | 6 | inferred_complete_timeline |
| `Action_None` | 211 | 216 | 6 | inferred_complete_timeline |
| `Action_None` | 218 | 347 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 126 | 84 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–339
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 108 | 66 | inferred_complete_timeline |
| `Action_None` | 112 | 207 | 96 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_None` | 226 | 339 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–515
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 178 | 136 | inferred_complete_timeline |
| `Action_None` | 189 | 192 | 4 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 207 | 10 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 218 | 244 | 27 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 252 | 270 | 19 | inferred_complete_timeline |
| `Action_None` | 274 | 397 | 124 | inferred_complete_timeline |
| `Action_None` | 409 | 412 | 4 | inferred_complete_timeline |
| `Action_None` | 426 | 492 | 67 | inferred_complete_timeline |
| `Action_None` | 505 | 509 | 5 | inferred_complete_timeline |
| `Action_None` | 512 | 515 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 150 | 108 | inferred_complete_timeline |
| `Action_None` | 153 | 156 | 4 | inferred_complete_timeline |
| `Action_None` | 160 | 163 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 102 | 60 | inferred_complete_timeline |
| `Action_None` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 112 | 115 | 4 | inferred_complete_timeline |
| `Action_None` | 118 | 124 | 7 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 154 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–535
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 185 | 143 | inferred_complete_timeline |
| `Action_None` | 198 | 262 | 65 | inferred_complete_timeline |
| `Action_None` | 272 | 278 | 7 | inferred_complete_timeline |
| `Action_None` | 280 | 332 | 53 | inferred_complete_timeline |
| `Action_None` | 334 | 345 | 12 | inferred_complete_timeline |
| `Action_None` | 347 | 528 | 182 | inferred_complete_timeline |
| `Action_None` | 530 | 532 | 3 | inferred_complete_timeline |
| `Action_None` | 534 | 535 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 108 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 178 | 136 | inferred_complete_timeline |
| `Action_None` | 180 | 194 | 15 | inferred_complete_timeline |
| `Action_None` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_None` | 207 | 247 | 41 | inferred_complete_timeline |
| `Action_None` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 259 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 51–65 | 15 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 57–77 | 20 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 61–150 | 90 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 64–139 | 71 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 64–201 | 95 | 6 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 120–150 | 29 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 131–133 | 3 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 137–211 | 29 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 138–299 | 141 | 7 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 138–139 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 145–150 | 6 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 186–243 | 8 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 187–629 | 398 | 12 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 188–189 | 2 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 190–191 | 2 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 194–223 | 9 | 3 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 196–287 | 50 | 8 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 196–211 | 12 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 204–629 | 421 | 4 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 208–549 | 330 | 6 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 210–558 | 283 | 6 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 217–219 | 3 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 227–629 | 401 | 5 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 228–229 | 2 | 1 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 230–629 | 387 | 5 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 243–629 | 340 | 9 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 249–251 | 3 | 1 | Undefined position; Undefined team |
| `46` | `63` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `47` | `64` | Position_Unknown | Team_Unknown | 260–629 | 346 | 6 | Undefined position; Undefined team |
| `48` | `66` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `49` | `67` | Position_Unknown | Team_Unknown | 266–267 | 2 | 1 | Undefined position; Undefined team |
| `50` | `70` | Position_Unknown | Team_Unknown | 271–272 | 2 | 1 | Undefined position; Undefined team |
| `51` | `72` | Position_Unknown | Team_Unknown | 276–629 | 292 | 18 | Undefined position; Undefined team |
| `52` | `74` | Position_Unknown | Team_Unknown | 280–282 | 3 | 1 | Undefined position; Undefined team |
| `53` | `78` | Position_Unknown | Team_Unknown | 302–458 | 155 | 3 | Undefined position; Undefined team |
| `54` | `81` | Position_Unknown | Team_Unknown | 306–366 | 59 | 2 | Undefined position; Undefined team |
| `55` | `82` | Position_Unknown | Team_Unknown | 310–318 | 9 | 1 | Undefined position; Undefined team |
| `56` | `83` | Position_Unknown | Team_Unknown | 310–311 | 2 | 1 | Undefined position; Undefined team |
| `57` | `84` | Position_Unknown | Team_Unknown | 314–629 | 278 | 11 | Undefined position; Undefined team |
| `58` | `85` | Position_Unknown | Team_Unknown | 317–552 | 217 | 7 | Undefined position; Undefined team |
| `59` | `86` | Position_Unknown | Team_Unknown | 319–612 | 282 | 8 | Undefined position; Undefined team |
| `60` | `87` | Position_Unknown | Team_Unknown | 322–561 | 240 | 1 | Undefined position; Undefined team |
| `61` | `88` | Position_Unknown | Team_Unknown | 347–566 | 188 | 6 | Undefined position; Undefined team |
| `62` | `90` | Position_Unknown | Team_Unknown | 363–496 | 103 | 7 | Undefined position; Undefined team |
| `63` | `91` | Position_Unknown | Team_Unknown | 385–626 | 154 | 3 | Undefined position; Undefined team |
| `64` | `92` | Position_Unknown | Team_Unknown | 445–488 | 20 | 4 | Undefined position; Undefined team |
| `65` | `95` | Position_Unknown | Team_Unknown | 497–499 | 3 | 1 | Undefined position; Undefined team |
| `66` | `96` | Position_Unknown | Team_Unknown | 508–509 | 2 | 1 | Undefined position; Undefined team |
| `67` | `97` | Position_Unknown | Team_Unknown | 511–517 | 6 | 2 | Undefined position; Undefined team |
| `68` | `98` | Position_Unknown | Team_Unknown | 531–534 | 4 | 1 | Undefined position; Undefined team |
| `69` | `102` | Position_Unknown | Team_Unknown | 547–629 | 72 | 3 | Undefined position; Undefined team |
| `70` | `103` | Position_Unknown | Team_Unknown | 552–553 | 2 | 1 | Undefined position; Undefined team |
| `71` | `106` | Position_Unknown | Team_Unknown | 567–629 | 50 | 5 | Undefined position; Undefined team |
| `72` | `107` | Position_Unknown | Team_Unknown | 587–622 | 15 | 3 | Undefined position; Undefined team |
| `73` | `108` | Position_Unknown | Team_Unknown | 594–614 | 5 | 2 | Undefined position; Undefined team |
| `74` | `109` | Position_Unknown | Team_Unknown | 594–595 | 2 | 1 | Undefined position; Undefined team |
| `75` | `111` | Position_Unknown | Team_Unknown | 602–629 | 22 | 3 | Undefined position; Undefined team |
| `76` | `114` | Position_Unknown | Team_Unknown | 621–629 | 8 | 2 | Undefined position; Undefined team |
| `77` | `115` | Position_Unknown | Team_Unknown | 623–629 | 7 | 1 | Undefined position; Undefined team |
| `78` | `119` | Position_Unknown | Team_Unknown | 629–629 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `56` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ 60 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 60 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 120 |
| Missing visible bounding boxes during action | 309 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [43-166] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-287] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-141] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-347] for track '1' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-157] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-251] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-274] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-307] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-348] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-360] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-379] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-388] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-403] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-409] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-463] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-108] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-207] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-339] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-178] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-194] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-247] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-108] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-185] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-262] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-278] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-332] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-345] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-528] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-532] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-535] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-102] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-124] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-159] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-219] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-207] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-244] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-270] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-397] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-412] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-492] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-509] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-515] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-57] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-150] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [43-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-79] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-268] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-309] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-353] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-124] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-280] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-337] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-77] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-167] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-253] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-267] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-294] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-303] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-342] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-427] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-480] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-611] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-65] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-77] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-126] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-130] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-166] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-146] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-199] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-166] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-176] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-265] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-299] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-191] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-275] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-304] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-536] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-545] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-554] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-574] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-270] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-211] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-233] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-426] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-629] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-253] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-270] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-346] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-351] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-436] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-549] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-218] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-265] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-298] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-519] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-541] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-558] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [270-491] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-240] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-253] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-526] for track '43' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-530] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-629] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-252] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-424] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-522] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-615] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-623] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-270] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-294] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-629] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-379] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-387] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-393] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-401] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-469] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-485] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-491] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-499] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-517] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-524] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-554] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-564] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-575] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-586] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-597] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-629] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-359] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-376] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-458] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-359] for track '54' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-366] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-318] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-408] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-418] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-423] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-443] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-456] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-481] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-612] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-622] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-332] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-349] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-360] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-385] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-474] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-521] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-552] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-352] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-361] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-373] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-379] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-428] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-566] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-607] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-612] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-561] for track '60' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-371] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-430] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-561] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-566] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-399] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-421] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-448] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-468] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-496] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-524] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-539] for track '63' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-626] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-450] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-464] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-484] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-488] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-499] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-509] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-514] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-517] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-534] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-572] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-581] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-629] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-553] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-589] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-597] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-604] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-610] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-597] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-603] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-622] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-595] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-614] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-595] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-604] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-607] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-622] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-629] for track '76' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>