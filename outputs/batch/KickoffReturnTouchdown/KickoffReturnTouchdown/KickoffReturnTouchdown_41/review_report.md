# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_41`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 78
- **Ball Tracks:** 0
- **Action Segments:** 317
- **Validation Warnings:** 425
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 8
- **Exact Matches:** 1
- **Group Expanded Events:** 3
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 311
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_KickBall` | Kicker | offense | `9` | `9` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `50` | `36` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `50` | `36` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `50` | `36` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `2` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `5` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `9` | `Group` | 0 | START | 0 | 12 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `9` | `9` | 13 | START | 13 | 35 |
| ❌ MISSING SEGMENT | `Action_KickBall` | Kicker | `9` | `9` | 79 | START | N/A | N/A |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `50` | `36` | 187 | START | 187 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `50` | `36` | 213 | START | 213 | 218 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `50` | `36` | 622 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–571
- **Visible Samples:** 517

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_KickApproach` | 13 | 35 | 23 | inferred_complete_timeline |
| `Action_KickApproach` | 37 | 41 | 5 | inferred_complete_timeline |
| `Action_KickApproach` | 43 | 49 | 7 | inferred_complete_timeline |
| `Action_None` | 102 | 181 | 80 | inferred_complete_timeline |
| `Action_None` | 183 | 571 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–337
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 52 | 40 | inferred_complete_timeline |
| `Action_None` | 58 | 118 | 61 | inferred_complete_timeline |
| `Action_None` | 125 | 300 | 176 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_None` | 310 | 317 | 8 | inferred_complete_timeline |
| `Action_None` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_None` | 336 | 337 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 304 | 292 | inferred_complete_timeline |
| `Action_None` | 307 | 321 | 15 | inferred_complete_timeline |
| `Action_None` | 324 | 335 | 12 | inferred_complete_timeline |
| `Action_None` | 340 | 351 | 12 | inferred_complete_timeline |
| `Action_None` | 353 | 354 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–415
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 142 | 130 | inferred_complete_timeline |
| `Action_None` | 146 | 152 | 7 | inferred_complete_timeline |
| `Action_None` | 156 | 162 | 7 | inferred_complete_timeline |
| `Action_None` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_None` | 172 | 180 | 9 | inferred_complete_timeline |
| `Action_None` | 212 | 214 | 3 | inferred_complete_timeline |
| `Action_None` | 261 | 269 | 9 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 346 | 68 | inferred_complete_timeline |
| `Action_None` | 356 | 407 | 52 | inferred_complete_timeline |
| `Action_None` | 409 | 415 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–542
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 27 | 15 | inferred_complete_timeline |
| `Action_None` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_None` | 34 | 96 | 63 | inferred_complete_timeline |
| `Action_None` | 98 | 106 | 9 | inferred_complete_timeline |
| `Action_None` | 110 | 115 | 6 | inferred_complete_timeline |
| `Action_None` | 117 | 134 | 18 | inferred_complete_timeline |
| `Action_None` | 136 | 152 | 17 | inferred_complete_timeline |
| `Action_None` | 156 | 160 | 5 | inferred_complete_timeline |
| `Action_None` | 163 | 170 | 8 | inferred_complete_timeline |
| `Action_None` | 173 | 180 | 8 | inferred_complete_timeline |
| `Action_None` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_None` | 189 | 215 | 27 | inferred_complete_timeline |
| `Action_None` | 232 | 257 | 26 | inferred_complete_timeline |
| `Action_None` | 272 | 274 | 3 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_None` | 294 | 295 | 2 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |
| `Action_None` | 300 | 301 | 2 | inferred_complete_timeline |
| `Action_None` | 304 | 502 | 199 | inferred_complete_timeline |
| `Action_None` | 541 | 542 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_None` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_None` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_None` | 85 | 96 | 12 | inferred_complete_timeline |
| `Action_None` | 98 | 104 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 3–115
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 12 | 10 | inferred_complete_timeline |
| `Action_None` | 13 | 21 | 9 | inferred_complete_timeline |
| `Action_None` | 23 | 28 | 6 | inferred_complete_timeline |
| `Action_None` | 77 | 82 | 6 | inferred_complete_timeline |
| `Action_None` | 86 | 92 | 7 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 578

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 190 | 178 | inferred_complete_timeline |
| `Action_None` | 200 | 216 | 17 | inferred_complete_timeline |
| `Action_None` | 225 | 267 | 43 | inferred_complete_timeline |
| `Action_None` | 270 | 311 | 42 | inferred_complete_timeline |
| `Action_None` | 313 | 319 | 7 | inferred_complete_timeline |
| `Action_None` | 325 | 331 | 7 | inferred_complete_timeline |
| `Action_None` | 340 | 341 | 2 | inferred_complete_timeline |
| `Action_None` | 343 | 453 | 111 | inferred_complete_timeline |
| `Action_None` | 456 | 458 | 3 | inferred_complete_timeline |
| `Action_None` | 460 | 462 | 3 | inferred_complete_timeline |
| `Action_None` | 466 | 467 | 2 | inferred_complete_timeline |
| `Action_None` | 471 | 600 | 130 | inferred_complete_timeline |
| `Action_None` | 610 | 629 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 103 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–2
- **Visible Samples:** 3

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 601

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 187 | 175 | inferred_complete_timeline |
| `Action_None` | 198 | 212 | 15 | inferred_complete_timeline |
| `Action_None` | 223 | 434 | 212 | inferred_complete_timeline |
| `Action_None` | 437 | 483 | 47 | inferred_complete_timeline |
| `Action_None` | 485 | 489 | 5 | inferred_complete_timeline |
| `Action_None` | 494 | 602 | 109 | inferred_complete_timeline |
| `Action_None` | 605 | 629 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 250 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 609

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 128 | 116 | inferred_complete_timeline |
| `Action_None` | 130 | 138 | 9 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 152 | 7 | inferred_complete_timeline |
| `Action_None` | 155 | 237 | 83 | inferred_complete_timeline |
| `Action_None` | 241 | 465 | 225 | inferred_complete_timeline |
| `Action_None` | 467 | 498 | 32 | inferred_complete_timeline |
| `Action_None` | 503 | 509 | 7 | inferred_complete_timeline |
| `Action_None` | 515 | 629 | 115 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–626 | 579 | 4 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 3–10 | 8 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 9–90 | 25 | 6 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 11–106 | 48 | 7 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 27–35 | 9 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 62–92 | 11 | 5 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 69–97 | 24 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 86–92 | 7 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 102–291 | 189 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 107–108 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 114–115 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 115–122 | 8 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 121–267 | 137 | 4 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 126–233 | 101 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 127–559 | 413 | 9 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 129–131 | 3 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 140–629 | 458 | 11 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 150–151 | 2 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 151–246 | 88 | 4 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 156–157 | 2 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 157–251 | 78 | 5 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 157–357 | 200 | 2 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 159–304 | 138 | 7 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 161–162 | 2 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 164–629 | 435 | 13 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 164–317 | 77 | 3 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 165–203 | 26 | 7 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `42` | `63` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 187–200 | 6 | 2 | Undefined position; Undefined team |
| `44` | `66` | Position_Unknown | Team_Unknown | 202–234 | 22 | 4 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |
| `46` | `68` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |
| `47` | `70` | Position_Unknown | Team_Unknown | 222–233 | 8 | 2 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 253–363 | 88 | 3 | Undefined position; Undefined team |
| `49` | `72` | Position_Unknown | Team_Unknown | 258–288 | 27 | 3 | Undefined position; Undefined team |
| `50` | `73` | Position_Unknown | Team_Unknown | 281–629 | 314 | 10 | Undefined position; Undefined team |
| `51` | `76` | Position_Unknown | Team_Unknown | 286–629 | 331 | 5 | Undefined position; Undefined team |
| `52` | `77` | Position_Unknown | Team_Unknown | 296–629 | 317 | 5 | Undefined position; Undefined team |
| `53` | `78` | Position_Unknown | Team_Unknown | 299–573 | 254 | 7 | Undefined position; Undefined team |
| `54` | `80` | Position_Unknown | Team_Unknown | 311–627 | 291 | 3 | Undefined position; Undefined team |
| `55` | `81` | Position_Unknown | Team_Unknown | 317–589 | 255 | 5 | Undefined position; Undefined team |
| `56` | `83` | Position_Unknown | Team_Unknown | 333–629 | 297 | 1 | Undefined position; Undefined team |
| `57` | `84` | Position_Unknown | Team_Unknown | 341–345 | 5 | 1 | Undefined position; Undefined team |
| `58` | `85` | Position_Unknown | Team_Unknown | 350–629 | 257 | 4 | Undefined position; Undefined team |
| `59` | `86` | Position_Unknown | Team_Unknown | 366–629 | 252 | 5 | Undefined position; Undefined team |
| `60` | `87` | Position_Unknown | Team_Unknown | 368–540 | 173 | 1 | Undefined position; Undefined team |
| `61` | `89` | Position_Unknown | Team_Unknown | 380–430 | 51 | 1 | Undefined position; Undefined team |
| `62` | `90` | Position_Unknown | Team_Unknown | 382–629 | 247 | 2 | Undefined position; Undefined team |
| `63` | `93` | Position_Unknown | Team_Unknown | 422–628 | 203 | 5 | Undefined position; Undefined team |
| `64` | `96` | Position_Unknown | Team_Unknown | 440–513 | 55 | 5 | Undefined position; Undefined team |
| `65` | `97` | Position_Unknown | Team_Unknown | 442–464 | 23 | 1 | Undefined position; Undefined team |
| `66` | `102` | Position_Unknown | Team_Unknown | 469–524 | 4 | 2 | Undefined position; Undefined team |
| `67` | `104` | Position_Unknown | Team_Unknown | 473–477 | 5 | 1 | Undefined position; Undefined team |
| `68` | `105` | Position_Unknown | Team_Unknown | 477–629 | 75 | 7 | Undefined position; Undefined team |
| `69` | `107` | Position_Unknown | Team_Unknown | 492–494 | 3 | 1 | Undefined position; Undefined team |
| `70` | `108` | Position_Unknown | Team_Unknown | 502–627 | 105 | 3 | Undefined position; Undefined team |
| `71` | `111` | Position_Unknown | Team_Unknown | 520–521 | 2 | 1 | Undefined position; Undefined team |
| `72` | `113` | Position_Unknown | Team_Unknown | 525–533 | 9 | 1 | Undefined position; Undefined team |
| `73` | `116` | Position_Unknown | Team_Unknown | 536–586 | 34 | 4 | Undefined position; Undefined team |
| `74` | `120` | Position_Unknown | Team_Unknown | 560–603 | 42 | 2 | Undefined position; Undefined team |
| `75` | `122` | Position_Unknown | Team_Unknown | 579–629 | 49 | 3 | Undefined position; Undefined team |
| `76` | `123` | Position_Unknown | Team_Unknown | 600–628 | 25 | 3 | Undefined position; Undefined team |
| `77` | `125` | Position_Unknown | Team_Unknown | 628–629 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `9` (3 segments found)
- ❌ Missing segment for action `Action_KickBall` on target `9` (Kicker)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `50` (3 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `50` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ 65 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 65 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 130 |
| Missing visible bounding boxes during action | 293 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '36' has invalid range: start=622, end=304. Clamping end to start.
- ⚠️ Action 'Action_None' range [13-103] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-250] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-52] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-118] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-300] for track '2' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-317] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-208] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-626] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-190] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-216] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-267] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-311] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-319] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-331] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-453] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-458] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-462] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-467] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-600] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-304] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-321] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-335] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-351] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-142] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-162] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-346] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-407] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-415] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-187] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-212] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-434] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-483] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-489] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-602] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-27] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-32] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-96] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-106] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-115] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-134] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-152] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-170] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-215] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-257] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-502] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-542] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [13-35] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [37-41] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [43-49] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-181] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-571] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-128] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-138] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-237] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-465] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-498] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-509] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-96] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-104] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-21] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-28] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-10] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-12] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-40] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-14] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-19] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-90] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-35] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-97] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-92] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-287] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-122] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-146] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-243] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-166] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-168] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-183] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-223] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-327] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-338] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-559] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-234] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-325] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-367] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-372] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-629] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-171] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-186] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-214] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-246] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-220] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-241] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-357] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchKick' range [187-193] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [213-218] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [221-260] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [266-304] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-181] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-228] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-315] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-330] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-601] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-608] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-177] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-240] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-208] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-229] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-288] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-302] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-363] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-288] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-356] for track '50' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-366] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-407] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-482] for track '50' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-489] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-510] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-516] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-299] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-304] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-363] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-629] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-495] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-600] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-609] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-372] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-458] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-464] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-515] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-560] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-567] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-573] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-336] for track '54' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-482] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-627] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-501] for track '55' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-508] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-515] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-585] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-589] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-629] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-345] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-432] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-466] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-490] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-629] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-371] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-509] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-548] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-540] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-430] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-584] for track '62' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-629] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-448] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-469] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-603] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-625] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-628] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-450] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-458] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-480] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-513] for track '64' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-464] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-524] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-477] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-574] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-577] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-593] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-608] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-619] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-629] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-494] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-534] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-593] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-627] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-533] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-538] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-556] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-574] for track '73' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-586] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-592] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-603] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-580] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-605] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-603] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-619] for track '76' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-628] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.

</details>