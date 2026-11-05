# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_89

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_89`
- **Frame Range:** 0 to 701 (702 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 701
- **Player Tracks:** 63
- **Ball Tracks:** 0
- **Action Segments:** 205
- **Validation Warnings:** 261
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 188
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `31` | `27` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `31` | `27` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `62` | `47` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `12` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `14` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `15` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `17` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `19` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `20` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `3` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `7` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `8` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `9` | `Group` | 0 | START | 0 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `19` | `19` | 36 | START | 36 | 58 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `8` | `8` | 61 | END | 61 | 61 |
| ✅ EXACT | `Action_PuntBall` | Punter | `8` | `8` | 86 | START | 86 | 104 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `31` | `27` | 189 | START | 189 | 211 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `31` | `27` | 226 | START | 226 | 265 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `62` | `47` | 631 | START | 631 | 643 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–655
- **Visible Samples:** 632

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 71 | 36 | inferred_complete_timeline |
| `Action_None` | 73 | 77 | 5 | inferred_complete_timeline |
| `Action_None` | 85 | 110 | 26 | inferred_complete_timeline |
| `Action_None` | 113 | 153 | 41 | inferred_complete_timeline |
| `Action_None` | 155 | 177 | 23 | inferred_complete_timeline |
| `Action_None` | 181 | 345 | 165 | inferred_complete_timeline |
| `Action_None` | 356 | 655 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–650
- **Visible Samples:** 643

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 272 | 237 | inferred_complete_timeline |
| `Action_None` | 274 | 279 | 6 | inferred_complete_timeline |
| `Action_None` | 282 | 329 | 48 | inferred_complete_timeline |
| `Action_None` | 331 | 644 | 314 | inferred_complete_timeline |
| `Action_None` | 649 | 650 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 138 | 103 | inferred_complete_timeline |
| `Action_None` | 140 | 257 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–618
- **Visible Samples:** 593

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_LongSnap` | 36 | 58 | 23 | inferred_complete_timeline |
| `Action_LongSnap` | 61 | 85 | 25 | inferred_complete_timeline |
| `Action_None` | 86 | 184 | 99 | inferred_complete_timeline |
| `Action_None` | 188 | 284 | 97 | inferred_complete_timeline |
| `Action_None` | 287 | 392 | 106 | inferred_complete_timeline |
| `Action_None` | 412 | 618 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 191 | 156 | inferred_complete_timeline |
| `Action_None` | 193 | 250 | 58 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_None` | 261 | 299 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 148 | 113 | inferred_complete_timeline |
| `Action_None` | 153 | 228 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–307
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 307 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–701
- **Visible Samples:** 697

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_SnapReceive` | 61 | 61 | 1 | inferred_complete_timeline |
| `Action_None` | 62 | 85 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 86 | 104 | 19 | inferred_complete_timeline |
| `Action_None` | 105 | 168 | 64 | inferred_complete_timeline |
| `Action_None` | 174 | 701 | 528 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 117 | 82 | inferred_complete_timeline |
| `Action_None` | 123 | 133 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 143 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–314
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 314 | 279 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 105 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 66 | 31 | inferred_complete_timeline |
| `Action_None` | 76 | 87 | 12 | inferred_complete_timeline |
| `Action_None` | 90 | 92 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–301
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 268 | 233 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_None` | 273 | 283 | 11 | inferred_complete_timeline |
| `Action_None` | 289 | 301 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 85 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–312
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 168 | 133 | inferred_complete_timeline |
| `Action_None` | 172 | 177 | 6 | inferred_complete_timeline |
| `Action_None` | 179 | 309 | 131 | inferred_complete_timeline |
| `Action_None` | 311 | 312 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–327
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 129 | 94 | inferred_complete_timeline |
| `Action_None` | 133 | 327 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 136 | 101 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_None` | 142 | 146 | 5 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 169 | 7 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 177 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 191 | 156 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_None` | 201 | 275 | 75 | inferred_complete_timeline |
| `Action_None` | 279 | 283 | 5 | inferred_complete_timeline |
| `Action_None` | 294 | 296 | 3 | inferred_complete_timeline |
| `Action_None` | 298 | 305 | 8 | inferred_complete_timeline |
| `Action_None` | 307 | 309 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–181 | 182 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 98–282 | 183 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 115–156 | 38 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 131–159 | 29 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 135–310 | 162 | 5 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 140–342 | 188 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 158–208 | 4 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 161–653 | 473 | 7 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 164–189 | 23 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 175–188 | 14 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 205–337 | 133 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 206–575 | 355 | 4 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 209–235 | 25 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 213–264 | 46 | 2 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 235–663 | 429 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 256–313 | 58 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 285–701 | 398 | 2 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 292–701 | 410 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 293–343 | 28 | 3 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 314–317 | 4 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 325–328 | 4 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 328–670 | 333 | 3 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 338–694 | 341 | 3 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 342–675 | 333 | 2 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 342–690 | 346 | 2 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 345–379 | 30 | 4 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 346–494 | 126 | 4 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 348–701 | 354 | 3 | Undefined position; Undefined team |
| `48` | `65` | Position_Unknown | Team_Unknown | 352–701 | 333 | 6 | Undefined position; Undefined team |
| `49` | `66` | Position_Unknown | Team_Unknown | 357–578 | 188 | 3 | Undefined position; Undefined team |
| `50` | `67` | Position_Unknown | Team_Unknown | 358–663 | 281 | 3 | Undefined position; Undefined team |
| `51` | `68` | Position_Unknown | Team_Unknown | 359–512 | 149 | 3 | Undefined position; Undefined team |
| `52` | `69` | Position_Unknown | Team_Unknown | 359–658 | 298 | 3 | Undefined position; Undefined team |
| `53` | `70` | Position_Unknown | Team_Unknown | 359–616 | 104 | 17 | Undefined position; Undefined team |
| `54` | `72` | Position_Unknown | Team_Unknown | 366–375 | 10 | 1 | Undefined position; Undefined team |
| `55` | `73` | Position_Unknown | Team_Unknown | 367–622 | 252 | 2 | Undefined position; Undefined team |
| `56` | `74` | Position_Unknown | Team_Unknown | 370–371 | 2 | 1 | Undefined position; Undefined team |
| `57` | `76` | Position_Unknown | Team_Unknown | 403–664 | 259 | 2 | Undefined position; Undefined team |
| `58` | `81` | Position_Unknown | Team_Unknown | 431–433 | 3 | 1 | Undefined position; Undefined team |
| `59` | `84` | Position_Unknown | Team_Unknown | 459–460 | 2 | 1 | Undefined position; Undefined team |
| `60` | `95` | Position_Unknown | Team_Unknown | 534–628 | 91 | 2 | Undefined position; Undefined team |
| `61` | `98` | Position_Unknown | Team_Unknown | 634–683 | 47 | 4 | Undefined position; Undefined team |
| `62` | `99` | Position_Unknown | Team_Unknown | 694–695 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `31` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Guard` position mapped to `offense` team
- ⚠️ 43 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 43 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 86 |
| Missing visible bounding boxes during action | 172 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 701 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [36-272] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-279] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-329] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-644] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [649-650] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-181] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-168] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-309] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-105] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-268] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-283] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-301] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-327] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-307] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-168] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-701] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-191] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-250] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-85] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-257] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-148] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-228] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-275] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-283] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-305] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-314] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [36-58] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-184] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-284] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-392] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-618] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-71] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-110] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-153] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-177] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-345] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-655] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-206] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-268] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-282] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-156] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-159] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-175] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-267] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-300] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-310] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-148] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-324] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-342] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [226-265] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [272-301] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [304-305] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [318-653] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-168] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-185] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-188] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-337] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-266] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-399] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-575] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-235] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-254] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-663] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-313] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-340] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-701] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-315] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-343] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-608] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-612] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-670] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-346] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-694] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-345] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-675] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-345] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-690] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-352] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-375] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-379] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-349] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-472] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-494] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-354] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-377] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-432] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-440] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-497] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-362] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-377] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-578] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-362] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-373] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-663] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-494] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-500] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-512] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-437] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-455] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-658] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-374] for track '53' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-401] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-407] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-426] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-434] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-446] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-458] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-464] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-472] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-482] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-491] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-520] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-538] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-556] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-564] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-605] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-616] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-375] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-383] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-622] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-405] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-664] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-433] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-547] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-628] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-648] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-656] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-665] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [667-683] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [694-695] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>