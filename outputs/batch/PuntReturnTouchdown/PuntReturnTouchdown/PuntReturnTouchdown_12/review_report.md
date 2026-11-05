# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_12

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_12`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 64
- **Ball Tracks:** 0
- **Action Segments:** 181
- **Validation Warnings:** 241
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 167
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Position_Unknown | Team_Unknown | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `26` | `24` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `26` | `24` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `26` | `24` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `0` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `1` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `15` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `2` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `3` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `4` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `7` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `9` | `Group` | 0 | START | 0 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Position_Unknown | `16` | `16` | 131 | START | 131 | 165 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `2` | `2` | 151 | END | 151 | 151 |
| ✅ EXACT | `Action_PuntBall` | Punter | `2` | `2` | 183 | START | 183 | 193 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `26` | `24` | 288 | START | 288 | 295 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `26` | `24` | 342 | START | 342 | 350 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `26` | `24` | 650 | START | 650 | 657 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–348
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 172 | 42 | inferred_complete_timeline |
| `Action_None` | 174 | 308 | 135 | inferred_complete_timeline |
| `Action_None` | 311 | 339 | 29 | inferred_complete_timeline |
| `Action_None` | 345 | 348 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–532
- **Visible Samples:** 524

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 228 | 98 | inferred_complete_timeline |
| `Action_None` | 230 | 376 | 147 | inferred_complete_timeline |
| `Action_None` | 378 | 443 | 66 | inferred_complete_timeline |
| `Action_None` | 449 | 459 | 11 | inferred_complete_timeline |
| `Action_None` | 462 | 532 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–640
- **Visible Samples:** 604

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 551 | 421 | inferred_complete_timeline |
| `Action_None` | 555 | 581 | 27 | inferred_complete_timeline |
| `Action_None` | 583 | 585 | 3 | inferred_complete_timeline |
| `Action_None` | 619 | 640 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–477
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 191 | 61 | inferred_complete_timeline |
| `Action_None` | 194 | 200 | 7 | inferred_complete_timeline |
| `Action_None` | 202 | 462 | 261 | inferred_complete_timeline |
| `Action_None` | 474 | 477 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 657

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 557 | 427 | inferred_complete_timeline |
| `Action_None` | 561 | 659 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_SnapReceive` | 151 | 151 | 1 | inferred_complete_timeline |
| `Action_None` | 152 | 182 | 31 | inferred_complete_timeline |
| `Action_PuntBall` | 183 | 193 | 11 | inferred_complete_timeline |
| `Action_None` | 194 | 200 | 7 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–658
- **Visible Samples:** 639

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 235 | 105 | inferred_complete_timeline |
| `Action_None` | 238 | 376 | 139 | inferred_complete_timeline |
| `Action_None` | 379 | 390 | 12 | inferred_complete_timeline |
| `Action_None` | 395 | 397 | 3 | inferred_complete_timeline |
| `Action_None` | 401 | 403 | 3 | inferred_complete_timeline |
| `Action_None` | 406 | 413 | 8 | inferred_complete_timeline |
| `Action_None` | 416 | 420 | 5 | inferred_complete_timeline |
| `Action_None` | 424 | 574 | 151 | inferred_complete_timeline |
| `Action_None` | 577 | 658 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 649

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 343 | 213 | inferred_complete_timeline |
| `Action_None` | 350 | 420 | 71 | inferred_complete_timeline |
| `Action_None` | 423 | 634 | 212 | inferred_complete_timeline |
| `Action_None` | 638 | 659 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–635
- **Visible Samples:** 611

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 221 | 91 | inferred_complete_timeline |
| `Action_None` | 235 | 416 | 182 | inferred_complete_timeline |
| `Action_None` | 420 | 456 | 37 | inferred_complete_timeline |
| `Action_None` | 459 | 488 | 30 | inferred_complete_timeline |
| `Action_None` | 490 | 545 | 56 | inferred_complete_timeline |
| `Action_None` | 547 | 574 | 28 | inferred_complete_timeline |
| `Action_None` | 576 | 625 | 50 | inferred_complete_timeline |
| `Action_None` | 627 | 630 | 4 | inferred_complete_timeline |
| `Action_None` | 634 | 635 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–627
- **Visible Samples:** 624

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 473 | 343 | inferred_complete_timeline |
| `Action_None` | 477 | 518 | 42 | inferred_complete_timeline |
| `Action_None` | 520 | 627 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 657

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 408 | 278 | inferred_complete_timeline |
| `Action_None` | 412 | 659 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–653
- **Visible Samples:** 642

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 178 | 48 | inferred_complete_timeline |
| `Action_None` | 183 | 466 | 284 | inferred_complete_timeline |
| `Action_None` | 474 | 624 | 151 | inferred_complete_timeline |
| `Action_None` | 626 | 653 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 215 | 85 | inferred_complete_timeline |
| `Action_None` | 217 | 223 | 7 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–626
- **Visible Samples:** 611

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 189 | 59 | inferred_complete_timeline |
| `Action_None` | 203 | 401 | 199 | inferred_complete_timeline |
| `Action_None` | 404 | 612 | 209 | inferred_complete_timeline |
| `Action_None` | 614 | 626 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 196 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 660

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 659 | 529 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 5–196 | 189 | 4 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 158–189 | 32 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 190–382 | 189 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 202–443 | 234 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 210–555 | 339 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 213–452 | 238 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 221–579 | 355 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 227–347 | 121 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 228–659 | 427 | 9 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 231–238 | 7 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 235–238 | 4 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 237–251 | 10 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 244–315 | 70 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 248–281 | 17 | 4 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 250–302 | 53 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 270–278 | 7 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 318–330 | 12 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 325–326 | 2 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 335–659 | 324 | 2 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 335–523 | 186 | 2 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 351–458 | 101 | 4 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 384–654 | 271 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 397–398 | 2 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 418–659 | 241 | 2 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 452–454 | 3 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 465–659 | 193 | 2 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 487–659 | 173 | 1 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 506–517 | 11 | 2 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 506–516 | 11 | 1 | Undefined position; Undefined team |
| `45` | `57` | Position_Unknown | Team_Unknown | 514–550 | 21 | 4 | Undefined position; Undefined team |
| `46` | `59` | Position_Unknown | Team_Unknown | 533–659 | 110 | 2 | Undefined position; Undefined team |
| `47` | `60` | Position_Unknown | Team_Unknown | 536–543 | 8 | 1 | Undefined position; Undefined team |
| `48` | `61` | Position_Unknown | Team_Unknown | 539–540 | 2 | 1 | Undefined position; Undefined team |
| `49` | `63` | Position_Unknown | Team_Unknown | 556–564 | 9 | 1 | Undefined position; Undefined team |
| `50` | `64` | Position_Unknown | Team_Unknown | 565–623 | 33 | 2 | Undefined position; Undefined team |
| `51` | `65` | Position_Unknown | Team_Unknown | 581–659 | 64 | 4 | Undefined position; Undefined team |
| `52` | `68` | Position_Unknown | Team_Unknown | 599–659 | 59 | 2 | Undefined position; Undefined team |
| `53` | `69` | Position_Unknown | Team_Unknown | 601–627 | 14 | 4 | Undefined position; Undefined team |
| `54` | `70` | Position_Unknown | Team_Unknown | 603–617 | 9 | 3 | Undefined position; Undefined team |
| `55` | `71` | Position_Unknown | Team_Unknown | 603–659 | 56 | 2 | Undefined position; Undefined team |
| `56` | `72` | Position_Unknown | Team_Unknown | 616–658 | 43 | 1 | Undefined position; Undefined team |
| `57` | `75` | Position_Unknown | Team_Unknown | 634–659 | 26 | 1 | Undefined position; Undefined team |
| `58` | `77` | Position_Unknown | Team_Unknown | 638–649 | 10 | 2 | Undefined position; Undefined team |
| `59` | `79` | Position_Unknown | Team_Unknown | 648–657 | 10 | 1 | Undefined position; Undefined team |
| `60` | `81` | Position_Unknown | Team_Unknown | 652–659 | 8 | 1 | Undefined position; Undefined team |
| `61` | `82` | Position_Unknown | Team_Unknown | 656–659 | 4 | 1 | Undefined position; Undefined team |
| `62` | `83` | Position_Unknown | Team_Unknown | 657–659 | 3 | 1 | Undefined position; Undefined team |
| `63` | `85` | Position_Unknown | Team_Unknown | 659–659 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `26` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Guard` position mapped to `offense` team
- ⚠️ 48 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 48 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 96 |
| Missing visible bounding boxes during action | 142 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [131-551] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-581] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-585] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-640] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-343] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-420] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-634] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-200] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-462] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-477] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-228] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-376] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-443] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-459] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-532] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-473] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-518] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-627] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-215] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-223] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-308] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-339] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-408] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-659] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-557] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-189] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-401] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-612] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-626] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-466] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-624] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-653] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-221] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-416] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-456] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-488] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-545] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-574] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-625] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-630] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-635] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-235] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-376] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-390] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-397] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-403] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-413] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-420] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-574] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-658] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [131-165] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-196] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-189] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-302] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-308] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-321] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-382] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-304] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-312] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-443] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-555] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-221] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-452] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-236] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-452] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-579] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-347] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-301] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [342-350] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [353-577] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-301] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-315] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-256] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-302] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-327] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-659] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-458] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-523] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-380] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-432] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-458] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-654] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-559] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-454] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-537] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-513] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-517] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-516] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-518] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-528] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-545] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-550] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-591] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-659] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-543] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-564] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-570] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-623] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-582] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-593] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-648] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-615] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-603] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-613] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-624] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-627] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-605] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-614] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-617] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-606] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-659] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-658] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-643] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-649] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-657] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-659] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>