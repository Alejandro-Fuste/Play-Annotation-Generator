# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_47

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_47`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 67
- **Ball Tracks:** 0
- **Action Segments:** 310
- **Validation Warnings:** 378
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 297
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `16` | `16` |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `30` | `26` |
| ✅ EXACT | `Action_PuntBall` | Position_Unknown | Team_Unknown | `30` | `26` |
| ✅ EXACT | `Action_CatchPunt` | Punt_Returner | defense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Punt_Returner | defense | `2` | `2` |
| ✅ EXACT | `Action_CrossGoalLine` | Punt_Returner | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `1` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `10` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `12` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `16` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `4` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `7` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `9` | `Group` | 0 | START | 0 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `16` | `16` | 52 | START | 52 | 71 |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | `30` | `26` | 85 | END | 97 | 97 |
| ✅ EXACT | `Action_PuntBall` | Position_Unknown | `30` | `26` | 111 | START | 111 | 119 |
| ✅ EXACT | `Action_CatchPunt` | Punt_Returner | `2` | `2` | 241 | START | 241 | 249 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Punt_Returner | `2` | `2` | 271 | START | 271 | 536 |
| ✅ EXACT | `Action_CrossGoalLine` | Punt_Returner | `2` | `2` | 550 | START | 550 | 557 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 72 | 21 | inferred_complete_timeline |
| `Action_None` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_None` | 83 | 195 | 113 | inferred_complete_timeline |
| `Action_None` | 201 | 208 | 8 | inferred_complete_timeline |
| `Action_None` | 211 | 223 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 106 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 105 | 54 | inferred_complete_timeline |
| `Action_None` | 109 | 113 | 5 | inferred_complete_timeline |
| `Action_None` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_None` | 123 | 262 | 140 | inferred_complete_timeline |
| `Action_None` | 264 | 277 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–288
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_LongSnap` | 52 | 71 | 20 | inferred_complete_timeline |
| `Action_LongSnap` | 77 | 110 | 34 | inferred_complete_timeline |
| `Action_None` | 111 | 138 | 28 | inferred_complete_timeline |
| `Action_None` | 142 | 203 | 62 | inferred_complete_timeline |
| `Action_None` | 206 | 208 | 3 | inferred_complete_timeline |
| `Action_None` | 210 | 214 | 5 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 277 | 49 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |
| `Action_None` | 284 | 288 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 104 | 53 | inferred_complete_timeline |
| `Action_None` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_None` | 150 | 153 | 4 | inferred_complete_timeline |
| `Action_None` | 158 | 162 | 5 | inferred_complete_timeline |
| `Action_None` | 190 | 194 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 85 | 34 | inferred_complete_timeline |
| `Action_None` | 88 | 107 | 20 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 119 | 136 | 18 | inferred_complete_timeline |
| `Action_None` | 139 | 149 | 11 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 208 | 9 | inferred_complete_timeline |
| `Action_None` | 210 | 223 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 98 | 47 | inferred_complete_timeline |
| `Action_None` | 100 | 104 | 5 | inferred_complete_timeline |
| `Action_None` | 116 | 136 | 21 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 146 | 149 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 78 | 27 | inferred_complete_timeline |
| `Action_None` | 98 | 126 | 29 | inferred_complete_timeline |
| `Action_None` | 128 | 145 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 97 | 46 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 108 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 110 | 59 | inferred_complete_timeline |
| `Action_None` | 113 | 118 | 6 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 106 | 55 | inferred_complete_timeline |
| `Action_None` | 110 | 152 | 43 | inferred_complete_timeline |
| `Action_None` | 155 | 216 | 62 | inferred_complete_timeline |
| `Action_None` | 221 | 250 | 30 | inferred_complete_timeline |
| `Action_None` | 259 | 298 | 40 | inferred_complete_timeline |
| `Action_None` | 300 | 308 | 9 | inferred_complete_timeline |
| `Action_None` | 310 | 380 | 71 | inferred_complete_timeline |
| `Action_None` | 383 | 384 | 2 | inferred_complete_timeline |
| `Action_None` | 390 | 392 | 3 | inferred_complete_timeline |
| `Action_None` | 394 | 401 | 8 | inferred_complete_timeline |
| `Action_None` | 406 | 500 | 95 | inferred_complete_timeline |
| `Action_None` | 503 | 509 | 7 | inferred_complete_timeline |
| `Action_None` | 513 | 551 | 39 | inferred_complete_timeline |
| `Action_None` | 553 | 568 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 267 | 216 | inferred_complete_timeline |
| `Action_None` | 270 | 272 | 3 | inferred_complete_timeline |
| `Action_None` | 293 | 294 | 2 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |
| `Action_None` | 307 | 309 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 524

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 214 | 163 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 253 | 34 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_None` | 264 | 279 | 16 | inferred_complete_timeline |
| `Action_None` | 285 | 290 | 6 | inferred_complete_timeline |
| `Action_None` | 293 | 296 | 4 | inferred_complete_timeline |
| `Action_None` | 302 | 303 | 2 | inferred_complete_timeline |
| `Action_None` | 314 | 521 | 208 | inferred_complete_timeline |
| `Action_None` | 524 | 525 | 2 | inferred_complete_timeline |
| `Action_None` | 528 | 534 | 7 | inferred_complete_timeline |
| `Action_None` | 537 | 543 | 7 | inferred_complete_timeline |
| `Action_None` | 551 | 569 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 206 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Returner — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 240 | 241 | inferred_complete_timeline |
| `Action_CatchPunt` | 241 | 249 | 9 | inferred_complete_timeline |
| `Action_None` | 250 | 270 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 271 | 536 | 266 | inferred_complete_timeline |
| `Action_BallCarry` | 539 | 541 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 547 | 549 | 3 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 550 | 557 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 558 | 569 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 156 | 105 | inferred_complete_timeline |
| `Action_None` | 161 | 163 | 3 | inferred_complete_timeline |
| `Action_None` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 189 | 17 | inferred_complete_timeline |
| `Action_None` | 192 | 213 | 22 | inferred_complete_timeline |
| `Action_None` | 215 | 220 | 6 | inferred_complete_timeline |
| `Action_None` | 222 | 236 | 15 | inferred_complete_timeline |
| `Action_None` | 238 | 240 | 3 | inferred_complete_timeline |
| `Action_None` | 243 | 253 | 11 | inferred_complete_timeline |
| `Action_None` | 255 | 258 | 4 | inferred_complete_timeline |
| `Action_None` | 266 | 380 | 115 | inferred_complete_timeline |
| `Action_None` | 383 | 384 | 2 | inferred_complete_timeline |
| `Action_None` | 392 | 395 | 4 | inferred_complete_timeline |
| `Action_None` | 398 | 401 | 4 | inferred_complete_timeline |
| `Action_None` | 409 | 427 | 19 | inferred_complete_timeline |
| `Action_None` | 429 | 440 | 12 | inferred_complete_timeline |
| `Action_None` | 443 | 449 | 7 | inferred_complete_timeline |
| `Action_None` | 463 | 569 | 107 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–192 | 158 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 7–16 | 10 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 11–569 | 500 | 8 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 12–183 | 111 | 11 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 13–80 | 52 | 6 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 44–569 | 427 | 8 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 54–55 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 57–86 | 19 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 81–89 | 9 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 93–569 | 458 | 10 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 97–209 | 96 | 10 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 100–140 | 25 | 5 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 116–140 | 25 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 141–150 | 10 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 149–155 | 7 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 155–569 | 406 | 4 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 156–569 | 413 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 160–161 | 2 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 166–267 | 93 | 5 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 177–569 | 337 | 5 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 184–243 | 50 | 4 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 201–307 | 68 | 7 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 204–205 | 2 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 209–222 | 14 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 220–551 | 285 | 11 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 227–435 | 179 | 7 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 239–314 | 32 | 4 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 239–246 | 6 | 2 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 240–277 | 37 | 2 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 271–409 | 116 | 4 | Undefined position; Undefined team |
| `47` | `65` | Position_Unknown | Team_Unknown | 277–304 | 16 | 2 | Undefined position; Undefined team |
| `48` | `66` | Position_Unknown | Team_Unknown | 287–374 | 62 | 3 | Undefined position; Undefined team |
| `49` | `67` | Position_Unknown | Team_Unknown | 294–407 | 110 | 2 | Undefined position; Undefined team |
| `50` | `68` | Position_Unknown | Team_Unknown | 294–569 | 271 | 6 | Undefined position; Undefined team |
| `51` | `69` | Position_Unknown | Team_Unknown | 299–346 | 36 | 4 | Undefined position; Undefined team |
| `52` | `70` | Position_Unknown | Team_Unknown | 306–381 | 70 | 4 | Undefined position; Undefined team |
| `53` | `72` | Position_Unknown | Team_Unknown | 310–569 | 260 | 1 | Undefined position; Undefined team |
| `54` | `73` | Position_Unknown | Team_Unknown | 313–319 | 7 | 1 | Undefined position; Undefined team |
| `55` | `74` | Position_Unknown | Team_Unknown | 316–317 | 2 | 1 | Undefined position; Undefined team |
| `56` | `75` | Position_Unknown | Team_Unknown | 328–398 | 71 | 1 | Undefined position; Undefined team |
| `57` | `76` | Position_Unknown | Team_Unknown | 337–360 | 17 | 2 | Undefined position; Undefined team |
| `58` | `78` | Position_Unknown | Team_Unknown | 354–569 | 187 | 8 | Undefined position; Undefined team |
| `59` | `80` | Position_Unknown | Team_Unknown | 371–515 | 136 | 4 | Undefined position; Undefined team |
| `60` | `81` | Position_Unknown | Team_Unknown | 383–453 | 68 | 2 | Undefined position; Undefined team |
| `61` | `82` | Position_Unknown | Team_Unknown | 400–410 | 4 | 2 | Undefined position; Undefined team |
| `62` | `83` | Position_Unknown | Team_Unknown | 406–498 | 61 | 5 | Undefined position; Undefined team |
| `63` | `86` | Position_Unknown | Team_Unknown | 426–460 | 30 | 4 | Undefined position; Undefined team |
| `64` | `87` | Position_Unknown | Team_Unknown | 480–523 | 44 | 1 | Undefined position; Undefined team |
| `65` | `90` | Position_Unknown | Team_Unknown | 540–542 | 3 | 1 | Undefined position; Undefined team |
| `66` | `91` | Position_Unknown | Team_Unknown | 566–569 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punt_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Jammer3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Jammer4` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Jammer5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 51 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 51 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 102 |
| Missing visible bounding boxes during action | 271 |
| Track-related warning | 2 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 96: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SnapReceive' for track '26' has invalid range: start=97, end=85. Clamping end to start.
- ⚠️ Action 'Action_None' range [52-106] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-152] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-216] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-250] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-298] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-308] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-380] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-392] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-401] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-500] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-509] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-551] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-568] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [271-536] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [539-541] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-110] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-98] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-189] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-213] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-220] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-236] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-253] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-380] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-395] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-401] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-427] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-440] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-449] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-569] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-85] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-136] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-149] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-208] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-223] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-267] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-104] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-194] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-105] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-262] for track '10' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-277] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-214] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-253] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-279] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-290] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-296] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-521] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-534] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-543] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-569] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-72] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-195] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-208] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-223] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-206] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-144] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [52-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-203] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-214] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-277] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-288] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-16] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-83] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-125] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-185] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-380] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-512] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-522] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-84] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-128] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-183] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-32] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-72] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-476] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-517] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-69] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-86] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-89] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-145] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-183] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-431] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-441] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-448] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-456] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-462] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-470] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-525] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-139] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-203] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-121] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-140] for track '28' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-224] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-550] for track '31' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-567] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-182] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-215] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-260] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-345] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-439] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-518] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-542] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-194] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-213] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-243] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-225] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-241] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-258] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-282] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-298] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-307] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-222] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-384] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-391] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-400] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-413] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-429] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-436] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-458] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-529] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-542] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-262] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-435] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-250] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-271] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-314] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-262] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-277] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-298] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-318] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-393] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-409] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-290] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-298] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-374] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-391] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-407] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-383] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-403] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-481] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-501] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-548] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-307] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-324] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-346] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-323] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-373] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-569] for track '53' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-319] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-398] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-341] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-360] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-374] for track '58' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-380] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-391] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-395] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-401] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-547] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-412] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-426] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-440] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-515] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-407] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-453] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-410] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-412] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-436] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-455] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-489] for track '62' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-498] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-431] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-441] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-446] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-460] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-523] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-542] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>