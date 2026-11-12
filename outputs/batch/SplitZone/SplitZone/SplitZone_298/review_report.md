# Play-Annotation-Generator Annotation Review — SplitZone_298

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_298`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 176
- **Validation Warnings:** 171
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 154
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `3` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 115 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 116 | START | 116 | 130 |
| ✅ EXACT | `Action_SplitBlock` | HB | `3` | `3` | 125 | START | 125 | 183 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `10` | 127 | START | 127 | 168 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `17` | 127 | START | 127 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 127 | START | 131 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `20` | 127 | START | 127 | 164 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `21` | 127 | START | 127 | 168 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 130 | END | 116 | 130 |
| ✅ EXACT | `Action_PressEdge` | RB | `12` | `12` | 140 | START | 140 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `13` | `13` | 152 | START | 152 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `12` | `12` | 161 | START | 161 | 188 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_SnapReceive` | 116 | 130 | 15 | inferred_complete_timeline |
| `Action_None` | 131 | 151 | 21 | inferred_complete_timeline |
| `Action_Handoff` | 152 | 159 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 389 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_PressEdge` | 140 | 160 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 161 | 188 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 192 | 206 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 208 | 270 | 63 | inferred_complete_timeline |
| `Action_BallCarry` | 272 | 273 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 277 | 310 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 313 | 324 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 327 | 338 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 346 | 348 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 350 | 355 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_SplitBlock` | 125 | 183 | 59 | inferred_complete_timeline |
| `Action_None` | 184 | 238 | 55 | inferred_complete_timeline |
| `Action_None` | 240 | 293 | 54 | inferred_complete_timeline |
| `Action_None` | 300 | 303 | 4 | inferred_complete_timeline |
| `Action_None` | 305 | 366 | 62 | inferred_complete_timeline |
| `Action_None` | 370 | 372 | 3 | inferred_complete_timeline |
| `Action_None` | 378 | 380 | 3 | inferred_complete_timeline |
| `Action_None` | 389 | 389 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 252 | 137 | inferred_complete_timeline |
| `Action_None` | 258 | 260 | 3 | inferred_complete_timeline |
| `Action_None` | 262 | 269 | 8 | inferred_complete_timeline |
| `Action_None` | 284 | 285 | 2 | inferred_complete_timeline |
| `Action_None` | 296 | 303 | 8 | inferred_complete_timeline |
| `Action_None` | 315 | 319 | 5 | inferred_complete_timeline |
| `Action_None` | 322 | 323 | 2 | inferred_complete_timeline |
| `Action_None` | 338 | 344 | 7 | inferred_complete_timeline |
| `Action_None` | 372 | 373 | 2 | inferred_complete_timeline |
| `Action_None` | 375 | 389 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 356 | 241 | inferred_complete_timeline |
| `Action_None` | 358 | 380 | 23 | inferred_complete_timeline |
| `Action_None` | 382 | 389 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–357
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 273 | 158 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 280 | 283 | 4 | inferred_complete_timeline |
| `Action_None` | 286 | 298 | 13 | inferred_complete_timeline |
| `Action_None` | 300 | 302 | 3 | inferred_complete_timeline |
| `Action_None` | 306 | 309 | 4 | inferred_complete_timeline |
| `Action_None` | 312 | 325 | 14 | inferred_complete_timeline |
| `Action_None` | 330 | 341 | 12 | inferred_complete_timeline |
| `Action_None` | 346 | 352 | 7 | inferred_complete_timeline |
| `Action_None` | 354 | 357 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 164 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 169 | 272 | 104 | inferred_complete_timeline |
| `Action_None` | 274 | 281 | 8 | inferred_complete_timeline |
| `Action_None` | 283 | 389 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 157 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 168 | 10 | inferred_complete_timeline |
| `Action_None` | 169 | 183 | 15 | inferred_complete_timeline |
| `Action_None` | 185 | 276 | 92 | inferred_complete_timeline |
| `Action_None` | 279 | 285 | 7 | inferred_complete_timeline |
| `Action_None` | 300 | 302 | 3 | inferred_complete_timeline |
| `Action_None` | 313 | 354 | 42 | inferred_complete_timeline |
| `Action_None` | 357 | 358 | 2 | inferred_complete_timeline |
| `Action_None` | 362 | 373 | 12 | inferred_complete_timeline |
| `Action_None` | 375 | 377 | 3 | inferred_complete_timeline |
| `Action_None` | 382 | 389 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_BallSnap` | 116 | 130 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 131 | 144 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 168 | 15 | inferred_complete_timeline |
| `Action_None` | 169 | 265 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–363
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 168 | 42 | inferred_complete_timeline |
| `Action_None` | 169 | 278 | 110 | inferred_complete_timeline |
| `Action_None` | 285 | 288 | 4 | inferred_complete_timeline |
| `Action_None` | 296 | 297 | 2 | inferred_complete_timeline |
| `Action_None` | 304 | 311 | 8 | inferred_complete_timeline |
| `Action_None` | 315 | 316 | 2 | inferred_complete_timeline |
| `Action_None` | 362 | 363 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 168 | 42 | inferred_complete_timeline |
| `Action_None` | 169 | 209 | 41 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 274 | 58 | inferred_complete_timeline |
| `Action_None` | 278 | 279 | 2 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_None` | 295 | 337 | 43 | inferred_complete_timeline |
| `Action_None` | 339 | 356 | 18 | inferred_complete_timeline |
| `Action_None` | 359 | 368 | 10 | inferred_complete_timeline |
| `Action_None` | 373 | 375 | 3 | inferred_complete_timeline |
| `Action_None` | 378 | 380 | 3 | inferred_complete_timeline |
| `Action_None` | 385 | 389 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–331
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 156 | 41 | inferred_complete_timeline |
| `Action_None` | 162 | 215 | 54 | inferred_complete_timeline |
| `Action_None` | 217 | 250 | 34 | inferred_complete_timeline |
| `Action_None` | 252 | 302 | 51 | inferred_complete_timeline |
| `Action_None` | 304 | 315 | 12 | inferred_complete_timeline |
| `Action_None` | 318 | 319 | 2 | inferred_complete_timeline |
| `Action_None` | 330 | 331 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 186 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 285 | 170 | inferred_complete_timeline |
| `Action_None` | 287 | 389 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 145 | 30 | inferred_complete_timeline |
| `Action_None` | 151 | 157 | 7 | inferred_complete_timeline |
| `Action_None` | 160 | 288 | 129 | inferred_complete_timeline |
| `Action_None` | 300 | 311 | 12 | inferred_complete_timeline |
| `Action_None` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_None` | 330 | 389 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 273 | 158 | inferred_complete_timeline |
| `Action_None` | 289 | 389 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 389 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 389 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 344 | 229 | inferred_complete_timeline |
| `Action_None` | 346 | 347 | 2 | inferred_complete_timeline |
| `Action_None` | 350 | 364 | 15 | inferred_complete_timeline |
| `Action_None` | 367 | 389 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 270 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–354
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 327 | 212 | inferred_complete_timeline |
| `Action_None` | 330 | 331 | 2 | inferred_complete_timeline |
| `Action_None` | 336 | 347 | 12 | inferred_complete_timeline |
| `Action_None` | 349 | 354 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–344
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 272 | 157 | inferred_complete_timeline |
| `Action_None` | 277 | 308 | 32 | inferred_complete_timeline |
| `Action_None` | 339 | 344 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 51–73 | 15 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 181–189 | 9 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 193–389 | 185 | 5 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 200–201 | 2 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 228–229 | 2 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 233–358 | 45 | 9 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 282–389 | 87 | 4 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 302–305 | 4 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 307–389 | 66 | 4 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 318–321 | 4 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 334–337 | 4 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 347–389 | 39 | 2 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 368–369 | 2 | 1 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 385–389 | 5 | 1 | Undefined position; Undefined team |
| `37` | `57` | Position_Unknown | Team_Unknown | 385–388 | 4 | 1 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 386–389 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (9 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 135 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [116–130], lower_priority='Action_ZoneBlock' annotated_start=127, effective_Action_ZoneBlock_start=131.
- ⚠️ Action 'Action_None' range [116-356] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-380] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-273] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-298] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-309] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-325] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-341] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-352] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-357] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-186] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-238] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-293] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-303] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-366] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-372] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-389] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-270] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-252] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-303] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-344] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-273] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-272] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-308] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-344] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-344] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-364] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-209] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-274] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-337] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-356] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-368] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-375] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-389] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-288] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-311] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-389] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [161-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [192-206] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [208-270] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [272-273] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [277-310] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [313-324] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [327-338] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [346-348] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [350-355] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [152-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-215] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-250] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-302] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-315] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-327] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-347] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-354] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-389] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [127-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-183] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-276] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-285] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-354] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-373] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-377] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-285] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-389] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [131-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-265] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [127-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-272] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-281] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [127-168] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-278] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-311] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-73] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-189] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-270] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-364] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-385] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-270] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-358] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-291] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-305] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-379] for track '30' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-321] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-357] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-389] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-389] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-388] for track '37' has 1 frames without a visible bounding box.
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

</details>