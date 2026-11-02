# Play-Annotation-Generator Annotation Review — JetSweep_147

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_147`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 150
- **Validation Warnings:** 171
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 122
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR4 | offense | `8` | `7` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Toss` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR4 | offense | `8` | `7` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `18` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `8` | `Group` | 0 | START | 0 | 34 |
| ✅ EXACT | `Action_JetMotion` | WR4 | `8` | `7` | 35 | START | 35 | 89 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 64 | START | 64 | 78 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `13` | 66 | START | 79 | 140 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `16` | `15` | 66 | START | 66 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `19` | `18` | 66 | START | 66 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 66 | START | 66 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 66 | START | 66 | 78 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 78 | END | 64 | 78 |
| ✅ EXACT | `Action_Toss` | QB | `4` | `3` | 81 | START | 81 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR4 | `8` | `7` | 90 | START | 90 | 239 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `16` | `15` | 99 | START | 99 | 140 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 140 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–307
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_SnapReceive` | 64 | 78 | 15 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_Toss` | 81 | 89 | 9 | inferred_complete_timeline |
| `Action_None` | 90 | 233 | 144 | inferred_complete_timeline |
| `Action_None` | 235 | 237 | 3 | inferred_complete_timeline |
| `Action_None` | 243 | 250 | 8 | inferred_complete_timeline |
| `Action_None` | 260 | 266 | 7 | inferred_complete_timeline |
| `Action_None` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_None` | 272 | 275 | 4 | inferred_complete_timeline |
| `Action_None` | 277 | 307 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 164 | 101 | inferred_complete_timeline |
| `Action_None` | 176 | 180 | 5 | inferred_complete_timeline |
| `Action_None` | 185 | 193 | 9 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–371
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 371 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 196 | 133 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_None` | 215 | 242 | 28 | inferred_complete_timeline |
| `Action_None` | 245 | 256 | 12 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_None` | 287 | 293 | 7 | inferred_complete_timeline |
| `Action_None` | 297 | 345 | 49 | inferred_complete_timeline |
| `Action_None` | 347 | 349 | 3 | inferred_complete_timeline |
| `Action_None` | 351 | 371 | 21 | inferred_complete_timeline |
| `Action_None` | 409 | 419 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_JetMotion` | 35 | 89 | 55 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 239 | 150 | inferred_complete_timeline |
| `Action_BallCarry` | 241 | 247 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–371
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 371 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 98 | 33 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 99 | 140 | 42 | inferred_complete_timeline |
| `Action_None` | 141 | 193 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 78 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 124 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–371
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_BallSnap` | 64 | 78 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 140 | 62 | inferred_complete_timeline |
| `Action_None` | 141 | 371 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–307
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 140 | 75 | inferred_complete_timeline |
| `Action_None` | 141 | 205 | 65 | inferred_complete_timeline |
| `Action_None` | 209 | 251 | 43 | inferred_complete_timeline |
| `Action_None` | 254 | 307 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 93 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 135 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 164 | 101 | inferred_complete_timeline |
| `Action_None` | 168 | 371 | 204 | inferred_complete_timeline |
| `Action_None` | 409 | 419 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–371
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 265 | 202 | inferred_complete_timeline |
| `Action_None` | 269 | 279 | 11 | inferred_complete_timeline |
| `Action_None` | 284 | 302 | 19 | inferred_complete_timeline |
| `Action_None` | 304 | 330 | 27 | inferred_complete_timeline |
| `Action_None` | 332 | 333 | 2 | inferred_complete_timeline |
| `Action_None` | 339 | 361 | 23 | inferred_complete_timeline |
| `Action_None` | 364 | 371 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–371
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 90 | 27 | inferred_complete_timeline |
| `Action_None` | 95 | 256 | 162 | inferred_complete_timeline |
| `Action_None` | 258 | 356 | 99 | inferred_complete_timeline |
| `Action_None` | 367 | 371 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 261 | 198 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 233 | 170 | inferred_complete_timeline |
| `Action_None` | 236 | 240 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 247 | 184 | inferred_complete_timeline |
| `Action_None` | 254 | 371 | 118 | inferred_complete_timeline |
| `Action_None` | 409 | 419 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–371
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 371 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 180 | 117 | inferred_complete_timeline |
| `Action_None` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 284 | 98 | inferred_complete_timeline |
| `Action_None` | 288 | 295 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–354
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 354 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 255 | 192 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–268 | 250 | 8 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 147–371 | 225 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 165–320 | 156 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 209–371 | 157 | 3 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 213–291 | 79 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 242–298 | 22 | 5 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 253–295 | 22 | 5 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 262–263 | 2 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 294–318 | 25 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 308–309 | 2 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 308–371 | 62 | 3 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 310–326 | 17 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 313–371 | 58 | 2 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 321–371 | 8 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 321–323 | 3 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 333–352 | 9 | 2 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 342–371 | 29 | 2 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 346–371 | 26 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 353–371 | 19 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 365–419 | 16 | 3 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 410–419 | 10 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 410–419 | 10 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 410–419 | 10 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 410–419 | 10 | 1 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 410–419 | 10 | 1 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 410–419 | 10 | 1 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 410–419 | 10 | 1 | Undefined position; Undefined team |
| `48` | `62` | Position_Unknown | Team_Unknown | 410–419 | 10 | 1 | Undefined position; Undefined team |
| `49` | `63` | Position_Unknown | Team_Unknown | 410–419 | 10 | 1 | Undefined position; Undefined team |
| `50` | `64` | Position_Unknown | Team_Unknown | 410–419 | 10 | 1 | Undefined position; Undefined team |
| `51` | `65` | Position_Unknown | Team_Unknown | 410–419 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 66 != Inferred start 79
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 107 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [64–78], lower_priority='Action_ZoneBlock' annotated_start=66, effective_Action_ZoneBlock_start=79.
- ⚠️ Action 'Action_None' range [64-196] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-242] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-256] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-293] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-345] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-371] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-371] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-371] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-233] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-250] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-266] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-307] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-164] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-193] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-371] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-261] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [241-247] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-247] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-371] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-90] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-256] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-356] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-371] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-284] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-295] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-233] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-178] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-248] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-371] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-265] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-279] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-302] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-330] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-361] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-371] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-193] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-255] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-371] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-251] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-307] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-354] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-93] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-124] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-371] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-320] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-230] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-281] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-371] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-291] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-252] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-272] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-258] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-295] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-318] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-316] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-327] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-371] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-326] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-371] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-371] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-339] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-345] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-371] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-371] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-371] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-371] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-412] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>