# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_81

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_81`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 92
- **Ball Tracks:** 0
- **Action Segments:** 335
- **Validation Warnings:** 446
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 320
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Position_Unknown | Team_Unknown | `22` | `22` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `14` | `14` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `14` | `14` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `46` | `38` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `46` | `38` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Interior_Rusher2 | defense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `12` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `14` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `15` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `17` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `19` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `2` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `20` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `5` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `9` | `Group` | 0 | START | 0 | 63 |
| ✅ EXACT | `Action_LongSnap` | Position_Unknown | `22` | `22` | 64 | START | 64 | 118 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `14` | `14` | 90 | END | 90 | 90 |
| ✅ EXACT | `Action_PuntBall` | Punter | `14` | `14` | 119 | START | 119 | 136 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `46` | `38` | 268 | START | 268 | 274 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `46` | `38` | 291 | START | 291 | 382 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Interior_Rusher2 | `7` | `7` | 593 | START | N/A | N/A |

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
- **Visible Frames:** 0–253
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 112 | 49 | inferred_complete_timeline |
| `Action_None` | 115 | 177 | 63 | inferred_complete_timeline |
| `Action_None` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_None` | 184 | 208 | 25 | inferred_complete_timeline |
| `Action_None` | 210 | 220 | 11 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_None` | 236 | 241 | 6 | inferred_complete_timeline |
| `Action_None` | 246 | 253 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 86 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 88 | 25 | inferred_complete_timeline |
| `Action_None` | 90 | 114 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 96 | 33 | inferred_complete_timeline |
| `Action_None` | 106 | 109 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 110 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–594
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 345 | 282 | inferred_complete_timeline |
| `Action_None` | 347 | 364 | 18 | inferred_complete_timeline |
| `Action_None` | 366 | 376 | 11 | inferred_complete_timeline |
| `Action_None` | 378 | 560 | 183 | inferred_complete_timeline |
| `Action_None` | 562 | 586 | 25 | inferred_complete_timeline |
| `Action_None` | 591 | 594 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_SnapReceive` | 90 | 90 | 1 | inferred_complete_timeline |
| `Action_None` | 91 | 118 | 28 | inferred_complete_timeline |
| `Action_PuntBall` | 119 | 136 | 18 | inferred_complete_timeline |
| `Action_None` | 137 | 143 | 7 | inferred_complete_timeline |
| `Action_None` | 149 | 153 | 5 | inferred_complete_timeline |
| `Action_None` | 155 | 170 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–315
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 80 | 17 | inferred_complete_timeline |
| `Action_None` | 82 | 110 | 29 | inferred_complete_timeline |
| `Action_None` | 125 | 202 | 78 | inferred_complete_timeline |
| `Action_None` | 204 | 209 | 6 | inferred_complete_timeline |
| `Action_None` | 211 | 219 | 9 | inferred_complete_timeline |
| `Action_None` | 221 | 233 | 13 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 238 | 247 | 10 | inferred_complete_timeline |
| `Action_None` | 259 | 275 | 17 | inferred_complete_timeline |
| `Action_None` | 278 | 282 | 5 | inferred_complete_timeline |
| `Action_None` | 313 | 315 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–343
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 343 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 85 | 22 | inferred_complete_timeline |
| `Action_None` | 87 | 138 | 52 | inferred_complete_timeline |
| `Action_None` | 141 | 148 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 193 | 130 | inferred_complete_timeline |
| `Action_None` | 196 | 198 | 3 | inferred_complete_timeline |
| `Action_None` | 206 | 247 | 42 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 265 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 243 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 63 | 19 | inferred_complete_timeline |
| `Action_None` | 64 | 202 | 139 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |
| `Action_None` | 214 | 216 | 3 | inferred_complete_timeline |
| `Action_None` | 221 | 235 | 15 | inferred_complete_timeline |
| `Action_None` | 238 | 245 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 141 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–282
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 253 | 190 | inferred_complete_timeline |
| `Action_None` | 261 | 273 | 13 | inferred_complete_timeline |
| `Action_None` | 275 | 282 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 110 | 47 | inferred_complete_timeline |
| `Action_None` | 112 | 115 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 299 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 209 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 172 | 109 | inferred_complete_timeline |
| `Action_None` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_None` | 186 | 220 | 35 | inferred_complete_timeline |
| `Action_None` | 222 | 225 | 4 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–98 | 76 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–104 | 85 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 7–418 | 403 | 11 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 100–120 | 21 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 112–398 | 275 | 9 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 115–351 | 198 | 9 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 125–126 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 136–159 | 17 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 136–449 | 293 | 7 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 137–233 | 97 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 153–596 | 401 | 10 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 161–378 | 215 | 3 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 163–168 | 6 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 167–169 | 3 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 181–353 | 139 | 9 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 182–265 | 61 | 6 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 195–235 | 34 | 2 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 211–353 | 22 | 5 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 215–401 | 174 | 5 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 224–599 | 333 | 6 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 231–599 | 333 | 8 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 239–330 | 71 | 7 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 242–283 | 8 | 2 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 261–412 | 123 | 2 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 261–366 | 38 | 9 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 263–283 | 20 | 2 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 275–322 | 6 | 2 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 280–282 | 3 | 1 | Undefined position; Undefined team |
| `49` | `68` | Position_Unknown | Team_Unknown | 289–292 | 4 | 1 | Undefined position; Undefined team |
| `50` | `69` | Position_Unknown | Team_Unknown | 290–392 | 99 | 2 | Undefined position; Undefined team |
| `51` | `72` | Position_Unknown | Team_Unknown | 306–308 | 3 | 1 | Undefined position; Undefined team |
| `52` | `74` | Position_Unknown | Team_Unknown | 312–316 | 5 | 1 | Undefined position; Undefined team |
| `53` | `75` | Position_Unknown | Team_Unknown | 313–314 | 2 | 1 | Undefined position; Undefined team |
| `54` | `76` | Position_Unknown | Team_Unknown | 314–360 | 5 | 2 | Undefined position; Undefined team |
| `55` | `77` | Position_Unknown | Team_Unknown | 314–322 | 9 | 1 | Undefined position; Undefined team |
| `56` | `80` | Position_Unknown | Team_Unknown | 320–409 | 37 | 4 | Undefined position; Undefined team |
| `57` | `83` | Position_Unknown | Team_Unknown | 324–412 | 81 | 3 | Undefined position; Undefined team |
| `58` | `87` | Position_Unknown | Team_Unknown | 332–449 | 51 | 5 | Undefined position; Undefined team |
| `59` | `89` | Position_Unknown | Team_Unknown | 334–338 | 5 | 1 | Undefined position; Undefined team |
| `60` | `91` | Position_Unknown | Team_Unknown | 336–364 | 25 | 2 | Undefined position; Undefined team |
| `61` | `96` | Position_Unknown | Team_Unknown | 349–386 | 13 | 3 | Undefined position; Undefined team |
| `62` | `100` | Position_Unknown | Team_Unknown | 357–598 | 221 | 4 | Undefined position; Undefined team |
| `63` | `103` | Position_Unknown | Team_Unknown | 362–502 | 134 | 3 | Undefined position; Undefined team |
| `64` | `105` | Position_Unknown | Team_Unknown | 367–599 | 217 | 8 | Undefined position; Undefined team |
| `65` | `106` | Position_Unknown | Team_Unknown | 369–416 | 40 | 2 | Undefined position; Undefined team |
| `66` | `107` | Position_Unknown | Team_Unknown | 371–599 | 196 | 6 | Undefined position; Undefined team |
| `67` | `108` | Position_Unknown | Team_Unknown | 375–455 | 25 | 5 | Undefined position; Undefined team |
| `68` | `109` | Position_Unknown | Team_Unknown | 376–377 | 2 | 1 | Undefined position; Undefined team |
| `69` | `110` | Position_Unknown | Team_Unknown | 376–599 | 158 | 4 | Undefined position; Undefined team |
| `70` | `116` | Position_Unknown | Team_Unknown | 406–419 | 11 | 2 | Undefined position; Undefined team |
| `71` | `117` | Position_Unknown | Team_Unknown | 412–448 | 24 | 3 | Undefined position; Undefined team |
| `72` | `119` | Position_Unknown | Team_Unknown | 416–489 | 73 | 2 | Undefined position; Undefined team |
| `73` | `120` | Position_Unknown | Team_Unknown | 417–419 | 3 | 1 | Undefined position; Undefined team |
| `74` | `122` | Position_Unknown | Team_Unknown | 437–464 | 11 | 3 | Undefined position; Undefined team |
| `75` | `123` | Position_Unknown | Team_Unknown | 437–599 | 128 | 7 | Undefined position; Undefined team |
| `76` | `124` | Position_Unknown | Team_Unknown | 437–449 | 13 | 1 | Undefined position; Undefined team |
| `77` | `125` | Position_Unknown | Team_Unknown | 437–599 | 153 | 4 | Undefined position; Undefined team |
| `78` | `127` | Position_Unknown | Team_Unknown | 440–599 | 101 | 5 | Undefined position; Undefined team |
| `79` | `128` | Position_Unknown | Team_Unknown | 453–483 | 23 | 3 | Undefined position; Undefined team |
| `80` | `132` | Position_Unknown | Team_Unknown | 475–476 | 2 | 1 | Undefined position; Undefined team |
| `81` | `133` | Position_Unknown | Team_Unknown | 492–561 | 67 | 2 | Undefined position; Undefined team |
| `82` | `136` | Position_Unknown | Team_Unknown | 496–599 | 104 | 1 | Undefined position; Undefined team |
| `83` | `137` | Position_Unknown | Team_Unknown | 497–599 | 92 | 3 | Undefined position; Undefined team |
| `84` | `139` | Position_Unknown | Team_Unknown | 498–599 | 102 | 1 | Undefined position; Undefined team |
| `85` | `141` | Position_Unknown | Team_Unknown | 499–599 | 84 | 3 | Undefined position; Undefined team |
| `86` | `142` | Position_Unknown | Team_Unknown | 500–516 | 17 | 1 | Undefined position; Undefined team |
| `87` | `143` | Position_Unknown | Team_Unknown | 507–510 | 4 | 1 | Undefined position; Undefined team |
| `88` | `145` | Position_Unknown | Team_Unknown | 525–599 | 63 | 4 | Undefined position; Undefined team |
| `89` | `147` | Position_Unknown | Team_Unknown | 538–598 | 48 | 5 | Undefined position; Undefined team |
| `90` | `150` | Position_Unknown | Team_Unknown | 546–571 | 23 | 3 | Undefined position; Undefined team |
| `91` | `151` | Position_Unknown | Team_Unknown | 567–599 | 23 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `46` (2 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `7` (Interior_Rusher2)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Guard` position mapped to `offense` team
- ⚠️ 72 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 72 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 144 |
| Missing visible bounding boxes during action | 298 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_CrossGoalLine' for track '7' has invalid range: start=593, end=152. Clamping end to start.
- ⚠️ Action 'Action_None' range [64-172] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-220] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-110] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-343] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-209] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-110] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-193] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-247] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-243] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-86] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-253] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-273] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-282] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-141] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-148] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-202] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-235] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-245] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-345] for track '15' has 9 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-364] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-376] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-560] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-586] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-594] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-220] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-241] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-88] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-114] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-71] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-110] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-202] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-219] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-233] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-247] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-275] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-282] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-75] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-176] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-310] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-392] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-409] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-418] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-120] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-220] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-234] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-250] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-287] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-317] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-333] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-398] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-154] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-170] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-243] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-267] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-327] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-342] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-351] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-154] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-143] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-172] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-257] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-423] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-442] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-449] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-233] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-187] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-294] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-344] for track '30' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-360] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-449] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-590] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-596] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-280] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-310] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-378] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-233] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-247] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-266] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-282] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-294] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-304] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-317] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-353] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-194] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-220] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-241] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-225] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-268] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-282] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [291-382] for track '38' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [396-401] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-407] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-515] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-599] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-426] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-449] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-452] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-462] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-481] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-554] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-558] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-255] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-282] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-308] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-316] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-330] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-247] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-381] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-265] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-301] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-315] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-366] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-268] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-283] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-322] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-350] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-392] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-316] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-316] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-322] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-335] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-392] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-409] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-367] for track '57' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-379] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-412] for track '57' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-344] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-356] for track '58' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-367] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-449] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-338] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-364] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-353] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-379] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-386] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-381] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-578] for track '62' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-584] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-598] for track '62' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-421] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-494] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-502] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-391] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-406] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-481] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-489] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-495] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-554] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-562] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-376] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-416] for track '65' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-404] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-418] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-449] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-599] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-449] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-455] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-443] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-595] for track '69' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-419] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-422] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-448] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-421] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-489] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-419] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-442] for track '74' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-464] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-449] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-465] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-481] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-506] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-555] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-566] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-449] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-572] for track '77' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-582] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-590] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-599] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-448] for track '78' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-526] for track '78' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-583] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-593] for track '78' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-466] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-477] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-483] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-476] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-554] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-561] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-559] for track '83' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-566] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-599] for track '84' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-554] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-577] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-599] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-516] for track '86' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-510] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-527] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-561] for track '88' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-588] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-567] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-575] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-582] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-588] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-598] for track '89' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-557] for track '90' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-563] for track '90' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-571] for track '90' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-575] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>