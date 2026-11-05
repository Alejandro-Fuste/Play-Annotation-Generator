# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_11

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_11`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 50
- **Ball Tracks:** 0
- **Action Segments:** 188
- **Validation Warnings:** 210
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 171
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `28` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `28` | `23` |
| ✅ EXACT | `Action_CrossGoalLine` | Right_Jammer3 | defense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `12` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `14` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `17` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `18` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `19` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `20` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `3` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `5` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `8` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `9` | `Group` | 0 | START | 0 | 29 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `9` | `9` | 30 | START | 30 | 82 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `12` | `12` | 55 | END | 55 | 55 |
| ✅ EXACT | `Action_PuntBall` | Punter | `12` | `12` | 83 | START | 83 | 93 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `28` | `23` | 187 | START | 187 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `28` | `23` | 197 | START | 197 | 213 |
| ✅ EXACT | `Action_CrossGoalLine` | Right_Jammer3 | `16` | `16` | 555 | START | 555 | 560 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 399 | 370 | inferred_complete_timeline |
| `Action_None` | 401 | 569 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 180 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 162 | 133 | inferred_complete_timeline |
| `Action_None` | 167 | 193 | 27 | inferred_complete_timeline |
| `Action_None` | 205 | 273 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_LongSnap` | 30 | 82 | 53 | inferred_complete_timeline |
| `Action_None` | 83 | 162 | 80 | inferred_complete_timeline |
| `Action_None` | 164 | 197 | 34 | inferred_complete_timeline |
| `Action_None` | 199 | 201 | 3 | inferred_complete_timeline |
| `Action_None` | 212 | 220 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 549 | 520 | inferred_complete_timeline |
| `Action_None` | 553 | 569 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–382
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 350 | 321 | inferred_complete_timeline |
| `Action_None` | 356 | 360 | 5 | inferred_complete_timeline |
| `Action_None` | 365 | 366 | 2 | inferred_complete_timeline |
| `Action_None` | 369 | 382 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 371 | 342 | inferred_complete_timeline |
| `Action_None` | 382 | 569 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_SnapReceive` | 55 | 55 | 1 | inferred_complete_timeline |
| `Action_None` | 56 | 82 | 27 | inferred_complete_timeline |
| `Action_PuntBall` | 83 | 93 | 11 | inferred_complete_timeline |
| `Action_None` | 94 | 217 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 49 | 20 | inferred_complete_timeline |
| `Action_None` | 53 | 190 | 138 | inferred_complete_timeline |
| `Action_None` | 194 | 226 | 33 | inferred_complete_timeline |
| `Action_None` | 228 | 569 | 342 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 213 | 184 | inferred_complete_timeline |
| `Action_None` | 219 | 221 | 3 | inferred_complete_timeline |
| `Action_None` | 229 | 569 | 341 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 242 | 213 | inferred_complete_timeline |
| `Action_None` | 245 | 510 | 266 | inferred_complete_timeline |
| `Action_None` | 516 | 569 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 552

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 200 | 171 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 215 | 4 | inferred_complete_timeline |
| `Action_None` | 217 | 244 | 28 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 259 | 5 | inferred_complete_timeline |
| `Action_None` | 261 | 530 | 270 | inferred_complete_timeline |
| `Action_None` | 532 | 569 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–365
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 189 | 160 | inferred_complete_timeline |
| `Action_None` | 191 | 202 | 12 | inferred_complete_timeline |
| `Action_None` | 204 | 207 | 4 | inferred_complete_timeline |
| `Action_None` | 210 | 215 | 6 | inferred_complete_timeline |
| `Action_None` | 217 | 345 | 129 | inferred_complete_timeline |
| `Action_None` | 347 | 360 | 14 | inferred_complete_timeline |
| `Action_None` | 362 | 365 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 83 | 54 | inferred_complete_timeline |
| `Action_None` | 85 | 143 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 557

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 186 | 157 | inferred_complete_timeline |
| `Action_None` | 189 | 451 | 263 | inferred_complete_timeline |
| `Action_None` | 463 | 569 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 177 | 148 | inferred_complete_timeline |
| `Action_None` | 180 | 223 | 44 | inferred_complete_timeline |
| `Action_None` | 225 | 569 | 345 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 164 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 569 | 540 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 569 | 540 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 166 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 554 | 382 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 555 | 560 | 6 | inferred_complete_timeline |
| `Action_None` | 561 | 569 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 547

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 186 | 157 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 211 | 547 | 337 | inferred_complete_timeline |
| `Action_None` | 549 | 569 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–122 | 121 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 116–171 | 47 | 4 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 151–564 | 394 | 7 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 190–569 | 373 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 193–569 | 357 | 7 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 233–569 | 327 | 6 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 239–569 | 309 | 6 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 269–272 | 4 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 276–569 | 74 | 16 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 278–569 | 283 | 4 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 295–569 | 275 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 299–300 | 2 | 1 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 332–333 | 2 | 1 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 354–356 | 3 | 1 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 359–560 | 201 | 2 | Undefined position; Undefined team |
| `37` | `59` | Position_Unknown | Team_Unknown | 368–569 | 202 | 1 | Undefined position; Undefined team |
| `38` | `62` | Position_Unknown | Team_Unknown | 394–401 | 6 | 2 | Undefined position; Undefined team |
| `39` | `67` | Position_Unknown | Team_Unknown | 450–463 | 14 | 1 | Undefined position; Undefined team |
| `40` | `69` | Position_Unknown | Team_Unknown | 462–569 | 37 | 6 | Undefined position; Undefined team |
| `41` | `73` | Position_Unknown | Team_Unknown | 485–569 | 52 | 7 | Undefined position; Undefined team |
| `42` | `75` | Position_Unknown | Team_Unknown | 494–544 | 37 | 6 | Undefined position; Undefined team |
| `43` | `77` | Position_Unknown | Team_Unknown | 503–505 | 3 | 1 | Undefined position; Undefined team |
| `44` | `78` | Position_Unknown | Team_Unknown | 503–560 | 17 | 4 | Undefined position; Undefined team |
| `45` | `79` | Position_Unknown | Team_Unknown | 511–514 | 4 | 1 | Undefined position; Undefined team |
| `46` | `82` | Position_Unknown | Team_Unknown | 531–532 | 2 | 1 | Undefined position; Undefined team |
| `47` | `83` | Position_Unknown | Team_Unknown | 532–569 | 27 | 3 | Undefined position; Undefined team |
| `48` | `85` | Position_Unknown | Team_Unknown | 556–557 | 2 | 1 | Undefined position; Undefined team |
| `49` | `88` | Position_Unknown | Team_Unknown | 564–565 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `28` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Jammer4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Jammer3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Guard` position mapped to `offense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 149 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [30-164] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-345] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-360] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-365] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-83] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-213] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-569] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-244] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-259] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-530] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-180] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-186] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-451] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-569] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-186] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-547] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-242] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-510] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [30-82] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-197] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-220] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-569] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-177] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-223] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-217] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-399] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-162] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-193] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-273] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-569] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-166] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-569] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-549] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-569] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-371] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-350] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-360] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-382] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-190] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-226] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-569] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-115] for track '21' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-156] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-171] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [197-213] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [215-511] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [524-525] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [530-535] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [539-564] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-216] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-209] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-279] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-287] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-331] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-569] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-335] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-345] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-535] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-540] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-549] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-569] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-358] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-516] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-524] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-556] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-561] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-374] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-408] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-427] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-466] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-478] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-492] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-498] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-504] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-537] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-542] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-305] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-388] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-569] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-356] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-557] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-560] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-569] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-396] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-401] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-463] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-469] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-489] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-497] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-507] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-548] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-490] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-523] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-540] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-564] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-569] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-507] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-527] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-534] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-538] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-541] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-544] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-505] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-512] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-519] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-526] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-560] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-514] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-532] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-542] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-545] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-569] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-557] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '49' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>