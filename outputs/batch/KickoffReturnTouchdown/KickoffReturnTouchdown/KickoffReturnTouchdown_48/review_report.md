# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_48

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_48`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 60
- **Ball Tracks:** 0
- **Action Segments:** 187
- **Validation Warnings:** 235
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 173
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `11` | `11` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `41` | `29` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `41` | `29` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `41` | `29` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `0` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `1` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `11` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `2` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `3` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `4` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `5` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `6` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `7` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `8` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `9` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `11` | `11` | 19 | START | 19 | 77 |
| ✅ EXACT | `Action_KickBall` | Kicker | `11` | `11` | 78 | START | 78 | 83 |
| ❌ MISSING SEGMENT | `Action_CatchKick` | Position_Unknown | `41` | `29` | 188 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `41` | `29` | 218 | START | 238 | 337 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `41` | `29` | 653 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–498
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_KickApproach` | 19 | 77 | 59 | inferred_complete_timeline |
| `Action_KickBall` | 78 | 83 | 6 | inferred_complete_timeline |
| `Action_None` | 84 | 132 | 49 | inferred_complete_timeline |
| `Action_None` | 134 | 490 | 357 | inferred_complete_timeline |
| `Action_None` | 492 | 498 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–360
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 344 | 326 | inferred_complete_timeline |
| `Action_None` | 346 | 355 | 10 | inferred_complete_timeline |
| `Action_None` | 359 | 360 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 653

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 162 | 144 | inferred_complete_timeline |
| `Action_None` | 169 | 402 | 234 | inferred_complete_timeline |
| `Action_None` | 404 | 659 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–495
- **Visible Samples:** 487

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 346 | 328 | inferred_complete_timeline |
| `Action_None` | 350 | 383 | 34 | inferred_complete_timeline |
| `Action_None` | 390 | 495 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 270 | 252 | inferred_complete_timeline |
| `Action_None` | 276 | 289 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–536
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 536 | 518 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 118 | 100 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_None` | 134 | 319 | 186 | inferred_complete_timeline |
| `Action_None` | 323 | 324 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–303
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 303 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 654

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 125 | 107 | inferred_complete_timeline |
| `Action_None` | 127 | 263 | 137 | inferred_complete_timeline |
| `Action_None` | 265 | 578 | 314 | inferred_complete_timeline |
| `Action_None` | 581 | 582 | 2 | inferred_complete_timeline |
| `Action_None` | 585 | 659 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–365
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 365 | 347 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 657

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 439 | 421 | inferred_complete_timeline |
| `Action_None` | 443 | 659 | 217 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 110 | 92 | inferred_complete_timeline |
| `Action_None` | 113 | 117 | 5 | inferred_complete_timeline |
| `Action_None` | 123 | 126 | 4 | inferred_complete_timeline |
| `Action_None` | 128 | 143 | 16 | inferred_complete_timeline |
| `Action_None` | 145 | 153 | 9 | inferred_complete_timeline |
| `Action_None` | 155 | 164 | 10 | inferred_complete_timeline |
| `Action_None` | 166 | 172 | 7 | inferred_complete_timeline |
| `Action_None` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_None` | 181 | 188 | 8 | inferred_complete_timeline |
| `Action_None` | 190 | 193 | 4 | inferred_complete_timeline |
| `Action_None` | 200 | 210 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–360
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 48 | 30 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 82 | 85 | 4 | inferred_complete_timeline |
| `Action_None` | 87 | 94 | 8 | inferred_complete_timeline |
| `Action_None` | 97 | 108 | 12 | inferred_complete_timeline |
| `Action_None` | 112 | 118 | 7 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 137 | 11 | inferred_complete_timeline |
| `Action_None` | 139 | 147 | 9 | inferred_complete_timeline |
| `Action_None` | 149 | 153 | 5 | inferred_complete_timeline |
| `Action_None` | 155 | 167 | 13 | inferred_complete_timeline |
| `Action_None` | 172 | 186 | 15 | inferred_complete_timeline |
| `Action_None` | 190 | 195 | 6 | inferred_complete_timeline |
| `Action_None` | 198 | 213 | 16 | inferred_complete_timeline |
| `Action_None` | 220 | 305 | 86 | inferred_complete_timeline |
| `Action_None` | 359 | 360 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 10 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 19 | 26 | 8 | inferred_complete_timeline |
| `Action_None` | 28 | 45 | 18 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_None` | 51 | 54 | 4 | inferred_complete_timeline |
| `Action_None` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_None` | 61 | 66 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–368
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 368 | 350 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 18 | 5 | inferred_complete_timeline |
| `Action_None` | 19 | 46 | 28 | inferred_complete_timeline |
| `Action_None` | 53 | 79 | 27 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 98 | 103 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 287 | 269 | inferred_complete_timeline |
| `Action_None` | 294 | 295 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–403
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 160 | 142 | inferred_complete_timeline |
| `Action_None` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 176 | 201 | 26 | inferred_complete_timeline |
| `Action_None` | 203 | 205 | 3 | inferred_complete_timeline |
| `Action_None` | 207 | 245 | 39 | inferred_complete_timeline |
| `Action_None` | 250 | 345 | 96 | inferred_complete_timeline |
| `Action_None` | 351 | 353 | 3 | inferred_complete_timeline |
| `Action_None` | 355 | 403 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 258 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 265 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–486
- **Visible Samples:** 487

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 486 | 468 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 4–263 | 250 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 57–63 | 6 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 68–69 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 109–117 | 5 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 114–115 | 2 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 117–119 | 3 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 117–498 | 329 | 7 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 225–466 | 231 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 238–501 | 242 | 5 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 275–463 | 167 | 4 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 275–659 | 385 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 284–482 | 149 | 4 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 285–554 | 265 | 3 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 303–659 | 356 | 2 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 311–391 | 71 | 3 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 333–447 | 113 | 2 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 334–659 | 325 | 2 | Undefined position; Undefined team |
| `38` | `63` | Position_Unknown | Team_Unknown | 376–573 | 198 | 1 | Undefined position; Undefined team |
| `39` | `65` | Position_Unknown | Team_Unknown | 409–435 | 27 | 1 | Undefined position; Undefined team |
| `40` | `66` | Position_Unknown | Team_Unknown | 411–659 | 248 | 2 | Undefined position; Undefined team |
| `41` | `68` | Position_Unknown | Team_Unknown | 421–659 | 237 | 2 | Undefined position; Undefined team |
| `42` | `69` | Position_Unknown | Team_Unknown | 429–652 | 217 | 4 | Undefined position; Undefined team |
| `43` | `70` | Position_Unknown | Team_Unknown | 439–659 | 221 | 1 | Undefined position; Undefined team |
| `44` | `75` | Position_Unknown | Team_Unknown | 505–510 | 6 | 1 | Undefined position; Undefined team |
| `45` | `76` | Position_Unknown | Team_Unknown | 546–547 | 2 | 1 | Undefined position; Undefined team |
| `46` | `77` | Position_Unknown | Team_Unknown | 549–567 | 13 | 3 | Undefined position; Undefined team |
| `47` | `78` | Position_Unknown | Team_Unknown | 555–558 | 4 | 1 | Undefined position; Undefined team |
| `48` | `79` | Position_Unknown | Team_Unknown | 558–569 | 12 | 1 | Undefined position; Undefined team |
| `49` | `80` | Position_Unknown | Team_Unknown | 561–568 | 7 | 2 | Undefined position; Undefined team |
| `50` | `84` | Position_Unknown | Team_Unknown | 596–649 | 54 | 1 | Undefined position; Undefined team |
| `51` | `86` | Position_Unknown | Team_Unknown | 599–659 | 61 | 1 | Undefined position; Undefined team |
| `52` | `89` | Position_Unknown | Team_Unknown | 601–659 | 59 | 1 | Undefined position; Undefined team |
| `53` | `91` | Position_Unknown | Team_Unknown | 602–659 | 58 | 1 | Undefined position; Undefined team |
| `54` | `94` | Position_Unknown | Team_Unknown | 620–629 | 5 | 2 | Undefined position; Undefined team |
| `55` | `95` | Position_Unknown | Team_Unknown | 620–654 | 7 | 2 | Undefined position; Undefined team |
| `56` | `103` | Position_Unknown | Team_Unknown | 631–659 | 29 | 1 | Undefined position; Undefined team |
| `57` | `106` | Position_Unknown | Team_Unknown | 633–659 | 24 | 2 | Undefined position; Undefined team |
| `58` | `108` | Position_Unknown | Team_Unknown | 638–647 | 10 | 1 | Undefined position; Undefined team |
| `59` | `109` | Position_Unknown | Team_Unknown | 641–642 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CatchKick` on target `41` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `41` (5 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `41` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Second_Level_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ 39 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 39 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 78 |
| Missing visible bounding boxes during action | 154 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Segment 'Action_CatchKick' for track '29' has invalid range: start=238, end=197. Clamping end to start.
- ⚠️ Segment 'Action_CrossGoalLine' for track '29' has invalid range: start=653, end=501. Clamping end to start.
- ⚠️ Action 'Action_None' range [19-162] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-402] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-365] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-303] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-346] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-383] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-495] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-344] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-355] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-270] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-289] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-125] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-263] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-578] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-582] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-439] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-536] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-319] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-265] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-132] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-490] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-498] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-143] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-153] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-258] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-160] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-201] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-245] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-345] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-353] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-403] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-287] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-486] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-368] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-46] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-103] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-94] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-108] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-137] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-167] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-186] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-195] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-213] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-305] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-10] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-26] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-45] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-66] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-177] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-209] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-263] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-60] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-162] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-194] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-268] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-286] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-354] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-404] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-498] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-318] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-466] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [238-337] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [351-361] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [366-368] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [370-406] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [411-501] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-306] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-338] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-344] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-463] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-306] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-357] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-482] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-536] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-542] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-554] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-355] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-659] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-376] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-386] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-346] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-447] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-406] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-659] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-573] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-435] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-418] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-659] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-505] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-659] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-629] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-642] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-649] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-652] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-510] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-547] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-550] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-560] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-558] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-569] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-565] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-568] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-649] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-622] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-629] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-624] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [653-654] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-649] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-647] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [641-642] for track '59' has 1 frames without a visible bounding box.
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

</details>