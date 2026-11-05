# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_38

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_38`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 75
- **Ball Tracks:** 0
- **Action Segments:** 230
- **Validation Warnings:** 309
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 216
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_CatchPunt` | Punt_Returner | defense | `2` | `2` |
| ✅ EXACT | `Action_BallCarry` | Punt_Returner | defense | `2` | `2` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `87` | `70` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `1` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `10` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `15` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `5` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `6` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `7` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `9` | `Group` | 0 | START | 0 | 26 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `10` | `10` | 27 | START | 27 | 86 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `6` | `6` | 59 | END | 59 | 59 |
| ✅ EXACT | `Action_PuntBall` | Punter | `6` | `6` | 87 | START | 87 | 98 |
| ✅ EXACT | `Action_CatchPunt` | Punt_Returner | `2` | `2` | 209 | START | 209 | 215 |
| ✅ EXACT | `Action_BallCarry` | Punt_Returner | `2` | `2` | 226 | START | 226 | 287 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `87` | `70` | 588 | START | 588 | 595 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–394
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 93 | 67 | inferred_complete_timeline |
| `Action_None` | 96 | 110 | 15 | inferred_complete_timeline |
| `Action_None` | 121 | 281 | 161 | inferred_complete_timeline |
| `Action_None` | 284 | 363 | 80 | inferred_complete_timeline |
| `Action_None` | 368 | 394 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 80 | 54 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 88 | 190 | 103 | inferred_complete_timeline |
| `Action_None` | 226 | 242 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_LongSnap` | 27 | 86 | 60 | inferred_complete_timeline |
| `Action_None` | 87 | 186 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 240 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 101 | 75 | inferred_complete_timeline |
| `Action_None` | 103 | 105 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_SnapReceive` | 59 | 59 | 1 | inferred_complete_timeline |
| `Action_None` | 60 | 86 | 27 | inferred_complete_timeline |
| `Action_PuntBall` | 87 | 98 | 12 | inferred_complete_timeline |
| `Action_None` | 99 | 103 | 5 | inferred_complete_timeline |
| `Action_None` | 105 | 126 | 22 | inferred_complete_timeline |
| `Action_None` | 129 | 182 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 105 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 94 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 54 | 28 | inferred_complete_timeline |
| `Action_None` | 99 | 268 | 170 | inferred_complete_timeline |
| `Action_None` | 276 | 364 | 89 | inferred_complete_timeline |
| `Action_None` | 366 | 374 | 9 | inferred_complete_timeline |
| `Action_None` | 378 | 385 | 8 | inferred_complete_timeline |
| `Action_None` | 388 | 390 | 3 | inferred_complete_timeline |
| `Action_None` | 425 | 545 | 121 | inferred_complete_timeline |
| `Action_None` | 552 | 589 | 38 | inferred_complete_timeline |
| `Action_None` | 596 | 599 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 71 | 45 | inferred_complete_timeline |
| `Action_None` | 73 | 91 | 19 | inferred_complete_timeline |
| `Action_None` | 95 | 131 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 48 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 82 | 56 | inferred_complete_timeline |
| `Action_None` | 85 | 150 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 46 | 20 | inferred_complete_timeline |
| `Action_None` | 56 | 159 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_None` | 36 | 60 | 25 | inferred_complete_timeline |
| `Action_None` | 66 | 78 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 112 | 86 | inferred_complete_timeline |
| `Action_None` | 115 | 117 | 3 | inferred_complete_timeline |
| `Action_None` | 138 | 242 | 105 | inferred_complete_timeline |
| `Action_None` | 244 | 299 | 56 | inferred_complete_timeline |
| `Action_None` | 303 | 370 | 68 | inferred_complete_timeline |
| `Action_None` | 372 | 419 | 48 | inferred_complete_timeline |
| `Action_None` | 422 | 424 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Returner — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_CatchPunt` | 209 | 215 | 7 | inferred_complete_timeline |
| `Action_None` | 216 | 225 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 226 | 287 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 55 | 29 | inferred_complete_timeline |
| `Action_None` | 67 | 70 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–171 | 172 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 5–38 | 34 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 47–183 | 137 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 70–362 | 289 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 74–292 | 111 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 86–159 | 74 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 86–166 | 78 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 118–192 | 75 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 125–157 | 33 | 1 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 128–157 | 30 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 137–514 | 368 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 137–142 | 6 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 146–210 | 65 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 171–173 | 3 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 189–214 | 26 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 195–414 | 214 | 3 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 196–208 | 8 | 2 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 210–228 | 19 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 213–235 | 13 | 2 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 215–335 | 110 | 3 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 222–599 | 354 | 7 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 223–540 | 287 | 7 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 224–552 | 310 | 6 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 226–599 | 319 | 10 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 229–288 | 58 | 2 | Undefined position; Undefined team |
| `42` | `48` | Position_Unknown | Team_Unknown | 233–599 | 342 | 6 | Undefined position; Undefined team |
| `43` | `49` | Position_Unknown | Team_Unknown | 236–356 | 121 | 1 | Undefined position; Undefined team |
| `44` | `50` | Position_Unknown | Team_Unknown | 243–348 | 106 | 1 | Undefined position; Undefined team |
| `45` | `52` | Position_Unknown | Team_Unknown | 249–516 | 238 | 4 | Undefined position; Undefined team |
| `46` | `53` | Position_Unknown | Team_Unknown | 250–282 | 16 | 5 | Undefined position; Undefined team |
| `47` | `54` | Position_Unknown | Team_Unknown | 253–340 | 87 | 2 | Undefined position; Undefined team |
| `48` | `55` | Position_Unknown | Team_Unknown | 271–596 | 300 | 11 | Undefined position; Undefined team |
| `49` | `56` | Position_Unknown | Team_Unknown | 292–304 | 13 | 1 | Undefined position; Undefined team |
| `50` | `58` | Position_Unknown | Team_Unknown | 296–578 | 253 | 8 | Undefined position; Undefined team |
| `51` | `59` | Position_Unknown | Team_Unknown | 298–326 | 8 | 2 | Undefined position; Undefined team |
| `52` | `60` | Position_Unknown | Team_Unknown | 311–599 | 263 | 4 | Undefined position; Undefined team |
| `53` | `61` | Position_Unknown | Team_Unknown | 315–326 | 9 | 2 | Undefined position; Undefined team |
| `54` | `62` | Position_Unknown | Team_Unknown | 315–478 | 163 | 2 | Undefined position; Undefined team |
| `55` | `65` | Position_Unknown | Team_Unknown | 345–599 | 200 | 7 | Undefined position; Undefined team |
| `56` | `66` | Position_Unknown | Team_Unknown | 370–590 | 206 | 3 | Undefined position; Undefined team |
| `57` | `67` | Position_Unknown | Team_Unknown | 372–599 | 211 | 4 | Undefined position; Undefined team |
| `58` | `68` | Position_Unknown | Team_Unknown | 385–517 | 132 | 2 | Undefined position; Undefined team |
| `59` | `70` | Position_Unknown | Team_Unknown | 397–456 | 56 | 2 | Undefined position; Undefined team |
| `60` | `73` | Position_Unknown | Team_Unknown | 410–430 | 21 | 1 | Undefined position; Undefined team |
| `61` | `75` | Position_Unknown | Team_Unknown | 417–599 | 160 | 2 | Undefined position; Undefined team |
| `62` | `76` | Position_Unknown | Team_Unknown | 419–599 | 113 | 6 | Undefined position; Undefined team |
| `63` | `78` | Position_Unknown | Team_Unknown | 480–599 | 111 | 2 | Undefined position; Undefined team |
| `64` | `79` | Position_Unknown | Team_Unknown | 517–599 | 83 | 1 | Undefined position; Undefined team |
| `65` | `80` | Position_Unknown | Team_Unknown | 517–518 | 2 | 1 | Undefined position; Undefined team |
| `66` | `81` | Position_Unknown | Team_Unknown | 519–543 | 25 | 1 | Undefined position; Undefined team |
| `67` | `82` | Position_Unknown | Team_Unknown | 520–599 | 80 | 1 | Undefined position; Undefined team |
| `68` | `84` | Position_Unknown | Team_Unknown | 526–527 | 2 | 1 | Undefined position; Undefined team |
| `69` | `86` | Position_Unknown | Team_Unknown | 529–599 | 69 | 2 | Undefined position; Undefined team |
| `70` | `87` | Position_Unknown | Team_Unknown | 562–599 | 38 | 3 | Undefined position; Undefined team |
| `71` | `88` | Position_Unknown | Team_Unknown | 578–599 | 22 | 1 | Undefined position; Undefined team |
| `72` | `90` | Position_Unknown | Team_Unknown | 597–599 | 3 | 1 | Undefined position; Undefined team |
| `73` | `91` | Position_Unknown | Team_Unknown | 597–599 | 3 | 1 | Undefined position; Undefined team |
| `74` | `92` | Position_Unknown | Team_Unknown | 597–598 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punt_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 58 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 58 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 116 |
| Missing visible bounding boxes during action | 190 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [27-46] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-105] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [226-287] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-55] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-70] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-112] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-242] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-299] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-370] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-419] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-424] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-101] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-126] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-182] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-80] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-190] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-242] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-186] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-54] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-268] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-364] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-374] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-385] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-390] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-545] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-589] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-48] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-91] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-240] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-281] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-363] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-394] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 27, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [27-27] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-60] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-78] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-38] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-352] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-362] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-178] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-245] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-292] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-159] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-94] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-166] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-192] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-157] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-157] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-502] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-514] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-214] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-242] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-291] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-414] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-228] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-222] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-270] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-283] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-335] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-273] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-357] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-392] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-468] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-262] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-449] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-460] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-498] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-518] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-522] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-540] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-312] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-390] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-393] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-446] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-534] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-552] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-348] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-460] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-483] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-510] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-517] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-527] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-531] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-543] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-551] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-237] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-288] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-259] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-279] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-356] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-367] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-534] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-356] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-348] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-325] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-349] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-485] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-516] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-262] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-269] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-340] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-276] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-322] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-347] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-385] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-432] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-435] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-439] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-522] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-529] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-596] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-304] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-341] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-366] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-446] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-481] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-522] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-563] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-578] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-330] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-362] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-388] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-332] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-478] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-368] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-395] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-498] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-574] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-583] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-377] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-383] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-590] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-375] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-388] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-578] for track '57' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-599] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-408] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-517] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-438] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-456] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-430] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-498] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-422] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-426] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-445] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-453] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-485] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-599] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-538] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-518] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-543] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-599] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-571] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-598] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>