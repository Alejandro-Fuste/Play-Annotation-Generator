# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_67

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_67`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 82
- **Ball Tracks:** 0
- **Action Segments:** 320
- **Validation Warnings:** 424
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 302
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `5` | `5` |
| ⚠️ START CHANGED | `Action_KickBall` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `37` | `31` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `37` | `31` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `37` | `31` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `12` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `13` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `14` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `2` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `5` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `6` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `7` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `8` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `9` | `Group` | 0 | START | 0 | 20 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `5` | `5` | 21 | START | 21 | 100 |
| ⚠️ START CHANGED | `Action_KickBall` | Kicker | `5` | `5` | 101 | START | 104 | 107 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `37` | `31` | 200 | START | 200 | 219 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `37` | `31` | 250 | START | 250 | 297 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `37` | `31` | 630 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_KickApproach` | 21 | 100 | 80 | inferred_complete_timeline |
| `Action_KickBall` | 104 | 107 | 4 | inferred_complete_timeline |
| `Action_None` | 108 | 117 | 10 | inferred_complete_timeline |
| `Action_None` | 123 | 168 | 46 | inferred_complete_timeline |
| `Action_None` | 182 | 196 | 15 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |
| `Action_None` | 212 | 222 | 11 | inferred_complete_timeline |
| `Action_None` | 233 | 255 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 6 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 20 | 12 | inferred_complete_timeline |
| `Action_None` | 21 | 38 | 18 | inferred_complete_timeline |
| `Action_None` | 40 | 45 | 6 | inferred_complete_timeline |
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–10
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 10 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 57 | 37 | inferred_complete_timeline |
| `Action_None` | 66 | 69 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 45 | 25 | inferred_complete_timeline |
| `Action_None` | 49 | 53 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 105 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 81 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 62 | 42 | inferred_complete_timeline |
| `Action_None` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_None` | 76 | 78 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 85 | 65 | inferred_complete_timeline |
| `Action_None` | 91 | 94 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 617

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 146 | 126 | inferred_complete_timeline |
| `Action_None` | 150 | 241 | 92 | inferred_complete_timeline |
| `Action_None` | 243 | 332 | 90 | inferred_complete_timeline |
| `Action_None` | 339 | 384 | 46 | inferred_complete_timeline |
| `Action_None` | 386 | 526 | 141 | inferred_complete_timeline |
| `Action_None` | 529 | 629 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 606

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 202 | 182 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 275 | 67 | inferred_complete_timeline |
| `Action_None` | 277 | 360 | 84 | inferred_complete_timeline |
| `Action_None` | 362 | 436 | 75 | inferred_complete_timeline |
| `Action_None` | 438 | 449 | 12 | inferred_complete_timeline |
| `Action_None` | 451 | 453 | 3 | inferred_complete_timeline |
| `Action_None` | 455 | 565 | 111 | inferred_complete_timeline |
| `Action_None` | 582 | 629 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 120 | 100 | inferred_complete_timeline |
| `Action_None` | 123 | 130 | 8 | inferred_complete_timeline |
| `Action_None` | 138 | 149 | 12 | inferred_complete_timeline |
| `Action_None` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_None` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_None` | 167 | 173 | 7 | inferred_complete_timeline |
| `Action_None` | 175 | 202 | 28 | inferred_complete_timeline |
| `Action_None` | 205 | 209 | 5 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 219 | 3 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 228 | 275 | 48 | inferred_complete_timeline |
| `Action_None` | 277 | 282 | 6 | inferred_complete_timeline |
| `Action_None` | 288 | 290 | 3 | inferred_complete_timeline |
| `Action_None` | 298 | 300 | 3 | inferred_complete_timeline |
| `Action_None` | 302 | 309 | 8 | inferred_complete_timeline |
| `Action_None` | 312 | 358 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 166 | 146 | inferred_complete_timeline |
| `Action_None` | 168 | 177 | 10 | inferred_complete_timeline |
| `Action_None` | 179 | 199 | 21 | inferred_complete_timeline |
| `Action_None` | 201 | 206 | 6 | inferred_complete_timeline |
| `Action_None` | 208 | 213 | 6 | inferred_complete_timeline |
| `Action_None` | 216 | 240 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–334
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 146 | 126 | inferred_complete_timeline |
| `Action_None` | 154 | 269 | 116 | inferred_complete_timeline |
| `Action_None` | 271 | 305 | 35 | inferred_complete_timeline |
| `Action_None` | 308 | 334 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 611

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 133 | 113 | inferred_complete_timeline |
| `Action_None` | 135 | 343 | 209 | inferred_complete_timeline |
| `Action_None` | 356 | 366 | 11 | inferred_complete_timeline |
| `Action_None` | 372 | 373 | 2 | inferred_complete_timeline |
| `Action_None` | 375 | 629 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 605

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 234 | 214 | inferred_complete_timeline |
| `Action_None` | 236 | 276 | 41 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 291 | 305 | 15 | inferred_complete_timeline |
| `Action_None` | 307 | 320 | 14 | inferred_complete_timeline |
| `Action_None` | 324 | 326 | 3 | inferred_complete_timeline |
| `Action_None` | 332 | 574 | 243 | inferred_complete_timeline |
| `Action_None` | 577 | 578 | 2 | inferred_complete_timeline |
| `Action_None` | 580 | 629 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 236 | 216 | inferred_complete_timeline |
| `Action_None` | 238 | 441 | 204 | inferred_complete_timeline |
| `Action_None` | 443 | 468 | 26 | inferred_complete_timeline |
| `Action_None` | 470 | 629 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 51–119 | 69 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 67–273 | 207 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 80–294 | 215 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 94–489 | 346 | 9 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 103–216 | 90 | 6 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 109–349 | 210 | 15 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 126–297 | 170 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 128–464 | 293 | 13 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 132–133 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 138–140 | 3 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 141–164 | 20 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 142–143 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 148–252 | 105 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 151–152 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 152–331 | 167 | 9 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 155–157 | 3 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 168–252 | 72 | 4 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 173–336 | 117 | 3 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 179–262 | 82 | 3 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 184–280 | 92 | 2 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 215–216 | 2 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 234–629 | 349 | 11 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 234–236 | 3 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 272–274 | 3 | 1 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 276–360 | 45 | 6 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 289–397 | 19 | 3 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 290–629 | 312 | 8 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 311–328 | 18 | 1 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 312–414 | 93 | 5 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 313–406 | 94 | 1 | Undefined position; Undefined team |
| `48` | `70` | Position_Unknown | Team_Unknown | 333–629 | 282 | 4 | Undefined position; Undefined team |
| `49` | `72` | Position_Unknown | Team_Unknown | 336–403 | 20 | 3 | Undefined position; Undefined team |
| `50` | `73` | Position_Unknown | Team_Unknown | 337–359 | 23 | 1 | Undefined position; Undefined team |
| `51` | `75` | Position_Unknown | Team_Unknown | 356–629 | 239 | 15 | Undefined position; Undefined team |
| `52` | `76` | Position_Unknown | Team_Unknown | 357–629 | 270 | 3 | Undefined position; Undefined team |
| `53` | `77` | Position_Unknown | Team_Unknown | 357–358 | 2 | 1 | Undefined position; Undefined team |
| `54` | `78` | Position_Unknown | Team_Unknown | 359–464 | 80 | 10 | Undefined position; Undefined team |
| `55` | `79` | Position_Unknown | Team_Unknown | 363–629 | 266 | 2 | Undefined position; Undefined team |
| `56` | `81` | Position_Unknown | Team_Unknown | 375–629 | 236 | 5 | Undefined position; Undefined team |
| `57` | `83` | Position_Unknown | Team_Unknown | 375–629 | 247 | 4 | Undefined position; Undefined team |
| `58` | `84` | Position_Unknown | Team_Unknown | 377–397 | 13 | 3 | Undefined position; Undefined team |
| `59` | `85` | Position_Unknown | Team_Unknown | 381–584 | 199 | 4 | Undefined position; Undefined team |
| `60` | `87` | Position_Unknown | Team_Unknown | 392–629 | 204 | 4 | Undefined position; Undefined team |
| `61` | `88` | Position_Unknown | Team_Unknown | 392–629 | 123 | 4 | Undefined position; Undefined team |
| `62` | `89` | Position_Unknown | Team_Unknown | 411–629 | 219 | 1 | Undefined position; Undefined team |
| `63` | `91` | Position_Unknown | Team_Unknown | 423–629 | 169 | 8 | Undefined position; Undefined team |
| `64` | `93` | Position_Unknown | Team_Unknown | 454–629 | 176 | 1 | Undefined position; Undefined team |
| `65` | `94` | Position_Unknown | Team_Unknown | 456–629 | 174 | 1 | Undefined position; Undefined team |
| `66` | `97` | Position_Unknown | Team_Unknown | 464–466 | 3 | 1 | Undefined position; Undefined team |
| `67` | `98` | Position_Unknown | Team_Unknown | 465–466 | 2 | 1 | Undefined position; Undefined team |
| `68` | `99` | Position_Unknown | Team_Unknown | 469–472 | 4 | 1 | Undefined position; Undefined team |
| `69` | `100` | Position_Unknown | Team_Unknown | 471–629 | 158 | 2 | Undefined position; Undefined team |
| `70` | `101` | Position_Unknown | Team_Unknown | 484–509 | 24 | 2 | Undefined position; Undefined team |
| `71` | `103` | Position_Unknown | Team_Unknown | 485–629 | 145 | 1 | Undefined position; Undefined team |
| `72` | `105` | Position_Unknown | Team_Unknown | 499–502 | 4 | 1 | Undefined position; Undefined team |
| `73` | `106` | Position_Unknown | Team_Unknown | 507–526 | 19 | 2 | Undefined position; Undefined team |
| `74` | `107` | Position_Unknown | Team_Unknown | 510–511 | 2 | 1 | Undefined position; Undefined team |
| `75` | `108` | Position_Unknown | Team_Unknown | 512–513 | 2 | 1 | Undefined position; Undefined team |
| `76` | `109` | Position_Unknown | Team_Unknown | 520–608 | 19 | 7 | Undefined position; Undefined team |
| `77` | `112` | Position_Unknown | Team_Unknown | 540–547 | 8 | 1 | Undefined position; Undefined team |
| `78` | `113` | Position_Unknown | Team_Unknown | 585–592 | 7 | 2 | Undefined position; Undefined team |
| `79` | `114` | Position_Unknown | Team_Unknown | 598–623 | 10 | 2 | Undefined position; Undefined team |
| `80` | `115` | Position_Unknown | Team_Unknown | 615–624 | 8 | 2 | Undefined position; Undefined team |
| `81` | `116` | Position_Unknown | Team_Unknown | 620–628 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_KickBall` for actor_track_id `5` (Kicker): Annotated start 101 != Inferred start 104
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `37` (3 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `37` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ 65 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 65 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 130 |
| Missing visible bounding boxes during action | 291 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '31' has invalid range: start=630, end=331. Clamping end to start.
- ⚠️ Action 'Action_None' range [21-133] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-343] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-366] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-629] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-234] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-276] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-305] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-320] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-574] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-629] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-85] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-120] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-130] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-149] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-173] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-202] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-275] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-282] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-300] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-309] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-358] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-177] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-199] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-213] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-240] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [21-100] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-168] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-196] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-222] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-255] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-202] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-275] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-360] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-436] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-449] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-453] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-565] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-146] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-241] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-332] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-384] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-526] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-105] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-269] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-305] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-334] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-236] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-441] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-468] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-629] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-62] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-57] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-10] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-6] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-38] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-45] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-119] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-273] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-294] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-117] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-232] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-287] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-304] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-380] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-459] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-489] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-119] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-145] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-216] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-119] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-126] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-144] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-166] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-174] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-203] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-227] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-270] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-301] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-339] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-349] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-293] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-139] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-148] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-196] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-293] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-357] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-367] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-384] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-402] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-451] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-458] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-158] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-252] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-156] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-161] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-164] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [250-297] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [302-305] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [308-331] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-230] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-281] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-336] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-262] for track '36' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-280] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-404] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-466] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-475] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-480] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-495] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-504] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-609] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-613] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-288] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-334] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-350] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-360] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-389] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-397] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-322] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-436] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-511] for track '44' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-518] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-523] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-540] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-587] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-328] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-347] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-366] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-414] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-406] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-339] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-361] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-434] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-629] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-347] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-373] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-403] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-359] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-416] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-452] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-466] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-473] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-500] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-532] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-549] for track '51' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-558] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-571] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-575] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-584] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-609] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-616] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-403] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-502] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-629] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-369] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-386] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-391] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-398] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-431] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-445] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-459] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-464] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-384] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-457] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-487] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-528] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-603] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-379] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-402] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-629] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-382] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-389] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-397] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-396] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-401] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-436] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-584] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-409] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-426] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-400] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-425] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-492] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-432] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-451] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-466] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-480] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-490] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-496] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-629] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-629] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-629] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-466] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-466] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-472] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-475] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-629] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-494] for track '70' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-509] for track '70' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-629] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-502] for track '72' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-511] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-526] for track '73' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-511] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-513] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-525] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-528] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-566] for track '76' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-569] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-574] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-608] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-547] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-587] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-592] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-605] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-623] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-617] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-624] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-628] for track '81' has 2 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 630. Video range is [0, 629].

</details>