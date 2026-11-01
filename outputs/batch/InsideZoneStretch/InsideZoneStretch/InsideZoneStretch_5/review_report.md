# Play-Annotation-Generator Annotation Review — InsideZoneStretch_5

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneStretch_5`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_InsideZoneStretch`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 199
- **Validation Warnings:** 210
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 177
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_PressGap` | RB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `23` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 3 | START | 3 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 3 | START | 3 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 3 | START | 3 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 3 | START | 3 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 3 | START | 3 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 3 | START | 3 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 3 | START | 3 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 3 | START | 3 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 3 | START | 3 | 158 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 146 | START | 146 | 151 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 151 | END | 146 | 151 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `12` | `12` | 159 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `17` | 159 | START | 159 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 159 | START | 159 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `20` | 159 | START | 159 | 160 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `9` | 159 | START | 159 | 195 |
| ✅ EXACT | `Action_PressGap` | RB | `7` | `7` | 174 | START | 174 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `16` | `16` | 180 | START | 180 | 186 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `23` | `22` | 188 | START | 188 | 204 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `7` | 192 | START | 192 | 208 |

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
- **Visible Frames:** 3–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 145 | 143 | inferred_complete_timeline |
| `Action_SnapReceive` | 146 | 151 | 6 | inferred_complete_timeline |
| `Action_None` | 152 | 179 | 28 | inferred_complete_timeline |
| `Action_Handoff` | 180 | 186 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 419 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 3–213
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 173 | 171 | inferred_complete_timeline |
| `Action_PressGap` | 174 | 191 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 192 | 208 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 211 | 213 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 3–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 145 | 143 | inferred_complete_timeline |
| `Action_None` | 146 | 361 | 216 | inferred_complete_timeline |
| `Action_None` | 363 | 419 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 3–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 145 | 143 | inferred_complete_timeline |
| `Action_None` | 146 | 316 | 171 | inferred_complete_timeline |
| `Action_None` | 318 | 338 | 21 | inferred_complete_timeline |
| `Action_None` | 340 | 360 | 21 | inferred_complete_timeline |
| `Action_None` | 362 | 369 | 8 | inferred_complete_timeline |
| `Action_None` | 371 | 375 | 5 | inferred_complete_timeline |
| `Action_None` | 378 | 383 | 6 | inferred_complete_timeline |
| `Action_None` | 385 | 390 | 6 | inferred_complete_timeline |
| `Action_None` | 392 | 399 | 8 | inferred_complete_timeline |
| `Action_None` | 402 | 419 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 3–257
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 158 | 156 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 195 | 37 | inferred_complete_timeline |
| `Action_None` | 196 | 199 | 4 | inferred_complete_timeline |
| `Action_None` | 203 | 257 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 3–419
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 155 | 153 | inferred_complete_timeline |
| `Action_None` | 221 | 316 | 96 | inferred_complete_timeline |
| `Action_None` | 321 | 322 | 2 | inferred_complete_timeline |
| `Action_None` | 325 | 329 | 5 | inferred_complete_timeline |
| `Action_None` | 335 | 336 | 2 | inferred_complete_timeline |
| `Action_None` | 341 | 342 | 2 | inferred_complete_timeline |
| `Action_None` | 345 | 360 | 16 | inferred_complete_timeline |
| `Action_None` | 365 | 368 | 4 | inferred_complete_timeline |
| `Action_None` | 372 | 374 | 3 | inferred_complete_timeline |
| `Action_None` | 379 | 382 | 4 | inferred_complete_timeline |
| `Action_None` | 384 | 390 | 7 | inferred_complete_timeline |
| `Action_None` | 392 | 397 | 6 | inferred_complete_timeline |
| `Action_None` | 402 | 419 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 3–172
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 145 | 143 | inferred_complete_timeline |
| `Action_BallSnap` | 146 | 151 | 6 | inferred_complete_timeline |
| `Action_None` | 152 | 158 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 162 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 167 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 172 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 3–419
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 14 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 22 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 158 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 159 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 195 | 35 | inferred_complete_timeline |
| `Action_None` | 196 | 237 | 42 | inferred_complete_timeline |
| `Action_None` | 239 | 242 | 4 | inferred_complete_timeline |
| `Action_None` | 247 | 255 | 9 | inferred_complete_timeline |
| `Action_None` | 259 | 261 | 3 | inferred_complete_timeline |
| `Action_None` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 270 | 5 | inferred_complete_timeline |
| `Action_None` | 272 | 278 | 7 | inferred_complete_timeline |
| `Action_None` | 289 | 316 | 28 | inferred_complete_timeline |
| `Action_None` | 325 | 329 | 5 | inferred_complete_timeline |
| `Action_None` | 334 | 419 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 3–419
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 158 | 156 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 192 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 198 | 3 | inferred_complete_timeline |
| `Action_None` | 201 | 333 | 133 | inferred_complete_timeline |
| `Action_None` | 335 | 338 | 4 | inferred_complete_timeline |
| `Action_None` | 341 | 343 | 3 | inferred_complete_timeline |
| `Action_None` | 351 | 419 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–260
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 145 | 143 | inferred_complete_timeline |
| `Action_None` | 146 | 216 | 71 | inferred_complete_timeline |
| `Action_None` | 223 | 231 | 9 | inferred_complete_timeline |
| `Action_None` | 234 | 245 | 12 | inferred_complete_timeline |
| `Action_None` | 247 | 260 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 3–18
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 18 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 3–419
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 145 | 143 | inferred_complete_timeline |
| `Action_None` | 146 | 187 | 42 | inferred_complete_timeline |
| `Action_None` | 190 | 245 | 56 | inferred_complete_timeline |
| `Action_None` | 247 | 329 | 83 | inferred_complete_timeline |
| `Action_None` | 340 | 419 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 145 | 143 | inferred_complete_timeline |
| `Action_None` | 146 | 185 | 40 | inferred_complete_timeline |
| `Action_None` | 198 | 283 | 86 | inferred_complete_timeline |
| `Action_None` | 290 | 328 | 39 | inferred_complete_timeline |
| `Action_None` | 335 | 338 | 4 | inferred_complete_timeline |
| `Action_None` | 340 | 343 | 4 | inferred_complete_timeline |
| `Action_None` | 345 | 386 | 42 | inferred_complete_timeline |
| `Action_None` | 389 | 419 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 3–411
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 145 | 143 | inferred_complete_timeline |
| `Action_None` | 146 | 198 | 53 | inferred_complete_timeline |
| `Action_None` | 200 | 299 | 100 | inferred_complete_timeline |
| `Action_None` | 301 | 312 | 12 | inferred_complete_timeline |
| `Action_None` | 315 | 316 | 2 | inferred_complete_timeline |
| `Action_None` | 318 | 331 | 14 | inferred_complete_timeline |
| `Action_None` | 335 | 393 | 59 | inferred_complete_timeline |
| `Action_None` | 396 | 397 | 2 | inferred_complete_timeline |
| `Action_None` | 410 | 411 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 3–173
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 145 | 143 | inferred_complete_timeline |
| `Action_None` | 146 | 173 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 3–416
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 145 | 143 | inferred_complete_timeline |
| `Action_None` | 146 | 404 | 259 | inferred_complete_timeline |
| `Action_None` | 406 | 416 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 3–297
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 145 | 143 | inferred_complete_timeline |
| `Action_None` | 146 | 290 | 145 | inferred_complete_timeline |
| `Action_None` | 293 | 297 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 3–387
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 145 | 143 | inferred_complete_timeline |
| `Action_None` | 146 | 320 | 175 | inferred_complete_timeline |
| `Action_None` | 324 | 327 | 4 | inferred_complete_timeline |
| `Action_None` | 334 | 374 | 41 | inferred_complete_timeline |
| `Action_None` | 385 | 387 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 3–419
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 145 | 143 | inferred_complete_timeline |
| `Action_None` | 146 | 201 | 56 | inferred_complete_timeline |
| `Action_None` | 203 | 216 | 14 | inferred_complete_timeline |
| `Action_None` | 218 | 237 | 20 | inferred_complete_timeline |
| `Action_None` | 275 | 309 | 35 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 318 | 320 | 3 | inferred_complete_timeline |
| `Action_None` | 324 | 344 | 21 | inferred_complete_timeline |
| `Action_None` | 346 | 419 | 74 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 3–201 | 199 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 3–351 | 335 | 8 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 11–182 | 167 | 6 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 20–419 | 378 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 177–278 | 89 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 181–419 | 213 | 7 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 185–281 | 93 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 223–419 | 185 | 5 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 232–329 | 87 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 248–395 | 146 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 261–388 | 117 | 3 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 268–419 | 111 | 6 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 281–346 | 52 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 288–419 | 110 | 7 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 299–419 | 112 | 4 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 313–323 | 8 | 2 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 372–419 | 48 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 383–384 | 2 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 397–399 | 3 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 404–419 | 16 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 407–419 | 13 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 409–419 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `12` (LG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 161 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 12: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 12: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_None' range [146-361] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-419] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-316] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-338] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-360] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-369] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-375] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-383] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-390] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-399] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-404] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-416] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-201] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-201] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-216] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-309] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-344] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-216] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-231] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-245] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-260] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-185] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-283] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-328] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-338] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-343] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-386] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [192-208] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [211-213] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-320] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-327] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-374] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-387] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-257] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-290] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-316] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-360] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-368] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-374] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-382] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-390] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-397] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-18] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-187] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-245] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-329] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-419] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-312] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-331] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-393] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [180-186] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [159-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [165-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-245] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-316] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-322] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-342] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-351] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-14] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-22] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-91] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-158] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '19' starts at frame 159, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [159-159] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [161-195] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-237] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-255] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-270] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-278] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-316] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-419] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [159-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [177-192] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-333] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-338] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-343] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-419] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-17] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-31] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-81] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-176] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-332] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-188] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-237] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-247] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-278] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-233] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-242] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-352] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-387] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-410] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-242] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-281] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-242] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-359] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-379] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-386] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-244] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-329] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-316] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-388] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-395] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-267] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-388] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-322] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-343] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-305] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-330] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-346] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-299] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-329] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-355] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-419] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-312] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-325] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-334] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-419] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-318] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-419] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-399] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-419] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>