# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_64

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_64`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 148
- **Validation Warnings:** 159
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 134
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `5` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `18` | `18` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `18` | `18` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | defense | `11` | `11` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `0` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `13` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `15` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `16` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `17` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `18` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `5` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `18` | `18` | 16 | START | 16 | 50 |
| ✅ EXACT | `Action_KickBall` | Kicker | `18` | `18` | 51 | START | 51 | 57 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `11` | `11` | 160 | START | 160 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | `11` | `11` | 180 | START | 180 | 399 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | `11` | `11` | 583 | START | 583 | 599 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–483
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_KickApproach` | 16 | 50 | 35 | inferred_complete_timeline |
| `Action_KickBall` | 51 | 57 | 7 | inferred_complete_timeline |
| `Action_None` | 58 | 409 | 352 | inferred_complete_timeline |
| `Action_None` | 411 | 459 | 49 | inferred_complete_timeline |
| `Action_None` | 477 | 478 | 2 | inferred_complete_timeline |
| `Action_None` | 480 | 483 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 339 | 324 | inferred_complete_timeline |
| `Action_None` | 342 | 599 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 49 | 34 | inferred_complete_timeline |
| `Action_None` | 51 | 96 | 46 | inferred_complete_timeline |
| `Action_None` | 102 | 216 | 115 | inferred_complete_timeline |
| `Action_None` | 218 | 220 | 3 | inferred_complete_timeline |
| `Action_None` | 224 | 240 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 571

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 202 | 187 | inferred_complete_timeline |
| `Action_None` | 232 | 599 | 368 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–435
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 116 | 101 | inferred_complete_timeline |
| `Action_None` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_None` | 125 | 435 | 311 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 234 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–375
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 287 | 272 | inferred_complete_timeline |
| `Action_None` | 289 | 375 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 593

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 376 | 361 | inferred_complete_timeline |
| `Action_None` | 378 | 379 | 2 | inferred_complete_timeline |
| `Action_None` | 384 | 398 | 15 | inferred_complete_timeline |
| `Action_None` | 401 | 599 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 572

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 242 | 227 | inferred_complete_timeline |
| `Action_None` | 247 | 256 | 10 | inferred_complete_timeline |
| `Action_None` | 259 | 263 | 5 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_None` | 269 | 273 | 5 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 280 | 2 | inferred_complete_timeline |
| `Action_None` | 283 | 301 | 19 | inferred_complete_timeline |
| `Action_None` | 303 | 308 | 6 | inferred_complete_timeline |
| `Action_None` | 311 | 312 | 2 | inferred_complete_timeline |
| `Action_None` | 321 | 335 | 15 | inferred_complete_timeline |
| `Action_None` | 339 | 599 | 261 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 355 | 340 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 599 | 584 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 599 | 584 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 213 | 198 | inferred_complete_timeline |
| `Action_None` | 218 | 220 | 3 | inferred_complete_timeline |
| `Action_None` | 224 | 226 | 3 | inferred_complete_timeline |
| `Action_None` | 229 | 234 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–480
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 291 | 276 | inferred_complete_timeline |
| `Action_None` | 305 | 341 | 37 | inferred_complete_timeline |
| `Action_None` | 345 | 480 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–340
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 271 | 256 | inferred_complete_timeline |
| `Action_None` | 273 | 304 | 32 | inferred_complete_timeline |
| `Action_None` | 306 | 315 | 10 | inferred_complete_timeline |
| `Action_None` | 317 | 340 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 159 | 22 | inferred_complete_timeline |
| `Action_CatchKick` | 160 | 164 | 5 | inferred_complete_timeline |
| `Action_None` | 165 | 179 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 180 | 399 | 220 | inferred_complete_timeline |
| `Action_BallCarry` | 402 | 582 | 181 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 583 | 599 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–540
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 535 | 520 | inferred_complete_timeline |
| `Action_None` | 539 | 540 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 244 | 229 | inferred_complete_timeline |
| `Action_None` | 246 | 250 | 5 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_None` | 268 | 599 | 332 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 273 | 258 | inferred_complete_timeline |
| `Action_None` | 275 | 599 | 325 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 599 | 584 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–247 | 248 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–28 | 8 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 6–599 | 577 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 43–45 | 3 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 90–185 | 12 | 5 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 113–241 | 40 | 10 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 243–525 | 283 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 249–250 | 2 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 258–411 | 154 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 270–599 | 330 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 318–599 | 282 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 345–599 | 255 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 375–376 | 2 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 424–599 | 176 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 444–599 | 156 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 454–599 | 98 | 11 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 461–478 | 13 | 3 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 482–485 | 4 | 1 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 523–526 | 4 | 1 | Undefined position; Undefined team |
| `39` | `60` | Position_Unknown | Team_Unknown | 542–599 | 46 | 4 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 545–561 | 10 | 2 | Undefined position; Undefined team |
| `41` | `62` | Position_Unknown | Team_Unknown | 547–552 | 6 | 1 | Undefined position; Undefined team |
| `42` | `64` | Position_Unknown | Team_Unknown | 559–563 | 5 | 1 | Undefined position; Undefined team |
| `43` | `66` | Position_Unknown | Team_Unknown | 570–580 | 5 | 2 | Undefined position; Undefined team |
| `44` | `70` | Position_Unknown | Team_Unknown | 578–583 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 108 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [16-234] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-273] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-242] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-256] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-273] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-301] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-308] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-335] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-244] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-599] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-287] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-375] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-213] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-234] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-291] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-341] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-480] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-535] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-271] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-304] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-315] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-340] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [180-399] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [583-599] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-355] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-376] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-398] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-599] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-435] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-96] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-216] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-240] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-339] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-409] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-459] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-483] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-247] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-6] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-28] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-9] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-119] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-126] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-45] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-122] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-525] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-411] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-456] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-463] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-470] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-485] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-503] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-506] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-509] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-527] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-533] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-599] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-465] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-469] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-478] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-485] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-526] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-548] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-577] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-589] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-552] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-561] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-552] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-563] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-572] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-580] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-583] for track '44' has 1 frames without a visible bounding box.
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