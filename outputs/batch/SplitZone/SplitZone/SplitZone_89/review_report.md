# Play-Annotation-Generator Annotation Review — SplitZone_89

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_89`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 156
- **Validation Warnings:** 153
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 133
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `17` | `17` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `3` | `3` |
| ✅ EXACT | `Action_BlockSecondLevel` | DT1 | defense | `9` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `19` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `18` | `18` | 148 | START | 148 | 154 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 155 | START | 155 | 158 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 158 | END | 155 | 158 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `14` | 158 | START | 159 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `15` | 158 | START | 158 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 158 | START | 158 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `8` | `8` | 158 | START | 158 | 227 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `17` | `17` | 160 | START | 160 | 197 |
| ✅ EXACT | `Action_BallCarry` | RB | `3` | `3` | 188 | START | 188 | 336 |
| ✅ EXACT | `Action_BlockSecondLevel` | DT1 | `9` | `9` | 189 | START | 189 | 276 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 276 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–449
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_Handoff` | 148 | 154 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 159 | 187 | 29 | inferred_complete_timeline |
| `Action_None` | 188 | 210 | 23 | inferred_complete_timeline |
| `Action_None` | 253 | 387 | 135 | inferred_complete_timeline |
| `Action_None` | 402 | 403 | 2 | inferred_complete_timeline |
| `Action_None` | 405 | 406 | 2 | inferred_complete_timeline |
| `Action_None` | 408 | 411 | 4 | inferred_complete_timeline |
| `Action_None` | 413 | 414 | 2 | inferred_complete_timeline |
| `Action_None` | 416 | 449 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–336
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 336 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–447
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 381 | 227 | inferred_complete_timeline |
| `Action_None` | 385 | 387 | 3 | inferred_complete_timeline |
| `Action_None` | 391 | 396 | 6 | inferred_complete_timeline |
| `Action_None` | 398 | 420 | 23 | inferred_complete_timeline |
| `Action_None` | 423 | 427 | 5 | inferred_complete_timeline |
| `Action_None` | 429 | 432 | 4 | inferred_complete_timeline |
| `Action_None` | 441 | 447 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 449 | 295 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 333 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–390
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_SplitBlock` | 160 | 197 | 38 | inferred_complete_timeline |
| `Action_SplitBlock` | 204 | 243 | 40 | inferred_complete_timeline |
| `Action_SplitBlock` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 260 | 271 | 12 | inferred_complete_timeline |
| `Action_SplitBlock` | 274 | 276 | 3 | inferred_complete_timeline |
| `Action_None` | 277 | 390 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 227 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 233 | 276 | 44 | inferred_complete_timeline |
| `Action_None` | 277 | 374 | 98 | inferred_complete_timeline |
| `Action_None` | 377 | 378 | 2 | inferred_complete_timeline |
| `Action_None` | 391 | 416 | 26 | inferred_complete_timeline |
| `Action_None` | 419 | 422 | 4 | inferred_complete_timeline |
| `Action_None` | 442 | 449 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 175 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 185 | 187 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_BallSnap` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 166 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 29 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 157 | 112 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 158 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 188 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 276 | 86 | inferred_complete_timeline |
| `Action_None` | 277 | 318 | 42 | inferred_complete_timeline |
| `Action_None` | 321 | 327 | 7 | inferred_complete_timeline |
| `Action_None` | 329 | 387 | 59 | inferred_complete_timeline |
| `Action_None` | 394 | 396 | 3 | inferred_complete_timeline |
| `Action_None` | 402 | 421 | 20 | inferred_complete_timeline |
| `Action_None` | 432 | 449 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 208 | 54 | inferred_complete_timeline |
| `Action_None` | 210 | 213 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 180 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–394
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 189 | 276 | 88 | inferred_complete_timeline |
| `Action_None` | 277 | 314 | 38 | inferred_complete_timeline |
| `Action_None` | 322 | 323 | 2 | inferred_complete_timeline |
| `Action_None` | 334 | 340 | 7 | inferred_complete_timeline |
| `Action_None` | 343 | 352 | 10 | inferred_complete_timeline |
| `Action_None` | 355 | 387 | 33 | inferred_complete_timeline |
| `Action_None` | 393 | 394 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 209 | 55 | inferred_complete_timeline |
| `Action_None` | 212 | 216 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–439
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 222 | 68 | inferred_complete_timeline |
| `Action_None` | 237 | 247 | 11 | inferred_complete_timeline |
| `Action_None` | 253 | 263 | 11 | inferred_complete_timeline |
| `Action_None` | 277 | 379 | 103 | inferred_complete_timeline |
| `Action_None` | 382 | 385 | 4 | inferred_complete_timeline |
| `Action_None` | 387 | 394 | 8 | inferred_complete_timeline |
| `Action_None` | 403 | 404 | 2 | inferred_complete_timeline |
| `Action_None` | 412 | 414 | 3 | inferred_complete_timeline |
| `Action_None` | 419 | 420 | 2 | inferred_complete_timeline |
| `Action_None` | 428 | 429 | 2 | inferred_complete_timeline |
| `Action_None` | 437 | 439 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 234 | 80 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 389 | 235 | inferred_complete_timeline |
| `Action_None` | 391 | 396 | 6 | inferred_complete_timeline |
| `Action_None` | 398 | 403 | 6 | inferred_complete_timeline |
| `Action_None` | 405 | 406 | 2 | inferred_complete_timeline |
| `Action_None` | 408 | 415 | 8 | inferred_complete_timeline |
| `Action_None` | 419 | 422 | 4 | inferred_complete_timeline |
| `Action_None` | 427 | 449 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 379 | 225 | inferred_complete_timeline |
| `Action_None` | 381 | 449 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 411 | 257 | inferred_complete_timeline |
| `Action_None` | 413 | 420 | 8 | inferred_complete_timeline |
| `Action_None` | 428 | 431 | 4 | inferred_complete_timeline |
| `Action_None` | 444 | 449 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 414 | 260 | inferred_complete_timeline |
| `Action_None` | 416 | 419 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 431

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 256 | 102 | inferred_complete_timeline |
| `Action_None` | 269 | 272 | 4 | inferred_complete_timeline |
| `Action_None` | 274 | 276 | 3 | inferred_complete_timeline |
| `Action_None` | 279 | 285 | 7 | inferred_complete_timeline |
| `Action_None` | 288 | 297 | 10 | inferred_complete_timeline |
| `Action_None` | 299 | 368 | 70 | inferred_complete_timeline |
| `Action_None` | 370 | 449 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 167–449 | 283 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 196–394 | 196 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 196–449 | 235 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 196–449 | 254 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 221–252 | 32 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 222–449 | 219 | 4 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 230–402 | 165 | 5 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 247–273 | 26 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 284–396 | 43 | 4 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 298–449 | 140 | 7 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 353–377 | 24 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 412–449 | 36 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_Handoff` and target `18` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 158 != Inferred start 159
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `17` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 124 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 180: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (LT) duration 119 frames exceeds threshold 90 frames [start=158, end=276].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [155–158], lower_priority='Action_ZoneBlock' annotated_start=158, effective_Action_ZoneBlock_start=159.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RG) duration 119 frames exceeds threshold 90 frames [start=158, end=276].
- ⚠️ Action 'Action_None' range [155-381] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-387] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-396] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-420] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-427] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-432] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-447] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-256] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-285] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-297] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-368] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-336] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-389] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-396] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-403] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-415] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-422] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-379] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-208] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-213] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [158-227] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [233-276] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-374] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-416] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-422] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-449] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-188] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [189-276] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-314] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-340] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-352] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-387] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-394] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-411] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-420] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-431] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-449] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-209] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-414] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-419] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-222] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-247] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-263] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-379] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-385] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-394] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-414] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-439] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [159-166] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [158-175] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [185-187] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-234] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [160-197] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [204-243] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [249-250] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [254-255] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [260-271] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-390] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-387] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-411] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-414] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-333] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-29] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-32] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '20' starts at frame 158, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [158-158] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-170] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [182-188] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [191-276] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-318] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-327] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-387] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-396] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-421] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-449] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-449] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-211] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-394] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-421] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-426] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-449] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-252] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-384] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-406] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-413] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-449] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-283] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-305] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-311] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-320] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-402] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-270] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-317] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-396] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-389] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-396] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-406] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-414] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-427] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-443] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-374] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-429] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-447] for track '32' has 2 frames without a visible bounding box.
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

</details>