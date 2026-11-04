# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_15

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_15`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 689
- **Player Tracks:** 68
- **Ball Tracks:** 0
- **Action Segments:** 239
- **Validation Warnings:** 319
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 219
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_KickBall` | Kicker | offense | `9` | `9` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `43` | `36` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `43` | `36` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `43` | `36` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `0` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `12` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `13` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `14` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `15` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `6` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `9` | `Group` | 0 | START | 0 | 123 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `9` | `9` | 124 | START | 124 | 167 |
| ❌ MISSING SEGMENT | `Action_KickBall` | Kicker | `9` | `9` | 187 | START | N/A | N/A |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `43` | `36` | 307 | START | 307 | 312 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `43` | `36` | 331 | START | 331 | 388 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `43` | `36` | 678 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_KickApproach` | 124 | 167 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 160 | 37 | inferred_complete_timeline |
| `Action_None` | 167 | 171 | 5 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 172 | 49 | inferred_complete_timeline |
| `Action_None` | 175 | 196 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 123 | 105 | inferred_complete_timeline |
| `Action_None` | 124 | 164 | 41 | inferred_complete_timeline |
| `Action_None` | 169 | 170 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 16 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 20 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 42 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 60 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 70 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 111 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 124 | 156 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 123 | 72 | inferred_complete_timeline |
| `Action_None` | 124 | 162 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 689 | 566 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 216 | 93 | inferred_complete_timeline |
| `Action_None` | 222 | 273 | 52 | inferred_complete_timeline |
| `Action_None` | 280 | 348 | 69 | inferred_complete_timeline |
| `Action_None` | 354 | 364 | 11 | inferred_complete_timeline |
| `Action_None` | 367 | 399 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–320
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 215 | 92 | inferred_complete_timeline |
| `Action_None` | 217 | 282 | 66 | inferred_complete_timeline |
| `Action_None` | 284 | 294 | 11 | inferred_complete_timeline |
| `Action_None` | 296 | 310 | 15 | inferred_complete_timeline |
| `Action_None` | 319 | 320 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 679

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 289 | 166 | inferred_complete_timeline |
| `Action_None` | 296 | 316 | 21 | inferred_complete_timeline |
| `Action_None` | 318 | 624 | 307 | inferred_complete_timeline |
| `Action_None` | 626 | 636 | 11 | inferred_complete_timeline |
| `Action_None` | 639 | 673 | 35 | inferred_complete_timeline |
| `Action_None` | 675 | 689 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 667

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 406 | 283 | inferred_complete_timeline |
| `Action_None` | 410 | 412 | 3 | inferred_complete_timeline |
| `Action_None` | 415 | 424 | 10 | inferred_complete_timeline |
| `Action_None` | 429 | 434 | 6 | inferred_complete_timeline |
| `Action_None` | 439 | 456 | 18 | inferred_complete_timeline |
| `Action_None` | 458 | 460 | 3 | inferred_complete_timeline |
| `Action_None` | 463 | 498 | 36 | inferred_complete_timeline |
| `Action_None` | 501 | 506 | 6 | inferred_complete_timeline |
| `Action_None` | 510 | 543 | 34 | inferred_complete_timeline |
| `Action_None` | 546 | 689 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–678
- **Visible Samples:** 633

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 372 | 249 | inferred_complete_timeline |
| `Action_None` | 379 | 567 | 189 | inferred_complete_timeline |
| `Action_None` | 572 | 574 | 3 | inferred_complete_timeline |
| `Action_None` | 579 | 580 | 2 | inferred_complete_timeline |
| `Action_None` | 582 | 605 | 24 | inferred_complete_timeline |
| `Action_None` | 608 | 611 | 4 | inferred_complete_timeline |
| `Action_None` | 618 | 619 | 2 | inferred_complete_timeline |
| `Action_None` | 621 | 630 | 10 | inferred_complete_timeline |
| `Action_None` | 652 | 658 | 7 | inferred_complete_timeline |
| `Action_None` | 660 | 678 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 684

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 660 | 537 | inferred_complete_timeline |
| `Action_None` | 667 | 689 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 224 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 675

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 372 | 249 | inferred_complete_timeline |
| `Action_None` | 380 | 398 | 19 | inferred_complete_timeline |
| `Action_None` | 406 | 640 | 235 | inferred_complete_timeline |
| `Action_None` | 642 | 689 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–656
- **Visible Samples:** 653

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 375 | 252 | inferred_complete_timeline |
| `Action_None` | 380 | 656 | 277 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 23–24 | 2 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 86–397 | 176 | 14 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 87–96 | 10 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 108–111 | 4 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 182–193 | 8 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 186–187 | 2 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 190–192 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 200–201 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 207–554 | 339 | 6 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 210–689 | 458 | 7 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 210–271 | 34 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 214–689 | 474 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 215–395 | 179 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 223–631 | 408 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 229–650 | 383 | 18 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 231–247 | 17 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 231–232 | 2 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 233–240 | 6 | 2 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 242–388 | 96 | 5 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 253–254 | 2 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 259–291 | 33 | 1 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 259–689 | 409 | 9 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 265–318 | 51 | 3 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 268–378 | 111 | 1 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 272–344 | 70 | 2 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 355–689 | 285 | 8 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 361–675 | 307 | 4 | Undefined position; Undefined team |
| `45` | `56` | Position_Unknown | Team_Unknown | 361–396 | 36 | 1 | Undefined position; Undefined team |
| `46` | `57` | Position_Unknown | Team_Unknown | 370–426 | 57 | 1 | Undefined position; Undefined team |
| `47` | `58` | Position_Unknown | Team_Unknown | 378–655 | 271 | 2 | Undefined position; Undefined team |
| `48` | `59` | Position_Unknown | Team_Unknown | 386–426 | 35 | 2 | Undefined position; Undefined team |
| `49` | `60` | Position_Unknown | Team_Unknown | 397–617 | 221 | 1 | Undefined position; Undefined team |
| `50` | `61` | Position_Unknown | Team_Unknown | 402–419 | 18 | 1 | Undefined position; Undefined team |
| `51` | `62` | Position_Unknown | Team_Unknown | 410–682 | 268 | 5 | Undefined position; Undefined team |
| `52` | `63` | Position_Unknown | Team_Unknown | 420–555 | 88 | 2 | Undefined position; Undefined team |
| `53` | `65` | Position_Unknown | Team_Unknown | 424–515 | 73 | 7 | Undefined position; Undefined team |
| `54` | `66` | Position_Unknown | Team_Unknown | 427–689 | 263 | 1 | Undefined position; Undefined team |
| `55` | `71` | Position_Unknown | Team_Unknown | 477–479 | 3 | 1 | Undefined position; Undefined team |
| `56` | `72` | Position_Unknown | Team_Unknown | 479–689 | 209 | 3 | Undefined position; Undefined team |
| `57` | `74` | Position_Unknown | Team_Unknown | 521–560 | 10 | 4 | Undefined position; Undefined team |
| `58` | `75` | Position_Unknown | Team_Unknown | 529–535 | 7 | 1 | Undefined position; Undefined team |
| `59` | `77` | Position_Unknown | Team_Unknown | 534–535 | 2 | 1 | Undefined position; Undefined team |
| `60` | `80` | Position_Unknown | Team_Unknown | 537–689 | 150 | 3 | Undefined position; Undefined team |
| `61` | `84` | Position_Unknown | Team_Unknown | 544–545 | 2 | 1 | Undefined position; Undefined team |
| `62` | `87` | Position_Unknown | Team_Unknown | 546–614 | 54 | 9 | Undefined position; Undefined team |
| `63` | `88` | Position_Unknown | Team_Unknown | 549–550 | 2 | 1 | Undefined position; Undefined team |
| `64` | `92` | Position_Unknown | Team_Unknown | 584–586 | 3 | 1 | Undefined position; Undefined team |
| `65` | `96` | Position_Unknown | Team_Unknown | 596–689 | 93 | 2 | Undefined position; Undefined team |
| `66` | `100` | Position_Unknown | Team_Unknown | 622–632 | 9 | 3 | Undefined position; Undefined team |
| `67` | `102` | Position_Unknown | Team_Unknown | 670–689 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_KickBall` on target `9` (Kicker)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `43` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ 52 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 52 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 104 |
| Missing visible bounding boxes during action | 211 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 32: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Segment 'Action_KickBall' for track '9' has invalid range: start=187, end=167. Clamping end to start.
- ⚠️ Segment 'Action_CrossGoalLine' for track '36' has invalid range: start=678, end=388. Clamping end to start.
- ⚠️ Action 'Action_None' range [124-689] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-375] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-656] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-372] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-398] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-640] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-406] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-412] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-424] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-434] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-456] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-460] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-498] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-506] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-543] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-689] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-215] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-282] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-294] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-310] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-289] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-316] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-624] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-636] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-673] for track '5' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-160] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-372] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-567] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-574] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-580] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-605] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-611] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-619] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-630] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-658] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [660-678] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-224] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [124-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-216] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-273] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-348] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-364] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-399] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-660] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-172] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-196] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-162] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-16] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-20] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-156] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-118] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-244] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-260] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-306] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-344] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-359] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-394] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-111] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-289] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-306] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-319] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-554] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-230] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-302] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-312] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-515] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-221] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-244] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-498] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-368] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-395] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-631] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-238] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-252] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-291] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-310] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-328] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-348] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-514] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-554] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-567] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-578] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-597] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-602] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-631] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-650] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-247] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-249] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [331-388] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-291] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-277] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-306] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-385] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-558] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-612] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-274] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-318] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-378] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-309] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-344] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-362] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-470] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-480] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-522] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-541] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-548] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-436] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-611] for track '44' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-626] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-675] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-396] for track '45' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-426] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-381] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-655] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-412] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-426] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-617] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-419] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-491] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-511] for track '51' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-517] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-524] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-682] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-505] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-555] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-466] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-471] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-478] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-491] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-496] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-505] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-515] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-689] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-479] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-493] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-642] for track '56' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-522] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-548] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-560] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-535] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-535] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-546] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-624] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-545] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-548] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-554] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-568] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-572] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-583] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-586] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-590] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-597] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-614] for track '62' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-550] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-586] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-602] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-689] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-626] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-629] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-632] for track '66' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.

</details>