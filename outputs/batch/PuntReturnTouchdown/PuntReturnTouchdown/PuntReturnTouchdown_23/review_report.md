# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_23

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_23`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 61
- **Ball Tracks:** 0
- **Action Segments:** 235
- **Validation Warnings:** 288
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 11
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
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | offense | `5` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | offense | `18` | `18` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Punter | offense | `20` | `20` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `20` | `20` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `37` | `29` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `37` | `29` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `37` | `29` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `0` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `10` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `12` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `17` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `19` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | `2` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `20` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `4` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | `5` | `Group` | 0 | START | 0 | 20 |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | `18` | `18` | 21 | START | 21 | 72 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Punter | `20` | `20` | 52 | END | N/A | N/A |
| ✅ EXACT | `Action_PuntBall` | Punter | `20` | `20` | 74 | START | 74 | 90 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `37` | `29` | 219 | START | 219 | 223 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `37` | `29` | 247 | START | 247 | 341 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `37` | `29` | 536 | START | N/A | N/A |

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
- **Visible Frames:** 0–208
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 72 | 52 | inferred_complete_timeline |
| `Action_None` | 74 | 109 | 36 | inferred_complete_timeline |
| `Action_None` | 112 | 121 | 10 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_None` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_None` | 136 | 142 | 7 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 186 | 27 | inferred_complete_timeline |
| `Action_None` | 189 | 197 | 9 | inferred_complete_timeline |
| `Action_None` | 204 | 208 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–341
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 84 | 64 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 223 | 107 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_None` | 306 | 341 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 103 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 99 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–395
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 82 | 62 | inferred_complete_timeline |
| `Action_None` | 88 | 186 | 99 | inferred_complete_timeline |
| `Action_None` | 190 | 203 | 14 | inferred_complete_timeline |
| `Action_None` | 223 | 307 | 85 | inferred_complete_timeline |
| `Action_None` | 310 | 364 | 55 | inferred_complete_timeline |
| `Action_None` | 371 | 395 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 138 | 118 | inferred_complete_timeline |
| `Action_None` | 140 | 153 | 14 | inferred_complete_timeline |
| `Action_None` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 162 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 101 | 81 | inferred_complete_timeline |
| `Action_None` | 103 | 140 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 134 | 114 | inferred_complete_timeline |
| `Action_None` | 136 | 150 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 34 | 5 | inferred_complete_timeline |
| `Action_None` | 58 | 73 | 16 | inferred_complete_timeline |
| `Action_PuntBall` | 74 | 90 | 17 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 110 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_LongSnap` | 21 | 72 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–478
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 48 | 28 | inferred_complete_timeline |
| `Action_None` | 51 | 121 | 71 | inferred_complete_timeline |
| `Action_None` | 123 | 187 | 65 | inferred_complete_timeline |
| `Action_None` | 203 | 209 | 7 | inferred_complete_timeline |
| `Action_None` | 212 | 452 | 241 | inferred_complete_timeline |
| `Action_None` | 454 | 473 | 20 | inferred_complete_timeline |
| `Action_None` | 475 | 478 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 112 | 92 | inferred_complete_timeline |
| `Action_None` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_None` | 121 | 130 | 10 | inferred_complete_timeline |
| `Action_None` | 132 | 208 | 77 | inferred_complete_timeline |
| `Action_None` | 214 | 233 | 20 | inferred_complete_timeline |
| `Action_None` | 237 | 283 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 114 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 168 | 148 | inferred_complete_timeline |
| `Action_None` | 171 | 177 | 7 | inferred_complete_timeline |
| `Action_None` | 182 | 185 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–338
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 303 | 283 | inferred_complete_timeline |
| `Action_None` | 337 | 338 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 168 | 148 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 183 | 187 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 121 | 101 | inferred_complete_timeline |
| `Action_None` | 132 | 208 | 77 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 218 | 237 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 177 | 157 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 256 | 22 | inferred_complete_timeline |
| `Action_None` | 258 | 262 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–436
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 205 | 185 | inferred_complete_timeline |
| `Action_None` | 207 | 328 | 122 | inferred_complete_timeline |
| `Action_None` | 332 | 380 | 49 | inferred_complete_timeline |
| `Action_None` | 387 | 388 | 2 | inferred_complete_timeline |
| `Action_None` | 399 | 400 | 2 | inferred_complete_timeline |
| `Action_None` | 435 | 436 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 528

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 186 | 166 | inferred_complete_timeline |
| `Action_None` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_None` | 197 | 404 | 208 | inferred_complete_timeline |
| `Action_None` | 407 | 469 | 63 | inferred_complete_timeline |
| `Action_None` | 473 | 539 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 128 | 108 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `23` | Position_Unknown | Team_Unknown | 57–58 | 2 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 78–426 | 283 | 19 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 83–84 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 84–141 | 54 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 105–150 | 46 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 131–132 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 139–306 | 166 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 142–250 | 109 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 156–341 | 186 | 4 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 216–248 | 28 | 3 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 218–281 | 64 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 235–357 | 119 | 3 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 239–539 | 276 | 10 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 245–528 | 269 | 4 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 256–539 | 277 | 4 | Undefined position; Undefined team |
| `37` | `57` | Position_Unknown | Team_Unknown | 257–537 | 273 | 6 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 277–539 | 246 | 5 | Undefined position; Undefined team |
| `39` | `60` | Position_Unknown | Team_Unknown | 278–402 | 91 | 5 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 281–539 | 245 | 7 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 296–539 | 240 | 2 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 302–454 | 153 | 1 | Undefined position; Undefined team |
| `43` | `67` | Position_Unknown | Team_Unknown | 321–539 | 217 | 2 | Undefined position; Undefined team |
| `44` | `68` | Position_Unknown | Team_Unknown | 325–376 | 52 | 1 | Undefined position; Undefined team |
| `45` | `69` | Position_Unknown | Team_Unknown | 325–384 | 55 | 3 | Undefined position; Undefined team |
| `46` | `72` | Position_Unknown | Team_Unknown | 342–454 | 107 | 2 | Undefined position; Undefined team |
| `47` | `75` | Position_Unknown | Team_Unknown | 372–539 | 159 | 3 | Undefined position; Undefined team |
| `48` | `76` | Position_Unknown | Team_Unknown | 377–464 | 69 | 5 | Undefined position; Undefined team |
| `49` | `77` | Position_Unknown | Team_Unknown | 385–394 | 8 | 2 | Undefined position; Undefined team |
| `50` | `78` | Position_Unknown | Team_Unknown | 387–404 | 18 | 1 | Undefined position; Undefined team |
| `51` | `81` | Position_Unknown | Team_Unknown | 397–539 | 142 | 2 | Undefined position; Undefined team |
| `52` | `82` | Position_Unknown | Team_Unknown | 400–416 | 17 | 1 | Undefined position; Undefined team |
| `53` | `85` | Position_Unknown | Team_Unknown | 431–433 | 3 | 1 | Undefined position; Undefined team |
| `54` | `86` | Position_Unknown | Team_Unknown | 434–517 | 34 | 7 | Undefined position; Undefined team |
| `55` | `87` | Position_Unknown | Team_Unknown | 439–539 | 100 | 2 | Undefined position; Undefined team |
| `56` | `89` | Position_Unknown | Team_Unknown | 458–516 | 54 | 3 | Undefined position; Undefined team |
| `57` | `91` | Position_Unknown | Team_Unknown | 463–517 | 29 | 3 | Undefined position; Undefined team |
| `58` | `98` | Position_Unknown | Team_Unknown | 473–539 | 63 | 4 | Undefined position; Undefined team |
| `59` | `107` | Position_Unknown | Team_Unknown | 503–539 | 37 | 1 | Undefined position; Undefined team |
| `60` | `108` | Position_Unknown | Team_Unknown | 524–539 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SnapReceive` on target `20` (Punter)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `37` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Punter` position mapped to `offense` team
- ⚠️ 40 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 40 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 80 |
| Missing visible bounding boxes during action | 204 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_CrossGoalLine' for track '29' has invalid range: start=536, end=341. Clamping end to start.
- ⚠️ Action 'Action_None' range [21-48] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-121] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-187] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-452] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-473] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-478] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-128] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-84] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-223] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-341] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-168] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-177] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-138] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-153] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-103] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-114] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-186] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-404] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-469] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-539] for track '7' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-303] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-205] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-328] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-380] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-400] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-168] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-187] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-140] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-208] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-237] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-177] for track '14' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-256] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-112] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-130] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-208] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-233] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-283] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-72] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-109] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-121] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-186] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-197] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-186] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-203] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-307] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-364] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-395] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [21-72] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-34] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [74-90] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-166] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-197] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-215] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-230] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-338] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-394] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-426] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-114] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-141] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-180] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-239] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-306] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-250] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [247-341] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-235] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-281] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-312] for track '33' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-354] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-355] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-461] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-481] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-484] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-488] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-498] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-530] for track '34' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-350] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-360] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-517] for track '35' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-528] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-300] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-355] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-388] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-300] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-504] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-521] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-530] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-294] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-394] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-398] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-476] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-316] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-340] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-370] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-394] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-492] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-508] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-523] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-527] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-532] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-461] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-454] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-418] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-539] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-376] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-341] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-384] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-429] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-454] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-376] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-393] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-539] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-389] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-442] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-458] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-464] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-390] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-394] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-404] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-412] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-416] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-433] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-439] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-448] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-454] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-466] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-473] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-517] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-445] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-539] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-463] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-469] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-516] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-508] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-517] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-509] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-524] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-528] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-539] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-539] for track '60' has 1 frames without a visible bounding box.
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