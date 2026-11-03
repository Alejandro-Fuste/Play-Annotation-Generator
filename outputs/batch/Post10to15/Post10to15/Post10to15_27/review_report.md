# Play-Annotation-Generator Annotation Review — Post10to15_27

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_27`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 54
- **Ball Tracks:** 0
- **Action Segments:** 174
- **Validation Warnings:** 201
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 155
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | DT | defense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 26 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 27 | START | 27 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `15` | `15` | 30 | START | 30 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `17` | `17` | 30 | START | 30 | 389 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 30 | START | 43 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 30 | START | 30 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 30 | START | 30 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | DT | `0` | `0` | 42 | START | 42 | 303 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 42 | END | 27 | 42 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 87 | START | 87 | 97 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 42 | 16 | inferred_complete_timeline |
| `Action_None` | 43 | 86 | 44 | inferred_complete_timeline |
| `Action_ThrowPass` | 87 | 97 | 11 | inferred_complete_timeline |
| `Action_None` | 98 | 314 | 217 | inferred_complete_timeline |
| `Action_None` | 330 | 419 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 55 | 29 | inferred_complete_timeline |
| `Action_None` | 58 | 419 | 362 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 324 | 298 | inferred_complete_timeline |
| `Action_None` | 326 | 392 | 67 | inferred_complete_timeline |
| `Action_None` | 401 | 417 | 17 | inferred_complete_timeline |
| `Action_None` | 419 | 419 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 338 | 312 | inferred_complete_timeline |
| `Action_None` | 340 | 341 | 2 | inferred_complete_timeline |
| `Action_None` | 343 | 419 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 201 | 175 | inferred_complete_timeline |
| `Action_None` | 205 | 276 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 59 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 320 | 258 | inferred_complete_timeline |
| `Action_PassBlock` | 322 | 393 | 72 | inferred_complete_timeline |
| `Action_PassBlock` | 395 | 419 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 57 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 73 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 144 | 145 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 27 | 42 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 88 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 99 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 259 | 159 | inferred_complete_timeline |
| `Action_PassBlock` | 261 | 419 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 49 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 328 | 273 | inferred_complete_timeline |
| `Action_PassBlock` | 332 | 367 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 370 | 371 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 374 | 419 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 389 | 360 | inferred_complete_timeline |
| `Action_PassBlock` | 391 | 419 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 210 | 184 | inferred_complete_timeline |
| `Action_None` | 240 | 243 | 4 | inferred_complete_timeline |
| `Action_None` | 246 | 419 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 200 | 174 | inferred_complete_timeline |
| `Action_None` | 208 | 419 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–393
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_RunPostRoute` | 42 | 303 | 262 | inferred_complete_timeline |
| `Action_RunPostRoute` | 305 | 328 | 24 | inferred_complete_timeline |
| `Action_RunPostRoute` | 331 | 363 | 33 | inferred_complete_timeline |
| `Action_RunPostRoute` | 367 | 390 | 24 | inferred_complete_timeline |
| `Action_RunPostRoute` | 392 | 393 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 101 | 75 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 288 | 179 | inferred_complete_timeline |
| `Action_None` | 290 | 322 | 33 | inferred_complete_timeline |
| `Action_None` | 326 | 340 | 15 | inferred_complete_timeline |
| `Action_None` | 342 | 343 | 2 | inferred_complete_timeline |
| `Action_None` | 345 | 419 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 118 | 92 | inferred_complete_timeline |
| `Action_None` | 122 | 128 | 7 | inferred_complete_timeline |
| `Action_None` | 131 | 134 | 4 | inferred_complete_timeline |
| `Action_None` | 143 | 145 | 3 | inferred_complete_timeline |
| `Action_None` | 175 | 253 | 79 | inferred_complete_timeline |
| `Action_None` | 267 | 273 | 7 | inferred_complete_timeline |
| `Action_None` | 275 | 313 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–413
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 277 | 251 | inferred_complete_timeline |
| `Action_None` | 282 | 287 | 6 | inferred_complete_timeline |
| `Action_None` | 301 | 302 | 2 | inferred_complete_timeline |
| `Action_None` | 316 | 319 | 4 | inferred_complete_timeline |
| `Action_None` | 324 | 380 | 57 | inferred_complete_timeline |
| `Action_None` | 386 | 393 | 8 | inferred_complete_timeline |
| `Action_None` | 406 | 408 | 3 | inferred_complete_timeline |
| `Action_None` | 412 | 413 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 326 | 300 | inferred_complete_timeline |
| `Action_None` | 410 | 419 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–376
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 365 | 339 | inferred_complete_timeline |
| `Action_None` | 370 | 376 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–349
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 235 | 209 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 330 | 82 | inferred_complete_timeline |
| `Action_None` | 345 | 349 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–415
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 197 | 171 | inferred_complete_timeline |
| `Action_None` | 207 | 215 | 9 | inferred_complete_timeline |
| `Action_None` | 217 | 273 | 57 | inferred_complete_timeline |
| `Action_None` | 275 | 345 | 71 | inferred_complete_timeline |
| `Action_None` | 349 | 370 | 22 | inferred_complete_timeline |
| `Action_None` | 376 | 415 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 198 | 172 | inferred_complete_timeline |
| `Action_None` | 201 | 207 | 7 | inferred_complete_timeline |
| `Action_None` | 211 | 237 | 27 | inferred_complete_timeline |
| `Action_None` | 258 | 318 | 61 | inferred_complete_timeline |
| `Action_None` | 322 | 419 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–172 | 170 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 125–419 | 294 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 151–419 | 267 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 152–155 | 4 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 163–166 | 4 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 184–189 | 4 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 197–283 | 43 | 9 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 216–244 | 18 | 3 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 240–254 | 13 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 241–242 | 2 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 253–255 | 3 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 272–274 | 3 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 293–322 | 14 | 3 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 297–298 | 2 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 299–363 | 38 | 6 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 319–320 | 2 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 320–419 | 100 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 324–410 | 61 | 7 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 340–386 | 46 | 2 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 344–345 | 2 | 1 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 349–350 | 2 | 1 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 366–419 | 54 | 1 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 368–419 | 52 | 1 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 388–410 | 12 | 3 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 388–390 | 3 | 1 | Undefined position; Undefined team |
| `47` | `63` | Position_Unknown | Team_Unknown | 390–419 | 30 | 1 | Undefined position; Undefined team |
| `48` | `65` | Position_Unknown | Team_Unknown | 401–419 | 19 | 1 | Undefined position; Undefined team |
| `49` | `66` | Position_Unknown | Team_Unknown | 401–402 | 2 | 1 | Undefined position; Undefined team |
| `50` | `69` | Position_Unknown | Team_Unknown | 407–408 | 2 | 1 | Undefined position; Undefined team |
| `51` | `70` | Position_Unknown | Team_Unknown | 407–419 | 12 | 2 | Undefined position; Undefined team |
| `52` | `73` | Position_Unknown | Team_Unknown | 411–415 | 5 | 1 | Undefined position; Undefined team |
| `53` | `74` | Position_Unknown | Team_Unknown | 414–417 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunPostRoute` and target `0` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 132 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 30: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [27–42], lower_priority='Action_PassBlock' annotated_start=30, effective_Action_PassBlock_start=43.
- ⚠️ Action 'Action_RunPostRoute' range [42-303] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [305-328] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [331-363] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [367-390] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [392-393] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-365] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-376] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-419] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-200] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-419] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-201] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-276] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-277] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-287] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-380] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-393] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-408] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-197] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-215] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-273] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-345] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-370] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-415] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-326] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-253] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-273] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-313] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-288] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-322] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-340] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-324] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-392] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-417] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-198] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-237] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-318] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-419] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-338] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-330] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-349] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-320] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [322-393] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-314] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-389] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-88] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-99] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [101-259] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [261-419] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-55] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-328] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [332-367] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [370-371] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-57] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [144-145] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-278] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-244] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-212] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-275] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-219] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-244] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-250] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-322] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-323] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-351] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-359] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-343] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-363] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-387] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-410] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-345] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-386] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-419] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-390] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-400] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-410] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-390] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-408] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-412] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-415] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-417] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>