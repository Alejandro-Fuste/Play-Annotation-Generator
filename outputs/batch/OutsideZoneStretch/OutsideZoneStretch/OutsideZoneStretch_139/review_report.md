# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_139

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_139`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 194
- **Validation Warnings:** 233
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
- **Inferred Coverage Segments (Action_None):** 150
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_PressEdge` | QB | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 254 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 177 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `1` | 95 | START | 95 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `10` | 95 | START | 95 | 132 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `14` | `14` | 95 | START | 95 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `17` | `17` | 95 | START | 95 | 107 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `19` | `19` | 95 | START | 95 | 99 |
| ✅ EXACT | `Action_PressEdge` | QB | `18` | `18` | 116 | START | 116 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `18` | `18` | 166 | START | 166 | 167 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_PressEdge` | 116 | 165 | 50 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 171 | 179 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 184 | 198 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 200 | 217 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 219 | 221 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–401
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 219 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 227 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 237 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 244 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 247 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 253 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 401 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 362 | 178 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 366 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 369 | 388 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 400 | 419 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 254 | 255 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 288 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 380 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 384 | 388 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 393 | 394 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 396 | 399 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 405 | 409 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 413 | 419 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 181 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 280 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 287 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 314 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 339 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 396 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 398 | 411 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 415 | 419 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 107 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 136 | 27 | inferred_complete_timeline |
| `Action_None` | 137 | 137 | 1 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 136 | 42 | inferred_complete_timeline |
| `Action_None` | 137 | 206 | 70 | inferred_complete_timeline |
| `Action_None` | 218 | 254 | 37 | inferred_complete_timeline |
| `Action_None` | 257 | 260 | 4 | inferred_complete_timeline |
| `Action_None` | 264 | 275 | 12 | inferred_complete_timeline |
| `Action_None` | 291 | 297 | 7 | inferred_complete_timeline |
| `Action_None` | 300 | 305 | 6 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_None` | 313 | 314 | 2 | inferred_complete_timeline |
| `Action_None` | 319 | 320 | 2 | inferred_complete_timeline |
| `Action_None` | 323 | 324 | 2 | inferred_complete_timeline |
| `Action_None` | 344 | 346 | 3 | inferred_complete_timeline |
| `Action_None` | 351 | 352 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 132 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 136 | 3 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_None` | 152 | 203 | 52 | inferred_complete_timeline |
| `Action_None` | 205 | 214 | 10 | inferred_complete_timeline |
| `Action_None` | 217 | 219 | 3 | inferred_complete_timeline |
| `Action_None` | 221 | 335 | 115 | inferred_complete_timeline |
| `Action_None` | 338 | 358 | 21 | inferred_complete_timeline |
| `Action_None` | 363 | 377 | 15 | inferred_complete_timeline |
| `Action_None` | 379 | 405 | 27 | inferred_complete_timeline |
| `Action_None` | 407 | 409 | 3 | inferred_complete_timeline |
| `Action_None` | 411 | 415 | 5 | inferred_complete_timeline |
| `Action_None` | 419 | 419 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 99 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–376
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 136 | 42 | inferred_complete_timeline |
| `Action_None` | 137 | 147 | 11 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 155 | 169 | 15 | inferred_complete_timeline |
| `Action_None` | 177 | 316 | 140 | inferred_complete_timeline |
| `Action_None` | 322 | 326 | 5 | inferred_complete_timeline |
| `Action_None` | 330 | 334 | 5 | inferred_complete_timeline |
| `Action_None` | 373 | 376 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 261 | 155 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 310 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 314 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 373 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 375 | 396 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 398 | 399 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 403 | 407 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 410 | 419 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 265 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 167 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 177 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 187 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 196 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 289 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 296 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 306 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 311 | 316 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 324 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 363 | 388 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 391 | 419 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 282 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 324 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 355 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 363 | 364 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 382 | 387 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 392 | 394 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 397 | 398 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 403 | 404 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 407 | 419 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 158 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 352 | 181 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 406 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 409 | 419 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 232 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 385 | 386 | inferred_complete_timeline |
| `Action_PreSnap` | 387 | 389 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–176 | 161 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 119–263 | 114 | 7 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 158–419 | 262 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 185–197 | 13 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 186–300 | 97 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 195–214 | 13 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 201–204 | 4 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 206–419 | 208 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 207–287 | 60 | 4 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 215–419 | 198 | 4 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 235–419 | 185 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 268–419 | 144 | 4 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 271–419 | 149 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 306–308 | 3 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 310–391 | 77 | 4 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 319–320 | 2 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 329–419 | 91 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 340–402 | 24 | 6 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 350–402 | 44 | 3 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 380–419 | 40 | 1 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 388–389 | 2 | 1 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 400–401 | 2 | 1 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 402–403 | 2 | 1 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 403–419 | 17 | 1 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 405–419 | 15 | 1 | Undefined position; Undefined team |
| `46` | `68` | Position_Unknown | Team_Unknown | 405–419 | 14 | 2 | Undefined position; Undefined team |
| `47` | `70` | Position_Unknown | Team_Unknown | 408–419 | 11 | 2 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 411–419 | 9 | 1 | Undefined position; Undefined team |
| `49` | `73` | Position_Unknown | Team_Unknown | 416–419 | 4 | 1 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 418–419 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 172 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-254] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-288] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-380] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-388] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-394] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-399] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-409] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-419] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-147] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-316] for track '1' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-326] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-334] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-291] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-177] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-183] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-362] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-366] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-388] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-419] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-385] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-118] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-352] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-406] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-282] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-324] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-355] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-364] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-387] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-394] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-398] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-404] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-232] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-238] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-132] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-335] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-358] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-377] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-405] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-409] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-415] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-156] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-172] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-181] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-280] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-287] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-314] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-339] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-396] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-411] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-146] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-219] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-227] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-237] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-244] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-247] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-253] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-401] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-206] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-254] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-275] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-297] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-305] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-346] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-261] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-310] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-314] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-373] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-396] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-399] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-407] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-167] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-187] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-196] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-289] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-296] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-306] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-316] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-324] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-388] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-419] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-136] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 137, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [137-137] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-167] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [171-179] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [184-198] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [200-217] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [219-221] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-419] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-124] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-158] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-197] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-257] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-263] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-419] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-197] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-211] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-289] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-300] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-214] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-204] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-211] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-217] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-280] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-287] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-326] for track '30' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-339] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-353] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-349] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-359] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-377] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-419] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-419] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-308] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-352] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-373] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-377] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-391] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-320] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-419] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-346] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-354] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-375] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-382] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-392] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-402] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-360] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-384] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-402] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-419] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-389] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-401] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-403] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-410] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-409] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-419] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>