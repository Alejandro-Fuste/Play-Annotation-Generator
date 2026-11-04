# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_35

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_35`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 75
- **Ball Tracks:** 0
- **Action Segments:** 345
- **Validation Warnings:** 453
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 1
- **Group Expanded Events:** 2
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 338
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `9` | `9` |
| ⚠️ START CHANGED | `Action_KickBall` | Position_Unknown | Team_Unknown | `20` | `15` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner | defense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner | defense | `10` | `10` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner | defense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `12` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `9` | `Group` | 0 | START | 0 | 8 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `9` | `9` | 9 | START | 9 | 45 |
| ⚠️ START CHANGED | `Action_KickBall` | Position_Unknown | `20` | `15` | 86 | START | 87 | 89 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner | `10` | `10` | 190 | START | 190 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner | `10` | `10` | 210 | START | 210 | 267 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner | `10` | `10` | 527 | START | N/A | N/A |

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
- **Visible Frames:** 0–389
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_KickApproach` | 9 | 45 | 37 | inferred_complete_timeline |
| `Action_KickApproach` | 48 | 57 | 10 | inferred_complete_timeline |
| `Action_KickApproach` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 108 | 379 | 272 | inferred_complete_timeline |
| `Action_KickApproach` | 383 | 389 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–331
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 8 | 1 | inferred_complete_timeline |
| `Action_None` | 9 | 16 | 8 | inferred_complete_timeline |
| `Action_None` | 23 | 44 | 22 | inferred_complete_timeline |
| `Action_None` | 51 | 59 | 9 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 68 | 74 | 7 | inferred_complete_timeline |
| `Action_None` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_None` | 84 | 96 | 13 | inferred_complete_timeline |
| `Action_None` | 98 | 117 | 20 | inferred_complete_timeline |
| `Action_None` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_None` | 129 | 138 | 10 | inferred_complete_timeline |
| `Action_None` | 143 | 296 | 154 | inferred_complete_timeline |
| `Action_None` | 305 | 331 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 145 | 137 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 184 | 24 | inferred_complete_timeline |
| `Action_None` | 195 | 321 | 127 | inferred_complete_timeline |
| `Action_None` | 323 | 325 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 154 | 146 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_None` | 23 | 41 | 19 | inferred_complete_timeline |
| `Action_None` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_None` | 78 | 99 | 22 | inferred_complete_timeline |
| `Action_None` | 156 | 160 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 100 | 92 | inferred_complete_timeline |
| `Action_None` | 102 | 105 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 104 | 96 | inferred_complete_timeline |
| `Action_None` | 108 | 117 | 10 | inferred_complete_timeline |
| `Action_None` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_None` | 124 | 235 | 112 | inferred_complete_timeline |
| `Action_None` | 255 | 514 | 260 | inferred_complete_timeline |
| `Action_None` | 518 | 523 | 6 | inferred_complete_timeline |
| `Action_None` | 525 | 529 | 5 | inferred_complete_timeline |
| `Action_None` | 531 | 533 | 3 | inferred_complete_timeline |
| `Action_None` | 535 | 539 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 142 | 134 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 160 | 248 | 89 | inferred_complete_timeline |
| `Action_None` | 252 | 319 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–384
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_CatchKick` | 190 | 198 | 9 | inferred_complete_timeline |
| `Action_None` | 199 | 209 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 210 | 267 | 58 | inferred_complete_timeline |
| `Action_BallCarry` | 269 | 292 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 294 | 301 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 317 | 329 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 383 | 384 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 141 | 133 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 278 | 132 | inferred_complete_timeline |
| `Action_None` | 292 | 294 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–339
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 303 | 295 | inferred_complete_timeline |
| `Action_None` | 305 | 319 | 15 | inferred_complete_timeline |
| `Action_None` | 324 | 331 | 8 | inferred_complete_timeline |
| `Action_None` | 333 | 334 | 2 | inferred_complete_timeline |
| `Action_None` | 338 | 339 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–457
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 138 | 130 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 158 | 3 | inferred_complete_timeline |
| `Action_None` | 162 | 166 | 5 | inferred_complete_timeline |
| `Action_None` | 170 | 243 | 74 | inferred_complete_timeline |
| `Action_None` | 246 | 253 | 8 | inferred_complete_timeline |
| `Action_None` | 261 | 273 | 13 | inferred_complete_timeline |
| `Action_None` | 282 | 288 | 7 | inferred_complete_timeline |
| `Action_None` | 291 | 295 | 5 | inferred_complete_timeline |
| `Action_None` | 299 | 392 | 94 | inferred_complete_timeline |
| `Action_None` | 395 | 398 | 4 | inferred_complete_timeline |
| `Action_None` | 400 | 423 | 24 | inferred_complete_timeline |
| `Action_None` | 426 | 430 | 5 | inferred_complete_timeline |
| `Action_None` | 436 | 442 | 7 | inferred_complete_timeline |
| `Action_None` | 448 | 449 | 2 | inferred_complete_timeline |
| `Action_None` | 456 | 457 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 501

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 258 | 250 | inferred_complete_timeline |
| `Action_None` | 282 | 288 | 7 | inferred_complete_timeline |
| `Action_None` | 290 | 344 | 55 | inferred_complete_timeline |
| `Action_None` | 360 | 539 | 180 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 2–61 | 48 | 5 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 10–61 | 44 | 3 | Undefined position; Undefined team |
| `15` | `20` | Position_Unknown | Team_Unknown | 87–89 | 3 | 1 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 87–103 | 14 | 3 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 87–158 | 65 | 5 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 93–280 | 127 | 13 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 96–99 | 4 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 98–99 | 2 | 1 | Undefined position; Undefined team |
| `21` | `31` | Position_Unknown | Team_Unknown | 110–312 | 147 | 16 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 111–384 | 167 | 14 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 111–442 | 284 | 9 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 113–431 | 304 | 6 | Undefined position; Undefined team |
| `25` | `43` | Position_Unknown | Team_Unknown | 128–244 | 107 | 5 | Undefined position; Undefined team |
| `26` | `47` | Position_Unknown | Team_Unknown | 132–294 | 134 | 11 | Undefined position; Undefined team |
| `27` | `48` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `28` | `51` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `29` | `52` | Position_Unknown | Team_Unknown | 141–170 | 19 | 3 | Undefined position; Undefined team |
| `30` | `54` | Position_Unknown | Team_Unknown | 142–220 | 62 | 3 | Undefined position; Undefined team |
| `31` | `61` | Position_Unknown | Team_Unknown | 165–322 | 150 | 3 | Undefined position; Undefined team |
| `32` | `64` | Position_Unknown | Team_Unknown | 167–168 | 2 | 1 | Undefined position; Undefined team |
| `33` | `65` | Position_Unknown | Team_Unknown | 167–171 | 5 | 1 | Undefined position; Undefined team |
| `34` | `66` | Position_Unknown | Team_Unknown | 175–176 | 2 | 1 | Undefined position; Undefined team |
| `35` | `68` | Position_Unknown | Team_Unknown | 178–201 | 24 | 1 | Undefined position; Undefined team |
| `36` | `71` | Position_Unknown | Team_Unknown | 181–238 | 57 | 2 | Undefined position; Undefined team |
| `37` | `73` | Position_Unknown | Team_Unknown | 183–278 | 87 | 3 | Undefined position; Undefined team |
| `38` | `75` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `39` | `78` | Position_Unknown | Team_Unknown | 202–539 | 256 | 10 | Undefined position; Undefined team |
| `40` | `81` | Position_Unknown | Team_Unknown | 236–249 | 14 | 1 | Undefined position; Undefined team |
| `41` | `82` | Position_Unknown | Team_Unknown | 243–539 | 150 | 12 | Undefined position; Undefined team |
| `42` | `83` | Position_Unknown | Team_Unknown | 256–354 | 60 | 2 | Undefined position; Undefined team |
| `43` | `84` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `44` | `86` | Position_Unknown | Team_Unknown | 273–539 | 257 | 3 | Undefined position; Undefined team |
| `45` | `88` | Position_Unknown | Team_Unknown | 292–528 | 217 | 9 | Undefined position; Undefined team |
| `46` | `89` | Position_Unknown | Team_Unknown | 306–539 | 201 | 6 | Undefined position; Undefined team |
| `47` | `90` | Position_Unknown | Team_Unknown | 315–403 | 83 | 3 | Undefined position; Undefined team |
| `48` | `91` | Position_Unknown | Team_Unknown | 316–361 | 40 | 4 | Undefined position; Undefined team |
| `49` | `92` | Position_Unknown | Team_Unknown | 324–539 | 134 | 10 | Undefined position; Undefined team |
| `50` | `93` | Position_Unknown | Team_Unknown | 327–339 | 9 | 2 | Undefined position; Undefined team |
| `51` | `94` | Position_Unknown | Team_Unknown | 330–331 | 2 | 1 | Undefined position; Undefined team |
| `52` | `97` | Position_Unknown | Team_Unknown | 345–351 | 6 | 2 | Undefined position; Undefined team |
| `53` | `99` | Position_Unknown | Team_Unknown | 355–447 | 78 | 8 | Undefined position; Undefined team |
| `54` | `100` | Position_Unknown | Team_Unknown | 356–357 | 2 | 1 | Undefined position; Undefined team |
| `55` | `101` | Position_Unknown | Team_Unknown | 359–440 | 82 | 1 | Undefined position; Undefined team |
| `56` | `102` | Position_Unknown | Team_Unknown | 362–364 | 3 | 1 | Undefined position; Undefined team |
| `57` | `103` | Position_Unknown | Team_Unknown | 365–379 | 4 | 2 | Undefined position; Undefined team |
| `58` | `105` | Position_Unknown | Team_Unknown | 370–371 | 2 | 1 | Undefined position; Undefined team |
| `59` | `109` | Position_Unknown | Team_Unknown | 378–536 | 136 | 14 | Undefined position; Undefined team |
| `60` | `110` | Position_Unknown | Team_Unknown | 378–386 | 7 | 2 | Undefined position; Undefined team |
| `61` | `112` | Position_Unknown | Team_Unknown | 382–443 | 57 | 3 | Undefined position; Undefined team |
| `62` | `117` | Position_Unknown | Team_Unknown | 410–533 | 68 | 12 | Undefined position; Undefined team |
| `63` | `121` | Position_Unknown | Team_Unknown | 420–539 | 114 | 4 | Undefined position; Undefined team |
| `64` | `123` | Position_Unknown | Team_Unknown | 443–448 | 6 | 1 | Undefined position; Undefined team |
| `65` | `124` | Position_Unknown | Team_Unknown | 448–449 | 2 | 1 | Undefined position; Undefined team |
| `66` | `128` | Position_Unknown | Team_Unknown | 479–527 | 34 | 8 | Undefined position; Undefined team |
| `67` | `130` | Position_Unknown | Team_Unknown | 485–486 | 2 | 1 | Undefined position; Undefined team |
| `68` | `133` | Position_Unknown | Team_Unknown | 489–490 | 2 | 1 | Undefined position; Undefined team |
| `69` | `134` | Position_Unknown | Team_Unknown | 494–495 | 2 | 1 | Undefined position; Undefined team |
| `70` | `135` | Position_Unknown | Team_Unknown | 496–537 | 35 | 3 | Undefined position; Undefined team |
| `71` | `140` | Position_Unknown | Team_Unknown | 525–527 | 3 | 1 | Undefined position; Undefined team |
| `72` | `141` | Position_Unknown | Team_Unknown | 534–539 | 6 | 1 | Undefined position; Undefined team |
| `73` | `142` | Position_Unknown | Team_Unknown | 534–539 | 6 | 1 | Undefined position; Undefined team |
| `74` | `143` | Position_Unknown | Team_Unknown | 536–537 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `9` (7 segments found)
- ⚠️ `Action_KickBall` for actor_track_id `20` (Position_Unknown): Annotated start 86 != Inferred start 87
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (5 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `10` (Kick_Returner)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ 62 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 62 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 124 |
| Missing visible bounding boxes during action | 327 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '10' has invalid range: start=527, end=384. Clamping end to start.
- ⚠️ Action 'Action_None' range [9-138] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-243] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-273] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-288] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-295] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-392] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-398] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-423] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-430] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-442] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-303] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-319] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-331] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-141] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-278] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-294] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-154] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-145] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-184] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-321] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-100] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-258] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-288] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-344] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-104] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-235] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-514] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-523] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-529] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-533] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-142] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-248] for track '8' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-319] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [9-45] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [48-57] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [64-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [88-89] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [98-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [108-379] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [383-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchKick' range [190-198] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [210-267] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [269-292] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [294-301] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [317-329] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [383-384] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-21] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-41] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-99] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-16] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-44] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-59] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-74] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-96] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-117] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-138] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-296] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-331] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-8] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-36] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-49] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-56] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-15] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-57] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [87-89] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-103] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-120] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-139] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-102] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-280] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-141] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-153] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-204] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-225] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-240] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-265] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-274] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-298] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-312] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-116] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-125] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-143] for track '22' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-216] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-225] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-276] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-358] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-373] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-118] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-134] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-233] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-433] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-438] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-121] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-197] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-419] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-423] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-131] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-142] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-238] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-139] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-173] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-201] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-216] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-228] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-243] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-294] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-152] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-170] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-187] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-205] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-172] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-316] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-201] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-233] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-192] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-278] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-214] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-414] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-450] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-469] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-490] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-500] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-507] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-539] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-249] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-249] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-272] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-303] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-314] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-378] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-407] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-470] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-537] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-264] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-354] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-302] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-449] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-425] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-436] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-447] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-456] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-462] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-488] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-514] for track '45' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-520] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-528] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-310] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-334] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-365] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-450] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-539] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-335] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-341] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-403] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-347] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-353] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-328] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-345] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-451] for track '49' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-456] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-460] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-470] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-477] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-481] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-487] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-539] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-339] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-361] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-380] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-429] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-435] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-443] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-447] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-440] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-364] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-382] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-396] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-404] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-413] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-429] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-433] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-481] for track '59' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-484] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-507] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-529] for track '59' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-536] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-386] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-396] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-404] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-443] for track '61' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-415] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-434] for track '62' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-450] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-456] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-475] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-486] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-500] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-508] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-514] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-526] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-530] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-463] for track '63' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-476] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-535] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-448] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-483] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-498] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-502] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-506] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-514] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-520] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-527] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-490] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-514] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-527] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-537] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-527] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-539] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '74' has 1 frames without a visible bounding box.
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

</details>