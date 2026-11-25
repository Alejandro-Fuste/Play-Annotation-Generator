# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_58

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_58`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 65
- **Ball Tracks:** 0
- **Action Segments:** 213
- **Validation Warnings:** 259
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
- **Inferred Coverage Segments (Action_None):** 198
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `17` | `17` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `17` | `17` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `16` | `16` |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner1 | defense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `0` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `1` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `10` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `14` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `17` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `4` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `8` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `9` | `Group` | 0 | START | 0 | 3 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `17` | `17` | 4 | START | 4 | 67 |
| ✅ EXACT | `Action_KickBall` | Kicker | `17` | `17` | 80 | START | 80 | 85 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `16` | `16` | 190 | START | 190 | 198 |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner1 | `16` | `16` | 213 | START | 213 | 599 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_KickApproach` | 4 | 67 | 64 | inferred_complete_timeline |
| `Action_KickApproach` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 76 | 79 | 4 | inferred_complete_timeline |
| `Action_KickBall` | 80 | 85 | 6 | inferred_complete_timeline |
| `Action_None` | 86 | 90 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 49 | 46 | inferred_complete_timeline |
| `Action_None` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_None` | 64 | 73 | 10 | inferred_complete_timeline |
| `Action_None` | 75 | 85 | 11 | inferred_complete_timeline |
| `Action_None` | 87 | 102 | 16 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 116 | 128 | 13 | inferred_complete_timeline |
| `Action_None` | 134 | 146 | 13 | inferred_complete_timeline |
| `Action_None` | 148 | 184 | 37 | inferred_complete_timeline |
| `Action_None` | 187 | 276 | 90 | inferred_complete_timeline |
| `Action_None` | 280 | 599 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–351
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 106 | 103 | inferred_complete_timeline |
| `Action_None` | 108 | 264 | 157 | inferred_complete_timeline |
| `Action_None` | 266 | 351 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 592

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 94 | 91 | inferred_complete_timeline |
| `Action_None` | 101 | 104 | 4 | inferred_complete_timeline |
| `Action_None` | 106 | 450 | 345 | inferred_complete_timeline |
| `Action_None` | 452 | 599 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–553
- **Visible Samples:** 546

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 315 | 312 | inferred_complete_timeline |
| `Action_None` | 317 | 332 | 16 | inferred_complete_timeline |
| `Action_None` | 334 | 545 | 212 | inferred_complete_timeline |
| `Action_None` | 552 | 553 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 130 | 127 | inferred_complete_timeline |
| `Action_None` | 132 | 599 | 468 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 161 | 158 | inferred_complete_timeline |
| `Action_None` | 166 | 177 | 12 | inferred_complete_timeline |
| `Action_None` | 179 | 195 | 17 | inferred_complete_timeline |
| `Action_None` | 197 | 202 | 6 | inferred_complete_timeline |
| `Action_None` | 206 | 599 | 394 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 91 | 88 | inferred_complete_timeline |
| `Action_None` | 94 | 117 | 24 | inferred_complete_timeline |
| `Action_None` | 119 | 132 | 14 | inferred_complete_timeline |
| `Action_None` | 136 | 160 | 25 | inferred_complete_timeline |
| `Action_None` | 164 | 216 | 53 | inferred_complete_timeline |
| `Action_None` | 222 | 241 | 20 | inferred_complete_timeline |
| `Action_None` | 249 | 281 | 33 | inferred_complete_timeline |
| `Action_None` | 287 | 375 | 89 | inferred_complete_timeline |
| `Action_None` | 398 | 440 | 43 | inferred_complete_timeline |
| `Action_None` | 443 | 446 | 4 | inferred_complete_timeline |
| `Action_None` | 450 | 452 | 3 | inferred_complete_timeline |
| `Action_None` | 458 | 551 | 94 | inferred_complete_timeline |
| `Action_None` | 554 | 579 | 26 | inferred_complete_timeline |
| `Action_None` | 584 | 590 | 7 | inferred_complete_timeline |
| `Action_None` | 593 | 599 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 580

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 93 | 90 | inferred_complete_timeline |
| `Action_None` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_None` | 106 | 108 | 3 | inferred_complete_timeline |
| `Action_None` | 113 | 132 | 20 | inferred_complete_timeline |
| `Action_None` | 137 | 453 | 317 | inferred_complete_timeline |
| `Action_None` | 456 | 554 | 99 | inferred_complete_timeline |
| `Action_None` | 557 | 578 | 22 | inferred_complete_timeline |
| `Action_None` | 581 | 599 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 103 | 100 | inferred_complete_timeline |
| `Action_None` | 105 | 110 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–427
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 127 | 124 | inferred_complete_timeline |
| `Action_None` | 129 | 375 | 247 | inferred_complete_timeline |
| `Action_None` | 377 | 427 | 51 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 339 | 336 | inferred_complete_timeline |
| `Action_None` | 350 | 565 | 216 | inferred_complete_timeline |
| `Action_None` | 569 | 599 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 358 | 355 | inferred_complete_timeline |
| `Action_None` | 360 | 363 | 4 | inferred_complete_timeline |
| `Action_None` | 365 | 599 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 216 | 213 | inferred_complete_timeline |
| `Action_None` | 222 | 239 | 18 | inferred_complete_timeline |
| `Action_None` | 241 | 384 | 144 | inferred_complete_timeline |
| `Action_None` | 388 | 599 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 223 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 599 | 596 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 599 | 596 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 189 | 23 | inferred_complete_timeline |
| `Action_CatchKick` | 190 | 198 | 9 | inferred_complete_timeline |
| `Action_None` | 199 | 212 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 213 | 599 | 387 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 330 | 327 | inferred_complete_timeline |
| `Action_None` | 332 | 599 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–307
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 307 | 304 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 599 | 596 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 599 | 596 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–83 | 50 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 134–136 | 3 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 136–599 | 452 | 6 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 140–599 | 440 | 8 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 149–150 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 166–168 | 3 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 204–257 | 34 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 229–233 | 5 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 231–293 | 63 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 262–277 | 16 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 295–299 | 4 | 2 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 305–599 | 295 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 309–599 | 262 | 7 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 348–350 | 3 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 351–408 | 23 | 7 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 360–599 | 240 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 361–409 | 18 | 3 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 410–411 | 2 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 412–453 | 29 | 3 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 435–436 | 2 | 1 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 447–599 | 153 | 1 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 453–488 | 31 | 3 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 454–485 | 27 | 3 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 461–470 | 9 | 2 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 462–463 | 2 | 1 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 462–485 | 16 | 3 | Undefined position; Undefined team |
| `49` | `68` | Position_Unknown | Team_Unknown | 465–478 | 12 | 2 | Undefined position; Undefined team |
| `50` | `69` | Position_Unknown | Team_Unknown | 477–478 | 2 | 1 | Undefined position; Undefined team |
| `51` | `73` | Position_Unknown | Team_Unknown | 487–599 | 93 | 6 | Undefined position; Undefined team |
| `52` | `75` | Position_Unknown | Team_Unknown | 500–572 | 20 | 3 | Undefined position; Undefined team |
| `53` | `77` | Position_Unknown | Team_Unknown | 518–599 | 65 | 4 | Undefined position; Undefined team |
| `54` | `78` | Position_Unknown | Team_Unknown | 526–528 | 3 | 1 | Undefined position; Undefined team |
| `55` | `79` | Position_Unknown | Team_Unknown | 528–529 | 2 | 1 | Undefined position; Undefined team |
| `56` | `82` | Position_Unknown | Team_Unknown | 536–599 | 59 | 2 | Undefined position; Undefined team |
| `57` | `83` | Position_Unknown | Team_Unknown | 536–599 | 61 | 3 | Undefined position; Undefined team |
| `58` | `89` | Position_Unknown | Team_Unknown | 564–599 | 24 | 4 | Undefined position; Undefined team |
| `59` | `90` | Position_Unknown | Team_Unknown | 568–599 | 32 | 1 | Undefined position; Undefined team |
| `60` | `93` | Position_Unknown | Team_Unknown | 575–587 | 9 | 4 | Undefined position; Undefined team |
| `61` | `94` | Position_Unknown | Team_Unknown | 578–584 | 6 | 2 | Undefined position; Undefined team |
| `62` | `95` | Position_Unknown | Team_Unknown | 579–586 | 4 | 2 | Undefined position; Undefined team |
| `63` | `99` | Position_Unknown | Team_Unknown | 592–599 | 8 | 1 | Undefined position; Undefined team |
| `64` | `100` | Position_Unknown | Team_Unknown | 599–599 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `17` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ 43 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 43 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 60, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '610,615,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 86 |
| Missing visible bounding boxes during action | 171 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [4-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-177] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-195] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-91] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-117] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-132] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-160] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-216] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-241] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-281] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-375] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-440] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-446] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-452] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-551] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-579] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-590] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-358] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-363] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-223] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-103] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-339] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-565] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-216] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-384] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-450] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-599] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-375] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-427] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-132] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-453] for track '10' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-554] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-578] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-599] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-315] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-332] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-545] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-553] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-599] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-599] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-307] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-165] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [4-67] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [71-72] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-330] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-599] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-599] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-106] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-264] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-351] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-49] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-85] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-102] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-128] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-146] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-184] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-276] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-599] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-16] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-64] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-83] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-599] for track '24' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-167] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-401] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-409] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-430] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-599] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-230] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-257] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-233] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-293] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-277] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-315] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-328] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-335] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-353] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-350] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-364] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-370] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-377] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-408] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-368] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-409] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-430] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-442] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-599] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-479] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-485] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-488] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-458] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-479] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-485] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-466] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-470] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-471] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-479] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-485] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-474] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-493] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-507] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-513] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-529] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-504] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-516] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-572] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-519] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-537] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-577] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-599] for track '53' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-528] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-529] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-599] for track '56' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-541] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-547] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-599] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-577] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-596] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-576] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-580] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-584] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-587] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-581] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-584] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-580] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-586] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-599] for track '63' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_58'; source metadata written as null.

</details>