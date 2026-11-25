# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_90

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_90`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 223
- **Validation Warnings:** 264
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 208
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `39` | `28` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `39` | `28` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `10` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `11` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `12` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `13` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `14` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `15` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `5` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `6` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `7` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `8` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `9` | `Group` | 0 | START | 0 | 63 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `12` | `12` | 64 | START | 64 | 113 |
| ✅ EXACT | `Action_KickBall` | Kicker | `12` | `12` | 114 | START | 114 | 119 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `39` | `28` | 230 | START | 230 | 234 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `39` | `28` | 244 | START | 244 | 629 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–467
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_KickApproach` | 64 | 113 | 50 | inferred_complete_timeline |
| `Action_KickBall` | 114 | 119 | 6 | inferred_complete_timeline |
| `Action_None` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_None` | 124 | 447 | 324 | inferred_complete_timeline |
| `Action_None` | 449 | 456 | 8 | inferred_complete_timeline |
| `Action_None` | 458 | 464 | 7 | inferred_complete_timeline |
| `Action_None` | 466 | 467 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 112 | 49 | inferred_complete_timeline |
| `Action_None` | 116 | 119 | 4 | inferred_complete_timeline |
| `Action_None` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 134 | 137 | 4 | inferred_complete_timeline |
| `Action_None` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_None` | 143 | 147 | 5 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 582

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 117 | 54 | inferred_complete_timeline |
| `Action_None` | 120 | 131 | 12 | inferred_complete_timeline |
| `Action_None` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 149 | 4 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 169 | 6 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 178 | 186 | 9 | inferred_complete_timeline |
| `Action_None` | 196 | 206 | 11 | inferred_complete_timeline |
| `Action_None` | 208 | 214 | 7 | inferred_complete_timeline |
| `Action_None` | 217 | 222 | 6 | inferred_complete_timeline |
| `Action_None` | 225 | 234 | 10 | inferred_complete_timeline |
| `Action_None` | 238 | 249 | 12 | inferred_complete_timeline |
| `Action_None` | 255 | 415 | 161 | inferred_complete_timeline |
| `Action_None` | 417 | 629 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 98 | 35 | inferred_complete_timeline |
| `Action_None` | 100 | 106 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 252 | 189 | inferred_complete_timeline |
| `Action_None` | 258 | 277 | 20 | inferred_complete_timeline |
| `Action_None` | 295 | 304 | 10 | inferred_complete_timeline |
| `Action_None` | 309 | 421 | 113 | inferred_complete_timeline |
| `Action_None` | 424 | 607 | 184 | inferred_complete_timeline |
| `Action_None` | 619 | 629 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 617

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 186 | 123 | inferred_complete_timeline |
| `Action_None` | 188 | 191 | 4 | inferred_complete_timeline |
| `Action_None` | 196 | 202 | 7 | inferred_complete_timeline |
| `Action_None` | 204 | 515 | 312 | inferred_complete_timeline |
| `Action_None` | 517 | 518 | 2 | inferred_complete_timeline |
| `Action_None` | 520 | 529 | 10 | inferred_complete_timeline |
| `Action_None` | 533 | 537 | 5 | inferred_complete_timeline |
| `Action_None` | 540 | 629 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 186 | 123 | inferred_complete_timeline |
| `Action_None` | 189 | 191 | 3 | inferred_complete_timeline |
| `Action_None` | 196 | 254 | 59 | inferred_complete_timeline |
| `Action_None` | 261 | 310 | 50 | inferred_complete_timeline |
| `Action_None` | 312 | 323 | 12 | inferred_complete_timeline |
| `Action_None` | 331 | 350 | 20 | inferred_complete_timeline |
| `Action_None` | 357 | 364 | 8 | inferred_complete_timeline |
| `Action_None` | 366 | 592 | 227 | inferred_complete_timeline |
| `Action_None` | 602 | 605 | 4 | inferred_complete_timeline |
| `Action_None` | 609 | 629 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 175 | 112 | inferred_complete_timeline |
| `Action_None` | 177 | 186 | 10 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 250 | 56 | inferred_complete_timeline |
| `Action_None` | 262 | 278 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 624

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 93 | 30 | inferred_complete_timeline |
| `Action_None` | 97 | 363 | 267 | inferred_complete_timeline |
| `Action_None` | 367 | 629 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 94 | 31 | inferred_complete_timeline |
| `Action_None` | 96 | 100 | 5 | inferred_complete_timeline |
| `Action_None` | 103 | 273 | 171 | inferred_complete_timeline |
| `Action_None` | 275 | 288 | 14 | inferred_complete_timeline |
| `Action_None` | 292 | 293 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–450
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 450 | 387 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–593
- **Visible Samples:** 555

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 206 | 143 | inferred_complete_timeline |
| `Action_None` | 220 | 312 | 93 | inferred_complete_timeline |
| `Action_None` | 315 | 317 | 3 | inferred_complete_timeline |
| `Action_None` | 320 | 327 | 8 | inferred_complete_timeline |
| `Action_None` | 336 | 340 | 5 | inferred_complete_timeline |
| `Action_None` | 346 | 472 | 127 | inferred_complete_timeline |
| `Action_None` | 476 | 584 | 109 | inferred_complete_timeline |
| `Action_None` | 591 | 593 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 235 | 172 | inferred_complete_timeline |
| `Action_None` | 238 | 269 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–364
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 246 | 183 | inferred_complete_timeline |
| `Action_None` | 248 | 276 | 29 | inferred_complete_timeline |
| `Action_None` | 289 | 296 | 8 | inferred_complete_timeline |
| `Action_None` | 363 | 364 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 252 | 189 | inferred_complete_timeline |
| `Action_None` | 254 | 259 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 620

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 279 | 216 | inferred_complete_timeline |
| `Action_None` | 282 | 287 | 6 | inferred_complete_timeline |
| `Action_None` | 290 | 593 | 304 | inferred_complete_timeline |
| `Action_None` | 597 | 613 | 17 | inferred_complete_timeline |
| `Action_None` | 617 | 629 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 93–94 | 2 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 107–157 | 39 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 118–629 | 402 | 15 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 129–629 | 485 | 5 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 141–142 | 2 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 145–253 | 80 | 8 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 147–286 | 127 | 5 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 148–629 | 481 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 159–629 | 469 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 172–189 | 9 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 178–629 | 439 | 4 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 217–629 | 413 | 4 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 234–238 | 5 | 1 | Undefined position; Undefined team |
| `30` | `49` | Position_Unknown | Team_Unknown | 265–304 | 34 | 3 | Undefined position; Undefined team |
| `31` | `51` | Position_Unknown | Team_Unknown | 268–629 | 355 | 4 | Undefined position; Undefined team |
| `32` | `53` | Position_Unknown | Team_Unknown | 275–629 | 355 | 1 | Undefined position; Undefined team |
| `33` | `55` | Position_Unknown | Team_Unknown | 287–628 | 340 | 2 | Undefined position; Undefined team |
| `34` | `57` | Position_Unknown | Team_Unknown | 288–289 | 2 | 1 | Undefined position; Undefined team |
| `35` | `58` | Position_Unknown | Team_Unknown | 292–293 | 2 | 1 | Undefined position; Undefined team |
| `36` | `60` | Position_Unknown | Team_Unknown | 306–629 | 312 | 4 | Undefined position; Undefined team |
| `37` | `63` | Position_Unknown | Team_Unknown | 312–629 | 318 | 1 | Undefined position; Undefined team |
| `38` | `65` | Position_Unknown | Team_Unknown | 322–407 | 86 | 1 | Undefined position; Undefined team |
| `39` | `66` | Position_Unknown | Team_Unknown | 331–629 | 299 | 1 | Undefined position; Undefined team |
| `40` | `67` | Position_Unknown | Team_Unknown | 334–585 | 252 | 1 | Undefined position; Undefined team |
| `41` | `68` | Position_Unknown | Team_Unknown | 373–376 | 4 | 1 | Undefined position; Undefined team |
| `42` | `69` | Position_Unknown | Team_Unknown | 447–629 | 155 | 9 | Undefined position; Undefined team |
| `43` | `70` | Position_Unknown | Team_Unknown | 469–536 | 24 | 3 | Undefined position; Undefined team |
| `44` | `71` | Position_Unknown | Team_Unknown | 471–629 | 159 | 1 | Undefined position; Undefined team |
| `45` | `73` | Position_Unknown | Team_Unknown | 478–481 | 4 | 1 | Undefined position; Undefined team |
| `46` | `77` | Position_Unknown | Team_Unknown | 497–506 | 6 | 3 | Undefined position; Undefined team |
| `47` | `78` | Position_Unknown | Team_Unknown | 507–629 | 101 | 6 | Undefined position; Undefined team |
| `48` | `79` | Position_Unknown | Team_Unknown | 508–605 | 71 | 7 | Undefined position; Undefined team |
| `49` | `82` | Position_Unknown | Team_Unknown | 540–561 | 19 | 3 | Undefined position; Undefined team |
| `50` | `84` | Position_Unknown | Team_Unknown | 564–565 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ 35 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 35 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 92, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '638,644,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 70 |
| Missing visible bounding boxes during action | 192 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action 'Action_None' range [64-235] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-206] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-312] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-327] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-472] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-584] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-593] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-279] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-287] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-593] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-613] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-246] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-276] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-296] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-252] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-259] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-450] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-186] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-254] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-310] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-323] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-350] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-364] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-592] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-605] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-175] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-250] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-278] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-117] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-131] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-186] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-206] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-214] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-222] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-234] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-249] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-415] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-629] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-252] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-277] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-304] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-421] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-607] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-186] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-515] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-518] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-529] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-537] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-447] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-456] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-464] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-467] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-112] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-363] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-629] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-273] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-288] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-138] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-157] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-137] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-183] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-252] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-319] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-591] for track '18' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-600] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-607] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-625] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-215] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-242] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-269] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-385] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-629] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-171] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-224] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-189] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-257] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-277] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-312] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-513] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-586] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-317] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-357] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-563] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-229] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [244-629] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-304] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-304] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-310] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-382] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-629] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-619] for track '33' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-628] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-379] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-436] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-629] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-629] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-407] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-629] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-585] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-527] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-545] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-565] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-571] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-576] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-581] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-596] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-619] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-480] for track '43' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-536] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-629] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-481] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-498] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-506] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-522] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-563] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-580] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-598] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-613] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-547] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-559] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-565] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-578] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-588] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-592] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-605] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-541] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-545] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-561] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '50' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_90'; source metadata written as null.

</details>