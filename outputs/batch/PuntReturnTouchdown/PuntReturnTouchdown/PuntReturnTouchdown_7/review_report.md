# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_7`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 689
- **Player Tracks:** 58
- **Ball Tracks:** 0
- **Action Segments:** 130
- **Validation Warnings:** 182
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 114
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `15` | `15` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `15` | `15` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `37` | `27` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `37` | `27` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `37` | `27` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `1` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | `12` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `14` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `15` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | `17` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `18` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `19` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `3` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `5` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `9` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `14` | `14` | 15 | START | 15 | 68 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `15` | `15` | 42 | END | 42 | 42 |
| ✅ EXACT | `Action_PuntBall` | Punter | `15` | `15` | 69 | START | 69 | 129 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `37` | `27` | 186 | START | 186 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `37` | `27` | 198 | START | 198 | 671 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `37` | `27` | 672 | START | 672 | 677 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–602
- **Visible Samples:** 597

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 25 | 11 | inferred_complete_timeline |
| `Action_None` | 31 | 527 | 497 | inferred_complete_timeline |
| `Action_None` | 529 | 602 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 82 | 68 | inferred_complete_timeline |
| `Action_None` | 87 | 90 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 689 | 675 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 206 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–306
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_LongSnap` | 15 | 68 | 54 | inferred_complete_timeline |
| `Action_None` | 69 | 306 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 156 | 142 | inferred_complete_timeline |
| `Action_None` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_None` | 163 | 262 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–345
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 345 | 331 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_None` | 43 | 68 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 69 | 129 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–668
- **Visible Samples:** 669

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 668 | 654 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 147 | 133 | inferred_complete_timeline |
| `Action_None` | 150 | 160 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 156 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–436
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 436 | 422 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–338
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 54 | 40 | inferred_complete_timeline |
| `Action_None` | 56 | 338 | 283 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 214 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 133 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 88 | 74 | inferred_complete_timeline |
| `Action_None` | 90 | 108 | 19 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 296 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–552
- **Visible Samples:** 543

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 401 | 387 | inferred_complete_timeline |
| `Action_None` | 404 | 430 | 27 | inferred_complete_timeline |
| `Action_None` | 434 | 436 | 3 | inferred_complete_timeline |
| `Action_None` | 442 | 552 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 173 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–432
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 127 | 113 | inferred_complete_timeline |
| `Action_None` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_None` | 137 | 184 | 48 | inferred_complete_timeline |
| `Action_None` | 188 | 190 | 3 | inferred_complete_timeline |
| `Action_None` | 195 | 198 | 4 | inferred_complete_timeline |
| `Action_None` | 201 | 237 | 37 | inferred_complete_timeline |
| `Action_None` | 239 | 432 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 260 | 246 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 6–52 | 43 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 62–139 | 78 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 123–161 | 12 | 3 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 145–146 | 2 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 149–152 | 4 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 160–162 | 3 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 166–227 | 58 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 171–689 | 517 | 6 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 214–339 | 126 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 231–667 | 437 | 1 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 295–643 | 349 | 1 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 305–458 | 154 | 1 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 319–336 | 18 | 1 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 332–426 | 95 | 1 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 355–466 | 112 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 357–586 | 225 | 3 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 357–452 | 85 | 2 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 359–645 | 283 | 3 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 360–558 | 197 | 2 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 373–377 | 5 | 1 | Undefined position; Undefined team |
| `40` | `60` | Position_Unknown | Team_Unknown | 376–377 | 2 | 1 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 379–384 | 6 | 1 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 382–383 | 2 | 1 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 390–512 | 121 | 3 | Undefined position; Undefined team |
| `44` | `66` | Position_Unknown | Team_Unknown | 390–663 | 274 | 1 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 393–689 | 297 | 1 | Undefined position; Undefined team |
| `46` | `68` | Position_Unknown | Team_Unknown | 403–673 | 271 | 1 | Undefined position; Undefined team |
| `47` | `69` | Position_Unknown | Team_Unknown | 404–409 | 4 | 2 | Undefined position; Undefined team |
| `48` | `70` | Position_Unknown | Team_Unknown | 406–408 | 3 | 1 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 406–658 | 246 | 4 | Undefined position; Undefined team |
| `50` | `75` | Position_Unknown | Team_Unknown | 445–450 | 6 | 1 | Undefined position; Undefined team |
| `51` | `77` | Position_Unknown | Team_Unknown | 453–689 | 237 | 1 | Undefined position; Undefined team |
| `52` | `79` | Position_Unknown | Team_Unknown | 457–522 | 45 | 5 | Undefined position; Undefined team |
| `53` | `80` | Position_Unknown | Team_Unknown | 479–505 | 4 | 2 | Undefined position; Undefined team |
| `54` | `83` | Position_Unknown | Team_Unknown | 563–572 | 9 | 2 | Undefined position; Undefined team |
| `55` | `85` | Position_Unknown | Team_Unknown | 569–570 | 2 | 1 | Undefined position; Undefined team |
| `56` | `86` | Position_Unknown | Team_Unknown | 576–585 | 10 | 1 | Undefined position; Undefined team |
| `57` | `88` | Position_Unknown | Team_Unknown | 648–676 | 29 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `37` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 103 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [15-133] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-147] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-436] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-262] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-173] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-345] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-260] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-54] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-338] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-214] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-668] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-127] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-184] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-237] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-432] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-156] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-82] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-401] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-430] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-436] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-552] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-306] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [69-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-296] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-689] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-527] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-602] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-206] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-10] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-52] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-143] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-227] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-179] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-184] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-671] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-339] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-667] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-643] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-458] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-336] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-426] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-466] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-370] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-477] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-586] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-381] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-452] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-601] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-640] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-645] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-526] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-558] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-377] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-384] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-462] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-475] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-512] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-663] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-673] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-408] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-420] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-633] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-653] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [655-658] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-450] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-689] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-458] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-469] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-487] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-508] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-522] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-480] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-505] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-566] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-572] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-570] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-585] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-676] for track '57' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>