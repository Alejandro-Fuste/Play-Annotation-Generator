# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_80

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_80`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 62
- **Ball Tracks:** 0
- **Action Segments:** 295
- **Validation Warnings:** 358
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
- **Inferred Coverage Segments (Action_None):** 280
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `13` | `13` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `13` | `13` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `26` | `22` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `26` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `0` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `12` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `13` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `14` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `15` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `3` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `4` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `5` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `6` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `7` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `8` | `Group` | 0 | START | 0 | 48 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `13` | `13` | 49 | START | 49 | 74 |
| ✅ EXACT | `Action_KickBall` | Kicker | `13` | `13` | 75 | START | 75 | 81 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `26` | `22` | 184 | START | 184 | 193 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `26` | `22` | 205 | START | 205 | 599 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 580

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_KickApproach` | 49 | 74 | 26 | inferred_complete_timeline |
| `Action_KickBall` | 75 | 81 | 7 | inferred_complete_timeline |
| `Action_None` | 82 | 356 | 275 | inferred_complete_timeline |
| `Action_None` | 358 | 362 | 5 | inferred_complete_timeline |
| `Action_None` | 365 | 369 | 5 | inferred_complete_timeline |
| `Action_None` | 372 | 374 | 3 | inferred_complete_timeline |
| `Action_None` | 377 | 385 | 9 | inferred_complete_timeline |
| `Action_None` | 389 | 425 | 37 | inferred_complete_timeline |
| `Action_None` | 436 | 599 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–527
- **Visible Samples:** 512

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 173 | 125 | inferred_complete_timeline |
| `Action_None` | 176 | 494 | 319 | inferred_complete_timeline |
| `Action_None` | 499 | 515 | 17 | inferred_complete_timeline |
| `Action_None` | 526 | 527 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–467
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 251 | 203 | inferred_complete_timeline |
| `Action_None` | 272 | 396 | 125 | inferred_complete_timeline |
| `Action_None` | 401 | 440 | 40 | inferred_complete_timeline |
| `Action_None` | 442 | 445 | 4 | inferred_complete_timeline |
| `Action_None` | 447 | 467 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 210 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–579
- **Visible Samples:** 553

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 94 | 46 | inferred_complete_timeline |
| `Action_None` | 102 | 105 | 4 | inferred_complete_timeline |
| `Action_None` | 108 | 230 | 123 | inferred_complete_timeline |
| `Action_None` | 234 | 245 | 12 | inferred_complete_timeline |
| `Action_None` | 248 | 302 | 55 | inferred_complete_timeline |
| `Action_None` | 305 | 309 | 5 | inferred_complete_timeline |
| `Action_None` | 315 | 345 | 31 | inferred_complete_timeline |
| `Action_None` | 348 | 443 | 96 | inferred_complete_timeline |
| `Action_None` | 446 | 574 | 129 | inferred_complete_timeline |
| `Action_None` | 577 | 579 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–571
- **Visible Samples:** 544

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 322 | 274 | inferred_complete_timeline |
| `Action_None` | 328 | 474 | 147 | inferred_complete_timeline |
| `Action_None` | 477 | 484 | 8 | inferred_complete_timeline |
| `Action_None` | 486 | 487 | 2 | inferred_complete_timeline |
| `Action_None` | 493 | 497 | 5 | inferred_complete_timeline |
| `Action_None` | 500 | 506 | 7 | inferred_complete_timeline |
| `Action_None` | 508 | 548 | 41 | inferred_complete_timeline |
| `Action_None` | 561 | 571 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–365
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 83 | 35 | inferred_complete_timeline |
| `Action_None` | 87 | 98 | 12 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 159 | 209 | 51 | inferred_complete_timeline |
| `Action_None` | 211 | 261 | 51 | inferred_complete_timeline |
| `Action_None` | 273 | 276 | 4 | inferred_complete_timeline |
| `Action_None` | 364 | 365 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 105 | 57 | inferred_complete_timeline |
| `Action_None` | 107 | 121 | 15 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 78 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 77 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 146 | 98 | inferred_complete_timeline |
| `Action_None` | 148 | 285 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–401
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 278 | 230 | inferred_complete_timeline |
| `Action_None` | 285 | 355 | 71 | inferred_complete_timeline |
| `Action_None` | 361 | 362 | 2 | inferred_complete_timeline |
| `Action_None` | 365 | 369 | 5 | inferred_complete_timeline |
| `Action_None` | 379 | 382 | 4 | inferred_complete_timeline |
| `Action_None` | 396 | 401 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 187 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 207 | 159 | inferred_complete_timeline |
| `Action_None` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_None` | 220 | 232 | 13 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_None` | 285 | 293 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 91 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 210 | 162 | inferred_complete_timeline |
| `Action_None` | 218 | 228 | 11 | inferred_complete_timeline |
| `Action_None` | 230 | 250 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 210 | 162 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_None` | 219 | 223 | 5 | inferred_complete_timeline |
| `Action_None` | 225 | 245 | 21 | inferred_complete_timeline |
| `Action_None` | 249 | 253 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 93–247 | 150 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 102–226 | 120 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 110–598 | 454 | 7 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 118–312 | 139 | 7 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 119–541 | 352 | 14 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 135–599 | 461 | 6 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 160–270 | 110 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 163–203 | 8 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 164–211 | 42 | 4 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 168–228 | 32 | 8 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 200–224 | 21 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 223–284 | 62 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 224–599 | 367 | 5 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 225–599 | 336 | 9 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 266–299 | 25 | 3 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 286–599 | 279 | 5 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 291–597 | 285 | 8 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 299–311 | 13 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 299–599 | 301 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 299–300 | 2 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 303–526 | 216 | 5 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 306–309 | 4 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 316–318 | 3 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 323–599 | 235 | 11 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 324–589 | 232 | 10 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 332–599 | 246 | 8 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 338–580 | 226 | 7 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 359–599 | 237 | 4 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 360–599 | 240 | 1 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 361–556 | 122 | 11 | Undefined position; Undefined team |
| `47` | `72` | Position_Unknown | Team_Unknown | 431–433 | 3 | 1 | Undefined position; Undefined team |
| `48` | `73` | Position_Unknown | Team_Unknown | 432–599 | 89 | 12 | Undefined position; Undefined team |
| `49` | `74` | Position_Unknown | Team_Unknown | 448–449 | 2 | 1 | Undefined position; Undefined team |
| `50` | `75` | Position_Unknown | Team_Unknown | 453–509 | 33 | 7 | Undefined position; Undefined team |
| `51` | `77` | Position_Unknown | Team_Unknown | 456–457 | 2 | 1 | Undefined position; Undefined team |
| `52` | `78` | Position_Unknown | Team_Unknown | 474–528 | 25 | 6 | Undefined position; Undefined team |
| `53` | `79` | Position_Unknown | Team_Unknown | 479–528 | 23 | 6 | Undefined position; Undefined team |
| `54` | `81` | Position_Unknown | Team_Unknown | 495–522 | 10 | 3 | Undefined position; Undefined team |
| `55` | `83` | Position_Unknown | Team_Unknown | 500–595 | 86 | 6 | Undefined position; Undefined team |
| `56` | `85` | Position_Unknown | Team_Unknown | 525–528 | 4 | 1 | Undefined position; Undefined team |
| `57` | `87` | Position_Unknown | Team_Unknown | 534–537 | 4 | 1 | Undefined position; Undefined team |
| `58` | `89` | Position_Unknown | Team_Unknown | 550–552 | 3 | 1 | Undefined position; Undefined team |
| `59` | `93` | Position_Unknown | Team_Unknown | 562–582 | 13 | 3 | Undefined position; Undefined team |
| `60` | `97` | Position_Unknown | Team_Unknown | 580–599 | 20 | 1 | Undefined position; Undefined team |
| `61` | `98` | Position_Unknown | Team_Unknown | 588–593 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ 45 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 45 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 82, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '576,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 90 |
| Missing visible bounding boxes during action | 266 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [49-251] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-396] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-440] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-445] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-467] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-228] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-250] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-278] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-355] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-369] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-382] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-401] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-173] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-494] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-515] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-322] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-474] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-484] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-487] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-497] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-506] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-548] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-571] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-94] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-230] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-245] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-302] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-309] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-345] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-443] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-574] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-579] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-78] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-146] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-285] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-245] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-207] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-232] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-293] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-187] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-83] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-261] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 82, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [82-356] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-362] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-369] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-374] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-385] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-425] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-599] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-121] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-247] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-219] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-285] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-318] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-333] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-581] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-587] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-598] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-173] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-245] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-306] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-174] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-200] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-255] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-294] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-335] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-372] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-493] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-505] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-515] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-524] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-528] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-541] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [205-599] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-174] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-270] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-211] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-204] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-215] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-284] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-325] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-374] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-495] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-540] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-229] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-262] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-279] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-294] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-485] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-490] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-494] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-599] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-287] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-326] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-462] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-583] for track '32' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-304] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-394] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-401] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-413] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-431] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-435] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-442] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-597] for track '33' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-311] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-307] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-314] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-322] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-507] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-526] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-309] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-345] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-468] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-478] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-488] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-508] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-552] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-564] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-572] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-593] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-440] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-452] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-504] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-512] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-521] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-543] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-549] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-566] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-572] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-589] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-347] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-482] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-494] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-564] for track '42' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-581] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-591] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-341] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-494] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-523] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-543] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-564] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-570] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-580] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-494] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-522] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-599] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-369] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-376] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-394] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-440] for track '46' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-466] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-504] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-513] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-524] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-536] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-556] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-433] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-435] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-449] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-472] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-495] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-506] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-524] for track '48' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-535] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-546] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-552] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-576] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-591] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-470] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-484] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-495] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-509] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-478] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-488] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-497] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-504] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-508] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-528] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-483] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-502] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-511] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-521] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-528] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-496] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-502] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-522] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-513] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-533] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-555] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-588] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-595] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-528] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-537] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-552] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-564] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-571] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-582] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-593] for track '61' has 3 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_80'; source metadata written as null.

</details>