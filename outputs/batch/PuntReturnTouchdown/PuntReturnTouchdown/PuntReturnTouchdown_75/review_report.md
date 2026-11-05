# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_75

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_75`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 96
- **Ball Tracks:** 0
- **Action Segments:** 289
- **Validation Warnings:** 408
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
- **Inferred Coverage Segments (Action_None):** 273
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `32` | `27` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `32` | `27` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `91` | `64` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `1` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `10` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `14` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `17` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `18` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `2` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `6` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `9` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `17` | `17` | 8 | START | 8 | 60 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `2` | `2` | 34 | END | 34 | 34 |
| ✅ EXACT | `Action_PuntBall` | Punter | `2` | `2` | 61 | START | 61 | 76 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `32` | `27` | 192 | START | 192 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `32` | `27` | 216 | START | 216 | 272 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `91` | `64` | 585 | START | 585 | 596 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 37 | 30 | inferred_complete_timeline |
| `Action_None` | 40 | 174 | 135 | inferred_complete_timeline |
| `Action_None` | 176 | 219 | 44 | inferred_complete_timeline |
| `Action_None` | 221 | 236 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 592

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 46 | 39 | inferred_complete_timeline |
| `Action_None` | 50 | 290 | 241 | inferred_complete_timeline |
| `Action_None` | 294 | 328 | 35 | inferred_complete_timeline |
| `Action_None` | 331 | 599 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–435
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 105 | 98 | inferred_complete_timeline |
| `Action_None` | 116 | 190 | 75 | inferred_complete_timeline |
| `Action_None` | 192 | 206 | 15 | inferred_complete_timeline |
| `Action_None` | 208 | 389 | 182 | inferred_complete_timeline |
| `Action_None` | 403 | 428 | 26 | inferred_complete_timeline |
| `Action_None` | 432 | 435 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_LongSnap` | 8 | 60 | 53 | inferred_complete_timeline |
| `Action_None` | 61 | 64 | 4 | inferred_complete_timeline |
| `Action_None` | 77 | 231 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–422
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 422 | 415 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 271 | 264 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 135 | 128 | inferred_complete_timeline |
| `Action_None` | 137 | 140 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 573

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_SnapReceive` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_None` | 35 | 60 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 61 | 76 | 16 | inferred_complete_timeline |
| `Action_None` | 77 | 223 | 147 | inferred_complete_timeline |
| `Action_None` | 238 | 269 | 32 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |
| `Action_None` | 281 | 286 | 6 | inferred_complete_timeline |
| `Action_None` | 291 | 599 | 309 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 34 | 27 | inferred_complete_timeline |
| `Action_None` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_None` | 41 | 135 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–304
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 133 | 126 | inferred_complete_timeline |
| `Action_None` | 136 | 144 | 9 | inferred_complete_timeline |
| `Action_None` | 146 | 188 | 43 | inferred_complete_timeline |
| `Action_None` | 191 | 194 | 4 | inferred_complete_timeline |
| `Action_None` | 196 | 206 | 11 | inferred_complete_timeline |
| `Action_None` | 208 | 289 | 82 | inferred_complete_timeline |
| `Action_None` | 291 | 294 | 4 | inferred_complete_timeline |
| `Action_None` | 298 | 304 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 576

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 42 | 35 | inferred_complete_timeline |
| `Action_None` | 44 | 123 | 80 | inferred_complete_timeline |
| `Action_None` | 126 | 324 | 199 | inferred_complete_timeline |
| `Action_None` | 340 | 364 | 25 | inferred_complete_timeline |
| `Action_None` | 366 | 425 | 60 | inferred_complete_timeline |
| `Action_None` | 427 | 546 | 120 | inferred_complete_timeline |
| `Action_None` | 549 | 554 | 6 | inferred_complete_timeline |
| `Action_None` | 557 | 599 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 168 | 161 | inferred_complete_timeline |
| `Action_None` | 170 | 190 | 21 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–356
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 163 | 156 | inferred_complete_timeline |
| `Action_None` | 170 | 321 | 152 | inferred_complete_timeline |
| `Action_None` | 327 | 356 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 579

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 69 | 62 | inferred_complete_timeline |
| `Action_None` | 73 | 130 | 58 | inferred_complete_timeline |
| `Action_None` | 133 | 160 | 28 | inferred_complete_timeline |
| `Action_None` | 163 | 317 | 155 | inferred_complete_timeline |
| `Action_None` | 331 | 362 | 32 | inferred_complete_timeline |
| `Action_None` | 364 | 599 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 68 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 105 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 33 | 26 | inferred_complete_timeline |
| `Action_None` | 40 | 313 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 68 | 61 | inferred_complete_timeline |
| `Action_None` | 71 | 175 | 105 | inferred_complete_timeline |
| `Action_None` | 177 | 244 | 68 | inferred_complete_timeline |
| `Action_None` | 248 | 308 | 61 | inferred_complete_timeline |
| `Action_None` | 311 | 419 | 109 | inferred_complete_timeline |
| `Action_None` | 435 | 436 | 2 | inferred_complete_timeline |
| `Action_None` | 448 | 536 | 89 | inferred_complete_timeline |
| `Action_None` | 538 | 584 | 47 | inferred_complete_timeline |
| `Action_None` | 591 | 593 | 3 | inferred_complete_timeline |
| `Action_None` | 595 | 599 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–49
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 29 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 40 | 3 | inferred_complete_timeline |
| `Action_None` | 47 | 49 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–133 | 124 | 5 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 48–119 | 72 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 54–100 | 47 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 61–79 | 10 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 96–146 | 51 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 113–165 | 34 | 5 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 128–599 | 468 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 131–133 | 3 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 134–280 | 145 | 5 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 134–167 | 34 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 149–150 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 154–249 | 96 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 155–160 | 6 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 162–306 | 119 | 7 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 175–235 | 44 | 4 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 175–178 | 4 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 178–203 | 10 | 2 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 188–302 | 65 | 9 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 195–294 | 100 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 195–232 | 38 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 205–412 | 199 | 2 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 241–243 | 3 | 1 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 243–448 | 153 | 5 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 249–253 | 5 | 1 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 250–594 | 324 | 4 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 250–308 | 56 | 4 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 253–316 | 61 | 3 | Undefined position; Undefined team |
| `48` | `68` | Position_Unknown | Team_Unknown | 262–263 | 2 | 1 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 265–268 | 4 | 1 | Undefined position; Undefined team |
| `50` | `70` | Position_Unknown | Team_Unknown | 270–446 | 173 | 3 | Undefined position; Undefined team |
| `51` | `71` | Position_Unknown | Team_Unknown | 275–287 | 12 | 2 | Undefined position; Undefined team |
| `52` | `72` | Position_Unknown | Team_Unknown | 292–293 | 2 | 1 | Undefined position; Undefined team |
| `53` | `73` | Position_Unknown | Team_Unknown | 292–599 | 297 | 6 | Undefined position; Undefined team |
| `54` | `75` | Position_Unknown | Team_Unknown | 294–499 | 192 | 5 | Undefined position; Undefined team |
| `55` | `76` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |
| `56` | `77` | Position_Unknown | Team_Unknown | 309–401 | 74 | 5 | Undefined position; Undefined team |
| `57` | `78` | Position_Unknown | Team_Unknown | 310–342 | 33 | 1 | Undefined position; Undefined team |
| `58` | `79` | Position_Unknown | Team_Unknown | 328–339 | 7 | 2 | Undefined position; Undefined team |
| `59` | `80` | Position_Unknown | Team_Unknown | 329–332 | 4 | 1 | Undefined position; Undefined team |
| `60` | `81` | Position_Unknown | Team_Unknown | 330–599 | 268 | 2 | Undefined position; Undefined team |
| `61` | `82` | Position_Unknown | Team_Unknown | 337–339 | 3 | 1 | Undefined position; Undefined team |
| `62` | `85` | Position_Unknown | Team_Unknown | 342–599 | 247 | 6 | Undefined position; Undefined team |
| `63` | `89` | Position_Unknown | Team_Unknown | 359–599 | 232 | 6 | Undefined position; Undefined team |
| `64` | `91` | Position_Unknown | Team_Unknown | 362–599 | 234 | 5 | Undefined position; Undefined team |
| `65` | `93` | Position_Unknown | Team_Unknown | 381–599 | 218 | 2 | Undefined position; Undefined team |
| `66` | `94` | Position_Unknown | Team_Unknown | 383–595 | 193 | 7 | Undefined position; Undefined team |
| `67` | `95` | Position_Unknown | Team_Unknown | 389–599 | 204 | 5 | Undefined position; Undefined team |
| `68` | `97` | Position_Unknown | Team_Unknown | 405–599 | 177 | 3 | Undefined position; Undefined team |
| `69` | `100` | Position_Unknown | Team_Unknown | 436–437 | 2 | 1 | Undefined position; Undefined team |
| `70` | `101` | Position_Unknown | Team_Unknown | 438–462 | 25 | 1 | Undefined position; Undefined team |
| `71` | `102` | Position_Unknown | Team_Unknown | 442–444 | 3 | 1 | Undefined position; Undefined team |
| `72` | `104` | Position_Unknown | Team_Unknown | 443–599 | 157 | 1 | Undefined position; Undefined team |
| `73` | `105` | Position_Unknown | Team_Unknown | 445–599 | 145 | 4 | Undefined position; Undefined team |
| `74` | `106` | Position_Unknown | Team_Unknown | 447–453 | 5 | 2 | Undefined position; Undefined team |
| `75` | `107` | Position_Unknown | Team_Unknown | 450–580 | 117 | 3 | Undefined position; Undefined team |
| `76` | `110` | Position_Unknown | Team_Unknown | 468–474 | 5 | 2 | Undefined position; Undefined team |
| `77` | `111` | Position_Unknown | Team_Unknown | 476–572 | 65 | 2 | Undefined position; Undefined team |
| `78` | `112` | Position_Unknown | Team_Unknown | 484–485 | 2 | 1 | Undefined position; Undefined team |
| `79` | `113` | Position_Unknown | Team_Unknown | 486–541 | 9 | 3 | Undefined position; Undefined team |
| `80` | `115` | Position_Unknown | Team_Unknown | 508–558 | 51 | 1 | Undefined position; Undefined team |
| `81` | `116` | Position_Unknown | Team_Unknown | 525–526 | 2 | 1 | Undefined position; Undefined team |
| `82` | `118` | Position_Unknown | Team_Unknown | 533–598 | 61 | 4 | Undefined position; Undefined team |
| `83` | `119` | Position_Unknown | Team_Unknown | 538–542 | 5 | 1 | Undefined position; Undefined team |
| `84` | `120` | Position_Unknown | Team_Unknown | 539–557 | 6 | 2 | Undefined position; Undefined team |
| `85` | `121` | Position_Unknown | Team_Unknown | 541–550 | 6 | 3 | Undefined position; Undefined team |
| `86` | `122` | Position_Unknown | Team_Unknown | 543–599 | 38 | 5 | Undefined position; Undefined team |
| `87` | `123` | Position_Unknown | Team_Unknown | 546–553 | 8 | 1 | Undefined position; Undefined team |
| `88` | `125` | Position_Unknown | Team_Unknown | 546–551 | 6 | 1 | Undefined position; Undefined team |
| `89` | `127` | Position_Unknown | Team_Unknown | 561–565 | 5 | 1 | Undefined position; Undefined team |
| `90` | `129` | Position_Unknown | Team_Unknown | 563–599 | 37 | 1 | Undefined position; Undefined team |
| `91` | `130` | Position_Unknown | Team_Unknown | 564–565 | 2 | 1 | Undefined position; Undefined team |
| `92` | `134` | Position_Unknown | Team_Unknown | 583–599 | 15 | 3 | Undefined position; Undefined team |
| `93` | `135` | Position_Unknown | Team_Unknown | 584–599 | 16 | 1 | Undefined position; Undefined team |
| `94` | `136` | Position_Unknown | Team_Unknown | 593–594 | 2 | 1 | Undefined position; Undefined team |
| `95` | `137` | Position_Unknown | Team_Unknown | 595–599 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `32` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 77 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 77 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 154 |
| Missing visible bounding boxes during action | 251 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [8-68] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-175] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-244] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-308] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-419] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-536] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-584] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-593] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-599] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-422] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-223] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-46] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-290] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-328] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-30] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-44] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-127] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-69] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-317] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-362] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-105] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-190] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-389] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-428] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-435] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-29] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-40] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-49] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-33] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-313] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-34] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-135] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-37] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-219] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-236] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-68] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-105] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-144] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-188] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-289] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-271] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-123] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-324] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-364] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-425] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-546] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-554] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-163] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-321] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-356] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-64] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-231] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-190] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-100] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-65] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-146] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-123] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-166] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-276] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-599] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [216-272] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [275-280] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-167] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-249] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-167] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-187] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-202] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-227] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-284] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-306] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-184] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-224] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-235] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-225] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-247] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-275] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-289] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-294] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-232] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-294] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-412] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-333] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-355] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-371] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-399] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-448] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-521] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-569] for track '45' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-574] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-594] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-266] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-278] for track '46' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-308] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-295] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-306] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-316] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-436] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-446] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-280] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-287] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-301] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-496] for track '53' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-506] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-599] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-372] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-386] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-437] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-446] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-499] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-321] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-385] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-397] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-401] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-342] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-331] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-339] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-332] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-554] for track '60' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-599] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-339] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-386] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-419] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-427] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-520] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-527] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-464] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-476] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-569] for track '63' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-581] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-595] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-380] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-422] for track '64' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-584] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-554] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-599] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-413] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-419] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-439] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-567] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-587] for track '66' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-595] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-419] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-569] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-586] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-595] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-599] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-411] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-415] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-599] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-437] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-462] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-444] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-599] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-569] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-576] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-581] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-599] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-449] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-518] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-564] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-580] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-474] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-572] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-485] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-488] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-499] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-541] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-558] for track '80' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-526] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-558] for track '82' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-566] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-591] for track '82' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-598] for track '82' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-542] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-542] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-557] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-542] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-546] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-550] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-545] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-558] for track '86' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-570] for track '86' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-585] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-553] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-551] for track '88' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-565] for track '89' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-585] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-590] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-599] for track '92' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-599] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-594] for track '94' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>