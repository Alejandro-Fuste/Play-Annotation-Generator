# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_69

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_69`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 61
- **Ball Tracks:** 0
- **Action Segments:** 183
- **Validation Warnings:** 234
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 167
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `1` | `1` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `1` | `1` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `25` | `21` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `25` | `21` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `59` | `42` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner2 | `0` | `Group` | 9 | START | 9 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `1` | `Group` | 9 | START | 9 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `12` | `Group` | 9 | START | 9 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `13` | `Group` | 9 | START | 9 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 9 | START | 9 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `16` | `Group` | 9 | START | 9 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `17` | `Group` | 9 | START | 9 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 9 | START | 9 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `20` | `Group` | 9 | START | 9 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner1 | `8` | `Group` | 9 | START | 9 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `9` | `Group` | 9 | START | 9 | 26 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `16` | `16` | 27 | START | 27 | 78 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `1` | `1` | 52 | END | 52 | 52 |
| ✅ EXACT | `Action_PuntBall` | Punter | `1` | `1` | 79 | START | 79 | 90 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `25` | `21` | 203 | START | 203 | 208 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `25` | `21` | 244 | START | N/A | N/A |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `59` | `42` | 553 | START | 553 | 558 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 9–161
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 91 | 65 | inferred_complete_timeline |
| `Action_None` | 95 | 101 | 7 | inferred_complete_timeline |
| `Action_None` | 108 | 117 | 10 | inferred_complete_timeline |
| `Action_None` | 119 | 161 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 9–118
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 118 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 9–166
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_LongSnap` | 27 | 78 | 52 | inferred_complete_timeline |
| `Action_None` | 79 | 166 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 9–569
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 569 | 543 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 9–48
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 42 | 16 | inferred_complete_timeline |
| `Action_None` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_None` | 47 | 48 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 9–258
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 254 | 228 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 9–153
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 51 | 43 | inferred_complete_timeline |
| `Action_SnapReceive` | 52 | 52 | 1 | inferred_complete_timeline |
| `Action_None` | 53 | 78 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 79 | 90 | 12 | inferred_complete_timeline |
| `Action_None` | 91 | 153 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 9–121
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 121 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 9–233
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 160 | 134 | inferred_complete_timeline |
| `Action_None` | 167 | 233 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 9–271
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 243 | 217 | inferred_complete_timeline |
| `Action_None` | 245 | 249 | 5 | inferred_complete_timeline |
| `Action_None` | 252 | 257 | 6 | inferred_complete_timeline |
| `Action_None` | 259 | 261 | 3 | inferred_complete_timeline |
| `Action_None` | 264 | 271 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 9–474
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 74 | 48 | inferred_complete_timeline |
| `Action_None` | 84 | 200 | 117 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 218 | 246 | 29 | inferred_complete_timeline |
| `Action_None` | 249 | 474 | 226 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 9–569
- **Visible Samples:** 557

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 375 | 349 | inferred_complete_timeline |
| `Action_None` | 379 | 510 | 132 | inferred_complete_timeline |
| `Action_None` | 512 | 569 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–483
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 154 | 128 | inferred_complete_timeline |
| `Action_None` | 158 | 229 | 72 | inferred_complete_timeline |
| `Action_None` | 233 | 240 | 8 | inferred_complete_timeline |
| `Action_None` | 242 | 349 | 108 | inferred_complete_timeline |
| `Action_None` | 353 | 392 | 40 | inferred_complete_timeline |
| `Action_None` | 394 | 483 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 9–221
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 33 | 7 | inferred_complete_timeline |
| `Action_None` | 36 | 39 | 4 | inferred_complete_timeline |
| `Action_None` | 43 | 176 | 134 | inferred_complete_timeline |
| `Action_None` | 178 | 195 | 18 | inferred_complete_timeline |
| `Action_None` | 203 | 213 | 11 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 9–370
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 134 | 108 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 366 | 215 | inferred_complete_timeline |
| `Action_None` | 369 | 370 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 9–569
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 228 | 202 | inferred_complete_timeline |
| `Action_None` | 232 | 569 | 338 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 9–442
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 59 | 33 | inferred_complete_timeline |
| `Action_None` | 62 | 442 | 381 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 9–232
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 232 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 9–476
- **Visible Samples:** 461

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 265 | 239 | inferred_complete_timeline |
| `Action_None` | 268 | 376 | 109 | inferred_complete_timeline |
| `Action_None` | 381 | 384 | 4 | inferred_complete_timeline |
| `Action_None` | 386 | 476 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 9–384
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 384 | 358 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 9–488 | 471 | 5 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 118–216 | 99 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 121–155 | 15 | 4 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 138–297 | 160 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 149–416 | 234 | 4 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 164–569 | 393 | 3 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 166–169 | 4 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 206–569 | 363 | 2 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 226–229 | 4 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 228–233 | 6 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 246–500 | 253 | 2 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 261–465 | 204 | 2 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 267–446 | 178 | 2 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 270–569 | 276 | 4 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 273–401 | 123 | 5 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 302–303 | 2 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 304–305 | 2 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 312–568 | 248 | 3 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 317–569 | 247 | 4 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 328–569 | 238 | 2 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 329–461 | 132 | 2 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 362–380 | 19 | 1 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 382–569 | 185 | 4 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 396–401 | 6 | 1 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 398–569 | 172 | 1 | Undefined position; Undefined team |
| `45` | `66` | Position_Unknown | Team_Unknown | 409–468 | 4 | 2 | Undefined position; Undefined team |
| `46` | `70` | Position_Unknown | Team_Unknown | 417–569 | 152 | 2 | Undefined position; Undefined team |
| `47` | `71` | Position_Unknown | Team_Unknown | 421–558 | 61 | 10 | Undefined position; Undefined team |
| `48` | `72` | Position_Unknown | Team_Unknown | 422–464 | 38 | 2 | Undefined position; Undefined team |
| `49` | `73` | Position_Unknown | Team_Unknown | 424–426 | 3 | 1 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 439–440 | 2 | 1 | Undefined position; Undefined team |
| `51` | `75` | Position_Unknown | Team_Unknown | 460–471 | 5 | 2 | Undefined position; Undefined team |
| `52` | `78` | Position_Unknown | Team_Unknown | 489–569 | 55 | 7 | Undefined position; Undefined team |
| `53` | `81` | Position_Unknown | Team_Unknown | 491–492 | 2 | 1 | Undefined position; Undefined team |
| `54` | `86` | Position_Unknown | Team_Unknown | 501–568 | 13 | 3 | Undefined position; Undefined team |
| `55` | `91` | Position_Unknown | Team_Unknown | 505–567 | 29 | 3 | Undefined position; Undefined team |
| `56` | `97` | Position_Unknown | Team_Unknown | 510–519 | 10 | 1 | Undefined position; Undefined team |
| `57` | `98` | Position_Unknown | Team_Unknown | 511–569 | 48 | 5 | Undefined position; Undefined team |
| `58` | `102` | Position_Unknown | Team_Unknown | 532–533 | 2 | 1 | Undefined position; Undefined team |
| `59` | `103` | Position_Unknown | Team_Unknown | 536–537 | 2 | 1 | Undefined position; Undefined team |
| `60` | `104` | Position_Unknown | Team_Unknown | 564–569 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallCarry` on target `25` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ 41 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 41 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 82 |
| Missing visible bounding boxes during action | 148 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_BallCarry' for track '21' has invalid range: start=244, end=216. Clamping end to start.
- ⚠️ Action 'Action_None' range [27-243] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-257] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-271] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-59] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-442] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-232] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-265] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-376] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-476] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-384] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-375] for track '6' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-510] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-243] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-488] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-160] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-233] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-74] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-200] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-246] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-474] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-229] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-240] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-349] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-392] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-483] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-366] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-569] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-254] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-228] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-569] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-117] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-161] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-166] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-176] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-195] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-213] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-42] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-48] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-216] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-297] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-204] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-375] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-416] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-188] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-362] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-569] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-238] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-569] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-233] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-449] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-500] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-270] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-465] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-283] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-446] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-275] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-442] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-468] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-569] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-311] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-354] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-401] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-508] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-556] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-568] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-320] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-327] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-436] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-390] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-569] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-426] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-461] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-380] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '42' starts at frame 559, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [559-559] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-401] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-410] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-468] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-544] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-430] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-444] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-450] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-471] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-484] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-503] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-518] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-537] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-558] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-446] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-464] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-426] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-440] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-471] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-490] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-494] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-499] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-506] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-551] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-559] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-550] for track '54' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-568] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-520] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-562] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-519] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-532] for track '57' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-535] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-555] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-562] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-569] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>