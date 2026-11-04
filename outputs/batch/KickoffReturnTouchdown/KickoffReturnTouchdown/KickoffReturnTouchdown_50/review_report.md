# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_50

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_50`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 191
- **Validation Warnings:** 229
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 177
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `11` | `11` |
| ⚠️ START CHANGED | `Action_KickBall` | Position_Unknown | Team_Unknown | `27` | `24` |
| ⚠️ START CHANGED | `Action_CatchKick` | Position_Unknown | Team_Unknown | `34` | `27` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `34` | `27` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `0` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `1` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `10` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `11` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `2` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `3` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `4` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `5` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `7` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `9` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `11` | `11` | 24 | START | 24 | 77 |
| ⚠️ START CHANGED | `Action_KickBall` | Position_Unknown | `27` | `24` | 112 | START | 123 | 123 |
| ⚠️ START CHANGED | `Action_CatchKick` | Position_Unknown | `34` | `27` | 225 | START | 238 | 238 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `34` | `27` | 243 | START | 247 | 248 |

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
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_KickApproach` | 24 | 77 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–510
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 343 | 320 | inferred_complete_timeline |
| `Action_None` | 345 | 366 | 22 | inferred_complete_timeline |
| `Action_None` | 368 | 510 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 164 | 141 | inferred_complete_timeline |
| `Action_None` | 167 | 599 | 433 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 273 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–416
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 194 | 171 | inferred_complete_timeline |
| `Action_None` | 202 | 326 | 125 | inferred_complete_timeline |
| `Action_None` | 349 | 416 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 165 | 142 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 197 | 8 | inferred_complete_timeline |
| `Action_None` | 201 | 233 | 33 | inferred_complete_timeline |
| `Action_None` | 237 | 262 | 26 | inferred_complete_timeline |
| `Action_None` | 265 | 280 | 16 | inferred_complete_timeline |
| `Action_None` | 283 | 292 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–375
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 169 | 146 | inferred_complete_timeline |
| `Action_None` | 171 | 207 | 37 | inferred_complete_timeline |
| `Action_None` | 218 | 272 | 55 | inferred_complete_timeline |
| `Action_None` | 275 | 351 | 77 | inferred_complete_timeline |
| `Action_None` | 356 | 375 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–373
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 167 | 144 | inferred_complete_timeline |
| `Action_None` | 171 | 179 | 9 | inferred_complete_timeline |
| `Action_None` | 183 | 342 | 160 | inferred_complete_timeline |
| `Action_None` | 354 | 373 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–360
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 124 | 101 | inferred_complete_timeline |
| `Action_None` | 126 | 165 | 40 | inferred_complete_timeline |
| `Action_None` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_None` | 188 | 237 | 50 | inferred_complete_timeline |
| `Action_None` | 241 | 325 | 85 | inferred_complete_timeline |
| `Action_None` | 331 | 332 | 2 | inferred_complete_timeline |
| `Action_None` | 339 | 340 | 2 | inferred_complete_timeline |
| `Action_None` | 342 | 354 | 13 | inferred_complete_timeline |
| `Action_None` | 357 | 360 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 207 | 184 | inferred_complete_timeline |
| `Action_None` | 212 | 320 | 109 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–344
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 295 | 272 | inferred_complete_timeline |
| `Action_None` | 300 | 335 | 36 | inferred_complete_timeline |
| `Action_None` | 337 | 338 | 2 | inferred_complete_timeline |
| `Action_None` | 342 | 344 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 118 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–353
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 295 | 272 | inferred_complete_timeline |
| `Action_None` | 302 | 353 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 42 | 19 | inferred_complete_timeline |
| `Action_None` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_None` | 49 | 74 | 26 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_None` | 104 | 113 | 10 | inferred_complete_timeline |
| `Action_None` | 122 | 132 | 11 | inferred_complete_timeline |
| `Action_None` | 135 | 148 | 14 | inferred_complete_timeline |
| `Action_None` | 160 | 164 | 5 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 185 | 6 | inferred_complete_timeline |
| `Action_None` | 188 | 198 | 11 | inferred_complete_timeline |
| `Action_None` | 200 | 203 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 66 | 43 | inferred_complete_timeline |
| `Action_None` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 84 | 6 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 93 | 111 | 19 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 131 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–361
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 232 | 209 | inferred_complete_timeline |
| `Action_None` | 237 | 259 | 23 | inferred_complete_timeline |
| `Action_None` | 262 | 361 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 216 | 193 | inferred_complete_timeline |
| `Action_None` | 218 | 224 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–377
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 225 | 202 | inferred_complete_timeline |
| `Action_None` | 244 | 258 | 15 | inferred_complete_timeline |
| `Action_None` | 268 | 324 | 57 | inferred_complete_timeline |
| `Action_None` | 333 | 335 | 3 | inferred_complete_timeline |
| `Action_None` | 337 | 377 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–320
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 229 | 206 | inferred_complete_timeline |
| `Action_None` | 237 | 281 | 45 | inferred_complete_timeline |
| `Action_None` | 283 | 298 | 16 | inferred_complete_timeline |
| `Action_None` | 300 | 320 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker5 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 108 | 85 | inferred_complete_timeline |
| `Action_None` | 115 | 121 | 7 | inferred_complete_timeline |
| `Action_None` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_None` | 135 | 259 | 125 | inferred_complete_timeline |
| `Action_None` | 262 | 266 | 5 | inferred_complete_timeline |
| `Action_None` | 270 | 295 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `22` | Position_Unknown | Team_Unknown | 23–269 | 197 | 11 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 37–357 | 312 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 52–158 | 43 | 10 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 82–599 | 511 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 123–386 | 259 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 152–156 | 5 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 162–297 | 121 | 7 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 238–268 | 13 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 242–468 | 224 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 274–310 | 37 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 290–416 | 98 | 6 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 303–599 | 292 | 3 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 303–315 | 13 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 304–599 | 279 | 4 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 315–317 | 3 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 324–344 | 21 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 347–467 | 109 | 3 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 359–363 | 5 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 362–369 | 7 | 2 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 363–445 | 83 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 368–408 | 41 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 376–391 | 15 | 2 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 404–599 | 196 | 1 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 419–500 | 81 | 2 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 429–485 | 57 | 1 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 465–486 | 22 | 1 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 474–475 | 2 | 1 | Undefined position; Undefined team |
| `47` | `67` | Position_Unknown | Team_Unknown | 523–536 | 10 | 2 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 543–558 | 15 | 2 | Undefined position; Undefined team |
| `49` | `76` | Position_Unknown | Team_Unknown | 586–599 | 14 | 1 | Undefined position; Undefined team |
| `50` | `80` | Position_Unknown | Team_Unknown | 589–599 | 11 | 1 | Undefined position; Undefined team |
| `51` | `82` | Position_Unknown | Team_Unknown | 590–599 | 10 | 1 | Undefined position; Undefined team |
| `52` | `83` | Position_Unknown | Team_Unknown | 592–599 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_KickBall` for actor_track_id `27` (Position_Unknown): Annotated start 112 != Inferred start 123
- ⚠️ `Action_CatchKick` for actor_track_id `34` (Position_Unknown): Annotated start 225 != Inferred start 238
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `34` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Second_Level_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_CrossGoalLine' at frame 600 targets track ID '?', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 160 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Segment 'Action_KickBall' for track '24' has invalid range: start=123, end=117. Clamping end to start.
- ⚠️ Segment 'Action_CatchKick' for track '27' has invalid range: start=238, end=234. Clamping end to start.
- ⚠️ Action 'Action_None' range [24-273] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-343] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-366] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-510] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-165] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-233] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-262] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-280] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-292] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-167] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-179] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-342] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-373] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-164] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-599] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-272] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-351] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-375] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-229] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-281] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-298] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-320] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-165] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-325] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-354] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-360] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-225] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-258] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-324] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-377] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-207] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-320] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-194] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-326] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-416] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [24-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-295] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-335] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-232] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-259] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-361] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-216] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-224] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-295] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-353] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-108] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-259] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-295] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-131] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-42] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-74] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-132] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-148] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-25] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-31] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-90] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-106] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-253] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-255] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-357] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-61] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-153] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-413] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-422] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-335] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-386] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-181] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-270] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-297] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [247-248] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [263-268] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-330] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-465] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-468] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-310] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-301] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-332] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-348] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-405] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-416] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-307] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-490] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-315] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-324] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-343] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-352] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-344] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-371] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-393] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-467] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-363] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-366] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-445] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-408] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-387] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-391] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-429] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-500] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-485] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-486] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-528] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-536] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-544] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-558] for track '48' has 1 frames without a visible bounding box.
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

</details>