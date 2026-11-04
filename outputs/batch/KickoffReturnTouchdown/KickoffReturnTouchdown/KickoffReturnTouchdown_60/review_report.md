# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_60

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_60`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 59
- **Ball Tracks:** 0
- **Action Segments:** 206
- **Validation Warnings:** 250
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 191
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `3` | `3` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `3` | `3` |
| ❌ MISSING SEGMENT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `29` | `26` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `29` | `26` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `29` | `26` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `0` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `1` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `10` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `11` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `14` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `18` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `2` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `3` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `4` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `7` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `9` | `Group` | 0 | START | 0 | 60 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `3` | `3` | 61 | START | 61 | 93 |
| ✅ EXACT | `Action_KickBall` | Kicker | `3` | `3` | 94 | START | 94 | 99 |
| ❌ MISSING SEGMENT | `Action_CatchKick` | Position_Unknown | `29` | `26` | 216 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `29` | `26` | 241 | START | 266 | 298 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `29` | `26` | 613 | START | 613 | 626 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_KickApproach` | 61 | 93 | 33 | inferred_complete_timeline |
| `Action_KickBall` | 94 | 99 | 6 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 110 | 7 | inferred_complete_timeline |
| `Action_None` | 113 | 115 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–384
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 225 | 165 | inferred_complete_timeline |
| `Action_None` | 229 | 308 | 80 | inferred_complete_timeline |
| `Action_None` | 314 | 384 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–521
- **Visible Samples:** 522

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 521 | 461 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 262 | 202 | inferred_complete_timeline |
| `Action_None` | 264 | 290 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 572

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 302 | 242 | inferred_complete_timeline |
| `Action_None` | 305 | 393 | 89 | inferred_complete_timeline |
| `Action_None` | 400 | 406 | 7 | inferred_complete_timeline |
| `Action_None` | 408 | 416 | 9 | inferred_complete_timeline |
| `Action_None` | 418 | 420 | 3 | inferred_complete_timeline |
| `Action_None` | 425 | 426 | 2 | inferred_complete_timeline |
| `Action_None` | 432 | 433 | 2 | inferred_complete_timeline |
| `Action_None` | 439 | 555 | 117 | inferred_complete_timeline |
| `Action_None` | 589 | 596 | 8 | inferred_complete_timeline |
| `Action_None` | 598 | 629 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 277 | 217 | inferred_complete_timeline |
| `Action_None` | 279 | 281 | 3 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_None` | 293 | 303 | 11 | inferred_complete_timeline |
| `Action_None` | 327 | 382 | 56 | inferred_complete_timeline |
| `Action_None` | 412 | 416 | 5 | inferred_complete_timeline |
| `Action_None` | 418 | 419 | 2 | inferred_complete_timeline |
| `Action_None` | 421 | 564 | 144 | inferred_complete_timeline |
| `Action_None` | 568 | 589 | 22 | inferred_complete_timeline |
| `Action_None` | 595 | 629 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–304
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 223 | 163 | inferred_complete_timeline |
| `Action_None` | 232 | 237 | 6 | inferred_complete_timeline |
| `Action_None` | 244 | 304 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–396
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 239 | 179 | inferred_complete_timeline |
| `Action_None` | 241 | 245 | 5 | inferred_complete_timeline |
| `Action_None` | 247 | 305 | 59 | inferred_complete_timeline |
| `Action_None` | 313 | 321 | 9 | inferred_complete_timeline |
| `Action_None` | 386 | 396 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–322
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 140 | 80 | inferred_complete_timeline |
| `Action_None` | 143 | 260 | 118 | inferred_complete_timeline |
| `Action_None` | 286 | 322 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–482
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 372 | 312 | inferred_complete_timeline |
| `Action_None` | 395 | 458 | 64 | inferred_complete_timeline |
| `Action_None` | 463 | 482 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 616

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 108 | 48 | inferred_complete_timeline |
| `Action_None` | 118 | 350 | 233 | inferred_complete_timeline |
| `Action_None` | 355 | 406 | 52 | inferred_complete_timeline |
| `Action_None` | 408 | 629 | 222 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 271 | 211 | inferred_complete_timeline |
| `Action_None` | 274 | 275 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 609

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 267 | 207 | inferred_complete_timeline |
| `Action_None` | 283 | 301 | 19 | inferred_complete_timeline |
| `Action_None` | 304 | 308 | 5 | inferred_complete_timeline |
| `Action_None` | 312 | 625 | 314 | inferred_complete_timeline |
| `Action_None` | 627 | 629 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 194 | 134 | inferred_complete_timeline |
| `Action_None` | 205 | 208 | 4 | inferred_complete_timeline |
| `Action_None` | 218 | 252 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 181 | 121 | inferred_complete_timeline |
| `Action_None` | 189 | 262 | 74 | inferred_complete_timeline |
| `Action_None` | 266 | 401 | 136 | inferred_complete_timeline |
| `Action_None` | 411 | 516 | 106 | inferred_complete_timeline |
| `Action_None` | 518 | 556 | 39 | inferred_complete_timeline |
| `Action_None` | 563 | 571 | 9 | inferred_complete_timeline |
| `Action_None` | 573 | 583 | 11 | inferred_complete_timeline |
| `Action_None` | 601 | 629 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 234 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–430
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 139 | 79 | inferred_complete_timeline |
| `Action_None` | 144 | 201 | 58 | inferred_complete_timeline |
| `Action_None` | 208 | 266 | 59 | inferred_complete_timeline |
| `Action_None` | 270 | 286 | 17 | inferred_complete_timeline |
| `Action_None` | 308 | 381 | 74 | inferred_complete_timeline |
| `Action_None` | 394 | 417 | 24 | inferred_complete_timeline |
| `Action_None` | 422 | 426 | 5 | inferred_complete_timeline |
| `Action_None` | 429 | 430 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–426
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 166 | 106 | inferred_complete_timeline |
| `Action_None` | 173 | 181 | 9 | inferred_complete_timeline |
| `Action_None` | 183 | 214 | 32 | inferred_complete_timeline |
| `Action_None` | 220 | 273 | 54 | inferred_complete_timeline |
| `Action_None` | 277 | 280 | 4 | inferred_complete_timeline |
| `Action_None` | 282 | 301 | 20 | inferred_complete_timeline |
| `Action_None` | 304 | 340 | 37 | inferred_complete_timeline |
| `Action_None` | 379 | 426 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 178 | 118 | inferred_complete_timeline |
| `Action_None` | 191 | 215 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 292 | 232 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 118–186 | 69 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 158–159 | 2 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 194–414 | 217 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 214–245 | 27 | 3 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 215–256 | 37 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 230–629 | 391 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 266–629 | 344 | 6 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 275–629 | 351 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 276–307 | 22 | 4 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 278–384 | 107 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 283–629 | 341 | 3 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 302–629 | 324 | 4 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 307–446 | 133 | 3 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 316–629 | 274 | 4 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 327–373 | 47 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 350–427 | 58 | 6 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 351–582 | 217 | 5 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 380–629 | 243 | 2 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 383–432 | 46 | 2 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 386–606 | 219 | 2 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 421–629 | 178 | 5 | Undefined position; Undefined team |
| `41` | `49` | Position_Unknown | Team_Unknown | 437–541 | 105 | 1 | Undefined position; Undefined team |
| `42` | `50` | Position_Unknown | Team_Unknown | 439–624 | 175 | 3 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 455–629 | 131 | 3 | Undefined position; Undefined team |
| `44` | `54` | Position_Unknown | Team_Unknown | 471–629 | 149 | 2 | Undefined position; Undefined team |
| `45` | `55` | Position_Unknown | Team_Unknown | 485–629 | 145 | 1 | Undefined position; Undefined team |
| `46` | `56` | Position_Unknown | Team_Unknown | 503–522 | 19 | 2 | Undefined position; Undefined team |
| `47` | `60` | Position_Unknown | Team_Unknown | 545–629 | 85 | 1 | Undefined position; Undefined team |
| `48` | `61` | Position_Unknown | Team_Unknown | 546–610 | 37 | 7 | Undefined position; Undefined team |
| `49` | `62` | Position_Unknown | Team_Unknown | 551–553 | 3 | 1 | Undefined position; Undefined team |
| `50` | `63` | Position_Unknown | Team_Unknown | 560–576 | 12 | 3 | Undefined position; Undefined team |
| `51` | `64` | Position_Unknown | Team_Unknown | 569–629 | 53 | 3 | Undefined position; Undefined team |
| `52` | `66` | Position_Unknown | Team_Unknown | 591–596 | 6 | 1 | Undefined position; Undefined team |
| `53` | `67` | Position_Unknown | Team_Unknown | 592–627 | 33 | 3 | Undefined position; Undefined team |
| `54` | `68` | Position_Unknown | Team_Unknown | 594–595 | 2 | 1 | Undefined position; Undefined team |
| `55` | `69` | Position_Unknown | Team_Unknown | 609–610 | 2 | 1 | Undefined position; Undefined team |
| `56` | `70` | Position_Unknown | Team_Unknown | 617–619 | 3 | 1 | Undefined position; Undefined team |
| `57` | `71` | Position_Unknown | Team_Unknown | 624–625 | 2 | 1 | Undefined position; Undefined team |
| `58` | `72` | Position_Unknown | Team_Unknown | 629–629 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CatchKick` on target `29` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `29` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ 39 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 39 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 78 |
| Missing visible bounding boxes during action | 170 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Segment 'Action_CatchKick' for track '26' has invalid range: start=266, end=223. Clamping end to start.
- ⚠️ Action 'Action_None' range [61-223] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-237] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-304] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-277] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-303] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-382] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-416] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-564] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-589] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-629] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-225] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-308] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-384] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-110] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-245] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-305] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-321] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-396] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-234] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-194] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-252] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-350] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-406] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-629] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-181] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-262] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-401] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-516] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-556] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-571] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-583] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-629] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-260] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-322] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-302] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-393] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-406] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-416] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-420] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-433] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-555] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-596] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-262] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-290] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-267] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-301] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-308] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-625] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-271] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-372] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-458] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-482] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-266] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-286] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-381] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-417] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-426] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-292] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-178] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-215] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-521] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-166] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-214] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-273] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-280] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-301] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-340] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-426] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-186] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-403] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-414] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-225] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-245] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-256] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-267] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-426] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-493] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-629] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [266-298] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [306-307] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [317-542] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-335] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-286] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-301] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-384] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-309] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-421] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-426] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-433] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-629] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-329] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-438] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-446] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-376] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-547] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-558] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-373] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-353] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-399] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-408] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-423] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-367] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-374] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-392] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-577] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-582] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-494] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-629] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-406] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-432] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-416] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-606] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-465] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-479] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-543] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-562] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-541] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-527] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-596] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-624] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-465] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-548] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-529] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-629] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-508] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-522] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-549] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-562] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-572] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-585] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-590] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-594] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-610] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-553] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-563] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-568] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-576] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-572] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-581] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-596] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-615] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-619] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-627] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-595] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-610] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-619] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-625] for track '57' has 1 frames without a visible bounding box.
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

</details>