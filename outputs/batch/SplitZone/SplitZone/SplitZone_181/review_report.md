# Play-Annotation-Generator Annotation Review — SplitZone_181

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_181`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 181
- **Validation Warnings:** 169
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 153
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `21` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 25 | START | 26 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 25 | START | 26 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 25 | START | 26 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 25 | START | 26 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 25 | START | 26 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 25 | START | 26 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 25 | START | 26 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 25 | START | 26 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 25 | START | 26 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 25 | START | 26 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 25 | START | 26 | 157 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 158 | START | 158 | 168 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `15` | 161 | START | 161 | 247 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `16` | 161 | START | 169 | 192 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `18` | 161 | START | 161 | 230 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 161 | START | 161 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `2` | 161 | START | 161 | 183 |
| ✅ EXACT | `Action_SplitBlock` | TE | `14` | `14` | 165 | START | 165 | 247 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 168 | END | 158 | 168 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `20` | 174 | START | 174 | 184 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `21` | `21` | 185 | START | 185 | 334 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 247 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 26–226
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 157 | 132 | inferred_complete_timeline |
| `Action_SnapReceive` | 158 | 168 | 11 | inferred_complete_timeline |
| `Action_None` | 169 | 173 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 174 | 184 | 11 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 194 | 217 | 24 | inferred_complete_timeline |
| `Action_None` | 224 | 226 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 26–384
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 53 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 85 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 102 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 111 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 124 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 140 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 184 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 185 | 334 | 150 | inferred_complete_timeline |
| `Action_BallCarry` | 338 | 339 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 342 | 363 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 383 | 384 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 26–387
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 157 | 132 | inferred_complete_timeline |
| `Action_None` | 158 | 337 | 180 | inferred_complete_timeline |
| `Action_None` | 345 | 348 | 4 | inferred_complete_timeline |
| `Action_None` | 350 | 353 | 4 | inferred_complete_timeline |
| `Action_None` | 355 | 358 | 4 | inferred_complete_timeline |
| `Action_None` | 372 | 373 | 2 | inferred_complete_timeline |
| `Action_None` | 386 | 387 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 26–251
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 157 | 132 | inferred_complete_timeline |
| `Action_None` | 158 | 251 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 26–207
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 157 | 132 | inferred_complete_timeline |
| `Action_None` | 158 | 207 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 26–419
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 164 | 139 | inferred_complete_timeline |
| `Action_SplitBlock` | 165 | 247 | 83 | inferred_complete_timeline |
| `Action_None` | 248 | 313 | 66 | inferred_complete_timeline |
| `Action_None` | 327 | 419 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 26–419
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 160 | 135 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 183 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 188 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 197 | 201 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 207 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 247 | 38 | inferred_complete_timeline |
| `Action_None` | 248 | 284 | 37 | inferred_complete_timeline |
| `Action_None` | 286 | 295 | 10 | inferred_complete_timeline |
| `Action_None` | 304 | 305 | 2 | inferred_complete_timeline |
| `Action_None` | 307 | 309 | 3 | inferred_complete_timeline |
| `Action_None` | 330 | 331 | 2 | inferred_complete_timeline |
| `Action_None` | 335 | 337 | 3 | inferred_complete_timeline |
| `Action_None` | 339 | 340 | 2 | inferred_complete_timeline |
| `Action_None` | 347 | 364 | 18 | inferred_complete_timeline |
| `Action_None` | 370 | 376 | 7 | inferred_complete_timeline |
| `Action_None` | 378 | 381 | 4 | inferred_complete_timeline |
| `Action_None` | 384 | 386 | 3 | inferred_complete_timeline |
| `Action_None` | 406 | 408 | 3 | inferred_complete_timeline |
| `Action_None` | 414 | 416 | 3 | inferred_complete_timeline |
| `Action_None` | 418 | 419 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 26–419
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 160 | 135 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 230 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 237 | 247 | 11 | inferred_complete_timeline |
| `Action_None` | 248 | 321 | 74 | inferred_complete_timeline |
| `Action_None` | 323 | 419 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 26–399
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 157 | 132 | inferred_complete_timeline |
| `Action_BallSnap` | 158 | 168 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 192 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 206 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 209 | 211 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 232 | 247 | 16 | inferred_complete_timeline |
| `Action_None` | 248 | 316 | 69 | inferred_complete_timeline |
| `Action_None` | 318 | 333 | 16 | inferred_complete_timeline |
| `Action_None` | 335 | 337 | 3 | inferred_complete_timeline |
| `Action_None` | 342 | 389 | 48 | inferred_complete_timeline |
| `Action_None` | 391 | 399 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 26–419
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 160 | 135 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 178 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 204 | 225 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 234 | 238 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 243 | 247 | 5 | inferred_complete_timeline |
| `Action_None` | 248 | 417 | 170 | inferred_complete_timeline |
| `Action_None` | 419 | 419 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 26–419
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 160 | 135 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 247 | 87 | inferred_complete_timeline |
| `Action_None` | 248 | 297 | 50 | inferred_complete_timeline |
| `Action_None` | 299 | 317 | 19 | inferred_complete_timeline |
| `Action_None` | 319 | 357 | 39 | inferred_complete_timeline |
| `Action_None` | 359 | 360 | 2 | inferred_complete_timeline |
| `Action_None` | 363 | 364 | 2 | inferred_complete_timeline |
| `Action_None` | 366 | 389 | 24 | inferred_complete_timeline |
| `Action_None` | 392 | 419 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 26–419
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 157 | 132 | inferred_complete_timeline |
| `Action_None` | 158 | 400 | 243 | inferred_complete_timeline |
| `Action_None` | 405 | 419 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 26–419
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 157 | 132 | inferred_complete_timeline |
| `Action_None` | 158 | 223 | 66 | inferred_complete_timeline |
| `Action_None` | 231 | 239 | 9 | inferred_complete_timeline |
| `Action_None` | 247 | 359 | 113 | inferred_complete_timeline |
| `Action_None` | 361 | 362 | 2 | inferred_complete_timeline |
| `Action_None` | 369 | 380 | 12 | inferred_complete_timeline |
| `Action_None` | 385 | 388 | 4 | inferred_complete_timeline |
| `Action_None` | 397 | 399 | 3 | inferred_complete_timeline |
| `Action_None` | 402 | 403 | 2 | inferred_complete_timeline |
| `Action_None` | 407 | 419 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 26–419
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 157 | 132 | inferred_complete_timeline |
| `Action_None` | 158 | 321 | 164 | inferred_complete_timeline |
| `Action_None` | 328 | 419 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 26–419
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 157 | 132 | inferred_complete_timeline |
| `Action_None` | 158 | 211 | 54 | inferred_complete_timeline |
| `Action_None` | 214 | 232 | 19 | inferred_complete_timeline |
| `Action_None` | 235 | 419 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 26–419
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 157 | 132 | inferred_complete_timeline |
| `Action_None` | 158 | 222 | 65 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 243 | 7 | inferred_complete_timeline |
| `Action_None` | 246 | 336 | 91 | inferred_complete_timeline |
| `Action_None` | 338 | 348 | 11 | inferred_complete_timeline |
| `Action_None` | 353 | 378 | 26 | inferred_complete_timeline |
| `Action_None` | 381 | 384 | 4 | inferred_complete_timeline |
| `Action_None` | 387 | 392 | 6 | inferred_complete_timeline |
| `Action_None` | 398 | 399 | 2 | inferred_complete_timeline |
| `Action_None` | 403 | 419 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 26–235
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 157 | 132 | inferred_complete_timeline |
| `Action_None` | 158 | 235 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 26–419
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 157 | 132 | inferred_complete_timeline |
| `Action_None` | 158 | 419 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 26–419
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 157 | 132 | inferred_complete_timeline |
| `Action_None` | 158 | 419 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 26–419
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 157 | 132 | inferred_complete_timeline |
| `Action_None` | 158 | 242 | 85 | inferred_complete_timeline |
| `Action_None` | 250 | 261 | 12 | inferred_complete_timeline |
| `Action_None` | 274 | 320 | 47 | inferred_complete_timeline |
| `Action_None` | 322 | 335 | 14 | inferred_complete_timeline |
| `Action_None` | 338 | 339 | 2 | inferred_complete_timeline |
| `Action_None` | 344 | 364 | 21 | inferred_complete_timeline |
| `Action_None` | 367 | 368 | 2 | inferred_complete_timeline |
| `Action_None` | 371 | 372 | 2 | inferred_complete_timeline |
| `Action_None` | 374 | 387 | 14 | inferred_complete_timeline |
| `Action_None` | 392 | 393 | 2 | inferred_complete_timeline |
| `Action_None` | 396 | 401 | 6 | inferred_complete_timeline |
| `Action_None` | 403 | 419 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 26–391
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 157 | 132 | inferred_complete_timeline |
| `Action_None` | 158 | 374 | 217 | inferred_complete_timeline |
| `Action_None` | 376 | 391 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 26–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 157 | 132 | inferred_complete_timeline |
| `Action_None` | 158 | 282 | 125 | inferred_complete_timeline |
| `Action_None` | 284 | 419 | 136 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 222–419 | 189 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 248–352 | 72 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 297–418 | 83 | 6 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 300–306 | 7 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 308–419 | 103 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 327–328 | 2 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 338–418 | 69 | 5 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 369–419 | 27 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 370–419 | 22 | 5 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 373–374 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 387–417 | 6 | 3 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 395–398 | 4 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 409–419 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 141 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [158–168], lower_priority='Action_ZoneBlock' annotated_start=161, effective_Action_ZoneBlock_start=169.
- ⚠️ Action 'Action_None' range [158-337] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-353] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-358] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-400] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [161-183] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [186-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [197-201] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-207] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-284] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-295] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-364] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-376] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-381] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-386] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-408] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-416] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-251] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-207] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-235] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-222] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-243] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-336] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-348] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-378] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-392] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-419] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-321] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-419] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-374] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-391] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-211] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-232] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-223] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-359] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-380] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-388] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-399] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-419] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-242] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-261] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-320] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-335] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-364] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-387] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-393] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-401] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [165-247] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-313] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-419] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-297] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-317] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-357] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-389] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-192] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [196-206] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [209-211] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-316] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-333] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-389] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-399] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-282] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [161-230] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-321] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-419] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [161-178] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [204-225] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [231-232] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [234-238] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [243-247] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-417] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-217] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-53] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-85] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-102] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-111] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [185-334] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [338-339] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [342-363] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [383-384] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-249] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-335] for track '22' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-419] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-258] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-268] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-331] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-352] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-305] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-332] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-363] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-392] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-418] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-306] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-322] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-411] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-343] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-375] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-398] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-418] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-374] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-398] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-419] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-374] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-402] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-414] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-398] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-419] for track '34' has 1 frames without a visible bounding box.
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