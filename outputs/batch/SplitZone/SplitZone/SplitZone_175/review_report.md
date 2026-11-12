# Play-Annotation-Generator Annotation Review — SplitZone_175

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_175`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 143
- **Validation Warnings:** 132
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
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 117
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `23` | `21` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 2 | START | 3 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 2 | START | 3 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 2 | START | 3 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 2 | START | 3 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 2 | START | 3 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 2 | START | 4 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 2 | START | 8 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 2 | START | 8 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `23` | `Group` | 2 | START | 70 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 2 | START | 3 | 213 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 2 | START | 3 | 189 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 180 | START | 180 | 193 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `13` | `13` | 183 | START | 183 | 263 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `18` | 183 | START | 194 | 263 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `19` | 183 | START | 183 | 222 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 183 | START | 183 | 200 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `23` | `21` | 183 | START | 183 | 197 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `8` | `8` | 190 | START | 190 | 263 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 193 | END | 180 | 193 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 200 | START | 200 | 213 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `5` | 214 | START | 214 | 385 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 263 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 3–312
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 179 | 177 | inferred_complete_timeline |
| `Action_SnapReceive` | 180 | 193 | 14 | inferred_complete_timeline |
| `Action_None` | 194 | 199 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 200 | 213 | 14 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 218 | 312 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 3–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 213 | 211 | inferred_complete_timeline |
| `Action_BallCarry` | 214 | 385 | 172 | inferred_complete_timeline |
| `Action_BallCarry` | 387 | 389 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 3–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 179 | 177 | inferred_complete_timeline |
| `Action_None` | 180 | 389 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 3–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 179 | 177 | inferred_complete_timeline |
| `Action_None` | 180 | 389 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 3–325
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 179 | 177 | inferred_complete_timeline |
| `Action_None` | 180 | 276 | 97 | inferred_complete_timeline |
| `Action_None` | 290 | 296 | 7 | inferred_complete_timeline |
| `Action_None` | 324 | 325 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 3–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 189 | 187 | inferred_complete_timeline |
| `Action_SplitBlock` | 190 | 263 | 74 | inferred_complete_timeline |
| `Action_None` | 264 | 389 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 3–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 182 | 180 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 263 | 81 | inferred_complete_timeline |
| `Action_None` | 264 | 264 | 1 | inferred_complete_timeline |
| `Action_None` | 268 | 389 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 8–200
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 11 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 162 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 182 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 200 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 4–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 9 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 12 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 179 | 166 | inferred_complete_timeline |
| `Action_BallSnap` | 180 | 193 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 263 | 70 | inferred_complete_timeline |
| `Action_None` | 264 | 337 | 74 | inferred_complete_timeline |
| `Action_None` | 348 | 389 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 8–389
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 182 | 175 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 222 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 225 | 239 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 243 | 263 | 21 | inferred_complete_timeline |
| `Action_None` | 264 | 291 | 28 | inferred_complete_timeline |
| `Action_None` | 293 | 300 | 8 | inferred_complete_timeline |
| `Action_None` | 304 | 312 | 9 | inferred_complete_timeline |
| `Action_None` | 316 | 317 | 2 | inferred_complete_timeline |
| `Action_None` | 319 | 324 | 6 | inferred_complete_timeline |
| `Action_None` | 327 | 330 | 4 | inferred_complete_timeline |
| `Action_None` | 332 | 350 | 19 | inferred_complete_timeline |
| `Action_None` | 352 | 353 | 2 | inferred_complete_timeline |
| `Action_None` | 356 | 359 | 4 | inferred_complete_timeline |
| `Action_None` | 366 | 368 | 3 | inferred_complete_timeline |
| `Action_None` | 384 | 389 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 70–197
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 70 | 78 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 182 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 197 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 3–311
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 179 | 177 | inferred_complete_timeline |
| `Action_None` | 180 | 225 | 46 | inferred_complete_timeline |
| `Action_None` | 227 | 247 | 21 | inferred_complete_timeline |
| `Action_None` | 254 | 302 | 49 | inferred_complete_timeline |
| `Action_None` | 306 | 311 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 3–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 179 | 177 | inferred_complete_timeline |
| `Action_None` | 180 | 302 | 123 | inferred_complete_timeline |
| `Action_None` | 306 | 308 | 3 | inferred_complete_timeline |
| `Action_None` | 312 | 313 | 2 | inferred_complete_timeline |
| `Action_None` | 320 | 378 | 59 | inferred_complete_timeline |
| `Action_None` | 380 | 389 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 3–376
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 179 | 177 | inferred_complete_timeline |
| `Action_None` | 180 | 241 | 62 | inferred_complete_timeline |
| `Action_None` | 262 | 299 | 38 | inferred_complete_timeline |
| `Action_None` | 304 | 305 | 2 | inferred_complete_timeline |
| `Action_None` | 344 | 350 | 7 | inferred_complete_timeline |
| `Action_None` | 352 | 359 | 8 | inferred_complete_timeline |
| `Action_None` | 362 | 366 | 5 | inferred_complete_timeline |
| `Action_None` | 372 | 376 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 3–389
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 179 | 177 | inferred_complete_timeline |
| `Action_None` | 180 | 316 | 137 | inferred_complete_timeline |
| `Action_None` | 319 | 321 | 3 | inferred_complete_timeline |
| `Action_None` | 327 | 348 | 22 | inferred_complete_timeline |
| `Action_None` | 351 | 354 | 4 | inferred_complete_timeline |
| `Action_None` | 356 | 357 | 2 | inferred_complete_timeline |
| `Action_None` | 360 | 370 | 11 | inferred_complete_timeline |
| `Action_None` | 378 | 380 | 3 | inferred_complete_timeline |
| `Action_None` | 388 | 389 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–221
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 179 | 177 | inferred_complete_timeline |
| `Action_None` | 180 | 221 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 179 | 177 | inferred_complete_timeline |
| `Action_None` | 180 | 299 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 3–369
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 179 | 177 | inferred_complete_timeline |
| `Action_None` | 180 | 297 | 118 | inferred_complete_timeline |
| `Action_None` | 305 | 312 | 8 | inferred_complete_timeline |
| `Action_None` | 316 | 317 | 2 | inferred_complete_timeline |
| `Action_None` | 333 | 337 | 5 | inferred_complete_timeline |
| `Action_None` | 354 | 360 | 7 | inferred_complete_timeline |
| `Action_None` | 363 | 364 | 2 | inferred_complete_timeline |
| `Action_None` | 368 | 369 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 179 | 177 | inferred_complete_timeline |
| `Action_None` | 180 | 312 | 133 | inferred_complete_timeline |
| `Action_None` | 314 | 319 | 6 | inferred_complete_timeline |
| `Action_None` | 324 | 326 | 3 | inferred_complete_timeline |
| `Action_None` | 328 | 343 | 16 | inferred_complete_timeline |
| `Action_None` | 346 | 365 | 20 | inferred_complete_timeline |
| `Action_None` | 367 | 371 | 5 | inferred_complete_timeline |
| `Action_None` | 373 | 385 | 13 | inferred_complete_timeline |
| `Action_None` | 389 | 389 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 179 | 177 | inferred_complete_timeline |
| `Action_None` | 180 | 389 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 3–323
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 179 | 177 | inferred_complete_timeline |
| `Action_None` | 180 | 312 | 133 | inferred_complete_timeline |
| `Action_None` | 315 | 319 | 5 | inferred_complete_timeline |
| `Action_None` | 321 | 323 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 3–380
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 179 | 177 | inferred_complete_timeline |
| `Action_None` | 180 | 321 | 142 | inferred_complete_timeline |
| `Action_None` | 325 | 326 | 2 | inferred_complete_timeline |
| `Action_None` | 331 | 334 | 4 | inferred_complete_timeline |
| `Action_None` | 336 | 340 | 5 | inferred_complete_timeline |
| `Action_None` | 343 | 347 | 5 | inferred_complete_timeline |
| `Action_None` | 357 | 360 | 4 | inferred_complete_timeline |
| `Action_None` | 374 | 380 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 216–226 | 11 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 236–299 | 53 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 255–267 | 13 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 260–389 | 121 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 289–388 | 82 | 6 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 297–304 | 7 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 313–389 | 77 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 325–389 | 58 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 337–389 | 52 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 374–375 | 2 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 380–389 | 10 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 385–389 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 104 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [180–193], lower_priority='Action_ZoneBlock' annotated_start=183, effective_Action_ZoneBlock_start=194.
- ⚠️ Action 'Action_None' range [180-299] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-312] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-321] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-334] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-347] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-360] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-380] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-297] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-312] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-337] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-360] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [214-385] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-221] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-312] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-319] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-343] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-365] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-371] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-385] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-312] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-302] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-378] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-389] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-389] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 264, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [264-264] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-225] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-247] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-302] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-311] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-316] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-348] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-370] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-241] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-350] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-359] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-366] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-376] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-276] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-296] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-9] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-12] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-179] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-263] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-337] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [225-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-291] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-300] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-312] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-324] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-350] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-359] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-368] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-11] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-162] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-200] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-197] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-226] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-299] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-267] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-297] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-318] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-389] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-299] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-313] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-350] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-360] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-383] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-388] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-300] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-304] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-332] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-389] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-343] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '32' has 1 frames without a visible bounding box.
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

</details>