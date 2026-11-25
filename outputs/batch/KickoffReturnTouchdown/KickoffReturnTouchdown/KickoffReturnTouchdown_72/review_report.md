# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_72

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_72`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 509
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 130
- **Validation Warnings:** 135
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 115
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `10` | `10` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `10` | `10` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | defense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `10` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `12` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `13` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `17` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `19` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `2` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `20` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `21` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `6` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `9` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `10` | `10` | 6 | START | 6 | 32 |
| ✅ EXACT | `Action_KickBall` | Kicker | `10` | `10` | 33 | START | 33 | 39 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `0` | `0` | 152 | START | 152 | 161 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | `0` | `0` | 175 | START | 175 | 316 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–332
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_KickApproach` | 6 | 32 | 27 | inferred_complete_timeline |
| `Action_KickBall` | 33 | 39 | 7 | inferred_complete_timeline |
| `Action_None` | 40 | 332 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 240 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 509 | 504 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 145 | 140 | inferred_complete_timeline |
| `Action_None` | 147 | 240 | 94 | inferred_complete_timeline |
| `Action_None` | 244 | 275 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–458
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 73 | 68 | inferred_complete_timeline |
| `Action_None` | 77 | 246 | 170 | inferred_complete_timeline |
| `Action_None` | 250 | 458 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 64 | 59 | inferred_complete_timeline |
| `Action_None` | 71 | 75 | 5 | inferred_complete_timeline |
| `Action_None` | 77 | 159 | 83 | inferred_complete_timeline |
| `Action_None` | 204 | 259 | 56 | inferred_complete_timeline |
| `Action_None` | 263 | 330 | 68 | inferred_complete_timeline |
| `Action_None` | 335 | 339 | 5 | inferred_complete_timeline |
| `Action_None` | 341 | 343 | 3 | inferred_complete_timeline |
| `Action_None` | 347 | 349 | 3 | inferred_complete_timeline |
| `Action_None` | 355 | 382 | 28 | inferred_complete_timeline |
| `Action_None` | 384 | 388 | 5 | inferred_complete_timeline |
| `Action_None` | 390 | 509 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 153 | 148 | inferred_complete_timeline |
| `Action_None` | 155 | 509 | 355 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 415 | 410 | inferred_complete_timeline |
| `Action_None` | 422 | 509 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–363
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 148 | 143 | inferred_complete_timeline |
| `Action_None` | 151 | 333 | 183 | inferred_complete_timeline |
| `Action_None` | 336 | 337 | 2 | inferred_complete_timeline |
| `Action_None` | 339 | 347 | 9 | inferred_complete_timeline |
| `Action_None` | 355 | 363 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–490
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 311 | 306 | inferred_complete_timeline |
| `Action_None` | 316 | 318 | 3 | inferred_complete_timeline |
| `Action_None` | 324 | 342 | 19 | inferred_complete_timeline |
| `Action_None` | 344 | 345 | 2 | inferred_complete_timeline |
| `Action_None` | 347 | 362 | 16 | inferred_complete_timeline |
| `Action_None` | 373 | 375 | 3 | inferred_complete_timeline |
| `Action_None` | 382 | 490 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 509 | 504 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 190 | 185 | inferred_complete_timeline |
| `Action_None` | 193 | 298 | 106 | inferred_complete_timeline |
| `Action_None` | 314 | 509 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–478
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 181 | 176 | inferred_complete_timeline |
| `Action_None` | 183 | 240 | 58 | inferred_complete_timeline |
| `Action_None` | 244 | 419 | 176 | inferred_complete_timeline |
| `Action_None` | 421 | 478 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 194 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 128 | 123 | inferred_complete_timeline |
| `Action_None` | 138 | 149 | 12 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 242 | 87 | inferred_complete_timeline |
| `Action_None` | 244 | 249 | 6 | inferred_complete_timeline |
| `Action_None` | 252 | 285 | 34 | inferred_complete_timeline |
| `Action_None` | 287 | 399 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 243 | 238 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |
| `Action_None` | 252 | 509 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 486

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_CatchKick` | 152 | 161 | 10 | inferred_complete_timeline |
| `Action_None` | 162 | 174 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 175 | 316 | 142 | inferred_complete_timeline |
| `Action_BallCarry` | 322 | 328 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 330 | 334 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 336 | 337 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 354 | 396 | 43 | inferred_complete_timeline |
| `Action_BallCarry` | 398 | 509 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–497
- **Visible Samples:** 473

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 140 | 135 | inferred_complete_timeline |
| `Action_None` | 143 | 249 | 107 | inferred_complete_timeline |
| `Action_None` | 252 | 309 | 58 | inferred_complete_timeline |
| `Action_None` | 322 | 390 | 69 | inferred_complete_timeline |
| `Action_None` | 399 | 489 | 91 | inferred_complete_timeline |
| `Action_None` | 491 | 497 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–506
- **Visible Samples:** 507

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 506 | 501 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 225 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–327
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 303 | 298 | inferred_complete_timeline |
| `Action_None` | 314 | 327 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 282 | 277 | inferred_complete_timeline |
| `Action_None` | 287 | 289 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 65–66 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 114–116 | 3 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 156–158 | 3 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 173–196 | 24 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 173–198 | 18 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 219–509 | 284 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 260–509 | 246 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 266–509 | 238 | 3 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 266–271 | 6 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 279–304 | 26 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 281–509 | 228 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 300–509 | 208 | 2 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 343–348 | 5 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 348–465 | 118 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 377–443 | 67 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 389–462 | 44 | 3 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 431–455 | 25 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 468–477 | 5 | 2 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 477–509 | 33 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 74, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '526,530,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 95 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action 'Action_BallCarry' range [175-316] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [322-328] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [330-334] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [336-337] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [354-396] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-303] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-327] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-73] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-246] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-458] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-225] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-190] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-298] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-509] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-506] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-153] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-509] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-194] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-243] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-148] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-333] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-347] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-363] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [6-32] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-332] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-249] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-309] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-390] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-489] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-497] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-415] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-64] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-259] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-330] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-339] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-343] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-382] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-388] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-149] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-242] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-285] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-399] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-282] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-240] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-275] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-181] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-240] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-419] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-478] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-240] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-311] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-342] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-362] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-375] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-490] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-196] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-184] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-306] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-318] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-394] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-291] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-509] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-271] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-304] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-449] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-303] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-465] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-443] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-391] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-424] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-462] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-455] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-477] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-509] for track '40' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_72'; source metadata written as null.

</details>