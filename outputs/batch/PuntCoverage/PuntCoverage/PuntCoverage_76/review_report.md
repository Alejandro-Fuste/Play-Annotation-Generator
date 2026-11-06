# Play-Annotation-Generator Annotation Review — PuntCoverage_76

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_76`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 449
- **Player Tracks:** 63
- **Ball Tracks:** 0
- **Action Segments:** 274
- **Validation Warnings:** 352
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 232
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `8` | `Group` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `20` | `20` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `26` | `26` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `26` | `26` |
| ❌ MISSING SEGMENT | `Action_Tackle` | Position_Unknown | Team_Unknown | `62` | `46` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `10` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `13` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `14` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `19` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `20` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `5` | `Group` | 0 | START | 0 | 381 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `6` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `7` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `8` | `Group` | 0 | START | 0 | 80 |
| ✅ EXACT | `Action_PuntBall` | Punter | `20` | `20` | 87 | START | 87 | 104 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `26` | `26` | 214 | START | 214 | 232 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `26` | `26` | 258 | START | 258 | 329 |
| ❌ MISSING SEGMENT | `Action_Tackle` | Position_Unknown | `62` | `46` | 420 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 130 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 149 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 156 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 163 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 179 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–360
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 172 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 179 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 264 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 353 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 360 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 381 | 382 | inferred_complete_timeline |
| `Action_PreSnap` | 383 | 391 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 405 | 449 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–442
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 368 | 237 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 378 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 392 | 400 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 433 | 434 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 438 | 442 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 86 | 16 | inferred_complete_timeline |
| `Action_PuntBall` | 87 | 104 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 90 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 96 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 102 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 130 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 172 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 143 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 154 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 164 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 175 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 234 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 449 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 128 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 140 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 146 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 349 | 202 | inferred_complete_timeline |
| `Action_PreSnap` | 351 | 448 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–308
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 226 | 227 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 308 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 424 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 427 | 428 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 432 | 442 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 446 | 449 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–381
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 225 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 303 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 316 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 329 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 336 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 364 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 368 | 370 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 379 | 381 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 123 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–337
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 316 | 317 | inferred_complete_timeline |
| `Action_PreSnap` | 319 | 320 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 337 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 236 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 292 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 330 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 406 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 408 | 414 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 438 | 449 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 304 | 186 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–45 | 46 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 51–371 | 241 | 15 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 54–55 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 84–292 | 147 | 6 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 112–449 | 324 | 7 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 126–167 | 23 | 4 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 127–373 | 230 | 8 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 137–235 | 38 | 4 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 160–449 | 258 | 11 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 180–182 | 3 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 183–294 | 105 | 3 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 183–269 | 71 | 5 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 209–314 | 18 | 5 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 210–212 | 3 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 233–449 | 165 | 11 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 248–449 | 194 | 3 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 249–284 | 29 | 3 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 253–312 | 36 | 6 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 254–374 | 118 | 2 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 257–265 | 9 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 259–260 | 2 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 269–447 | 139 | 6 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 281–297 | 9 | 2 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 285–292 | 7 | 2 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 295–386 | 92 | 1 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 298–449 | 93 | 11 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 298–412 | 100 | 4 | Undefined position; Undefined team |
| `47` | `64` | Position_Unknown | Team_Unknown | 312–386 | 60 | 5 | Undefined position; Undefined team |
| `48` | `66` | Position_Unknown | Team_Unknown | 315–448 | 118 | 7 | Undefined position; Undefined team |
| `49` | `67` | Position_Unknown | Team_Unknown | 316–448 | 86 | 13 | Undefined position; Undefined team |
| `50` | `69` | Position_Unknown | Team_Unknown | 328–445 | 89 | 5 | Undefined position; Undefined team |
| `51` | `74` | Position_Unknown | Team_Unknown | 336–431 | 48 | 6 | Undefined position; Undefined team |
| `52` | `75` | Position_Unknown | Team_Unknown | 337–353 | 6 | 2 | Undefined position; Undefined team |
| `53` | `76` | Position_Unknown | Team_Unknown | 350–449 | 57 | 7 | Undefined position; Undefined team |
| `54` | `77` | Position_Unknown | Team_Unknown | 367–368 | 2 | 1 | Undefined position; Undefined team |
| `55` | `78` | Position_Unknown | Team_Unknown | 368–449 | 68 | 4 | Undefined position; Undefined team |
| `56` | `79` | Position_Unknown | Team_Unknown | 389–449 | 43 | 5 | Undefined position; Undefined team |
| `57` | `81` | Position_Unknown | Team_Unknown | 395–431 | 34 | 3 | Undefined position; Undefined team |
| `58` | `84` | Position_Unknown | Team_Unknown | 399–415 | 16 | 2 | Undefined position; Undefined team |
| `59` | `86` | Position_Unknown | Team_Unknown | 404–449 | 26 | 3 | Undefined position; Undefined team |
| `60` | `87` | Position_Unknown | Team_Unknown | 415–449 | 34 | 2 | Undefined position; Undefined team |
| `61` | `88` | Position_Unknown | Team_Unknown | 434–449 | 15 | 2 | Undefined position; Undefined team |
| `62` | `89` | Position_Unknown | Team_Unknown | 434–439 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `26` (5 segments found)
- ❌ Missing segment for action `Action_Tackle` on target `62` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Punter` position mapped to `offense` team
- ⚠️ 43 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 43 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 86 |
| Missing visible bounding boxes during action | 263 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 153: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Segment 'Action_Tackle' for track '46' has invalid range: start=420, end=412. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-186] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-226] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-308] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-140] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-146] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-349] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-448] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-316] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-320] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-337] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-303] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-316] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-336] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-364] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-370] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-381] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-381] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-391] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-368] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-378] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-400] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-434] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-442] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-90] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-96] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-130] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-172] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-220] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-236] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-292] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-330] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-406] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-414] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-449] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-149] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-156] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-179] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-304] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-143] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-154] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-164] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-172] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-179] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-186] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-209] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-264] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-353] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-360] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-175] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-449] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-259] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-424] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-428] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-442] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-130] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [87-104] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-53] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-165] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-177] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-189] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-213] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-219] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-228] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-255] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-275] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-314] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-341] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-365] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-371] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-88] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-203] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-208] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-276] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-279] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-292] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-187] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-206] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-213] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-220] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-228] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-449] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-136] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-155] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-167] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [258-329] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [331-349] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [352-353] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [366-369] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [372-373] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-167] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-231] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-163] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-179] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-219] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-223] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-263] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-267] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-396] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-404] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-438] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-182] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-215] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-284] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-294] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-190] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-209] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-225] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-216] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-220] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-253] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-266] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-212] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-263] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-336] for track '34' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-359] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-382] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-393] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-399] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-403] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-423] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-435] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-255] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-427] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-449] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-252] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-267] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-284] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-256] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-265] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-281] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-296] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-305] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-312] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-330] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-374] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-265] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-260] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-276] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-372] for track '41' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-393] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-414] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-433] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-447] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-287] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-289] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-292] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-386] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-306] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-337] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-345] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-349] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-365] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-382] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-396] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-401] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-438] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-444] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-390] for track '46' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-393] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-401] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-412] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-330] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-346] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-349] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-370] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-386] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-322] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-326] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-336] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-349] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-354] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-437] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-448] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-317] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-355] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-360] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-363] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-370] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-376] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-385] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-394] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-397] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-404] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-426] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-441] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-448] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-336] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-347] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-414] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-438] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-445] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-337] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-340] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-349] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-364] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-376] for track '51' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-431] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-340] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-353] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-353] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-362] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-369] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-398] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-420] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-423] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-449] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-368] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-370] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-383] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-393] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-393] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-411] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-423] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-435] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-422] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-428] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-431] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-412] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-415] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-415] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-433] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-449] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-418] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-443] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [445-449] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-439] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>