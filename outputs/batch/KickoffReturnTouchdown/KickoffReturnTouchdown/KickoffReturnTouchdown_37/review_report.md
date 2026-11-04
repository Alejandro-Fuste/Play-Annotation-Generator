# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_37`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 91
- **Ball Tracks:** 0
- **Action Segments:** 332
- **Validation Warnings:** 449
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 319
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_KickBall` | Position_Unknown | Team_Unknown | `28` | `23` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner | defense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner | defense | `11` | `11` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner | defense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `0` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `1` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `10` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `12` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `15` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `16` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `7` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `9` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `12` | `12` | 31 | START | 31 | 43 |
| ⚠️ START CHANGED | `Action_KickBall` | Position_Unknown | `28` | `23` | 87 | START | 89 | 92 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner | `11` | `11` | 204 | START | 204 | 209 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner | `11` | `11` | 227 | START | 227 | 302 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner | `11` | `11` | 659 | START | 659 | 659 |

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
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_KickApproach` | 31 | 43 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–40
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 35 | 40 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 41 | 61 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 45 | 15 | inferred_complete_timeline |
| `Action_None` | 48 | 50 | 3 | inferred_complete_timeline |
| `Action_None` | 54 | 55 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 66 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 638

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 44 | 14 | inferred_complete_timeline |
| `Action_None` | 54 | 66 | 13 | inferred_complete_timeline |
| `Action_None` | 71 | 77 | 7 | inferred_complete_timeline |
| `Action_None` | 79 | 101 | 23 | inferred_complete_timeline |
| `Action_None` | 103 | 251 | 149 | inferred_complete_timeline |
| `Action_None` | 253 | 260 | 8 | inferred_complete_timeline |
| `Action_None` | 263 | 292 | 30 | inferred_complete_timeline |
| `Action_None` | 297 | 659 | 363 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 47 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 655

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 278 | 248 | inferred_complete_timeline |
| `Action_None` | 283 | 285 | 3 | inferred_complete_timeline |
| `Action_None` | 287 | 659 | 373 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–42
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 27 | 4 | inferred_complete_timeline |
| `Action_None` | 41 | 42 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 190 | 160 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 206 | 209 | 4 | inferred_complete_timeline |
| `Action_None` | 211 | 390 | 180 | inferred_complete_timeline |
| `Action_None` | 392 | 526 | 135 | inferred_complete_timeline |
| `Action_None` | 532 | 544 | 13 | inferred_complete_timeline |
| `Action_None` | 546 | 608 | 63 | inferred_complete_timeline |
| `Action_None` | 614 | 619 | 6 | inferred_complete_timeline |
| `Action_None` | 621 | 642 | 22 | inferred_complete_timeline |
| `Action_None` | 646 | 652 | 7 | inferred_complete_timeline |
| `Action_None` | 654 | 659 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 47 | 17 | inferred_complete_timeline |
| `Action_None` | 50 | 62 | 13 | inferred_complete_timeline |
| `Action_None` | 65 | 76 | 12 | inferred_complete_timeline |
| `Action_None` | 83 | 90 | 8 | inferred_complete_timeline |
| `Action_None` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 100 | 106 | 7 | inferred_complete_timeline |
| `Action_None` | 109 | 116 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–345
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 240 | 210 | inferred_complete_timeline |
| `Action_None` | 248 | 255 | 8 | inferred_complete_timeline |
| `Action_None` | 257 | 260 | 4 | inferred_complete_timeline |
| `Action_None` | 264 | 265 | 2 | inferred_complete_timeline |
| `Action_None` | 268 | 345 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 200 | 170 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 223 | 233 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 634

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |
| `Action_CatchKick` | 204 | 209 | 6 | inferred_complete_timeline |
| `Action_None` | 210 | 226 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 227 | 302 | 76 | inferred_complete_timeline |
| `Action_BallCarry` | 305 | 307 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 316 | 381 | 66 | inferred_complete_timeline |
| `Action_BallCarry` | 384 | 631 | 248 | inferred_complete_timeline |
| `Action_BallCarry` | 648 | 658 | 11 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 659 | 659 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–300
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 259 | 229 | inferred_complete_timeline |
| `Action_None` | 262 | 268 | 7 | inferred_complete_timeline |
| `Action_None` | 271 | 300 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 634

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 222 | 192 | inferred_complete_timeline |
| `Action_None` | 224 | 272 | 49 | inferred_complete_timeline |
| `Action_None` | 289 | 292 | 4 | inferred_complete_timeline |
| `Action_None` | 297 | 300 | 4 | inferred_complete_timeline |
| `Action_None` | 304 | 367 | 64 | inferred_complete_timeline |
| `Action_None` | 370 | 659 | 290 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 632

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 58 | 28 | inferred_complete_timeline |
| `Action_None` | 67 | 73 | 7 | inferred_complete_timeline |
| `Action_None` | 75 | 103 | 29 | inferred_complete_timeline |
| `Action_None` | 105 | 109 | 5 | inferred_complete_timeline |
| `Action_None` | 114 | 294 | 181 | inferred_complete_timeline |
| `Action_None` | 299 | 577 | 279 | inferred_complete_timeline |
| `Action_None` | 584 | 622 | 39 | inferred_complete_timeline |
| `Action_None` | 625 | 627 | 3 | inferred_complete_timeline |
| `Action_None` | 630 | 659 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–300
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 125 | 95 | inferred_complete_timeline |
| `Action_None` | 127 | 294 | 168 | inferred_complete_timeline |
| `Action_None` | 297 | 300 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–121 | 88 | 6 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 3–60 | 58 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 15–62 | 48 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 21–22 | 2 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 71–279 | 199 | 5 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 74–596 | 465 | 13 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 76–659 | 526 | 12 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 82–323 | 222 | 10 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 85–127 | 10 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 90–92 | 3 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 92–97 | 6 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 96–108 | 4 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 98–114 | 12 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 105–659 | 528 | 9 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 108–258 | 150 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 110–659 | 549 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 110–543 | 422 | 5 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 115–335 | 180 | 11 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 115–511 | 396 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 116–144 | 5 | 2 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 118–147 | 12 | 3 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 120–348 | 215 | 3 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 123–163 | 26 | 4 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 131–163 | 24 | 4 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 131–215 | 8 | 2 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 136–138 | 3 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 148–352 | 192 | 5 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 150–155 | 6 | 1 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 152–240 | 59 | 6 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 155–157 | 3 | 1 | Undefined position; Undefined team |
| `48` | `63` | Position_Unknown | Team_Unknown | 159–160 | 2 | 1 | Undefined position; Undefined team |
| `49` | `66` | Position_Unknown | Team_Unknown | 203–215 | 13 | 1 | Undefined position; Undefined team |
| `50` | `69` | Position_Unknown | Team_Unknown | 246–314 | 69 | 1 | Undefined position; Undefined team |
| `51` | `71` | Position_Unknown | Team_Unknown | 283–323 | 41 | 1 | Undefined position; Undefined team |
| `52` | `74` | Position_Unknown | Team_Unknown | 311–312 | 2 | 1 | Undefined position; Undefined team |
| `53` | `76` | Position_Unknown | Team_Unknown | 313–436 | 112 | 5 | Undefined position; Undefined team |
| `54` | `78` | Position_Unknown | Team_Unknown | 315–317 | 3 | 1 | Undefined position; Undefined team |
| `55` | `79` | Position_Unknown | Team_Unknown | 316–510 | 186 | 6 | Undefined position; Undefined team |
| `56` | `80` | Position_Unknown | Team_Unknown | 317–318 | 2 | 1 | Undefined position; Undefined team |
| `57` | `82` | Position_Unknown | Team_Unknown | 322–659 | 338 | 1 | Undefined position; Undefined team |
| `58` | `84` | Position_Unknown | Team_Unknown | 335–500 | 166 | 1 | Undefined position; Undefined team |
| `59` | `85` | Position_Unknown | Team_Unknown | 346–656 | 279 | 8 | Undefined position; Undefined team |
| `60` | `86` | Position_Unknown | Team_Unknown | 361–510 | 140 | 7 | Undefined position; Undefined team |
| `61` | `87` | Position_Unknown | Team_Unknown | 366–659 | 292 | 2 | Undefined position; Undefined team |
| `62` | `88` | Position_Unknown | Team_Unknown | 382–659 | 278 | 1 | Undefined position; Undefined team |
| `63` | `93` | Position_Unknown | Team_Unknown | 392–659 | 267 | 2 | Undefined position; Undefined team |
| `64` | `94` | Position_Unknown | Team_Unknown | 410–659 | 235 | 5 | Undefined position; Undefined team |
| `65` | `95` | Position_Unknown | Team_Unknown | 411–606 | 78 | 12 | Undefined position; Undefined team |
| `66` | `96` | Position_Unknown | Team_Unknown | 421–423 | 3 | 1 | Undefined position; Undefined team |
| `67` | `97` | Position_Unknown | Team_Unknown | 432–435 | 4 | 1 | Undefined position; Undefined team |
| `68` | `98` | Position_Unknown | Team_Unknown | 444–659 | 216 | 1 | Undefined position; Undefined team |
| `69` | `100` | Position_Unknown | Team_Unknown | 447–449 | 3 | 1 | Undefined position; Undefined team |
| `70` | `103` | Position_Unknown | Team_Unknown | 462–463 | 2 | 1 | Undefined position; Undefined team |
| `71` | `104` | Position_Unknown | Team_Unknown | 462–650 | 153 | 8 | Undefined position; Undefined team |
| `72` | `108` | Position_Unknown | Team_Unknown | 477–478 | 2 | 1 | Undefined position; Undefined team |
| `73` | `110` | Position_Unknown | Team_Unknown | 482–483 | 2 | 1 | Undefined position; Undefined team |
| `74` | `116` | Position_Unknown | Team_Unknown | 522–524 | 3 | 1 | Undefined position; Undefined team |
| `75` | `118` | Position_Unknown | Team_Unknown | 535–659 | 107 | 9 | Undefined position; Undefined team |
| `76` | `121` | Position_Unknown | Team_Unknown | 542–600 | 44 | 6 | Undefined position; Undefined team |
| `77` | `123` | Position_Unknown | Team_Unknown | 547–659 | 113 | 1 | Undefined position; Undefined team |
| `78` | `124` | Position_Unknown | Team_Unknown | 549–659 | 94 | 4 | Undefined position; Undefined team |
| `79` | `126` | Position_Unknown | Team_Unknown | 562–659 | 66 | 9 | Undefined position; Undefined team |
| `80` | `129` | Position_Unknown | Team_Unknown | 583–584 | 2 | 1 | Undefined position; Undefined team |
| `81` | `130` | Position_Unknown | Team_Unknown | 583–586 | 4 | 1 | Undefined position; Undefined team |
| `82` | `133` | Position_Unknown | Team_Unknown | 601–659 | 59 | 1 | Undefined position; Undefined team |
| `83` | `136` | Position_Unknown | Team_Unknown | 611–622 | 4 | 2 | Undefined position; Undefined team |
| `84` | `137` | Position_Unknown | Team_Unknown | 615–659 | 45 | 1 | Undefined position; Undefined team |
| `85` | `141` | Position_Unknown | Team_Unknown | 633–636 | 4 | 1 | Undefined position; Undefined team |
| `86` | `143` | Position_Unknown | Team_Unknown | 644–645 | 2 | 1 | Undefined position; Undefined team |
| `87` | `146` | Position_Unknown | Team_Unknown | 649–650 | 2 | 1 | Undefined position; Undefined team |
| `88` | `147` | Position_Unknown | Team_Unknown | 652–653 | 2 | 1 | Undefined position; Undefined team |
| `89` | `149` | Position_Unknown | Team_Unknown | 655–659 | 5 | 1 | Undefined position; Undefined team |
| `90` | `150` | Position_Unknown | Team_Unknown | 655–659 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_KickBall` for actor_track_id `28` (Position_Unknown): Annotated start 87 != Inferred start 89
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ 73 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 73 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 146 |
| Missing visible bounding boxes during action | 302 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action 'Action_None' range [31-278] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-659] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-66] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-259] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-300] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-240] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-255] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-345] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-272] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-300] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-367] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-233] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-190] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-390] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-526] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-544] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-608] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-619] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-642] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-652] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-45] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-50] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-125] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-294] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-300] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-44] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-66] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-77] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-251] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-260] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-292] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-47] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [227-302] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [305-307] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [309-310] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [316-381] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [384-631] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [31-43] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-58] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-73] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-103] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-109] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-294] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-577] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-622] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-627] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 31, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [31-31] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-82] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-40] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-61] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-27] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-62] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-30] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-60] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-22] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-122] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-263] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-279] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-77] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [89-92] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-123] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-224] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-277] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-292] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-315] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-509] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-534] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-557] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-596] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-96] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-260] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-287] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-302] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-576] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-592] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-602] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-614] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-620] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-634] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [654-655] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-659] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-90] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-113] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-201] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-211] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-224] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-310] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-323] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-97] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-114] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-112] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-164] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-496] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-509] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-587] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-593] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-599] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-607] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-134] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-258] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-580] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-659] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-359] for track '34' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-511] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-526] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-543] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-202] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-211] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-250] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-261] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-305] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-335] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-166] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-511] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-191] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-240] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-348] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-132] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-163] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-163] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-193] for track '44' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-272] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-320] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-352] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-155] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-164] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-199] for track '46' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-215] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-314] for track '50' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-323] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-344] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-348] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-367] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-436] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-323] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-341] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-481] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-507] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-659] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-500] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-356] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-361] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-376] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-394] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-557] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-630] for track '59' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [636-637] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-656] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-461] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-470] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-476] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-505] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-400] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-659] for track '61' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-659] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-642] for track '63' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-554] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-558] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-623] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-650] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-417] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-486] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-493] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-503] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-520] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-541] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-548] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-564] for track '65' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-574] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-587] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-606] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-423] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-435] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-449] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-500] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-514] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-522] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-608] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-622] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-632] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-650] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-524] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-537] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-544] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-549] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-572] for track '75' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-596] for track '75' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-607] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-611] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-642] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-659] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-553] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-558] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-573] for track '76' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-586] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-589] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-600] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-659] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-566] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-574] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-586] for track '78' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-659] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-569] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-577] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-590] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-607] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-615] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-620] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-643] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-647] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-659] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-584] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-586] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-659] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-612] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-622] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-659] for track '84' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-636] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-645] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [649-650] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-653] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>