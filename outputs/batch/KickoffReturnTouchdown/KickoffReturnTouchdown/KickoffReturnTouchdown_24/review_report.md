# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_24

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_24`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 44
- **Ball Tracks:** 1
- **Action Segments:** 102
- **Validation Warnings:** 111
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Second_Level_Blocker4 | defense | `6` | `6` |
| ✅ EXACT | `Action_KickBall` | Second_Level_Blocker4 | defense | `6` | `6` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | defense | `12` | `12` |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner2 | defense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner2 | defense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `10` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `13` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `16` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `17` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `18` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `19` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `21` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `5` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `7` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `8` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `9` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_KickApproach` | Second_Level_Blocker4 | `6` | `6` | 31 | START | 31 | 88 |
| ✅ EXACT | `Action_KickBall` | Second_Level_Blocker4 | `6` | `6` | 89 | START | 89 | 97 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | `12` | `12` | 194 | START | 194 | 204 |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner2 | `12` | `12` | 212 | START | 212 | 569 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner2 | `12` | `12` | 570 | START | N/A | N/A |

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
- **Visible Frames:** 0–394
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 394 | 364 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 260 | 230 | inferred_complete_timeline |
| `Action_None` | 264 | 418 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 267 | 237 | inferred_complete_timeline |
| `Action_None` | 275 | 297 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 557

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 235 | 205 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |
| `Action_None` | 242 | 255 | 14 | inferred_complete_timeline |
| `Action_None` | 260 | 265 | 6 | inferred_complete_timeline |
| `Action_None` | 269 | 288 | 20 | inferred_complete_timeline |
| `Action_None` | 290 | 293 | 4 | inferred_complete_timeline |
| `Action_None` | 295 | 569 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 217 | 187 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 234 | 6 | inferred_complete_timeline |
| `Action_None` | 237 | 289 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–330
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 218 | 188 | inferred_complete_timeline |
| `Action_None` | 223 | 266 | 44 | inferred_complete_timeline |
| `Action_None` | 269 | 330 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 206 | 176 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 274 | 569 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 569 | 539 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 516

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 219 | 189 | inferred_complete_timeline |
| `Action_None` | 273 | 465 | 193 | inferred_complete_timeline |
| `Action_None` | 467 | 569 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–457
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 267 | 237 | inferred_complete_timeline |
| `Action_None` | 277 | 457 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–567
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 567 | 537 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 247 | 217 | inferred_complete_timeline |
| `Action_None` | 249 | 252 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 326 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–452
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 147 | 117 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |
| `Action_None` | 271 | 392 | 122 | inferred_complete_timeline |
| `Action_None` | 451 | 452 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 276 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 569 | 539 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 476 | 446 | inferred_complete_timeline |
| `Action_None` | 482 | 569 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_CatchKick` | 194 | 204 | 11 | inferred_complete_timeline |
| `Action_None` | 205 | 211 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 212 | 569 | 358 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 232 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 564

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 228 | 198 | inferred_complete_timeline |
| `Action_None` | 232 | 382 | 151 | inferred_complete_timeline |
| `Action_None` | 386 | 569 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–336
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 336 | 306 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_KickApproach` | 31 | 88 | 58 | inferred_complete_timeline |
| `Action_KickBall` | 89 | 97 | 9 | inferred_complete_timeline |
| `Action_None` | 98 | 275 | 178 | inferred_complete_timeline |
| `Action_None` | 278 | 293 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 20–24 | 5 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 108–110 | 3 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 122–123 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 142–156 | 13 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 220–569 | 348 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 231–276 | 46 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 234–569 | 282 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 235–327 | 91 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 256–569 | 314 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 264–266 | 3 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 291–392 | 102 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 305–308 | 4 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 322–333 | 12 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 366–386 | 8 | 2 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 385–389 | 5 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 483–569 | 87 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 486–530 | 44 | 2 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 489–569 | 81 | 1 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 490–569 | 80 | 1 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 516–569 | 54 | 1 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 552–555 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `36` | `48` | 331 | 331 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CrossGoalLine` on target `12` (Kick_Returner2)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '12' has invalid range: start=570, end=569. Clamping end to start.
- ⚠️ Action 'Action_None' range [31-336] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-232] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-476] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-228] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-382] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-147] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-392] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-452] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-206] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-275] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-293] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-267] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-297] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-267] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-457] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-217] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-234] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-289] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-219] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-465] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-569] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-247] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-567] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-326] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-276] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-394] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-260] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-418] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-218] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-266] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-330] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-569] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-235] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-255] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-288] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-24] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-156] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-271] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-276] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-569] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-323] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-392] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-308] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-333] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-370] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-386] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-389] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-503] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-530] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-555] for track '44' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 570. Video range is [0, 569].

</details>