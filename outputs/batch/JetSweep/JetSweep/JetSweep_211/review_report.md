# Play-Annotation-Generator Annotation Review — JetSweep_211

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_211`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 599
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 138
- **Validation Warnings:** 155
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 111
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR3 | offense | `4` | `3` |
| ✅ EXACT | `Action_BallSnap` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `22` | `Group` | 0 | START | 0 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 155 |
| ✅ EXACT | `Action_JetMotion` | WR3 | `4` | `3` | 109 | START | 109 | 177 |
| ✅ EXACT | `Action_BallSnap` | LG | `21` | `20` | 155 | START | 155 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `22` | `21` | 156 | START | 156 | 232 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 156 | START | 156 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 156 | START | 156 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `19` | 156 | START | 156 | 206 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `20` | 156 | START | 156 | 203 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `7` | 156 | START | 156 | 241 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 167 | END | 155 | 167 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 173 | START | 173 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `4` | `3` | 178 | START | 178 | 238 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 241 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_SnapReceive` | 155 | 167 | 13 | inferred_complete_timeline |
| `Action_None` | 168 | 172 | 5 | inferred_complete_timeline |
| `Action_Toss` | 173 | 177 | 5 | inferred_complete_timeline |
| `Action_None` | 178 | 271 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–331
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 331 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–360
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 360 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–302
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 302 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–436
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_JetMotion` | 109 | 177 | 69 | inferred_complete_timeline |
| `Action_BallCarry` | 178 | 238 | 61 | inferred_complete_timeline |
| `Action_BallCarry` | 242 | 436 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_LeadBlock` | 156 | 232 | 77 | inferred_complete_timeline |
| `Action_LeadBlock` | 234 | 238 | 5 | inferred_complete_timeline |
| `Action_LeadBlock` | 240 | 241 | 2 | inferred_complete_timeline |
| `Action_None` | 242 | 299 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 241 | 86 | inferred_complete_timeline |
| `Action_None` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_None` | 245 | 274 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_BallSnap` | 155 | 155 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 203 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 174 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 190 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 202 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 223 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 226 | 238 | 13 | inferred_complete_timeline |
| `Action_None` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 254 | 5 | inferred_complete_timeline |
| `Action_None` | 256 | 599 | 344 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 206 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 212 | 238 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 240 | 241 | 2 | inferred_complete_timeline |
| `Action_None` | 242 | 280 | 39 | inferred_complete_timeline |
| `Action_None` | 283 | 297 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–301
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 177 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 185 | 194 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 206 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 241 | 32 | inferred_complete_timeline |
| `Action_None` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 301 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–422
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 206 | 52 | inferred_complete_timeline |
| `Action_None` | 215 | 240 | 26 | inferred_complete_timeline |
| `Action_None` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_None` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_None` | 252 | 254 | 3 | inferred_complete_timeline |
| `Action_None` | 256 | 330 | 75 | inferred_complete_timeline |
| `Action_None` | 338 | 357 | 20 | inferred_complete_timeline |
| `Action_None` | 359 | 365 | 7 | inferred_complete_timeline |
| `Action_None` | 368 | 422 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–330
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 221 | 67 | inferred_complete_timeline |
| `Action_None` | 223 | 238 | 16 | inferred_complete_timeline |
| `Action_None` | 240 | 243 | 4 | inferred_complete_timeline |
| `Action_None` | 250 | 327 | 78 | inferred_complete_timeline |
| `Action_None` | 329 | 330 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 206 | 52 | inferred_complete_timeline |
| `Action_None` | 213 | 289 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–305
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 206 | 52 | inferred_complete_timeline |
| `Action_None` | 211 | 238 | 28 | inferred_complete_timeline |
| `Action_None` | 241 | 243 | 3 | inferred_complete_timeline |
| `Action_None` | 250 | 305 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–441
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 238 | 84 | inferred_complete_timeline |
| `Action_None` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_None` | 252 | 254 | 3 | inferred_complete_timeline |
| `Action_None` | 256 | 441 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–357
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 243 | 89 | inferred_complete_timeline |
| `Action_None` | 245 | 357 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–364
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 364 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–378
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 378 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 329 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 279 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 326 | 172 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–3 | 4 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 75–156 | 82 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 193–292 | 81 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 284–599 | 296 | 6 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 287–293 | 7 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 336–339 | 4 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 361–425 | 63 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 389–428 | 40 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 390–410 | 10 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 392–542 | 133 | 8 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 396–406 | 11 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 398–498 | 101 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 404–437 | 25 | 5 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 405–433 | 29 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 411–415 | 5 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 418–438 | 21 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 447–559 | 113 | 1 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 469–515 | 47 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 478–512 | 35 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 482–599 | 118 | 1 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 485–528 | 39 | 2 | Undefined position; Undefined team |
| `43` | `63` | Position_Unknown | Team_Unknown | 519–597 | 79 | 1 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 533–548 | 16 | 1 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 547–552 | 6 | 1 | Undefined position; Undefined team |
| `46` | `68` | Position_Unknown | Team_Unknown | 587–590 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (9 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 104 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [155-302] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-360] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-206] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-240] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-330] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-357] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-365] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-422] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [178-238] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [242-436] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-206] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-238] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-305] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-238] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-441] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-364] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-274] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-289] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-331] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-271] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-243] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-357] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-378] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-279] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-326] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-221] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-238] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-327] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-329] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [187-190] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-223] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [226-238] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [185-194] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [196-206] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-301] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-206] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [212-238] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-280] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-297] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-203] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [156-232] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [234-238] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-292] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-391] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-415] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-561] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-585] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-599] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-293] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-339] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-408] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-425] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-428] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-397] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-410] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-395] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-413] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-421] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-443] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-454] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-459] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-467] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-542] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-406] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-498] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-406] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-413] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-421] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-432] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-437] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-433] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-415] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-438] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-559] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-515] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-512] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-512] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-528] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-597] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-548] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-552] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-590] for track '46' has 1 frames without a visible bounding box.
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

</details>