# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_43`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 509
- **Player Tracks:** 77
- **Ball Tracks:** 0
- **Action Segments:** 303
- **Validation Warnings:** 409
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 289
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `56` | `34` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `56` | `34` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `56` | `34` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `1` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `10` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `2` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `3` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `4` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `5` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `7` | `Group` | 0 | START | 0 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Position_Unknown | `18` | `17` | 85 | START | 85 | 98 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `3` | `3` | 111 | END | 111 | 111 |
| ✅ EXACT | `Action_PuntBall` | Punter | `3` | `3` | 139 | START | 139 | 150 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `56` | `34` | 254 | START | 254 | 261 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `56` | `34` | 280 | START | 280 | 429 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `56` | `34` | 510 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Gunner — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 501

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 156 | 72 | inferred_complete_timeline |
| `Action_None` | 159 | 449 | 291 | inferred_complete_timeline |
| `Action_None` | 457 | 509 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 134 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 209 | 125 | inferred_complete_timeline |
| `Action_None` | 213 | 216 | 4 | inferred_complete_timeline |
| `Action_None` | 219 | 261 | 43 | inferred_complete_timeline |
| `Action_None` | 263 | 385 | 123 | inferred_complete_timeline |
| `Action_None` | 387 | 397 | 11 | inferred_complete_timeline |
| `Action_None` | 416 | 421 | 6 | inferred_complete_timeline |
| `Action_None` | 434 | 438 | 5 | inferred_complete_timeline |
| `Action_None` | 447 | 448 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 375 | 291 | inferred_complete_timeline |
| `Action_None` | 385 | 386 | 2 | inferred_complete_timeline |
| `Action_None` | 420 | 426 | 7 | inferred_complete_timeline |
| `Action_None` | 429 | 430 | 2 | inferred_complete_timeline |
| `Action_None` | 452 | 453 | 2 | inferred_complete_timeline |
| `Action_None` | 471 | 472 | 2 | inferred_complete_timeline |
| `Action_None` | 479 | 482 | 4 | inferred_complete_timeline |
| `Action_None` | 485 | 487 | 3 | inferred_complete_timeline |
| `Action_None` | 489 | 509 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 190 | 106 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 210 | 14 | inferred_complete_timeline |
| `Action_None` | 213 | 262 | 50 | inferred_complete_timeline |
| `Action_None` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_None` | 269 | 303 | 35 | inferred_complete_timeline |
| `Action_None` | 306 | 314 | 9 | inferred_complete_timeline |
| `Action_None` | 316 | 348 | 33 | inferred_complete_timeline |
| `Action_None` | 354 | 365 | 12 | inferred_complete_timeline |
| `Action_None` | 368 | 373 | 6 | inferred_complete_timeline |
| `Action_None` | 379 | 387 | 9 | inferred_complete_timeline |
| `Action_None` | 389 | 390 | 2 | inferred_complete_timeline |
| `Action_None` | 393 | 404 | 12 | inferred_complete_timeline |
| `Action_None` | 415 | 417 | 3 | inferred_complete_timeline |
| `Action_None` | 424 | 457 | 34 | inferred_complete_timeline |
| `Action_None` | 459 | 462 | 4 | inferred_complete_timeline |
| `Action_None` | 466 | 509 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_SnapReceive` | 111 | 111 | 1 | inferred_complete_timeline |
| `Action_None` | 112 | 138 | 27 | inferred_complete_timeline |
| `Action_PuntBall` | 139 | 150 | 12 | inferred_complete_timeline |
| `Action_None` | 151 | 164 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 5 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 84 | 78 | inferred_complete_timeline |
| `Action_None` | 85 | 98 | 14 | inferred_complete_timeline |
| `Action_None` | 109 | 122 | 14 | inferred_complete_timeline |
| `Action_None` | 124 | 134 | 11 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 157 | 5 | inferred_complete_timeline |
| `Action_None` | 162 | 206 | 45 | inferred_complete_timeline |
| `Action_None` | 208 | 231 | 24 | inferred_complete_timeline |
| `Action_None` | 234 | 426 | 193 | inferred_complete_timeline |
| `Action_None` | 430 | 431 | 2 | inferred_complete_timeline |
| `Action_None` | 433 | 434 | 2 | inferred_complete_timeline |
| `Action_None` | 436 | 443 | 8 | inferred_complete_timeline |
| `Action_None` | 445 | 509 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher6 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 98 | 14 | inferred_complete_timeline |
| `Action_None` | 101 | 146 | 46 | inferred_complete_timeline |
| `Action_None` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_None` | 164 | 206 | 43 | inferred_complete_timeline |
| `Action_None` | 213 | 228 | 16 | inferred_complete_timeline |
| `Action_None` | 241 | 246 | 6 | inferred_complete_timeline |
| `Action_None` | 248 | 253 | 6 | inferred_complete_timeline |
| `Action_None` | 265 | 267 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 98 | 14 | inferred_complete_timeline |
| `Action_None` | 103 | 106 | 4 | inferred_complete_timeline |
| `Action_None` | 109 | 111 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 128 | 44 | inferred_complete_timeline |
| `Action_None` | 130 | 242 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–348
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 348 | 264 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 4–131 | 116 | 7 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 4–132 | 117 | 7 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 4–492 | 443 | 8 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 9–134 | 122 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 9–194 | 140 | 5 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 9–131 | 108 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 9–110 | 90 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 9–134 | 102 | 11 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 9–234 | 212 | 5 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 20–509 | 444 | 9 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 116–509 | 340 | 12 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 144–185 | 42 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 148–159 | 10 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 153–154 | 2 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 162–419 | 258 | 1 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 165–316 | 130 | 6 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 168–380 | 195 | 7 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 168–509 | 314 | 5 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 170–508 | 328 | 5 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 171–457 | 201 | 6 | Undefined position; Undefined team |
| `31` | `52` | Position_Unknown | Team_Unknown | 200–509 | 309 | 2 | Undefined position; Undefined team |
| `32` | `53` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |
| `33` | `55` | Position_Unknown | Team_Unknown | 212–226 | 11 | 2 | Undefined position; Undefined team |
| `34` | `56` | Position_Unknown | Team_Unknown | 216–509 | 290 | 5 | Undefined position; Undefined team |
| `35` | `58` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `36` | `60` | Position_Unknown | Team_Unknown | 229–237 | 9 | 1 | Undefined position; Undefined team |
| `37` | `63` | Position_Unknown | Team_Unknown | 235–237 | 3 | 1 | Undefined position; Undefined team |
| `38` | `64` | Position_Unknown | Team_Unknown | 236–238 | 3 | 1 | Undefined position; Undefined team |
| `39` | `65` | Position_Unknown | Team_Unknown | 236–242 | 6 | 2 | Undefined position; Undefined team |
| `40` | `67` | Position_Unknown | Team_Unknown | 239–509 | 265 | 4 | Undefined position; Undefined team |
| `41` | `70` | Position_Unknown | Team_Unknown | 255–256 | 2 | 1 | Undefined position; Undefined team |
| `42` | `71` | Position_Unknown | Team_Unknown | 256–259 | 4 | 1 | Undefined position; Undefined team |
| `43` | `72` | Position_Unknown | Team_Unknown | 265–509 | 239 | 4 | Undefined position; Undefined team |
| `44` | `78` | Position_Unknown | Team_Unknown | 285–291 | 7 | 1 | Undefined position; Undefined team |
| `45` | `79` | Position_Unknown | Team_Unknown | 287–295 | 4 | 2 | Undefined position; Undefined team |
| `46` | `80` | Position_Unknown | Team_Unknown | 293–308 | 16 | 1 | Undefined position; Undefined team |
| `47` | `82` | Position_Unknown | Team_Unknown | 303–305 | 3 | 1 | Undefined position; Undefined team |
| `48` | `83` | Position_Unknown | Team_Unknown | 314–317 | 4 | 1 | Undefined position; Undefined team |
| `49` | `84` | Position_Unknown | Team_Unknown | 315–347 | 10 | 3 | Undefined position; Undefined team |
| `50` | `86` | Position_Unknown | Team_Unknown | 320–509 | 189 | 2 | Undefined position; Undefined team |
| `51` | `87` | Position_Unknown | Team_Unknown | 326–509 | 182 | 2 | Undefined position; Undefined team |
| `52` | `89` | Position_Unknown | Team_Unknown | 334–433 | 64 | 9 | Undefined position; Undefined team |
| `53` | `90` | Position_Unknown | Team_Unknown | 337–374 | 13 | 3 | Undefined position; Undefined team |
| `54` | `91` | Position_Unknown | Team_Unknown | 357–479 | 104 | 11 | Undefined position; Undefined team |
| `55` | `93` | Position_Unknown | Team_Unknown | 382–383 | 2 | 1 | Undefined position; Undefined team |
| `56` | `95` | Position_Unknown | Team_Unknown | 392–414 | 19 | 2 | Undefined position; Undefined team |
| `57` | `98` | Position_Unknown | Team_Unknown | 400–478 | 32 | 9 | Undefined position; Undefined team |
| `58` | `99` | Position_Unknown | Team_Unknown | 403–405 | 3 | 1 | Undefined position; Undefined team |
| `59` | `101` | Position_Unknown | Team_Unknown | 410–411 | 2 | 1 | Undefined position; Undefined team |
| `60` | `102` | Position_Unknown | Team_Unknown | 413–509 | 78 | 3 | Undefined position; Undefined team |
| `61` | `104` | Position_Unknown | Team_Unknown | 415–509 | 93 | 2 | Undefined position; Undefined team |
| `62` | `105` | Position_Unknown | Team_Unknown | 418–436 | 16 | 3 | Undefined position; Undefined team |
| `63` | `107` | Position_Unknown | Team_Unknown | 424–482 | 59 | 1 | Undefined position; Undefined team |
| `64` | `108` | Position_Unknown | Team_Unknown | 424–496 | 41 | 5 | Undefined position; Undefined team |
| `65` | `111` | Position_Unknown | Team_Unknown | 436–483 | 46 | 3 | Undefined position; Undefined team |
| `66` | `114` | Position_Unknown | Team_Unknown | 466–487 | 19 | 2 | Undefined position; Undefined team |
| `67` | `117` | Position_Unknown | Team_Unknown | 471–476 | 6 | 1 | Undefined position; Undefined team |
| `68` | `118` | Position_Unknown | Team_Unknown | 477–509 | 32 | 2 | Undefined position; Undefined team |
| `69` | `121` | Position_Unknown | Team_Unknown | 484–509 | 22 | 3 | Undefined position; Undefined team |
| `70` | `122` | Position_Unknown | Team_Unknown | 486–509 | 23 | 2 | Undefined position; Undefined team |
| `71` | `123` | Position_Unknown | Team_Unknown | 486–509 | 18 | 3 | Undefined position; Undefined team |
| `72` | `124` | Position_Unknown | Team_Unknown | 491–493 | 3 | 1 | Undefined position; Undefined team |
| `73` | `125` | Position_Unknown | Team_Unknown | 496–500 | 5 | 1 | Undefined position; Undefined team |
| `74` | `126` | Position_Unknown | Team_Unknown | 496–498 | 3 | 1 | Undefined position; Undefined team |
| `75` | `128` | Position_Unknown | Team_Unknown | 502–508 | 6 | 2 | Undefined position; Undefined team |
| `76` | `129` | Position_Unknown | Team_Unknown | 506–509 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `56` (2 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `56` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 66 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 66 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 132 |
| Missing visible bounding boxes during action | 272 |
| Track-related warning | 1 |
| Other | 4 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_CrossGoalLine' for track '34' has invalid range: start=510, end=509. Clamping end to start.
- ⚠️ Action 'Action_None' range [85-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-242] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-209] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-261] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-385] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-397] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-421] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-438] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-156] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-449] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-164] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-375] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-426] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-472] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-482] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-487] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-509] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-190] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-262] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-303] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-314] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-348] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-365] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-373] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-387] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-404] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-417] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-457] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-462] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-509] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-348] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-134] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-98] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-146] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-206] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-228] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-246] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-98] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-5] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-98] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-134] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-206] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-231] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-426] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-434] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-443] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-509] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-114] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-131] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-6] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-16] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-23] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-133] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-438] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-457] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-462] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-485] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-492] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-134] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-16] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-132] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-194] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-84] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-131] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-16] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [85-98] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [109-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-16] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-20] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-16] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-20] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-96] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-234] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-31] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-73] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-98] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-257] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-509] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-134] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-192] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-237] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-254] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-290] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-446] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-456] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-474] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-485] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-505] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-185] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-155] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-419] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-220] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-248] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-313] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-234] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-308] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-342] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-366] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-372] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-225] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-255] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-323] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-509] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-270] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-485] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-493] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-508] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-207] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-255] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-348] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-372] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-457] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-303] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-509] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [280-429] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [434-509] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-237] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-263] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-291] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-356] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-509] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-259] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-413] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-420] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-431] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-308] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-324] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-483] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-344] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-509] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-370] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-397] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-403] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-420] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-433] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-341] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-354] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-365] for track '54' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-373] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-391] for track '54' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-414] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-420] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-451] for track '54' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-469] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-479] for track '54' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-403] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-414] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-402] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-414] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-422] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-431] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-455] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-467] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-405] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-438] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-442] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-509] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-449] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-421] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-429] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-436] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-482] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-443] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-449] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-454] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-485] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-496] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-444] for track '65' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-472] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-483] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-474] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-487] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-476] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-485] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-488] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-498] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-488] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-509] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-498] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-505] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-493] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-500] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-498] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-508] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 510. Video range is [0, 509].
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>