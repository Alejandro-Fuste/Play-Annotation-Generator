# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_35

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_35`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 479
- **Player Tracks:** 88
- **Ball Tracks:** 0
- **Action Segments:** 270
- **Validation Warnings:** 394
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 259
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_LongSnap` | Position_Unknown | Team_Unknown | `20` | `17` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `0` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `10` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `3` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `4` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `5` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `6` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `7` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `8` | `Group` | 0 | START | 0 | 92 |
| ⚠️ START CHANGED | `Action_LongSnap` | Position_Unknown | `20` | `17` | 93 | START | 99 | 103 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `6` | `6` | 120 | END | 120 | 120 |
| ✅ EXACT | `Action_PuntBall` | Punter | `6` | `6` | 143 | START | 143 | 153 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 110 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 316 | 224 | inferred_complete_timeline |
| `Action_None` | 318 | 333 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 127 | 35 | inferred_complete_timeline |
| `Action_None` | 129 | 146 | 18 | inferred_complete_timeline |
| `Action_None` | 172 | 177 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–420
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 135 | 43 | inferred_complete_timeline |
| `Action_None` | 192 | 383 | 192 | inferred_complete_timeline |
| `Action_None` | 390 | 403 | 14 | inferred_complete_timeline |
| `Action_None` | 412 | 420 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 134 | 42 | inferred_complete_timeline |
| `Action_None` | 142 | 144 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_SnapReceive` | 120 | 120 | 1 | inferred_complete_timeline |
| `Action_None` | 121 | 142 | 22 | inferred_complete_timeline |
| `Action_PuntBall` | 143 | 153 | 11 | inferred_complete_timeline |
| `Action_None` | 154 | 165 | 12 | inferred_complete_timeline |
| `Action_None` | 215 | 233 | 19 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |
| `Action_None` | 245 | 267 | 23 | inferred_complete_timeline |
| `Action_None` | 271 | 281 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 207 | 115 | inferred_complete_timeline |
| `Action_None` | 211 | 275 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 252 | 160 | inferred_complete_timeline |
| `Action_None` | 255 | 349 | 95 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 111 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 472

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 267 | 175 | inferred_complete_timeline |
| `Action_None` | 275 | 469 | 195 | inferred_complete_timeline |
| `Action_None` | 471 | 479 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 165 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–343
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 308 | 216 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_None` | 325 | 327 | 3 | inferred_complete_timeline |
| `Action_None` | 329 | 343 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–437
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 145 | 53 | inferred_complete_timeline |
| `Action_None` | 149 | 162 | 14 | inferred_complete_timeline |
| `Action_None` | 165 | 282 | 118 | inferred_complete_timeline |
| `Action_None` | 284 | 285 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 293 | 6 | inferred_complete_timeline |
| `Action_None` | 298 | 301 | 4 | inferred_complete_timeline |
| `Action_None` | 307 | 377 | 71 | inferred_complete_timeline |
| `Action_None` | 379 | 380 | 2 | inferred_complete_timeline |
| `Action_None` | 382 | 437 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 8–248 | 231 | 6 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 21–169 | 74 | 4 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 34–479 | 425 | 13 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 64–68 | 5 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 99–103 | 5 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 101–144 | 36 | 3 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 107–118 | 8 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 109–111 | 3 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 115–157 | 15 | 4 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 124–125 | 2 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 126–440 | 275 | 11 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 126–143 | 14 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 131–479 | 344 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 131–133 | 3 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 133–150 | 18 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 157–354 | 190 | 6 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 166–460 | 269 | 6 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 167–174 | 8 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 172–178 | 5 | 2 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 176–479 | 301 | 3 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 178–338 | 156 | 4 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 180–479 | 273 | 9 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 193–384 | 192 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 201–479 | 260 | 2 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 205–479 | 244 | 12 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 205–479 | 269 | 3 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 230–232 | 3 | 1 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 235–308 | 74 | 1 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 242–243 | 2 | 1 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 245–246 | 2 | 1 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 247–248 | 2 | 1 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 261–275 | 13 | 2 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 265–316 | 28 | 3 | Undefined position; Undefined team |
| `47` | `67` | Position_Unknown | Team_Unknown | 267–317 | 46 | 3 | Undefined position; Undefined team |
| `48` | `68` | Position_Unknown | Team_Unknown | 269–469 | 140 | 22 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 278–479 | 202 | 1 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 288–305 | 5 | 2 | Undefined position; Undefined team |
| `51` | `73` | Position_Unknown | Team_Unknown | 293–345 | 17 | 3 | Undefined position; Undefined team |
| `52` | `74` | Position_Unknown | Team_Unknown | 307–375 | 55 | 5 | Undefined position; Undefined team |
| `53` | `75` | Position_Unknown | Team_Unknown | 316–324 | 6 | 2 | Undefined position; Undefined team |
| `54` | `76` | Position_Unknown | Team_Unknown | 326–329 | 4 | 1 | Undefined position; Undefined team |
| `55` | `79` | Position_Unknown | Team_Unknown | 328–331 | 4 | 1 | Undefined position; Undefined team |
| `56` | `84` | Position_Unknown | Team_Unknown | 332–479 | 135 | 9 | Undefined position; Undefined team |
| `57` | `86` | Position_Unknown | Team_Unknown | 333–334 | 2 | 1 | Undefined position; Undefined team |
| `58` | `87` | Position_Unknown | Team_Unknown | 335–479 | 144 | 2 | Undefined position; Undefined team |
| `59` | `89` | Position_Unknown | Team_Unknown | 337–398 | 62 | 1 | Undefined position; Undefined team |
| `60` | `90` | Position_Unknown | Team_Unknown | 341–354 | 4 | 2 | Undefined position; Undefined team |
| `61` | `91` | Position_Unknown | Team_Unknown | 352–479 | 125 | 2 | Undefined position; Undefined team |
| `62` | `92` | Position_Unknown | Team_Unknown | 365–399 | 26 | 2 | Undefined position; Undefined team |
| `63` | `96` | Position_Unknown | Team_Unknown | 373–395 | 10 | 3 | Undefined position; Undefined team |
| `64` | `97` | Position_Unknown | Team_Unknown | 373–386 | 14 | 1 | Undefined position; Undefined team |
| `65` | `98` | Position_Unknown | Team_Unknown | 385–391 | 7 | 1 | Undefined position; Undefined team |
| `66` | `102` | Position_Unknown | Team_Unknown | 400–475 | 46 | 4 | Undefined position; Undefined team |
| `67` | `104` | Position_Unknown | Team_Unknown | 410–457 | 48 | 1 | Undefined position; Undefined team |
| `68` | `109` | Position_Unknown | Team_Unknown | 416–420 | 5 | 1 | Undefined position; Undefined team |
| `69` | `113` | Position_Unknown | Team_Unknown | 421–479 | 56 | 3 | Undefined position; Undefined team |
| `70` | `114` | Position_Unknown | Team_Unknown | 421–479 | 55 | 3 | Undefined position; Undefined team |
| `71` | `116` | Position_Unknown | Team_Unknown | 430–440 | 10 | 2 | Undefined position; Undefined team |
| `72` | `118` | Position_Unknown | Team_Unknown | 435–436 | 2 | 1 | Undefined position; Undefined team |
| `73` | `119` | Position_Unknown | Team_Unknown | 437–479 | 43 | 1 | Undefined position; Undefined team |
| `74` | `122` | Position_Unknown | Team_Unknown | 440–479 | 34 | 3 | Undefined position; Undefined team |
| `75` | `124` | Position_Unknown | Team_Unknown | 444–445 | 2 | 1 | Undefined position; Undefined team |
| `76` | `125` | Position_Unknown | Team_Unknown | 446–447 | 2 | 1 | Undefined position; Undefined team |
| `77` | `126` | Position_Unknown | Team_Unknown | 446–447 | 2 | 1 | Undefined position; Undefined team |
| `78` | `129` | Position_Unknown | Team_Unknown | 450–479 | 27 | 3 | Undefined position; Undefined team |
| `79` | `130` | Position_Unknown | Team_Unknown | 450–469 | 20 | 1 | Undefined position; Undefined team |
| `80` | `132` | Position_Unknown | Team_Unknown | 452–460 | 4 | 2 | Undefined position; Undefined team |
| `81` | `133` | Position_Unknown | Team_Unknown | 456–457 | 2 | 1 | Undefined position; Undefined team |
| `82` | `134` | Position_Unknown | Team_Unknown | 463–466 | 4 | 1 | Undefined position; Undefined team |
| `83` | `135` | Position_Unknown | Team_Unknown | 463–479 | 16 | 2 | Undefined position; Undefined team |
| `84` | `137` | Position_Unknown | Team_Unknown | 467–479 | 13 | 1 | Undefined position; Undefined team |
| `85` | `138` | Position_Unknown | Team_Unknown | 470–473 | 4 | 1 | Undefined position; Undefined team |
| `86` | `139` | Position_Unknown | Team_Unknown | 470–471 | 2 | 1 | Undefined position; Undefined team |
| `87` | `140` | Position_Unknown | Team_Unknown | 472–473 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_LongSnap` for actor_track_id `20` (Position_Unknown): Annotated start 93 != Inferred start 99

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 75 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 75 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 150 |
| Missing visible bounding boxes during action | 241 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [93-127] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-146] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-308] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-343] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-145] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-282] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-293] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-377] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-437] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-135] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-383] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-403] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-420] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-316] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-333] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-252] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-349] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-233] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-267] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-281] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-165] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-207] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-275] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-267] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-469] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-236] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-68] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-81] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-135] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-56] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-92] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-143] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-178] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-253] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-271] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-279] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-406] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-459] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-68] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [99-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-167] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-237] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-303] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-422] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-440] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-135] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-264] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-150] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-221] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-230] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-244] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-348] for track '29' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-354] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-274] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-296] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-310] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-425] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-438] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-460] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-174] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-272] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-382] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-212] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-219] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-338] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-204] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-249] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-326] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-368] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-417] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-424] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-384] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-340] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-479] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-227] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-283] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-301] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-319] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-331] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-479] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-308] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-307] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-316] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-278] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-287] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-317] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-285] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-313] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-347] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-358] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-377] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-385] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-401] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-410] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-438] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-447] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-469] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-479] for track '49' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-298] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-345] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-314] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-322] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-337] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-344] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-375] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-331] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-376] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-387] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-464] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-479] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-377] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-479] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-398] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-398] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-386] for track '62' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-399] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-377] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-386] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-391] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-426] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-445] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-454] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-475] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-457] for track '67' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-420] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-426] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-431] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-456] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-432] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-440] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-447] for track '74' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-451] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-479] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-454] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-462] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-469] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-466] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-474] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-479] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-473] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '80' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '80' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '81' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '81' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '82' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '82' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '83' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '83' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '84' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '84' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '85' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '85' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '86' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '86' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '87' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '87' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>