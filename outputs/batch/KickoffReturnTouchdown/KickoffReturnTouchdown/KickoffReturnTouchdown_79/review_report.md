# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_79

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_79`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 509
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 159
- **Validation Warnings:** 174
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
- **Inferred Coverage Segments (Action_None):** 136
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner | defense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner | defense | `6` | `6` |
| ✅ EXACT | `Action_CrossGoalLine` | Left_Coverage4 | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `10` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `11` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `13` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `14` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `15` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `16` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `17` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `18` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `19` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `4` | `Group` | 0 | START | 0 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `9` | `Group` | 0 | START | 0 | 26 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `15` | `15` | 27 | START | 27 | 84 |
| ✅ EXACT | `Action_KickBall` | Kicker | `15` | `15` | 85 | START | 85 | 89 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner | `6` | `6` | 189 | START | 189 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner | `6` | `6` | 213 | START | 213 | 245 |
| ✅ EXACT | `Action_CrossGoalLine` | Left_Coverage4 | `4` | `4` | 507 | START | 507 | 509 |

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
- **Visible Frames:** 0–477
- **Visible Samples:** 461

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_KickApproach` | 27 | 84 | 58 | inferred_complete_timeline |
| `Action_KickBall` | 85 | 89 | 5 | inferred_complete_timeline |
| `Action_None` | 90 | 276 | 187 | inferred_complete_timeline |
| `Action_None` | 279 | 395 | 117 | inferred_complete_timeline |
| `Action_None` | 401 | 422 | 22 | inferred_complete_timeline |
| `Action_None` | 429 | 455 | 27 | inferred_complete_timeline |
| `Action_None` | 460 | 477 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 285 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–468
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 203 | 177 | inferred_complete_timeline |
| `Action_None` | 232 | 331 | 100 | inferred_complete_timeline |
| `Action_None` | 333 | 337 | 5 | inferred_complete_timeline |
| `Action_None` | 341 | 353 | 13 | inferred_complete_timeline |
| `Action_None` | 356 | 389 | 34 | inferred_complete_timeline |
| `Action_None` | 394 | 407 | 14 | inferred_complete_timeline |
| `Action_None` | 409 | 468 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 240 | 214 | inferred_complete_timeline |
| `Action_None` | 256 | 287 | 32 | inferred_complete_timeline |
| `Action_None` | 291 | 509 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 211 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 244 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 271 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 387 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 389 | 459 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 465 | 506 | 42 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 507 | 509 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 206 | 180 | inferred_complete_timeline |
| `Action_None` | 208 | 509 | 302 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 194 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 174 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_None` | 27 | 35 | 9 | inferred_complete_timeline |
| `Action_None` | 49 | 260 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 486

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 224 | 198 | inferred_complete_timeline |
| `Action_None` | 239 | 241 | 3 | inferred_complete_timeline |
| `Action_None` | 246 | 252 | 7 | inferred_complete_timeline |
| `Action_None` | 255 | 289 | 35 | inferred_complete_timeline |
| `Action_None` | 294 | 509 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–452
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 215 | 189 | inferred_complete_timeline |
| `Action_None` | 217 | 231 | 15 | inferred_complete_timeline |
| `Action_None` | 233 | 290 | 58 | inferred_complete_timeline |
| `Action_None` | 292 | 452 | 161 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–352
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 331 | 305 | inferred_complete_timeline |
| `Action_None` | 342 | 347 | 6 | inferred_complete_timeline |
| `Action_None` | 350 | 352 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 195 | 169 | inferred_complete_timeline |
| `Action_None` | 198 | 290 | 93 | inferred_complete_timeline |
| `Action_None` | 292 | 361 | 70 | inferred_complete_timeline |
| `Action_None` | 370 | 371 | 2 | inferred_complete_timeline |
| `Action_None` | 374 | 509 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 188 | 162 | inferred_complete_timeline |
| `Action_None` | 190 | 253 | 64 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 508

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 110 | 84 | inferred_complete_timeline |
| `Action_None` | 112 | 219 | 108 | inferred_complete_timeline |
| `Action_None` | 221 | 509 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 489

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 188 | 12 | inferred_complete_timeline |
| `Action_CatchKick` | 189 | 210 | 22 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 213 | 245 | 33 | inferred_complete_timeline |
| `Action_BallCarry` | 248 | 266 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 268 | 288 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 291 | 360 | 70 | inferred_complete_timeline |
| `Action_BallCarry` | 365 | 509 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–506
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 270 | 244 | inferred_complete_timeline |
| `Action_None` | 274 | 506 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 122 | 96 | inferred_complete_timeline |
| `Action_None` | 130 | 173 | 44 | inferred_complete_timeline |
| `Action_None` | 176 | 188 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 494

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 334 | 308 | inferred_complete_timeline |
| `Action_None` | 339 | 340 | 2 | inferred_complete_timeline |
| `Action_None` | 343 | 345 | 3 | inferred_complete_timeline |
| `Action_None` | 351 | 397 | 47 | inferred_complete_timeline |
| `Action_None` | 403 | 509 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 250 | 224 | inferred_complete_timeline |
| `Action_None` | 254 | 260 | 7 | inferred_complete_timeline |
| `Action_None` | 262 | 268 | 7 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |
| `Action_None` | 315 | 345 | 31 | inferred_complete_timeline |
| `Action_None` | 350 | 509 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 5–509 | 469 | 8 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 20–408 | 303 | 8 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 100–133 | 7 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 104–137 | 6 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 120–121 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 195–196 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 201–509 | 304 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 244–275 | 22 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 255–509 | 250 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 279–509 | 216 | 4 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 283–509 | 219 | 3 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 290–298 | 9 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 306–308 | 3 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 308–309 | 2 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 310–509 | 182 | 3 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 325–509 | 183 | 2 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 367–397 | 31 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 367–509 | 132 | 4 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 386–395 | 6 | 2 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 408–411 | 4 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 421–509 | 89 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 462–466 | 5 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 496–509 | 9 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 123 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action 'Action_None' range [27-195] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-290] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-361] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-509] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-334] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-397] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-188] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-253] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-250] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-260] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-345] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-211] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-244] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-271] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-387] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-459] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-331] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-347] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-164] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [213-245] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [248-266] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [268-288] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [291-360] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-188] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-270] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-506] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-285] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-206] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-509] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-331] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-337] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-353] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-389] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-407] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-468] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-219] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-194] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-215] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-290] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-452] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-276] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-395] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-422] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-455] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-477] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-240] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-287] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-174] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-224] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-252] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-289] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-35] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-260] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-104] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-250] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-509] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-108] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-272] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-317] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-331] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-346] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-408] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-253] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-509] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-281] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-509] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-315] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-331] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-337] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-290] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-509] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-298] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-355] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-509] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-397] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-387] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-410] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-509] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-389] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-411] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-466] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-509] for track '44' has 1 frames without a visible bounding box.
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

</details>