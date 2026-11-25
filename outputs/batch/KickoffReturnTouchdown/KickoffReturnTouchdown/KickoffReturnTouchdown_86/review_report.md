# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_86

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_86`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 65
- **Ball Tracks:** 0
- **Action Segments:** 209
- **Validation Warnings:** 269
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 197
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Front_Blocker2 | defense | `11` | `11` |
| ✅ EXACT | `Action_KickBall` | Front_Blocker2 | defense | `11` | `11` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `36` | `26` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `36` | `26` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `0` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `10` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `12` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `14` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `15` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `16` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `18` | `Group` | 0 | START | 4 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `9` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_KickApproach` | Front_Blocker2 | `11` | `11` | 14 | START | 14 | 77 |
| ✅ EXACT | `Action_KickBall` | Front_Blocker2 | `11` | `11` | 78 | START | 78 | 82 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `36` | `26` | 196 | START | 196 | 202 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `36` | `26` | 211 | START | 211 | 569 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 172 | 159 | inferred_complete_timeline |
| `Action_None` | 174 | 540 | 367 | inferred_complete_timeline |
| `Action_None` | 542 | 569 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 307 | 294 | inferred_complete_timeline |
| `Action_None` | 309 | 569 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 548

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 510 | 497 | inferred_complete_timeline |
| `Action_None` | 523 | 524 | 2 | inferred_complete_timeline |
| `Action_None` | 531 | 534 | 4 | inferred_complete_timeline |
| `Action_None` | 538 | 543 | 6 | inferred_complete_timeline |
| `Action_None` | 545 | 569 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 63 | 50 | inferred_complete_timeline |
| `Action_None` | 65 | 71 | 7 | inferred_complete_timeline |
| `Action_None` | 74 | 93 | 20 | inferred_complete_timeline |
| `Action_None` | 96 | 114 | 19 | inferred_complete_timeline |
| `Action_None` | 117 | 130 | 14 | inferred_complete_timeline |
| `Action_None` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_None` | 142 | 149 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 4–6
- **Visible Samples:** 3

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 6 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 69 | 56 | inferred_complete_timeline |
| `Action_None` | 71 | 165 | 95 | inferred_complete_timeline |
| `Action_None` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 254 | 35 | inferred_complete_timeline |
| `Action_None` | 295 | 296 | 2 | inferred_complete_timeline |
| `Action_None` | 299 | 308 | 10 | inferred_complete_timeline |
| `Action_None` | 310 | 569 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 553

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 96 | 83 | inferred_complete_timeline |
| `Action_None` | 98 | 142 | 45 | inferred_complete_timeline |
| `Action_None` | 148 | 170 | 23 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 187 | 6 | inferred_complete_timeline |
| `Action_None` | 189 | 207 | 19 | inferred_complete_timeline |
| `Action_None` | 209 | 311 | 103 | inferred_complete_timeline |
| `Action_None` | 314 | 569 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 566

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 296 | 283 | inferred_complete_timeline |
| `Action_None` | 299 | 300 | 2 | inferred_complete_timeline |
| `Action_None` | 303 | 569 | 267 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 292 | 279 | inferred_complete_timeline |
| `Action_None` | 296 | 303 | 8 | inferred_complete_timeline |
| `Action_None` | 329 | 331 | 3 | inferred_complete_timeline |
| `Action_None` | 334 | 569 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_KickApproach` | 14 | 77 | 64 | inferred_complete_timeline |
| `Action_KickBall` | 78 | 82 | 5 | inferred_complete_timeline |
| `Action_None` | 83 | 228 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 566

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 283 | 270 | inferred_complete_timeline |
| `Action_None` | 288 | 569 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 529 | 516 | inferred_complete_timeline |
| `Action_None` | 531 | 532 | 2 | inferred_complete_timeline |
| `Action_None` | 548 | 569 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 205 | 192 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 569 | 556 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 125 | 112 | inferred_complete_timeline |
| `Action_None` | 127 | 148 | 22 | inferred_complete_timeline |
| `Action_None` | 150 | 155 | 6 | inferred_complete_timeline |
| `Action_None` | 159 | 169 | 11 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 194 | 14 | inferred_complete_timeline |
| `Action_None` | 196 | 220 | 25 | inferred_complete_timeline |
| `Action_None` | 224 | 235 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 513

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 207 | 194 | inferred_complete_timeline |
| `Action_None` | 260 | 281 | 22 | inferred_complete_timeline |
| `Action_None` | 285 | 519 | 235 | inferred_complete_timeline |
| `Action_None` | 522 | 569 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 259 | 246 | inferred_complete_timeline |
| `Action_None` | 261 | 345 | 85 | inferred_complete_timeline |
| `Action_None` | 350 | 569 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 553

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 220 | 207 | inferred_complete_timeline |
| `Action_None` | 231 | 251 | 21 | inferred_complete_timeline |
| `Action_None` | 257 | 260 | 4 | inferred_complete_timeline |
| `Action_None` | 262 | 543 | 282 | inferred_complete_timeline |
| `Action_None` | 545 | 569 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `23` | Position_Unknown | Team_Unknown | 78–83 | 6 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 85–91 | 5 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 86–159 | 9 | 4 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 93–94 | 2 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 105–569 | 440 | 7 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 118–443 | 326 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 121–569 | 443 | 3 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 142–569 | 428 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 143–569 | 427 | 4 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 198–569 | 355 | 6 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 203–204 | 2 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 204–248 | 31 | 4 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 204–222 | 14 | 4 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 221–292 | 65 | 3 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 253–555 | 289 | 4 | Undefined position; Undefined team |
| `34` | `55` | Position_Unknown | Team_Unknown | 271–327 | 55 | 2 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 286–288 | 3 | 1 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 291–293 | 3 | 1 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 296–525 | 221 | 2 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 299–328 | 27 | 3 | Undefined position; Undefined team |
| `39` | `60` | Position_Unknown | Team_Unknown | 304–569 | 266 | 1 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 327–328 | 2 | 1 | Undefined position; Undefined team |
| `41` | `67` | Position_Unknown | Team_Unknown | 345–352 | 4 | 2 | Undefined position; Undefined team |
| `42` | `69` | Position_Unknown | Team_Unknown | 346–569 | 206 | 6 | Undefined position; Undefined team |
| `43` | `75` | Position_Unknown | Team_Unknown | 364–368 | 5 | 1 | Undefined position; Undefined team |
| `44` | `81` | Position_Unknown | Team_Unknown | 404–569 | 126 | 14 | Undefined position; Undefined team |
| `45` | `82` | Position_Unknown | Team_Unknown | 412–413 | 2 | 1 | Undefined position; Undefined team |
| `46` | `83` | Position_Unknown | Team_Unknown | 412–431 | 13 | 4 | Undefined position; Undefined team |
| `47` | `84` | Position_Unknown | Team_Unknown | 425–426 | 2 | 1 | Undefined position; Undefined team |
| `48` | `85` | Position_Unknown | Team_Unknown | 428–431 | 4 | 1 | Undefined position; Undefined team |
| `49` | `88` | Position_Unknown | Team_Unknown | 440–569 | 130 | 1 | Undefined position; Undefined team |
| `50` | `89` | Position_Unknown | Team_Unknown | 440–441 | 2 | 1 | Undefined position; Undefined team |
| `51` | `90` | Position_Unknown | Team_Unknown | 447–565 | 100 | 7 | Undefined position; Undefined team |
| `52` | `92` | Position_Unknown | Team_Unknown | 470–471 | 2 | 1 | Undefined position; Undefined team |
| `53` | `94` | Position_Unknown | Team_Unknown | 472–473 | 2 | 1 | Undefined position; Undefined team |
| `54` | `95` | Position_Unknown | Team_Unknown | 474–475 | 2 | 1 | Undefined position; Undefined team |
| `55` | `97` | Position_Unknown | Team_Unknown | 480–569 | 36 | 8 | Undefined position; Undefined team |
| `56` | `98` | Position_Unknown | Team_Unknown | 485–486 | 2 | 1 | Undefined position; Undefined team |
| `57` | `100` | Position_Unknown | Team_Unknown | 492–498 | 5 | 2 | Undefined position; Undefined team |
| `58` | `101` | Position_Unknown | Team_Unknown | 499–501 | 3 | 1 | Undefined position; Undefined team |
| `59` | `103` | Position_Unknown | Team_Unknown | 515–516 | 2 | 1 | Undefined position; Undefined team |
| `60` | `107` | Position_Unknown | Team_Unknown | 532–534 | 3 | 1 | Undefined position; Undefined team |
| `61` | `109` | Position_Unknown | Team_Unknown | 544–547 | 4 | 1 | Undefined position; Undefined team |
| `62` | `110` | Position_Unknown | Team_Unknown | 548–552 | 4 | 2 | Undefined position; Undefined team |
| `63` | `113` | Position_Unknown | Team_Unknown | 559–560 | 2 | 1 | Undefined position; Undefined team |
| `64` | `114` | Position_Unknown | Team_Unknown | 561–569 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ 47 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 47 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 88, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '580,585,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 94 |
| Missing visible bounding boxes during action | 169 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '20' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action 'Action_None' range [14-296] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-283] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-205] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-529] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-532] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-281] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-519] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-259] for track '6' has 9 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-345] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-569] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-292] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-303] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-331] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-220] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-251] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-543] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-569] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-307] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-69] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-254] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-308] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-228] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-510] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-524] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-534] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-543] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-148] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-155] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-169] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-194] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-220] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-235] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-96] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-142] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-207] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-311] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-569] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-172] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-540] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-63] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-93] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-114] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-130] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-149] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-6] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-83] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-276] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-306] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-335] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-522] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-569] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-443] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-297] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-565] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-569] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-219] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-569] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-248] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-266] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-292] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-324] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-376] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-395] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-555] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-285] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-327] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-525] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-307] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-319] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-328] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-359] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-367] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-464] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-526] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-543] for track '42' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-368] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-409] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-413] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-422] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-429] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-443] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-471] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-476] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-503] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-519] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-532] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-539] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-551] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-558] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-415] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-431] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-431] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-441] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-458] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-476] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-495] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-529] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-547] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-554] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-565] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-484] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-500] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-509] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-516] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-531] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-556] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-561] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-493] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-498] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-501] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-516] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-534] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-547] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-549] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-552] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-560] for track '63' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_86'; source metadata written as null.

</details>