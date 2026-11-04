# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_101

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_101`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 53
- **Ball Tracks:** 1
- **Action Segments:** 170
- **Validation Warnings:** 206
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 156
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `16` | `16` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `16` | `16` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `42` | `32` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `42` | `32` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `42` | `32` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `0` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `1` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `12` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `3` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `4` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `8` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `9` | `Group` | 0 | START | 0 | 12 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `16` | `16` | 21 | START | 21 | 36 |
| ✅ EXACT | `Action_KickBall` | Kicker | `16` | `16` | 86 | START | 86 | 92 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `42` | `32` | 200 | START | 200 | 207 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `42` | `32` | 217 | START | 217 | 539 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `42` | `32` | 540 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–497
- **Visible Samples:** 495

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 20 | 18 | inferred_complete_timeline |
| `Action_KickApproach` | 21 | 36 | 16 | inferred_complete_timeline |
| `Action_KickApproach` | 39 | 85 | 47 | inferred_complete_timeline |
| `Action_KickBall` | 86 | 92 | 7 | inferred_complete_timeline |
| `Action_None` | 93 | 497 | 405 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 518

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 20 | 4 | inferred_complete_timeline |
| `Action_None` | 21 | 29 | 9 | inferred_complete_timeline |
| `Action_None` | 36 | 90 | 55 | inferred_complete_timeline |
| `Action_None` | 95 | 149 | 55 | inferred_complete_timeline |
| `Action_None` | 152 | 300 | 149 | inferred_complete_timeline |
| `Action_None` | 307 | 539 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–411
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 169 | 149 | inferred_complete_timeline |
| `Action_None` | 173 | 180 | 8 | inferred_complete_timeline |
| `Action_None` | 182 | 214 | 33 | inferred_complete_timeline |
| `Action_None` | 219 | 278 | 60 | inferred_complete_timeline |
| `Action_None` | 289 | 297 | 9 | inferred_complete_timeline |
| `Action_None` | 305 | 411 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–535
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 106 | 86 | inferred_complete_timeline |
| `Action_None` | 113 | 123 | 11 | inferred_complete_timeline |
| `Action_None` | 127 | 130 | 4 | inferred_complete_timeline |
| `Action_None` | 142 | 144 | 3 | inferred_complete_timeline |
| `Action_None` | 157 | 160 | 4 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 535 | 366 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 495

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 120 | 100 | inferred_complete_timeline |
| `Action_None` | 128 | 136 | 9 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 166 | 212 | 47 | inferred_complete_timeline |
| `Action_None` | 216 | 302 | 87 | inferred_complete_timeline |
| `Action_None` | 313 | 378 | 66 | inferred_complete_timeline |
| `Action_None` | 380 | 539 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 520

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 120 | 100 | inferred_complete_timeline |
| `Action_None` | 126 | 146 | 21 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 157 | 288 | 132 | inferred_complete_timeline |
| `Action_None` | 297 | 539 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 160 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 92 | 72 | inferred_complete_timeline |
| `Action_None` | 94 | 539 | 446 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 441 | 421 | inferred_complete_timeline |
| `Action_None` | 469 | 470 | 2 | inferred_complete_timeline |
| `Action_None` | 473 | 475 | 3 | inferred_complete_timeline |
| `Action_None` | 487 | 488 | 2 | inferred_complete_timeline |
| `Action_None` | 491 | 539 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 264 | 244 | inferred_complete_timeline |
| `Action_None` | 266 | 539 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–314
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 305 | 285 | inferred_complete_timeline |
| `Action_None` | 313 | 314 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–526
- **Visible Samples:** 522

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 519 | 499 | inferred_complete_timeline |
| `Action_None` | 525 | 526 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 539 | 519 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 20 | 6 | inferred_complete_timeline |
| `Action_None` | 21 | 76 | 56 | inferred_complete_timeline |
| `Action_None` | 78 | 83 | 6 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 118 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 244 | 224 | inferred_complete_timeline |
| `Action_None` | 254 | 302 | 49 | inferred_complete_timeline |
| `Action_None` | 306 | 317 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 200 | 180 | inferred_complete_timeline |
| `Action_None` | 203 | 205 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 252 | 232 | inferred_complete_timeline |
| `Action_None` | 260 | 275 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 114 | 94 | inferred_complete_timeline |
| `Action_None` | 116 | 119 | 4 | inferred_complete_timeline |
| `Action_None` | 122 | 539 | 418 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–65 | 66 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–93 | 26 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–6 | 7 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 15–248 | 222 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 30–31 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 32–539 | 500 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 43–539 | 493 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 64–102 | 18 | 4 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 130–539 | 406 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 140–214 | 18 | 5 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 150–153 | 4 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 158–407 | 245 | 3 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 165–539 | 375 | 4 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 240–245 | 5 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 252–253 | 2 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 253–509 | 246 | 4 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 268–280 | 5 | 2 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 286–539 | 250 | 4 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 311–539 | 228 | 2 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 322–539 | 218 | 1 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 325–539 | 205 | 5 | Undefined position; Undefined team |
| `42` | `68` | Position_Unknown | Team_Unknown | 401–539 | 135 | 2 | Undefined position; Undefined team |
| `43` | `70` | Position_Unknown | Team_Unknown | 430–539 | 108 | 2 | Undefined position; Undefined team |
| `44` | `71` | Position_Unknown | Team_Unknown | 465–466 | 2 | 1 | Undefined position; Undefined team |
| `45` | `73` | Position_Unknown | Team_Unknown | 476–477 | 2 | 1 | Undefined position; Undefined team |
| `46` | `74` | Position_Unknown | Team_Unknown | 477–539 | 53 | 5 | Undefined position; Undefined team |
| `47` | `76` | Position_Unknown | Team_Unknown | 491–492 | 2 | 1 | Undefined position; Undefined team |
| `48` | `80` | Position_Unknown | Team_Unknown | 504–505 | 2 | 1 | Undefined position; Undefined team |
| `49` | `85` | Position_Unknown | Team_Unknown | 517–539 | 23 | 1 | Undefined position; Undefined team |
| `50` | `87` | Position_Unknown | Team_Unknown | 521–539 | 12 | 4 | Undefined position; Undefined team |
| `51` | `88` | Position_Unknown | Team_Unknown | 523–539 | 17 | 1 | Undefined position; Undefined team |
| `52` | `89` | Position_Unknown | Team_Unknown | 528–534 | 6 | 2 | Undefined position; Undefined team |
| `53` | `92` | Position_Unknown | Team_Unknown | 539–539 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | 0 | 57 | 39 | 67.2% | 29–42, 50–53, 56 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `16` (2 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `42` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ 35 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 35 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 70 |
| Missing visible bounding boxes during action | 133 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '32' has invalid range: start=540, end=539. Clamping end to start.
- ⚠️ Action 'Action_None' range [21-120] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-136] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-212] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-302] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-378] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-214] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-278] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-297] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-411] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-264] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-146] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-288] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-539] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-535] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-519] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-526] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-305] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-200] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-92] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-539] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-29] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-90] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-149] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-300] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-441] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-475] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-488] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-539] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-539] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-252] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-275] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-244] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-302] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-317] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [21-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-497] for track '16' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-114] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-539] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-68] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-93] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-76] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-118] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-18] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-94] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-248] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-31] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-36] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-47] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-339] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-402] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-539] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-53] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-97] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-68] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-76] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-93] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-539] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-274] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-310] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-407] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-485] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-490] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-500] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-509] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-314] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-484] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-316] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-539] for track '39' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-335] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-351] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-531] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-539] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-434] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-466] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-482] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-490] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-494] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-505] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-526] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-537] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-529] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-534] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 540. Video range is [0, 539].

</details>