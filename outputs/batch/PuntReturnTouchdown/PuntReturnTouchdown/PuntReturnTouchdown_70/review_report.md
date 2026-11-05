# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_70

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_70`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 189
- **Validation Warnings:** 231
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
- **Inferred Coverage Segments (Action_None):** 175
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchPunt` | Punt_Returner | defense | `8` | `8` |
| ✅ EXACT | `Action_BallCarry` | Punt_Returner | defense | `8` | `8` |
| ✅ EXACT | `Action_CrossGoalLine` | Punt_Returner | defense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `12` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `13` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `14` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `15` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `17` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `6` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `9` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `9` | `9` | 11 | START | 11 | 57 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `12` | `12` | 37 | END | 37 | 37 |
| ✅ EXACT | `Action_PuntBall` | Punter | `12` | `12` | 58 | START | 58 | 74 |
| ✅ EXACT | `Action_CatchPunt` | Punt_Returner | `8` | `8` | 176 | START | 176 | 192 |
| ✅ EXACT | `Action_BallCarry` | Punt_Returner | `8` | `8` | 226 | START | 226 | 534 |
| ✅ EXACT | `Action_CrossGoalLine` | Punt_Returner | `8` | `8` | 535 | START | 535 | 539 |

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
- **Visible Frames:** 0–39
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 18 | 39 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 14 | 52 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 530

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_LongSnap` | 11 | 57 | 47 | inferred_complete_timeline |
| `Action_None` | 58 | 68 | 11 | inferred_complete_timeline |
| `Action_None` | 70 | 149 | 80 | inferred_complete_timeline |
| `Action_None` | 152 | 379 | 228 | inferred_complete_timeline |
| `Action_None` | 387 | 539 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 539 | 529 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 482

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 36 | 26 | inferred_complete_timeline |
| `Action_None` | 38 | 101 | 64 | inferred_complete_timeline |
| `Action_None` | 104 | 121 | 18 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 297 | 171 | inferred_complete_timeline |
| `Action_None` | 309 | 311 | 3 | inferred_complete_timeline |
| `Action_None` | 323 | 365 | 43 | inferred_complete_timeline |
| `Action_None` | 371 | 442 | 72 | inferred_complete_timeline |
| `Action_None` | 448 | 449 | 2 | inferred_complete_timeline |
| `Action_None` | 456 | 459 | 4 | inferred_complete_timeline |
| `Action_None` | 474 | 539 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 196 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–538
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_SnapReceive` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_None` | 38 | 57 | 20 | inferred_complete_timeline |
| `Action_PuntBall` | 58 | 74 | 17 | inferred_complete_timeline |
| `Action_None` | 75 | 104 | 30 | inferred_complete_timeline |
| `Action_None` | 106 | 126 | 21 | inferred_complete_timeline |
| `Action_None` | 130 | 142 | 13 | inferred_complete_timeline |
| `Action_None` | 145 | 538 | 394 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–31
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 16 | 6 | inferred_complete_timeline |
| `Action_None` | 19 | 31 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 252 | 242 | inferred_complete_timeline |
| `Action_None` | 254 | 257 | 4 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 269 | 287 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 512

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 322 | 312 | inferred_complete_timeline |
| `Action_None` | 324 | 397 | 74 | inferred_complete_timeline |
| `Action_None` | 404 | 468 | 65 | inferred_complete_timeline |
| `Action_None` | 473 | 474 | 2 | inferred_complete_timeline |
| `Action_None` | 479 | 480 | 2 | inferred_complete_timeline |
| `Action_None` | 482 | 485 | 4 | inferred_complete_timeline |
| `Action_None` | 493 | 508 | 16 | inferred_complete_timeline |
| `Action_None` | 511 | 529 | 19 | inferred_complete_timeline |
| `Action_None` | 532 | 536 | 5 | inferred_complete_timeline |
| `Action_None` | 538 | 539 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–338
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 70 | 60 | inferred_complete_timeline |
| `Action_None` | 80 | 156 | 77 | inferred_complete_timeline |
| `Action_None` | 160 | 320 | 161 | inferred_complete_timeline |
| `Action_None` | 336 | 338 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 129 | 119 | inferred_complete_timeline |
| `Action_None` | 131 | 146 | 16 | inferred_complete_timeline |
| `Action_None` | 151 | 239 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 74 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Returner — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_CatchPunt` | 176 | 192 | 17 | inferred_complete_timeline |
| `Action_None` | 193 | 208 | 16 | inferred_complete_timeline |
| `Action_None` | 212 | 225 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 226 | 534 | 309 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 535 | 539 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–4
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 43 | 33 | inferred_complete_timeline |
| `Action_None` | 45 | 233 | 189 | inferred_complete_timeline |
| `Action_None` | 239 | 338 | 100 | inferred_complete_timeline |
| `Action_None` | 340 | 351 | 12 | inferred_complete_timeline |
| `Action_None` | 353 | 539 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 511

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 173 | 163 | inferred_complete_timeline |
| `Action_None` | 178 | 468 | 291 | inferred_complete_timeline |
| `Action_None` | 483 | 484 | 2 | inferred_complete_timeline |
| `Action_None` | 488 | 524 | 37 | inferred_complete_timeline |
| `Action_None` | 527 | 528 | 2 | inferred_complete_timeline |
| `Action_None` | 535 | 539 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–197 | 198 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 2–47 | 45 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 15–43 | 29 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 35–539 | 479 | 7 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 47–220 | 167 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 49–288 | 235 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 54–208 | 144 | 7 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 59–141 | 83 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 60–539 | 476 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 63–246 | 168 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 80–409 | 326 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 86–539 | 433 | 9 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 106–133 | 13 | 5 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 151–539 | 389 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 165–166 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 212–264 | 51 | 3 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 215–371 | 148 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 216–255 | 27 | 3 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 230–251 | 21 | 2 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 242–437 | 181 | 5 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 246–247 | 2 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 249–539 | 287 | 2 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 250–539 | 287 | 3 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 259–539 | 257 | 8 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 283–539 | 257 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 308–539 | 224 | 4 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 318–403 | 8 | 3 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 319–539 | 219 | 3 | Undefined position; Undefined team |
| `46` | `63` | Position_Unknown | Team_Unknown | 354–397 | 16 | 3 | Undefined position; Undefined team |
| `47` | `65` | Position_Unknown | Team_Unknown | 377–539 | 147 | 4 | Undefined position; Undefined team |
| `48` | `66` | Position_Unknown | Team_Unknown | 377–378 | 2 | 1 | Undefined position; Undefined team |
| `49` | `70` | Position_Unknown | Team_Unknown | 411–422 | 12 | 1 | Undefined position; Undefined team |
| `50` | `71` | Position_Unknown | Team_Unknown | 450–539 | 90 | 1 | Undefined position; Undefined team |
| `51` | `72` | Position_Unknown | Team_Unknown | 490–539 | 50 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punt_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 35 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 35 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 70 |
| Missing visible bounding boxes during action | 157 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 142: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [11-129] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-146] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-239] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-173] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-468] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-484] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-524] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-528] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-197] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-252] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-287] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-43] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-233] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-338] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-351] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-539] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-16] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-31] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-70] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-156] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-320] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-338] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-208] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [226-534] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [535-539] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-379] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-322] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-397] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-468] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-480] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-485] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-508] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-529] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-536] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-74] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-538] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-297] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-311] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-365] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-442] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-459] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-539] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-196] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-52] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-5] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-10] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 11, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [11-47] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-43] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-46] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-94] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-118] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-195] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-372] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-508] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-539] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-55] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-90] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-220] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-206] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-288] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-137] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-197] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-141] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-351] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-486] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-79] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-139] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-246] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-301] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-404] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-236] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-305] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-362] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-402] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-503] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-513] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-516] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-539] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-539] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-257] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-357] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-371] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-230] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-255] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-251] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-298] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-338] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-360] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-368] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-437] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-498] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-301] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-340] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-335] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-352] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-413] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-431] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-435] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-539] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-316] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-335] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-341] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-393] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-331] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-350] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-362] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-372] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-419] for track '47' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-427] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-435] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-422] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-539] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>