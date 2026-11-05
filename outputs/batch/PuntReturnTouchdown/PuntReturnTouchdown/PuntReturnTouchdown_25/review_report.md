# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_25`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 61
- **Ball Tracks:** 0
- **Action Segments:** 243
- **Validation Warnings:** 290
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
- **Inferred Coverage Segments (Action_None):** 227
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `16` | `16` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `16` | `16` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `27` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `27` | `23` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `27` | `23` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `10` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `11` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `12` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `13` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `14` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `16` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `17` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `18` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `9` | `Group` | 0 | START | 0 | 72 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `12` | `12` | 73 | START | 73 | 132 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `16` | `16` | 103 | END | 103 | 103 |
| ✅ EXACT | `Action_PuntBall` | Punter | `16` | `16` | 133 | START | 133 | 143 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `27` | `23` | 267 | START | 267 | 278 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `27` | `23` | 279 | START | 279 | 499 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `27` | `23` | 582 | START | 582 | 588 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–593
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 144 | 72 | inferred_complete_timeline |
| `Action_None` | 146 | 178 | 33 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 184 | 195 | 12 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 593 | 357 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 102 | 30 | inferred_complete_timeline |
| `Action_None` | 107 | 196 | 90 | inferred_complete_timeline |
| `Action_None` | 198 | 200 | 3 | inferred_complete_timeline |
| `Action_None` | 202 | 210 | 9 | inferred_complete_timeline |
| `Action_None` | 212 | 214 | 3 | inferred_complete_timeline |
| `Action_None` | 217 | 222 | 6 | inferred_complete_timeline |
| `Action_None` | 224 | 238 | 15 | inferred_complete_timeline |
| `Action_None` | 247 | 252 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_LongSnap` | 73 | 132 | 60 | inferred_complete_timeline |
| `Action_None` | 133 | 185 | 53 | inferred_complete_timeline |
| `Action_None` | 187 | 195 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–486
- **Visible Samples:** 459

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 232 | 160 | inferred_complete_timeline |
| `Action_None` | 234 | 238 | 5 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 268 | 486 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 215 | 143 | inferred_complete_timeline |
| `Action_None` | 239 | 241 | 3 | inferred_complete_timeline |
| `Action_None` | 243 | 330 | 88 | inferred_complete_timeline |
| `Action_None` | 336 | 405 | 70 | inferred_complete_timeline |
| `Action_None` | 410 | 412 | 3 | inferred_complete_timeline |
| `Action_None` | 414 | 463 | 50 | inferred_complete_timeline |
| `Action_None` | 465 | 545 | 81 | inferred_complete_timeline |
| `Action_None` | 549 | 550 | 2 | inferred_complete_timeline |
| `Action_None` | 553 | 576 | 24 | inferred_complete_timeline |
| `Action_None` | 579 | 599 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 133 | 61 | inferred_complete_timeline |
| `Action_None` | 135 | 140 | 6 | inferred_complete_timeline |
| `Action_None` | 143 | 192 | 50 | inferred_complete_timeline |
| `Action_None` | 194 | 210 | 17 | inferred_complete_timeline |
| `Action_None` | 212 | 219 | 8 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 231 | 234 | 4 | inferred_complete_timeline |
| `Action_None` | 238 | 246 | 9 | inferred_complete_timeline |
| `Action_None` | 248 | 360 | 113 | inferred_complete_timeline |
| `Action_None` | 385 | 599 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 596

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_SnapReceive` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_None` | 104 | 132 | 29 | inferred_complete_timeline |
| `Action_PuntBall` | 133 | 143 | 11 | inferred_complete_timeline |
| `Action_None` | 144 | 476 | 333 | inferred_complete_timeline |
| `Action_None` | 478 | 549 | 72 | inferred_complete_timeline |
| `Action_None` | 553 | 599 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 171 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 495

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 104 | 32 | inferred_complete_timeline |
| `Action_None` | 169 | 189 | 21 | inferred_complete_timeline |
| `Action_None` | 191 | 197 | 7 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_None` | 210 | 212 | 3 | inferred_complete_timeline |
| `Action_None` | 215 | 263 | 49 | inferred_complete_timeline |
| `Action_None` | 286 | 317 | 32 | inferred_complete_timeline |
| `Action_None` | 319 | 354 | 36 | inferred_complete_timeline |
| `Action_None` | 360 | 599 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–482
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 179 | 107 | inferred_complete_timeline |
| `Action_None` | 182 | 188 | 7 | inferred_complete_timeline |
| `Action_None` | 193 | 198 | 6 | inferred_complete_timeline |
| `Action_None` | 221 | 249 | 29 | inferred_complete_timeline |
| `Action_None` | 252 | 259 | 8 | inferred_complete_timeline |
| `Action_None` | 264 | 271 | 8 | inferred_complete_timeline |
| `Action_None` | 273 | 482 | 210 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 206 | 134 | inferred_complete_timeline |
| `Action_None` | 209 | 220 | 12 | inferred_complete_timeline |
| `Action_None` | 222 | 227 | 6 | inferred_complete_timeline |
| `Action_None` | 232 | 235 | 4 | inferred_complete_timeline |
| `Action_None` | 238 | 247 | 10 | inferred_complete_timeline |
| `Action_None` | 252 | 599 | 348 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 135 | 63 | inferred_complete_timeline |
| `Action_None` | 139 | 146 | 8 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 157 | 6 | inferred_complete_timeline |
| `Action_None` | 165 | 178 | 14 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 241 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 157 | 85 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 96 | 24 | inferred_complete_timeline |
| `Action_None` | 98 | 135 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 261 | 189 | inferred_complete_timeline |
| `Action_None` | 263 | 264 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 559

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 227 | 155 | inferred_complete_timeline |
| `Action_None` | 229 | 235 | 7 | inferred_complete_timeline |
| `Action_None` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 253 | 5 | inferred_complete_timeline |
| `Action_None` | 256 | 260 | 5 | inferred_complete_timeline |
| `Action_None` | 264 | 321 | 58 | inferred_complete_timeline |
| `Action_None` | 323 | 327 | 5 | inferred_complete_timeline |
| `Action_None` | 329 | 406 | 78 | inferred_complete_timeline |
| `Action_None` | 410 | 490 | 81 | inferred_complete_timeline |
| `Action_None` | 493 | 524 | 32 | inferred_complete_timeline |
| `Action_None` | 536 | 545 | 10 | inferred_complete_timeline |
| `Action_None` | 548 | 589 | 42 | inferred_complete_timeline |
| `Action_None` | 591 | 593 | 3 | inferred_complete_timeline |
| `Action_None` | 597 | 599 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 158 | 86 | inferred_complete_timeline |
| `Action_None` | 160 | 173 | 14 | inferred_complete_timeline |
| `Action_None` | 176 | 182 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–596
- **Visible Samples:** 581

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 371 | 299 | inferred_complete_timeline |
| `Action_None` | 378 | 387 | 10 | inferred_complete_timeline |
| `Action_None` | 389 | 406 | 18 | inferred_complete_timeline |
| `Action_None` | 416 | 596 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 200 | 128 | inferred_complete_timeline |
| `Action_None` | 202 | 220 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–599 | 593 | 6 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 2–195 | 190 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 109–395 | 287 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 166–254 | 79 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 195–599 | 403 | 7 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 204–231 | 24 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 204–304 | 84 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 221–224 | 4 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 222–300 | 76 | 3 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 247–248 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 253–599 | 339 | 7 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 254–420 | 36 | 5 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 255–256 | 2 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 259–309 | 45 | 4 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 270–272 | 3 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 270–296 | 20 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 271–281 | 11 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 272–304 | 29 | 3 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 278–304 | 27 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 285–599 | 305 | 3 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 295–545 | 251 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 300–309 | 9 | 2 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 305–599 | 275 | 9 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 327–599 | 251 | 4 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 334–465 | 121 | 6 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 341–498 | 158 | 1 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 345–436 | 20 | 5 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 349–415 | 57 | 2 | Undefined position; Undefined team |
| `47` | `64` | Position_Unknown | Team_Unknown | 358–599 | 239 | 3 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 449–599 | 151 | 1 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 469–599 | 124 | 4 | Undefined position; Undefined team |
| `50` | `70` | Position_Unknown | Team_Unknown | 473–474 | 2 | 1 | Undefined position; Undefined team |
| `51` | `71` | Position_Unknown | Team_Unknown | 474–599 | 126 | 1 | Undefined position; Undefined team |
| `52` | `75` | Position_Unknown | Team_Unknown | 496–522 | 27 | 1 | Undefined position; Undefined team |
| `53` | `79` | Position_Unknown | Team_Unknown | 502–599 | 80 | 6 | Undefined position; Undefined team |
| `54` | `81` | Position_Unknown | Team_Unknown | 530–599 | 68 | 2 | Undefined position; Undefined team |
| `55` | `84` | Position_Unknown | Team_Unknown | 572–599 | 28 | 1 | Undefined position; Undefined team |
| `56` | `85` | Position_Unknown | Team_Unknown | 574–575 | 2 | 1 | Undefined position; Undefined team |
| `57` | `86` | Position_Unknown | Team_Unknown | 574–589 | 14 | 2 | Undefined position; Undefined team |
| `58` | `87` | Position_Unknown | Team_Unknown | 580–589 | 6 | 2 | Undefined position; Undefined team |
| `59` | `89` | Position_Unknown | Team_Unknown | 586–587 | 2 | 1 | Undefined position; Undefined team |
| `60` | `90` | Position_Unknown | Team_Unknown | 599–599 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `27` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Wing` position mapped to `offense` team
- ⚠️ 42 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 42 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 84 |
| Missing visible bounding boxes during action | 202 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 51: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [73-206] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-220] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-247] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-157] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-371] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-387] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-406] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-596] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-135] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-261] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-227] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-235] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-321] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-327] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-406] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-490] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-524] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-545] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-589] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-593] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-146] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-178] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-241] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-158] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-173] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-182] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-200] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-220] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-215] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-330] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-405] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-412] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-463] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-545] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-550] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-576] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-102] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-238] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-252] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-185] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-195] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-140] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-192] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-219] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-246] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-360] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-232] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-486] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-144] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-195] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-593] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-476] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-549] for track '16' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-599] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-104] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-189] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-197] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-263] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-317] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-354] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-179] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-198] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-249] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-259] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-271] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-482] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-171] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-200] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-367] for track '19' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-599] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-33] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-190] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-395] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-221] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-234] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-254] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [279-499] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [501-577] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [589-599] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-215] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-231] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-213] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-293] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-304] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-242] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-300] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-336] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-352] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-390] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-397] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-580] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-584] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-353] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-395] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-283] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-292] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-304] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-309] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-281] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-296] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-281] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-304] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-304] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-336] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-398] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-599] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-545] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-309] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-382] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-392] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-436] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-540] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-550] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-556] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-568] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-576] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-551] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-554] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-561] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-599] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-351] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-397] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-405] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-461] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-465] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-498] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-356] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-371] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-415] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-362] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-374] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-545] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-568] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-571] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-599] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-599] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-522] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-508] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-537] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-543] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-556] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-573] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-593] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-575] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-579] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-589] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-581] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-589] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-587] for track '59' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>