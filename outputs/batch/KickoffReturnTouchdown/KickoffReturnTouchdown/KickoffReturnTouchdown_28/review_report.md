# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_28

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_28`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 132
- **Validation Warnings:** 130
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
- **Inferred Coverage Segments (Action_None):** 116
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `8` | `8` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `8` | `8` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | defense | `21` | `21` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `0` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `10` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `11` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `12` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `16` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `18` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `4` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `6` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `8` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `9` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `8` | `8` | 20 | START | 20 | 89 |
| ✅ EXACT | `Action_KickBall` | Kicker | `8` | `8` | 90 | START | 90 | 93 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `21` | `21` | 193 | START | 193 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | `21` | `21` | 225 | START | 225 | 582 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | `21` | `21` | 583 | START | 583 | 598 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_KickApproach` | 20 | 89 | 70 | inferred_complete_timeline |
| `Action_KickBall` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_None` | 94 | 141 | 48 | inferred_complete_timeline |
| `Action_None` | 144 | 388 | 245 | inferred_complete_timeline |
| `Action_None` | 396 | 599 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–430
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 426 | 407 | inferred_complete_timeline |
| `Action_None` | 429 | 430 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 596

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 301 | 282 | inferred_complete_timeline |
| `Action_None` | 303 | 481 | 179 | inferred_complete_timeline |
| `Action_None` | 485 | 599 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 589

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 338 | 319 | inferred_complete_timeline |
| `Action_None` | 342 | 535 | 194 | inferred_complete_timeline |
| `Action_None` | 537 | 538 | 2 | inferred_complete_timeline |
| `Action_None` | 546 | 599 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 593

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 228 | 209 | inferred_complete_timeline |
| `Action_None` | 231 | 309 | 79 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 317 | 599 | 283 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 231 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 584

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 387 | 368 | inferred_complete_timeline |
| `Action_None` | 397 | 430 | 34 | inferred_complete_timeline |
| `Action_None` | 437 | 440 | 4 | inferred_complete_timeline |
| `Action_None` | 442 | 599 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 130 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 285 | 266 | inferred_complete_timeline |
| `Action_None` | 307 | 368 | 62 | inferred_complete_timeline |
| `Action_None` | 378 | 379 | 2 | inferred_complete_timeline |
| `Action_None` | 381 | 599 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 312 | 293 | inferred_complete_timeline |
| `Action_None` | 321 | 338 | 18 | inferred_complete_timeline |
| `Action_None` | 345 | 599 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 290 | 271 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 263 | 244 | inferred_complete_timeline |
| `Action_None` | 265 | 599 | 335 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–331
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 311 | 292 | inferred_complete_timeline |
| `Action_None` | 313 | 331 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–598
- **Visible Samples:** 526

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 203 | 184 | inferred_complete_timeline |
| `Action_None` | 205 | 212 | 8 | inferred_complete_timeline |
| `Action_None` | 216 | 245 | 30 | inferred_complete_timeline |
| `Action_None` | 300 | 304 | 5 | inferred_complete_timeline |
| `Action_None` | 307 | 309 | 3 | inferred_complete_timeline |
| `Action_None` | 313 | 361 | 49 | inferred_complete_timeline |
| `Action_None` | 364 | 365 | 2 | inferred_complete_timeline |
| `Action_None` | 370 | 395 | 26 | inferred_complete_timeline |
| `Action_None` | 400 | 598 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 588

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 220 | 201 | inferred_complete_timeline |
| `Action_None` | 224 | 326 | 103 | inferred_complete_timeline |
| `Action_None` | 334 | 545 | 212 | inferred_complete_timeline |
| `Action_None` | 548 | 599 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 345 | 326 | inferred_complete_timeline |
| `Action_None` | 354 | 355 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_CatchKick` | 193 | 207 | 15 | inferred_complete_timeline |
| `Action_None` | 208 | 224 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 225 | 582 | 358 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 583 | 598 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 599 | 599 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–538
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 328 | 309 | inferred_complete_timeline |
| `Action_None` | 330 | 538 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–384
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 264 | 245 | inferred_complete_timeline |
| `Action_None` | 268 | 344 | 77 | inferred_complete_timeline |
| `Action_None` | 346 | 369 | 24 | inferred_complete_timeline |
| `Action_None` | 372 | 376 | 5 | inferred_complete_timeline |
| `Action_None` | 378 | 384 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–598
- **Visible Samples:** 589

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 264 | 245 | inferred_complete_timeline |
| `Action_None` | 273 | 301 | 29 | inferred_complete_timeline |
| `Action_None` | 304 | 598 | 295 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 592

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 86 | 67 | inferred_complete_timeline |
| `Action_None` | 89 | 100 | 12 | inferred_complete_timeline |
| `Action_None` | 107 | 599 | 493 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–320
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 320 | 301 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 147–148 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 152–275 | 122 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 214–216 | 3 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 243–246 | 4 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 249–599 | 331 | 7 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 314–599 | 276 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 332–592 | 248 | 6 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 333–599 | 244 | 6 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 348–350 | 3 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 355–599 | 243 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 381–382 | 2 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 394–599 | 203 | 3 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 416–417 | 2 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 431–599 | 169 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 458–463 | 6 | 1 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 508–515 | 8 | 1 | Undefined position; Undefined team |
| `38` | `62` | Position_Unknown | Team_Unknown | 541–599 | 59 | 1 | Undefined position; Undefined team |
| `39` | `64` | Position_Unknown | Team_Unknown | 547–551 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 93 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [20-301] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-481] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-599] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-220] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-326] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-545] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-426] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-311] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-331] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-290] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-264] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-344] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-369] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-376] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-384] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-338] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-535] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-538] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-320] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-141] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-388] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-312] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-338] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-130] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-387] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-430] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-440] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-599] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-228] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-309] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-264] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-301] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-598] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-203] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-212] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-245] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-304] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-361] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-395] for track '14' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-598] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-345] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-285] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-368] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-263] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-231] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-328] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-538] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-599] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [225-582] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-275] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-280] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-306] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-323] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-350] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-599] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-324] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-384] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-390] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-570] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-580] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-587] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-592] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-341] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-369] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-383] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-430] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-599] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-350] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-450] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-487] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-493] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-463] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-515] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-599] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-551] for track '39' has 2 frames without a visible bounding box.
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

</details>