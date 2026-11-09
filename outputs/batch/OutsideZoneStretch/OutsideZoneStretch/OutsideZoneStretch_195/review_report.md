# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_195

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_195`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 195
- **Validation Warnings:** 224
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 156
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `4` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 373 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 0 | START | 0 | 313 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 147 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `13` | 124 | START | 124 | 125 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `17` | 124 | START | 124 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 124 | START | 124 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `20` | 124 | START | 124 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 124 | START | 124 | 127 |
| ✅ EXACT | `Action_PressEdge` | RB | `4` | `4` | 134 | START | 134 | 155 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `5` | 148 | START | 148 | 162 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_Handoff` | 148 | 162 | 15 | inferred_complete_timeline |
| `Action_None` | 163 | 479 | 317 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_PressEdge` | 134 | 155 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 313 | 314 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 345 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 364 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 367 | 397 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 399 | 457 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 467 | 469 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 473 | 479 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 373 | 374 | inferred_complete_timeline |
| `Action_PreSnap` | 391 | 400 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 402 | 410 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 412 | 466 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 468 | 470 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 474 | 479 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–416
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 186 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 232 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 275 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 300 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 334 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 383 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 386 | 391 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 397 | 401 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 415 | 416 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 143 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 168 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–410
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 127 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 170 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 188 | 16 | inferred_complete_timeline |
| `Action_None` | 194 | 239 | 46 | inferred_complete_timeline |
| `Action_None` | 246 | 304 | 59 | inferred_complete_timeline |
| `Action_None` | 306 | 400 | 95 | inferred_complete_timeline |
| `Action_None` | 403 | 410 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 126 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 136 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 155 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 170 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 125 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 125 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 142 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 170 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 259 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 479 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 168 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 479 | 303 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 169 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 255 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 275 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 479 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–429
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 348 | 349 | inferred_complete_timeline |
| `Action_PreSnap` | 350 | 351 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 356 | 364 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 368 | 372 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 374 | 378 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 381 | 406 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 409 | 410 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 416 | 421 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 428 | 429 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–352
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 300 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 352 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 183 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 388 | 191 | inferred_complete_timeline |
| `Action_PreSnap` | 390 | 413 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 416 | 421 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 425 | 428 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 436 | 437 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 443 | 445 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 450 | 451 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 453 | 454 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 458 | 463 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 468 | 471 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 476 | 479 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 479 | 357 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–440
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 408 | 409 | inferred_complete_timeline |
| `Action_PreSnap` | 414 | 432 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 434 | 440 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–423
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 240 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 306 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 364 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 367 | 372 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 375 | 378 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 388 | 389 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 412 | 413 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 420 | 423 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–411
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 297 | 298 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 411 | 110 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 159–213 | 48 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 166–281 | 67 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 166–479 | 267 | 10 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 178–479 | 297 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 180–294 | 79 | 5 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 198–479 | 277 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 219–479 | 261 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 249–479 | 197 | 5 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 253–479 | 214 | 3 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 363–472 | 64 | 11 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 374–479 | 91 | 8 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 377–455 | 45 | 8 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 377–378 | 2 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 378–468 | 49 | 8 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 411–414 | 4 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 417–479 | 63 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 431–437 | 7 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 437–438 | 2 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 442–444 | 3 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 451–477 | 18 | 4 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 452–454 | 3 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 458–479 | 19 | 2 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 478–479 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF3` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 176 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 392: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-373] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-400] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-410] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-466] for track '0' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [468-470] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-479] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-170] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-259] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-479] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-408] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-432] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-440] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-240] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-306] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-364] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-372] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-378] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-389] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-413] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-423] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [134-155] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-348] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-351] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-364] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-372] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-378] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-406] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-410] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-421] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-297] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-411] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-255] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-275] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-244] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-300] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-352] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-168] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-479] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-183] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-388] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-413] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-421] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-428] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-437] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-445] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-451] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [453-454] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [458-463] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [468-471] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-169] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-313] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-345] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-364] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-397] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-457] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-469] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [473-479] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-186] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-232] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-275] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-300] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-334] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-383] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-391] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-401] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-416] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-126] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-136] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [165-170] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [139-143] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [152-155] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [158-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [165-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-188] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-239] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-304] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-400] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-410] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-198] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-213] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-234] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-281] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-192] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-236] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-244] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-345] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-360] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-371] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-395] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-461] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-265] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-286] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-188] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-203] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-221] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-294] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-201] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-479] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-279] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-297] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-307] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-322] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-255] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-279] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-479] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-364] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-374] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-379] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-387] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-392] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-419] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-422] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-426] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-433] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-448] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-472] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-380] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-383] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-393] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-432] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-438] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-447] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [449-471] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-380] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-404] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-422] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-429] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-432] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-442] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-445] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-455] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-378] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-379] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-404] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-420] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-428] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-432] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-445] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [457-458] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [464-468] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-414] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-479] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-437] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-438] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-444] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [451-454] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [459-462] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-472] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-477] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-454] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [458-469] for track '43' has 2 frames without a visible bounding box.
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

</details>