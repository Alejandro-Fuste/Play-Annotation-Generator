# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_60

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_60`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 509
- **Player Tracks:** 87
- **Ball Tracks:** 0
- **Action Segments:** 321
- **Validation Warnings:** 447
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 308
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `41` | `33` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `41` | `33` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `125` | `78` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `1` | `Group` | 3 | START | 3 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `11` | `Group` | 3 | START | 3 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `2` | `Group` | 3 | START | 3 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `3` | `Group` | 3 | START | 3 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `4` | `Group` | 3 | START | 3 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `6` | `Group` | 3 | START | 3 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `9` | `Group` | 3 | START | 3 | 76 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `9` | `9` | 77 | START | 77 | 132 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `6` | `6` | 106 | END | 106 | 106 |
| ✅ EXACT | `Action_PuntBall` | Punter | `6` | `6` | 133 | START | 133 | 141 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `41` | `33` | 225 | START | 225 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `41` | `33` | 251 | START | 251 | 405 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `125` | `78` | 501 | START | 501 | 508 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 3–509
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 76 | 74 | inferred_complete_timeline |
| `Action_None` | 77 | 201 | 125 | inferred_complete_timeline |
| `Action_None` | 204 | 269 | 66 | inferred_complete_timeline |
| `Action_None` | 273 | 307 | 35 | inferred_complete_timeline |
| `Action_None` | 309 | 407 | 99 | inferred_complete_timeline |
| `Action_None` | 427 | 455 | 29 | inferred_complete_timeline |
| `Action_None` | 463 | 464 | 2 | inferred_complete_timeline |
| `Action_None` | 468 | 472 | 5 | inferred_complete_timeline |
| `Action_None` | 480 | 509 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 3–144
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 76 | 74 | inferred_complete_timeline |
| `Action_None` | 77 | 144 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 3–303
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 76 | 74 | inferred_complete_timeline |
| `Action_LongSnap` | 77 | 132 | 56 | inferred_complete_timeline |
| `Action_None` | 133 | 303 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 3–509
- **Visible Samples:** 502

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 76 | 74 | inferred_complete_timeline |
| `Action_None` | 77 | 234 | 158 | inferred_complete_timeline |
| `Action_None` | 237 | 369 | 133 | inferred_complete_timeline |
| `Action_None` | 371 | 446 | 76 | inferred_complete_timeline |
| `Action_None` | 448 | 449 | 2 | inferred_complete_timeline |
| `Action_None` | 451 | 509 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 3–467
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 105 | 103 | inferred_complete_timeline |
| `Action_SnapReceive` | 106 | 106 | 1 | inferred_complete_timeline |
| `Action_None` | 107 | 132 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 133 | 141 | 9 | inferred_complete_timeline |
| `Action_None` | 146 | 153 | 8 | inferred_complete_timeline |
| `Action_None` | 166 | 174 | 9 | inferred_complete_timeline |
| `Action_None` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_None` | 184 | 213 | 30 | inferred_complete_timeline |
| `Action_None` | 217 | 303 | 87 | inferred_complete_timeline |
| `Action_None` | 308 | 423 | 116 | inferred_complete_timeline |
| `Action_None` | 426 | 430 | 5 | inferred_complete_timeline |
| `Action_None` | 435 | 460 | 26 | inferred_complete_timeline |
| `Action_None` | 466 | 467 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 3–169
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 76 | 74 | inferred_complete_timeline |
| `Action_None` | 77 | 120 | 44 | inferred_complete_timeline |
| `Action_None` | 123 | 149 | 27 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 3–187
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 76 | 74 | inferred_complete_timeline |
| `Action_None` | 77 | 159 | 83 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–83
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 76 | 74 | inferred_complete_timeline |
| `Action_None` | 77 | 83 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–140
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 42 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 48 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 76 | 27 | inferred_complete_timeline |
| `Action_None` | 78 | 140 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 3–133
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 11 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 15 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 28 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 76 | 42 | inferred_complete_timeline |
| `Action_None` | 77 | 94 | 18 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 133 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 3–311
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 40 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_None` | 77 | 77 | 1 | inferred_complete_timeline |
| `Action_None` | 82 | 92 | 11 | inferred_complete_timeline |
| `Action_None` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 109 | 122 | 14 | inferred_complete_timeline |
| `Action_None` | 124 | 172 | 49 | inferred_complete_timeline |
| `Action_None` | 182 | 186 | 5 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 311 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 3–219
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 76 | 74 | inferred_complete_timeline |
| `Action_None` | 77 | 189 | 113 | inferred_complete_timeline |
| `Action_None` | 191 | 219 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 3–326
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 17 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 28 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 48 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 55 | 6 | inferred_complete_timeline |
| `Action_None` | 89 | 98 | 10 | inferred_complete_timeline |
| `Action_None` | 100 | 105 | 6 | inferred_complete_timeline |
| `Action_None` | 109 | 200 | 92 | inferred_complete_timeline |
| `Action_None` | 202 | 210 | 9 | inferred_complete_timeline |
| `Action_None` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 220 | 5 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |
| `Action_None` | 225 | 282 | 58 | inferred_complete_timeline |
| `Action_None` | 285 | 326 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 3–152
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 13 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 76 | 62 | inferred_complete_timeline |
| `Action_None` | 77 | 98 | 22 | inferred_complete_timeline |
| `Action_None` | 102 | 108 | 7 | inferred_complete_timeline |
| `Action_None` | 124 | 152 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 3–179 | 138 | 8 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 7–158 | 136 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 26–313 | 167 | 12 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 81–85 | 5 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 95–318 | 190 | 4 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 95–453 | 331 | 10 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 113–189 | 53 | 5 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 129–332 | 192 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 133–230 | 95 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 165–219 | 45 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 174–198 | 20 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 176–216 | 39 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 176–251 | 74 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 181–193 | 13 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 185–191 | 7 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 192–194 | 3 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 194–332 | 127 | 4 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 195–211 | 4 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 195–217 | 22 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 197–420 | 221 | 6 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 197–200 | 4 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 199–222 | 23 | 2 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 202–204 | 3 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 209–211 | 3 | 1 | Undefined position; Undefined team |
| `39` | `61` | Position_Unknown | Team_Unknown | 210–211 | 2 | 1 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 211–247 | 26 | 2 | Undefined position; Undefined team |
| `41` | `64` | Position_Unknown | Team_Unknown | 212–242 | 29 | 2 | Undefined position; Undefined team |
| `42` | `71` | Position_Unknown | Team_Unknown | 218–260 | 38 | 2 | Undefined position; Undefined team |
| `43` | `72` | Position_Unknown | Team_Unknown | 218–235 | 12 | 2 | Undefined position; Undefined team |
| `44` | `73` | Position_Unknown | Team_Unknown | 218–285 | 25 | 4 | Undefined position; Undefined team |
| `45` | `74` | Position_Unknown | Team_Unknown | 218–238 | 16 | 2 | Undefined position; Undefined team |
| `46` | `76` | Position_Unknown | Team_Unknown | 225–226 | 2 | 1 | Undefined position; Undefined team |
| `47` | `77` | Position_Unknown | Team_Unknown | 226–509 | 277 | 5 | Undefined position; Undefined team |
| `48` | `78` | Position_Unknown | Team_Unknown | 228–509 | 239 | 4 | Undefined position; Undefined team |
| `49` | `79` | Position_Unknown | Team_Unknown | 228–233 | 6 | 1 | Undefined position; Undefined team |
| `50` | `82` | Position_Unknown | Team_Unknown | 232–236 | 4 | 2 | Undefined position; Undefined team |
| `51` | `84` | Position_Unknown | Team_Unknown | 235–250 | 11 | 2 | Undefined position; Undefined team |
| `52` | `86` | Position_Unknown | Team_Unknown | 244–417 | 165 | 3 | Undefined position; Undefined team |
| `53` | `90` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |
| `54` | `91` | Position_Unknown | Team_Unknown | 254–412 | 141 | 4 | Undefined position; Undefined team |
| `55` | `92` | Position_Unknown | Team_Unknown | 257–509 | 234 | 4 | Undefined position; Undefined team |
| `56` | `93` | Position_Unknown | Team_Unknown | 257–260 | 4 | 1 | Undefined position; Undefined team |
| `57` | `94` | Position_Unknown | Team_Unknown | 260–474 | 182 | 8 | Undefined position; Undefined team |
| `58` | `95` | Position_Unknown | Team_Unknown | 260–306 | 45 | 2 | Undefined position; Undefined team |
| `59` | `100` | Position_Unknown | Team_Unknown | 286–318 | 16 | 5 | Undefined position; Undefined team |
| `60` | `102` | Position_Unknown | Team_Unknown | 312–467 | 147 | 7 | Undefined position; Undefined team |
| `61` | `103` | Position_Unknown | Team_Unknown | 316–509 | 178 | 6 | Undefined position; Undefined team |
| `62` | `104` | Position_Unknown | Team_Unknown | 325–476 | 140 | 3 | Undefined position; Undefined team |
| `63` | `105` | Position_Unknown | Team_Unknown | 327–509 | 166 | 8 | Undefined position; Undefined team |
| `64` | `106` | Position_Unknown | Team_Unknown | 327–399 | 4 | 2 | Undefined position; Undefined team |
| `65` | `108` | Position_Unknown | Team_Unknown | 328–435 | 104 | 4 | Undefined position; Undefined team |
| `66` | `109` | Position_Unknown | Team_Unknown | 331–339 | 9 | 1 | Undefined position; Undefined team |
| `67` | `111` | Position_Unknown | Team_Unknown | 340–495 | 148 | 7 | Undefined position; Undefined team |
| `68` | `113` | Position_Unknown | Team_Unknown | 342–509 | 150 | 4 | Undefined position; Undefined team |
| `69` | `114` | Position_Unknown | Team_Unknown | 343–344 | 2 | 1 | Undefined position; Undefined team |
| `70` | `115` | Position_Unknown | Team_Unknown | 344–472 | 110 | 6 | Undefined position; Undefined team |
| `71` | `118` | Position_Unknown | Team_Unknown | 377–415 | 38 | 2 | Undefined position; Undefined team |
| `72` | `119` | Position_Unknown | Team_Unknown | 383–386 | 4 | 1 | Undefined position; Undefined team |
| `73` | `120` | Position_Unknown | Team_Unknown | 405–509 | 91 | 9 | Undefined position; Undefined team |
| `74` | `121` | Position_Unknown | Team_Unknown | 420–509 | 73 | 5 | Undefined position; Undefined team |
| `75` | `122` | Position_Unknown | Team_Unknown | 425–509 | 80 | 3 | Undefined position; Undefined team |
| `76` | `123` | Position_Unknown | Team_Unknown | 437–480 | 44 | 1 | Undefined position; Undefined team |
| `77` | `124` | Position_Unknown | Team_Unknown | 438–439 | 2 | 1 | Undefined position; Undefined team |
| `78` | `125` | Position_Unknown | Team_Unknown | 442–509 | 53 | 7 | Undefined position; Undefined team |
| `79` | `127` | Position_Unknown | Team_Unknown | 477–508 | 25 | 3 | Undefined position; Undefined team |
| `80` | `130` | Position_Unknown | Team_Unknown | 481–509 | 29 | 1 | Undefined position; Undefined team |
| `81` | `131` | Position_Unknown | Team_Unknown | 482–509 | 22 | 2 | Undefined position; Undefined team |
| `82` | `132` | Position_Unknown | Team_Unknown | 483–509 | 17 | 3 | Undefined position; Undefined team |
| `83` | `133` | Position_Unknown | Team_Unknown | 483–509 | 27 | 1 | Undefined position; Undefined team |
| `84` | `134` | Position_Unknown | Team_Unknown | 484–509 | 25 | 2 | Undefined position; Undefined team |
| `85` | `135` | Position_Unknown | Team_Unknown | 486–509 | 24 | 1 | Undefined position; Undefined team |
| `86` | `138` | Position_Unknown | Team_Unknown | 502–503 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `41` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ 73 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 73 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 146 |
| Missing visible bounding boxes during action | 297 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 122: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [77-189] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-219] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-201] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-269] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-307] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-407] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-455] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-472] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-144] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-149] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-159] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-83] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-132] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [133-141] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-153] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-213] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-303] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-423] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-430] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-460] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-467] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-42] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-48] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-76] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-140] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-11] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-15] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-28] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-76] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-133] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-76] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [77-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-303] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-25] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-64] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-70] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-107] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-145] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-179] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-234] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-369] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-446] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-509] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-17] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-28] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-48] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-105] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-200] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-282] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-326] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-40] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 77, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [77-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-122] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-311] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-13] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-108] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-8] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-28] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-96] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-236] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-261] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-296] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-121] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-318] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-230] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-253] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-403] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-408] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-414] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-422] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-429] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-453] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-189] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-262] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-302] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-332] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-168] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-194] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-230] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-219] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-191] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-197] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-216] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-198] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-233] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-251] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-193] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-202] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-306] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-316] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-332] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-217] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [251-405] for track '33' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [408-412] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [414-420] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-219] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-234] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-236] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-253] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-235] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-228] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-285] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-238] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-432] for track '47' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-442] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-457] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-509] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-278] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-488] for track '48' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-233] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-243] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-261] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-292] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-417] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-280] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-306] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-412] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-431] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-473] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-484] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-509] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-293] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-335] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-345] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-413] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-419] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-447] for track '57' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-460] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-474] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-299] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-306] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-290] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-415] for track '60' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-420] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-423] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-445] for track '60' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-453] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-467] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-397] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-421] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-455] for track '61' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-471] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-432] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-453] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-476] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-368] for track '63' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-419] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-446] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-467] for track '63' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-478] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-501] for track '63' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-509] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-409] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-415] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-435] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-339] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-408] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-436] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-448] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-476] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-495] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-378] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-457] for track '68' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-475] for track '68' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-358] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-423] for track '70' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-455] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-472] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-415] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-386] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-418] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-427] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-431] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-454] for track '73' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-465] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-472] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-482] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-487] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-509] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-438] for track '74' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-456] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-465] for track '74' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-509] for track '74' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-439] for track '75' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-454] for track '75' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-509] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-480] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-445] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [453-454] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-472] for track '78' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-478] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [480-500] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-480] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-508] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-509] for track '80' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-493] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-509] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-487] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-509] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-488] for track '84' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>