# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_17`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 509
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 146
- **Validation Warnings:** 168
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
- **Inferred Coverage Segments (Action_None):** 128
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `16` | `16` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `16` | `16` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner | defense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner | defense | `11` | `11` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner | defense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `10` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `14` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `15` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `16` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `17` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `18` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `19` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `6` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `7` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `16` | `16` | 47 | START | 47 | 64 |
| ✅ EXACT | `Action_KickBall` | Kicker | `16` | `16` | 65 | START | 65 | 69 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner | `11` | `11` | 183 | START | 183 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner | `11` | `11` | 196 | START | 196 | 270 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner | `11` | `11` | 495 | START | 495 | 508 |

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
- **Visible Frames:** 0–509
- **Visible Samples:** 503

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_KickApproach` | 47 | 64 | 18 | inferred_complete_timeline |
| `Action_KickBall` | 65 | 69 | 5 | inferred_complete_timeline |
| `Action_None` | 70 | 76 | 7 | inferred_complete_timeline |
| `Action_None` | 82 | 370 | 289 | inferred_complete_timeline |
| `Action_None` | 373 | 509 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–42
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 42 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–48
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 47 | 48 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–410
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 75 | 29 | inferred_complete_timeline |
| `Action_None` | 84 | 135 | 52 | inferred_complete_timeline |
| `Action_None` | 137 | 166 | 30 | inferred_complete_timeline |
| `Action_None` | 168 | 241 | 74 | inferred_complete_timeline |
| `Action_None` | 243 | 284 | 42 | inferred_complete_timeline |
| `Action_None` | 286 | 410 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 120 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 118 | 72 | inferred_complete_timeline |
| `Action_None` | 120 | 126 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 127 | 81 | inferred_complete_timeline |
| `Action_None` | 132 | 202 | 71 | inferred_complete_timeline |
| `Action_None` | 204 | 509 | 306 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 32 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 46 | 5 | inferred_complete_timeline |
| `Action_None` | 47 | 509 | 463 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 494

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 162 | 116 | inferred_complete_timeline |
| `Action_None` | 165 | 244 | 80 | inferred_complete_timeline |
| `Action_None` | 257 | 267 | 11 | inferred_complete_timeline |
| `Action_None` | 270 | 509 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–507
- **Visible Samples:** 490

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 175 | 129 | inferred_complete_timeline |
| `Action_None` | 180 | 184 | 5 | inferred_complete_timeline |
| `Action_None` | 186 | 280 | 95 | inferred_complete_timeline |
| `Action_None` | 289 | 326 | 38 | inferred_complete_timeline |
| `Action_None` | 328 | 330 | 3 | inferred_complete_timeline |
| `Action_None` | 335 | 507 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 485

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 95 | 49 | inferred_complete_timeline |
| `Action_None` | 102 | 171 | 70 | inferred_complete_timeline |
| `Action_None` | 178 | 202 | 25 | inferred_complete_timeline |
| `Action_None` | 204 | 273 | 70 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_None` | 290 | 509 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 181 | 135 | inferred_complete_timeline |
| `Action_None` | 184 | 202 | 19 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 286 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 506

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_CatchKick` | 183 | 189 | 7 | inferred_complete_timeline |
| `Action_None` | 190 | 195 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 196 | 270 | 75 | inferred_complete_timeline |
| `Action_BallCarry` | 273 | 330 | 58 | inferred_complete_timeline |
| `Action_BallCarry` | 333 | 494 | 162 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 495 | 508 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 509 | 509 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 95 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 447 | 401 | inferred_complete_timeline |
| `Action_None` | 449 | 509 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 265 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 241 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 431 | 385 | inferred_complete_timeline |
| `Action_None` | 433 | 438 | 6 | inferred_complete_timeline |
| `Action_None` | 440 | 443 | 4 | inferred_complete_timeline |
| `Action_None` | 448 | 452 | 5 | inferred_complete_timeline |
| `Action_None` | 457 | 460 | 4 | inferred_complete_timeline |
| `Action_None` | 462 | 463 | 2 | inferred_complete_timeline |
| `Action_None` | 465 | 509 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 43–509 | 444 | 10 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 59–61 | 3 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 65–137 | 59 | 7 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 83–84 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 96–97 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 103–423 | 316 | 4 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 107–109 | 3 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 109–509 | 394 | 5 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 113–138 | 26 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 138–509 | 365 | 4 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 143–283 | 140 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 143–144 | 2 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 146–148 | 3 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 151–509 | 358 | 2 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 155–348 | 190 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 161–509 | 245 | 4 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 239–509 | 267 | 2 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 256–509 | 254 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 278–477 | 198 | 2 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 294–296 | 3 | 1 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 300–301 | 2 | 1 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 300–301 | 2 | 1 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 323–324 | 2 | 1 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 354–440 | 23 | 5 | Undefined position; Undefined team |
| `44` | `69` | Position_Unknown | Team_Unknown | 502–509 | 8 | 1 | Undefined position; Undefined team |
| `45` | `71` | Position_Unknown | Team_Unknown | 503–509 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Second_Level_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 115 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action 'Action_None' range [47-447] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-175] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-184] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-280] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-326] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-507] for track '1' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-265] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-286] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-181] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-202] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-241] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-120] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-126] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-431] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-438] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-443] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-452] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-460] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-509] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-162] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-244] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-267] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-509] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-75] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-135] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-166] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-241] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-284] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-410] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-270] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [273-330] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [333-494] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-171] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-202] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-273] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-202] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-509] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-76] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-370] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-14] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-509] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-48] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-42] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-74] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-118] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-164] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-176] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-343] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-77] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-113] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-220] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-423] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-115] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-245] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-509] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-138] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-176] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-298] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-509] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-283] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-178] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-221] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-348] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-259] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-509] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-279] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-509] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-509] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-290] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-477] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-357] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-363] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-380] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-440] for track '43' has 2 frames without a visible bounding box.
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

</details>