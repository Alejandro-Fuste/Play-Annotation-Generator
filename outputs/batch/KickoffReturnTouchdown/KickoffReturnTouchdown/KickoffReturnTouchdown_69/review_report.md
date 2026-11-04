# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_69

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_69`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 57
- **Ball Tracks:** 0
- **Action Segments:** 191
- **Validation Warnings:** 235
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
- **Inferred Coverage Segments (Action_None):** 175
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `8` | `8` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `8` | `8` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `27` | `27` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `27` | `27` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `27` | `27` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `0` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `1` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `11` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `14` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `15` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `16` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `2` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `3` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `4` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `7` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `8` | `Group` | 0 | START | 0 | 22 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `8` | `8` | 23 | START | 23 | 57 |
| ✅ EXACT | `Action_KickBall` | Kicker | `8` | `8` | 58 | START | 58 | 62 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `27` | `27` | 177 | START | 177 | 192 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `27` | `27` | 221 | START | 221 | 590 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `27` | `27` | 591 | START | 591 | 597 |

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
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_KickApproach` | 23 | 57 | 35 | inferred_complete_timeline |
| `Action_KickBall` | 58 | 62 | 5 | inferred_complete_timeline |
| `Action_None` | 63 | 554 | 492 | inferred_complete_timeline |
| `Action_None` | 556 | 599 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 129 | 107 | inferred_complete_timeline |
| `Action_None` | 137 | 328 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 40 | 18 | inferred_complete_timeline |
| `Action_None` | 43 | 54 | 12 | inferred_complete_timeline |
| `Action_None` | 56 | 65 | 10 | inferred_complete_timeline |
| `Action_None` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_None` | 80 | 85 | 6 | inferred_complete_timeline |
| `Action_None` | 95 | 100 | 6 | inferred_complete_timeline |
| `Action_None` | 103 | 106 | 4 | inferred_complete_timeline |
| `Action_None` | 112 | 125 | 14 | inferred_complete_timeline |
| `Action_None` | 127 | 132 | 6 | inferred_complete_timeline |
| `Action_None` | 137 | 292 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–455
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 46 | 24 | inferred_complete_timeline |
| `Action_None` | 48 | 54 | 7 | inferred_complete_timeline |
| `Action_None` | 56 | 64 | 9 | inferred_complete_timeline |
| `Action_None` | 67 | 72 | 6 | inferred_complete_timeline |
| `Action_None` | 75 | 87 | 13 | inferred_complete_timeline |
| `Action_None` | 95 | 197 | 103 | inferred_complete_timeline |
| `Action_None` | 245 | 455 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–467
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 213 | 191 | inferred_complete_timeline |
| `Action_None` | 226 | 255 | 30 | inferred_complete_timeline |
| `Action_None` | 258 | 353 | 96 | inferred_complete_timeline |
| `Action_None` | 360 | 467 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 597

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 39 | 17 | inferred_complete_timeline |
| `Action_None` | 42 | 228 | 187 | inferred_complete_timeline |
| `Action_None` | 230 | 599 | 370 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 145 | 123 | inferred_complete_timeline |
| `Action_None` | 147 | 199 | 53 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 594 | 572 | inferred_complete_timeline |
| `Action_None` | 596 | 599 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–466
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 227 | 205 | inferred_complete_timeline |
| `Action_None` | 233 | 244 | 12 | inferred_complete_timeline |
| `Action_None` | 249 | 332 | 84 | inferred_complete_timeline |
| `Action_None` | 341 | 344 | 4 | inferred_complete_timeline |
| `Action_None` | 347 | 466 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 599 | 577 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 585

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 520 | 498 | inferred_complete_timeline |
| `Action_None` | 523 | 528 | 6 | inferred_complete_timeline |
| `Action_None` | 530 | 533 | 4 | inferred_complete_timeline |
| `Action_None` | 535 | 540 | 6 | inferred_complete_timeline |
| `Action_None` | 551 | 564 | 14 | inferred_complete_timeline |
| `Action_None` | 566 | 599 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 173 | 151 | inferred_complete_timeline |
| `Action_None` | 179 | 191 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 172 | 150 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–458
- **Visible Samples:** 459

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 458 | 436 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–300
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 268 | 246 | inferred_complete_timeline |
| `Action_None` | 299 | 300 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 271 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 596

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 244 | 222 | inferred_complete_timeline |
| `Action_None` | 246 | 288 | 43 | inferred_complete_timeline |
| `Action_None` | 292 | 599 | 308 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 34–143 | 79 | 7 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 102–599 | 496 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 124–125 | 2 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 124–241 | 97 | 4 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 129–599 | 380 | 6 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 133–135 | 3 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 134–175 | 40 | 2 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 157–599 | 441 | 2 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 167–599 | 433 | 6 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 190–599 | 406 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 211–236 | 14 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 213–219 | 7 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 234–490 | 184 | 17 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 245–599 | 350 | 3 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 251–262 | 12 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 257–270 | 13 | 2 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 266–422 | 145 | 4 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 268–599 | 326 | 3 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 281–599 | 315 | 4 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 285–599 | 315 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 289–599 | 306 | 2 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 316–317 | 2 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 359–434 | 76 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 367–400 | 6 | 3 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 372–376 | 4 | 2 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 383–507 | 98 | 6 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 430–472 | 22 | 2 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 433–560 | 100 | 6 | Undefined position; Undefined team |
| `47` | `65` | Position_Unknown | Team_Unknown | 464–468 | 5 | 1 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 470–599 | 114 | 4 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 493–494 | 2 | 1 | Undefined position; Undefined team |
| `50` | `71` | Position_Unknown | Team_Unknown | 557–599 | 42 | 2 | Undefined position; Undefined team |
| `51` | `72` | Position_Unknown | Team_Unknown | 557–599 | 43 | 1 | Undefined position; Undefined team |
| `52` | `75` | Position_Unknown | Team_Unknown | 572–599 | 27 | 2 | Undefined position; Undefined team |
| `53` | `77` | Position_Unknown | Team_Unknown | 579–599 | 16 | 2 | Undefined position; Undefined team |
| `54` | `79` | Position_Unknown | Team_Unknown | 581–599 | 18 | 2 | Undefined position; Undefined team |
| `55` | `81` | Position_Unknown | Team_Unknown | 586–587 | 2 | 1 | Undefined position; Undefined team |
| `56` | `82` | Position_Unknown | Team_Unknown | 590–598 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `27` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ 40 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 40 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 80 |
| Missing visible bounding boxes during action | 154 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [23-520] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-528] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-533] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-540] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-564] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-599] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-227] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-244] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-332] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-344] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-466] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-145] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-199] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-39] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-228] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-599] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-268] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-271] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-594] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-554] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-191] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-129] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-328] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-244] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-288] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-458] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-54] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-85] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-292] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-46] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-72] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-197] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-455] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-213] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-255] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-353] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-467] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-51] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-70] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-86] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-127] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-550] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-222] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-185] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-206] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-433] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-449] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-599] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-169] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-590] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [221-590] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-355] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-222] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-219] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-246] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-257] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-293] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-300] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-317] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-407] for track '31' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-412] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-434] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-454] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-458] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-463] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-483] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-490] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-258] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-416] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-599] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-262] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-267] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-282] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-290] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-422] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-389] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-533] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-530] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-538] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-548] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-599] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-550] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-599] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-434] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-400] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-393] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-410] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-463] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-475] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-492] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-507] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-472] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-494] for track '46' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-505] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-526] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-533] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-542] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-560] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-468] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-531] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-542] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-550] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-494] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-571] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-599] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-574] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-599] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-590] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-582] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-587] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-598] for track '56' has 2 frames without a visible bounding box.
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

</details>