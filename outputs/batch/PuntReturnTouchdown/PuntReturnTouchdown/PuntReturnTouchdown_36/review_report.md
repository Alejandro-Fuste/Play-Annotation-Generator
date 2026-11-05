# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_36

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_36`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 479
- **Player Tracks:** 61
- **Ball Tracks:** 0
- **Action Segments:** 253
- **Validation Warnings:** 309
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 239
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `10` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `12` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `13` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `17` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `2` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `3` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `5` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `6` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `7` | `Group` | 0 | START | 0 | 114 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `13` | `13` | 87 | START | 87 | 140 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `7` | `7` | 115 | END | 115 | 115 |
| ✅ EXACT | `Action_PuntBall` | Punter | `7` | `7` | 141 | START | 141 | 144 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 103 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 86 | 37 | inferred_complete_timeline |
| `Action_None` | 87 | 90 | 4 | inferred_complete_timeline |
| `Action_None` | 94 | 165 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–370
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_LongSnap` | 87 | 140 | 54 | inferred_complete_timeline |
| `Action_None` | 141 | 141 | 1 | inferred_complete_timeline |
| `Action_None` | 145 | 370 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 122 | 36 | inferred_complete_timeline |
| `Action_None` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_None` | 174 | 335 | 162 | inferred_complete_timeline |
| `Action_None` | 337 | 368 | 32 | inferred_complete_timeline |
| `Action_None` | 371 | 377 | 7 | inferred_complete_timeline |
| `Action_None` | 382 | 383 | 2 | inferred_complete_timeline |
| `Action_None` | 385 | 445 | 61 | inferred_complete_timeline |
| `Action_None` | 457 | 479 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–395
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 133 | 47 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 378 | 180 | inferred_complete_timeline |
| `Action_None` | 381 | 383 | 3 | inferred_complete_timeline |
| `Action_None` | 385 | 395 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 111 | 25 | inferred_complete_timeline |
| `Action_None` | 127 | 309 | 183 | inferred_complete_timeline |
| `Action_None` | 312 | 479 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_SnapReceive` | 115 | 115 | 1 | inferred_complete_timeline |
| `Action_None` | 116 | 140 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 141 | 144 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–2
- **Visible Samples:** 3

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 103 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 145 | 59 | inferred_complete_timeline |
| `Action_None` | 181 | 368 | 188 | inferred_complete_timeline |
| `Action_None` | 421 | 422 | 2 | inferred_complete_timeline |
| `Action_None` | 425 | 426 | 2 | inferred_complete_timeline |
| `Action_None` | 428 | 479 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 224 | 138 | inferred_complete_timeline |
| `Action_None` | 232 | 235 | 4 | inferred_complete_timeline |
| `Action_None` | 247 | 249 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 142 | 56 | inferred_complete_timeline |
| `Action_None` | 145 | 153 | 9 | inferred_complete_timeline |
| `Action_None` | 155 | 158 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 125 | 39 | inferred_complete_timeline |
| `Action_None` | 127 | 139 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–471
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 153 | 67 | inferred_complete_timeline |
| `Action_None` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_None` | 162 | 177 | 16 | inferred_complete_timeline |
| `Action_None` | 181 | 211 | 31 | inferred_complete_timeline |
| `Action_None` | 228 | 306 | 79 | inferred_complete_timeline |
| `Action_None` | 313 | 323 | 11 | inferred_complete_timeline |
| `Action_None` | 325 | 395 | 71 | inferred_complete_timeline |
| `Action_None` | 399 | 436 | 38 | inferred_complete_timeline |
| `Action_None` | 439 | 456 | 18 | inferred_complete_timeline |
| `Action_None` | 470 | 471 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 145 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 186 | 100 | inferred_complete_timeline |
| `Action_None` | 191 | 194 | 4 | inferred_complete_timeline |
| `Action_None` | 196 | 201 | 6 | inferred_complete_timeline |
| `Action_None` | 206 | 295 | 90 | inferred_complete_timeline |
| `Action_None` | 297 | 376 | 80 | inferred_complete_timeline |
| `Action_None` | 390 | 394 | 5 | inferred_complete_timeline |
| `Action_None` | 397 | 398 | 2 | inferred_complete_timeline |
| `Action_None` | 401 | 459 | 59 | inferred_complete_timeline |
| `Action_None` | 461 | 479 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Returner — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–451
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 98 | 12 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 192 | 71 | inferred_complete_timeline |
| `Action_None` | 194 | 215 | 22 | inferred_complete_timeline |
| `Action_None` | 218 | 380 | 163 | inferred_complete_timeline |
| `Action_None` | 399 | 423 | 25 | inferred_complete_timeline |
| `Action_None` | 425 | 431 | 7 | inferred_complete_timeline |
| `Action_None` | 434 | 446 | 13 | inferred_complete_timeline |
| `Action_None` | 450 | 451 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–467
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 140 | 54 | inferred_complete_timeline |
| `Action_None` | 142 | 232 | 91 | inferred_complete_timeline |
| `Action_None` | 236 | 352 | 117 | inferred_complete_timeline |
| `Action_None` | 358 | 378 | 21 | inferred_complete_timeline |
| `Action_None` | 382 | 467 | 86 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `20` | Position_Unknown | Team_Unknown | 95–205 | 111 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 102–108 | 7 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 109–407 | 272 | 6 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 114–479 | 338 | 7 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 115–135 | 21 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 117–150 | 34 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 151–479 | 260 | 17 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 151–428 | 237 | 9 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 159–319 | 143 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 165–201 | 21 | 6 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 197–477 | 180 | 10 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 200–271 | 48 | 8 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 212–414 | 189 | 3 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 217–479 | 223 | 7 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 225–479 | 237 | 6 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 229–344 | 116 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 233–311 | 76 | 2 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 247–252 | 6 | 1 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 267–428 | 150 | 5 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 272–476 | 170 | 6 | Undefined position; Undefined team |
| `38` | `62` | Position_Unknown | Team_Unknown | 326–479 | 154 | 1 | Undefined position; Undefined team |
| `39` | `63` | Position_Unknown | Team_Unknown | 329–352 | 7 | 2 | Undefined position; Undefined team |
| `40` | `66` | Position_Unknown | Team_Unknown | 350–351 | 2 | 1 | Undefined position; Undefined team |
| `41` | `69` | Position_Unknown | Team_Unknown | 360–386 | 21 | 3 | Undefined position; Undefined team |
| `42` | `70` | Position_Unknown | Team_Unknown | 371–479 | 68 | 10 | Undefined position; Undefined team |
| `43` | `71` | Position_Unknown | Team_Unknown | 372–385 | 14 | 1 | Undefined position; Undefined team |
| `44` | `73` | Position_Unknown | Team_Unknown | 378–441 | 64 | 1 | Undefined position; Undefined team |
| `45` | `74` | Position_Unknown | Team_Unknown | 383–479 | 87 | 6 | Undefined position; Undefined team |
| `46` | `75` | Position_Unknown | Team_Unknown | 386–395 | 10 | 1 | Undefined position; Undefined team |
| `47` | `77` | Position_Unknown | Team_Unknown | 389–399 | 11 | 1 | Undefined position; Undefined team |
| `48` | `78` | Position_Unknown | Team_Unknown | 414–479 | 66 | 1 | Undefined position; Undefined team |
| `49` | `79` | Position_Unknown | Team_Unknown | 431–474 | 34 | 4 | Undefined position; Undefined team |
| `50` | `80` | Position_Unknown | Team_Unknown | 432–479 | 46 | 3 | Undefined position; Undefined team |
| `51` | `81` | Position_Unknown | Team_Unknown | 432–479 | 37 | 4 | Undefined position; Undefined team |
| `52` | `82` | Position_Unknown | Team_Unknown | 440–441 | 2 | 1 | Undefined position; Undefined team |
| `53` | `83` | Position_Unknown | Team_Unknown | 442–479 | 35 | 2 | Undefined position; Undefined team |
| `54` | `86` | Position_Unknown | Team_Unknown | 448–468 | 16 | 3 | Undefined position; Undefined team |
| `55` | `87` | Position_Unknown | Team_Unknown | 451–475 | 13 | 3 | Undefined position; Undefined team |
| `56` | `90` | Position_Unknown | Team_Unknown | 451–476 | 18 | 4 | Undefined position; Undefined team |
| `57` | `91` | Position_Unknown | Team_Unknown | 458–479 | 14 | 3 | Undefined position; Undefined team |
| `58` | `92` | Position_Unknown | Team_Unknown | 472–475 | 4 | 1 | Undefined position; Undefined team |
| `59` | `93` | Position_Unknown | Team_Unknown | 474–479 | 5 | 2 | Undefined position; Undefined team |
| `60` | `95` | Position_Unknown | Team_Unknown | 477–479 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Punt_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Gunner` position mapped to `offense` team
- ⚠️ 43 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 43 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 86 |
| Missing visible bounding boxes during action | 220 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [87-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-232] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-352] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-378] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-467] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-145] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-103] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-103] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-145] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-368] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-122] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-335] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-368] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-377] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-445] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-48] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [141-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-177] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-211] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-306] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-323] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-395] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-436] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-456] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-224] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-133] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-378] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-383] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-395] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-186] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-295] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-376] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-394] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-459] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-479] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-111] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-309] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 141, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [141-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-370] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-98] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-192] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-215] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-380] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-423] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-431] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-446] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-451] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-228] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-343] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-359] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-364] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-394] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-191] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-400] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-405] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-479] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-273] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-292] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-344] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-352] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-375] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-395] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-404] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-416] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-427] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-436] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-446] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-457] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-477] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-256] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-366] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-383] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-395] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-419] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-428] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-319] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-229] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-249] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-305] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-354] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-366] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-419] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-434] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-440] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-455] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-477] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-221] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-262] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-392] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-408] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-414] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-223] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-320] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-401] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-408] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-423] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-446] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-256] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-344] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-387] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-451] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-465] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-344] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-303] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-311] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-252] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-316] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-364] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-378] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-391] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-428] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-476] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-331] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-352] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-365] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-375] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-386] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-375] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-393] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-422] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-434] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-443] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-452] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-473] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-385] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-441] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-395] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-408] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-446] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-470] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-395] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-399] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-438] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-462] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-471] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-446] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-470] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-439] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-458] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-467] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-441] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-456] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-451] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-465] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-468] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-455] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-475] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-453] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-456] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-464] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-476] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-461] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-467] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-475] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-476] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-479] for track '60' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>