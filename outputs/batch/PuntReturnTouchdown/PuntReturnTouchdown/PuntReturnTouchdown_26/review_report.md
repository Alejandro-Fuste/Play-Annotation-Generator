# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_26

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_26`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 185
- **Validation Warnings:** 218
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 170
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `29` | `26` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `29` | `26` |
| ⚠️ START CHANGED | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `29` | `26` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `0` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `1` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `10` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `15` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `3` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `4` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `5` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `7` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `8` | `Group` | 0 | START | 0 | 70 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `4` | `4` | 71 | START | 71 | 125 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `3` | `3` | 94 | END | 94 | 94 |
| ✅ EXACT | `Action_PuntBall` | Punter | `3` | `3` | 126 | START | 126 | 140 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `29` | `26` | 254 | START | 254 | 260 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `29` | `26` | 261 | START | 261 | 264 |
| ⚠️ START CHANGED | `Action_CrossGoalLine` | Position_Unknown | `29` | `26` | 574 | START | 581 | 581 |

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
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 228 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 341 | 271 | inferred_complete_timeline |
| `Action_None` | 343 | 344 | 2 | inferred_complete_timeline |
| `Action_None` | 346 | 435 | 90 | inferred_complete_timeline |
| `Action_None` | 437 | 513 | 77 | inferred_complete_timeline |
| `Action_None` | 515 | 586 | 72 | inferred_complete_timeline |
| `Action_None` | 589 | 599 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 575

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_LongSnap` | 71 | 125 | 55 | inferred_complete_timeline |
| `Action_None` | 126 | 365 | 240 | inferred_complete_timeline |
| `Action_None` | 378 | 417 | 40 | inferred_complete_timeline |
| `Action_None` | 423 | 582 | 160 | inferred_complete_timeline |
| `Action_None` | 591 | 599 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 266 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–310
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 310 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_SnapReceive` | 94 | 94 | 1 | inferred_complete_timeline |
| `Action_None` | 95 | 125 | 31 | inferred_complete_timeline |
| `Action_PuntBall` | 126 | 140 | 15 | inferred_complete_timeline |
| `Action_None` | 141 | 426 | 286 | inferred_complete_timeline |
| `Action_None` | 429 | 484 | 56 | inferred_complete_timeline |
| `Action_None` | 512 | 525 | 14 | inferred_complete_timeline |
| `Action_None` | 527 | 536 | 10 | inferred_complete_timeline |
| `Action_None` | 538 | 544 | 7 | inferred_complete_timeline |
| `Action_None` | 549 | 599 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–508
- **Visible Samples:** 495

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 281 | 211 | inferred_complete_timeline |
| `Action_None` | 286 | 372 | 87 | inferred_complete_timeline |
| `Action_None` | 374 | 450 | 77 | inferred_complete_timeline |
| `Action_None` | 452 | 458 | 7 | inferred_complete_timeline |
| `Action_None` | 467 | 508 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 592

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 128 | 58 | inferred_complete_timeline |
| `Action_None` | 131 | 311 | 181 | inferred_complete_timeline |
| `Action_None` | 314 | 496 | 183 | inferred_complete_timeline |
| `Action_None` | 501 | 599 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 136 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 185 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 229 | 159 | inferred_complete_timeline |
| `Action_None` | 231 | 452 | 222 | inferred_complete_timeline |
| `Action_None` | 455 | 577 | 123 | inferred_complete_timeline |
| `Action_None` | 580 | 599 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 572

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 171 | 101 | inferred_complete_timeline |
| `Action_None` | 185 | 346 | 162 | inferred_complete_timeline |
| `Action_None` | 351 | 381 | 31 | inferred_complete_timeline |
| `Action_None` | 391 | 480 | 90 | inferred_complete_timeline |
| `Action_None` | 483 | 599 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 593

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 203 | 133 | inferred_complete_timeline |
| `Action_None` | 205 | 245 | 41 | inferred_complete_timeline |
| `Action_None` | 251 | 276 | 26 | inferred_complete_timeline |
| `Action_None` | 278 | 599 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 85 | 15 | inferred_complete_timeline |
| `Action_None` | 87 | 456 | 370 | inferred_complete_timeline |
| `Action_None` | 466 | 520 | 55 | inferred_complete_timeline |
| `Action_None` | 525 | 548 | 24 | inferred_complete_timeline |
| `Action_None` | 596 | 599 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher6 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 125 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher7 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 91 | 21 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_None` | 105 | 124 | 20 | inferred_complete_timeline |
| `Action_None` | 134 | 136 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher8 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 84 | 14 | inferred_complete_timeline |
| `Action_None` | 89 | 131 | 43 | inferred_complete_timeline |
| `Action_None` | 138 | 205 | 68 | inferred_complete_timeline |
| `Action_None` | 215 | 272 | 58 | inferred_complete_timeline |
| `Action_None` | 280 | 296 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher9 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 585

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 105 | 35 | inferred_complete_timeline |
| `Action_None` | 111 | 158 | 48 | inferred_complete_timeline |
| `Action_None` | 163 | 407 | 245 | inferred_complete_timeline |
| `Action_None` | 409 | 520 | 112 | inferred_complete_timeline |
| `Action_None` | 525 | 574 | 50 | inferred_complete_timeline |
| `Action_None` | 576 | 599 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–487
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 280 | 210 | inferred_complete_timeline |
| `Action_None` | 286 | 421 | 136 | inferred_complete_timeline |
| `Action_None` | 465 | 487 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–118 | 119 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 12–73 | 38 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 19–599 | 537 | 8 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 121–221 | 100 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 140–527 | 358 | 7 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 141–484 | 314 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 143–592 | 442 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 145–596 | 431 | 10 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 187–468 | 278 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 229–260 | 31 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 269–273 | 5 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 273–599 | 313 | 5 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 292–591 | 295 | 3 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 301–366 | 66 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 313–457 | 143 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 327–342 | 16 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 354–376 | 21 | 2 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 362–412 | 11 | 4 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 372–599 | 224 | 2 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 378–391 | 12 | 3 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 385–599 | 211 | 2 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 433–452 | 20 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 467–599 | 108 | 6 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 483–503 | 21 | 1 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 491–599 | 109 | 1 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 497–501 | 5 | 1 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 540–551 | 9 | 2 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 553–599 | 47 | 1 | Undefined position; Undefined team |
| `47` | `65` | Position_Unknown | Team_Unknown | 565–568 | 4 | 1 | Undefined position; Undefined team |
| `48` | `66` | Position_Unknown | Team_Unknown | 566–599 | 34 | 1 | Undefined position; Undefined team |
| `49` | `67` | Position_Unknown | Team_Unknown | 574–599 | 19 | 2 | Undefined position; Undefined team |
| `50` | `68` | Position_Unknown | Team_Unknown | 577–598 | 19 | 2 | Undefined position; Undefined team |
| `51` | `69` | Position_Unknown | Team_Unknown | 586–596 | 9 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `29` (6 segments found)
- ⚠️ `Action_CrossGoalLine` for actor_track_id `29` (Position_Unknown): Annotated start 574 != Inferred start 581

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Edge_Rusher9` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Edge_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Edge_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Edge_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Edge_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Edge_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Edge_Rusher2` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 149 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [71-341] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-435] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-513] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-586] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-128] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-311] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-496] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-599] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-118] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-426] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-484] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-525] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-536] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-544] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-365] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-417] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-582] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-84] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-131] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-205] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-272] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-296] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-228] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-310] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-280] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-421] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-487] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-281] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-372] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-450] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-458] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-508] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-105] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-407] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-520] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-574] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-599] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-456] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-520] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-548] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-599] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-203] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-245] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-276] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-266] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-185] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-346] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-381] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-480] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-124] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-229] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-452] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-577] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-17] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-43] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-63] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 71, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [71-73] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-35] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-40] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '21' starts at frame 71, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [71-74] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-371] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-483] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-562] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-599] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-221] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-166] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-204] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-476] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-490] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-514] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-519] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-527] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-268] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-362] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-446] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-471] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-484] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-446] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-588] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-592] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-209] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [261-264] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [266-420] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [423-561] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [568-569] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [571-572] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '26' starts at frame 582, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [582-596] for track '26' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-442] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-468] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-273] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-442] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-502] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-536] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-572] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-599] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-415] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-530] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-591] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-366] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-418] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-457] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-342] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-358] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-376] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-406] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-488] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-391] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-489] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-452] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-510] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-515] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-533] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-545] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-576] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-503] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-599] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-501] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-544] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-551] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-568] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-576] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-599] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-589] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-598] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-589] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-596] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>