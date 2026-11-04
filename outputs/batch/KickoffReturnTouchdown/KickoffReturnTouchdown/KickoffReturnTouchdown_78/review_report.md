# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_78

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_78`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 66
- **Ball Tracks:** 0
- **Action Segments:** 253
- **Validation Warnings:** 314
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 237
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `7` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `34` | `27` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `34` | `27` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `34` | `27` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `10` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `11` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `13` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `17` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `18` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `2` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `3` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `4` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `5` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `6` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `7` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `5` | `5` | 14 | START | 14 | 102 |
| ✅ EXACT | `Action_KickBall` | Kicker | `5` | `5` | 103 | START | 103 | 107 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `34` | `27` | 207 | START | 207 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `34` | `27` | 221 | START | 221 | 270 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `34` | `27` | 528 | START | 528 | 537 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_KickApproach` | 14 | 102 | 89 | inferred_complete_timeline |
| `Action_KickBall` | 103 | 107 | 5 | inferred_complete_timeline |
| `Action_None` | 108 | 168 | 61 | inferred_complete_timeline |
| `Action_None` | 197 | 212 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 321 | 308 | inferred_complete_timeline |
| `Action_None` | 325 | 327 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 209 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 263 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 179 | 166 | inferred_complete_timeline |
| `Action_None` | 181 | 234 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 147 | 134 | inferred_complete_timeline |
| `Action_None` | 149 | 159 | 11 | inferred_complete_timeline |
| `Action_None` | 162 | 173 | 12 | inferred_complete_timeline |
| `Action_None` | 175 | 179 | 5 | inferred_complete_timeline |
| `Action_None` | 188 | 256 | 69 | inferred_complete_timeline |
| `Action_None` | 259 | 260 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 281 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 161 | 148 | inferred_complete_timeline |
| `Action_None` | 163 | 169 | 7 | inferred_complete_timeline |
| `Action_None` | 171 | 186 | 16 | inferred_complete_timeline |
| `Action_None` | 188 | 267 | 80 | inferred_complete_timeline |
| `Action_None` | 277 | 282 | 6 | inferred_complete_timeline |
| `Action_None` | 284 | 290 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 37 | 69 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 254 | 241 | inferred_complete_timeline |
| `Action_None` | 265 | 267 | 3 | inferred_complete_timeline |
| `Action_None` | 278 | 281 | 4 | inferred_complete_timeline |
| `Action_None` | 284 | 286 | 3 | inferred_complete_timeline |
| `Action_None` | 288 | 289 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 74 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–486
- **Visible Samples:** 475

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 197 | 184 | inferred_complete_timeline |
| `Action_None` | 202 | 435 | 234 | inferred_complete_timeline |
| `Action_None` | 442 | 482 | 41 | inferred_complete_timeline |
| `Action_None` | 485 | 486 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 312 | 299 | inferred_complete_timeline |
| `Action_None` | 382 | 385 | 4 | inferred_complete_timeline |
| `Action_None` | 390 | 394 | 5 | inferred_complete_timeline |
| `Action_None` | 396 | 400 | 5 | inferred_complete_timeline |
| `Action_None` | 404 | 454 | 51 | inferred_complete_timeline |
| `Action_None` | 473 | 531 | 59 | inferred_complete_timeline |
| `Action_None` | 535 | 536 | 2 | inferred_complete_timeline |
| `Action_None` | 539 | 539 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 151 | 138 | inferred_complete_timeline |
| `Action_None` | 153 | 229 | 77 | inferred_complete_timeline |
| `Action_None` | 234 | 261 | 28 | inferred_complete_timeline |
| `Action_None` | 264 | 268 | 5 | inferred_complete_timeline |
| `Action_None` | 279 | 281 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 190 | 177 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 238 | 254 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 111 | 98 | inferred_complete_timeline |
| `Action_None` | 117 | 539 | 423 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 287 | 274 | inferred_complete_timeline |
| `Action_None` | 289 | 304 | 16 | inferred_complete_timeline |
| `Action_None` | 364 | 385 | 22 | inferred_complete_timeline |
| `Action_None` | 394 | 395 | 2 | inferred_complete_timeline |
| `Action_None` | 406 | 539 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 195 | 182 | inferred_complete_timeline |
| `Action_None` | 202 | 208 | 7 | inferred_complete_timeline |
| `Action_None` | 215 | 231 | 17 | inferred_complete_timeline |
| `Action_None` | 236 | 255 | 20 | inferred_complete_timeline |
| `Action_None` | 260 | 267 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 258 | 245 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |
| `Action_None` | 278 | 281 | 4 | inferred_complete_timeline |
| `Action_None` | 284 | 286 | 3 | inferred_complete_timeline |
| `Action_None` | 288 | 289 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–107 | 40 | 6 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 77–539 | 452 | 6 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 92–539 | 424 | 7 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 114–124 | 9 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 126–539 | 397 | 8 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 132–133 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 137–539 | 388 | 6 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 139–267 | 120 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 156–188 | 23 | 4 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 158–539 | 359 | 9 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 190–212 | 14 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 212–226 | 15 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 222–401 | 175 | 4 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 232–339 | 103 | 3 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 244–539 | 258 | 4 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 267–539 | 211 | 14 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 270–287 | 9 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 276–277 | 2 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 291–539 | 249 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 305–511 | 139 | 13 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 306–539 | 232 | 2 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 308–322 | 9 | 4 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 328–331 | 4 | 1 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 342–343 | 2 | 1 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 344–345 | 2 | 1 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 346–539 | 192 | 2 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 356–539 | 176 | 4 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 360–362 | 3 | 1 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 364–390 | 24 | 2 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 369–370 | 2 | 1 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 372–539 | 157 | 4 | Undefined position; Undefined team |
| `49` | `73` | Position_Unknown | Team_Unknown | 376–377 | 2 | 1 | Undefined position; Undefined team |
| `50` | `75` | Position_Unknown | Team_Unknown | 381–493 | 87 | 9 | Undefined position; Undefined team |
| `51` | `77` | Position_Unknown | Team_Unknown | 388–392 | 5 | 1 | Undefined position; Undefined team |
| `52` | `79` | Position_Unknown | Team_Unknown | 392–534 | 143 | 1 | Undefined position; Undefined team |
| `53` | `80` | Position_Unknown | Team_Unknown | 394–539 | 126 | 9 | Undefined position; Undefined team |
| `54` | `81` | Position_Unknown | Team_Unknown | 395–539 | 138 | 4 | Undefined position; Undefined team |
| `55` | `83` | Position_Unknown | Team_Unknown | 401–521 | 121 | 1 | Undefined position; Undefined team |
| `56` | `85` | Position_Unknown | Team_Unknown | 402–539 | 137 | 2 | Undefined position; Undefined team |
| `57` | `88` | Position_Unknown | Team_Unknown | 410–513 | 74 | 5 | Undefined position; Undefined team |
| `58` | `89` | Position_Unknown | Team_Unknown | 412–500 | 83 | 5 | Undefined position; Undefined team |
| `59` | `90` | Position_Unknown | Team_Unknown | 416–425 | 10 | 1 | Undefined position; Undefined team |
| `60` | `93` | Position_Unknown | Team_Unknown | 421–438 | 18 | 1 | Undefined position; Undefined team |
| `61` | `94` | Position_Unknown | Team_Unknown | 422–423 | 2 | 1 | Undefined position; Undefined team |
| `62` | `101` | Position_Unknown | Team_Unknown | 496–514 | 19 | 1 | Undefined position; Undefined team |
| `63` | `102` | Position_Unknown | Team_Unknown | 499–533 | 32 | 3 | Undefined position; Undefined team |
| `64` | `105` | Position_Unknown | Team_Unknown | 536–539 | 4 | 1 | Undefined position; Undefined team |
| `65` | `106` | Position_Unknown | Team_Unknown | 537–539 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `34` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ 48 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 48 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 96 |
| Missing visible bounding boxes during action | 217 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action 'Action_None' range [14-258] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-269] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-312] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-385] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-394] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-400] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-454] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-531] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-321] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-263] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-168] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-212] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-179] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-234] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-147] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-159] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-256] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-287] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-304] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-385] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-195] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-208] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-231] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-255] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-267] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-161] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-186] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-267] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-282] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-290] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-197] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-435] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-482] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-111] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-539] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-254] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-190] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-254] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-37] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-151] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-229] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-261] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-69] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-201] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-269] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-281] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-291] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-438] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-539] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-156] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-191] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-254] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-340] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-118] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-217] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-264] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-273] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-282] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-289] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-479] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-494] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-539] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-234] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-269] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-282] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-304] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-364] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-228] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-255] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-267] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-179] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [221-270] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [279-280] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [288-289] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [298-527] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-204] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-226] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-237] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-397] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-401] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-303] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-308] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-339] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-290] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-539] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-273] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-303] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-392] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-402] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-442] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-459] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-472] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-483] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-488] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-505] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-527] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-539] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-275] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-539] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-369] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-420] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-437] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-455] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-477] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-480] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-492] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-507] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-511] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-339] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-539] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-331] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-413] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-365] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-373] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-380] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-362] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-377] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-390] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-383] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-389] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-430] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-391] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-394] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-400] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-409] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-451] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-477] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-485] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-493] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-392] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-534] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-413] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-450] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-460] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-466] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-474] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-517] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-520] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-528] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-407] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-420] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-539] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-521] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-484] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-415] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-429] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-435] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-455] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-513] for track '57' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-421] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-462] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-497] for track '58' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-425] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-438] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-423] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-514] for track '62' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-506] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-515] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-533] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>