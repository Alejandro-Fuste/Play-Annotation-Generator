# Play-Annotation-Generator Annotation Review — InsideZoneRead_47

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_47`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 218
- **Validation Warnings:** 225
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 191
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `24` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `31` | `24` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 8 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 8 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 11 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `24` | `Group` | 0 | START | 24 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 152 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 153 | START | 153 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 155 | START | 191 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `16` | 155 | START | 155 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `17` | 155 | START | 155 | 160 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `18` | 155 | START | 155 | 158 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `24` | `19` | 155 | START | 155 | 159 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 167 | END | 153 | 167 |
| ✅ EXACT | `Action_ReadDefender` | QB | `9` | `8` | 173 | START | 173 | 189 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `8` | 190 | START | 190 | 202 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `31` | `24` | 203 | START | 203 | 219 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 239 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_SnapReceive` | 153 | 167 | 15 | inferred_complete_timeline |
| `Action_None` | 168 | 172 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 173 | 189 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 190 | 202 | 13 | inferred_complete_timeline |
| `Action_None` | 203 | 234 | 32 | inferred_complete_timeline |
| `Action_None` | 237 | 241 | 5 | inferred_complete_timeline |
| `Action_None` | 259 | 260 | 2 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 291 | 293 | 3 | inferred_complete_timeline |
| `Action_None` | 297 | 302 | 6 | inferred_complete_timeline |
| `Action_None` | 305 | 313 | 9 | inferred_complete_timeline |
| `Action_None` | 315 | 319 | 5 | inferred_complete_timeline |
| `Action_None` | 324 | 332 | 9 | inferred_complete_timeline |
| `Action_None` | 338 | 449 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 186 | 34 | inferred_complete_timeline |
| `Action_None` | 188 | 349 | 162 | inferred_complete_timeline |
| `Action_None` | 352 | 367 | 16 | inferred_complete_timeline |
| `Action_None` | 369 | 370 | 2 | inferred_complete_timeline |
| `Action_None` | 373 | 385 | 13 | inferred_complete_timeline |
| `Action_None` | 387 | 392 | 6 | inferred_complete_timeline |
| `Action_None` | 397 | 409 | 13 | inferred_complete_timeline |
| `Action_None` | 411 | 449 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 213 | 61 | inferred_complete_timeline |
| `Action_None` | 216 | 311 | 96 | inferred_complete_timeline |
| `Action_None` | 314 | 326 | 13 | inferred_complete_timeline |
| `Action_None` | 331 | 339 | 9 | inferred_complete_timeline |
| `Action_None` | 341 | 360 | 20 | inferred_complete_timeline |
| `Action_None` | 369 | 385 | 17 | inferred_complete_timeline |
| `Action_None` | 387 | 393 | 7 | inferred_complete_timeline |
| `Action_None` | 402 | 418 | 17 | inferred_complete_timeline |
| `Action_None` | 422 | 449 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–337
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 337 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 449 | 297 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `24`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 24–159
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 154 | 131 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 159 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 8–449
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 17 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 154 | 133 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 160 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 197 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 204 | 213 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 217 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 225 | 227 | 3 | inferred_complete_timeline |
| `Action_None` | 247 | 260 | 14 | inferred_complete_timeline |
| `Action_None` | 272 | 273 | 2 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 293 | 6 | inferred_complete_timeline |
| `Action_None` | 295 | 305 | 11 | inferred_complete_timeline |
| `Action_None` | 353 | 358 | 6 | inferred_complete_timeline |
| `Action_None` | 361 | 362 | 2 | inferred_complete_timeline |
| `Action_None` | 365 | 367 | 3 | inferred_complete_timeline |
| `Action_None` | 372 | 375 | 4 | inferred_complete_timeline |
| `Action_None` | 381 | 394 | 14 | inferred_complete_timeline |
| `Action_None` | 397 | 449 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_BallSnap` | 153 | 160 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 197 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 220 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 225 | 229 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 237 | 239 | 3 | inferred_complete_timeline |
| `Action_None` | 240 | 257 | 18 | inferred_complete_timeline |
| `Action_None` | 264 | 266 | 3 | inferred_complete_timeline |
| `Action_None` | 270 | 277 | 8 | inferred_complete_timeline |
| `Action_None` | 282 | 296 | 15 | inferred_complete_timeline |
| `Action_None` | 300 | 303 | 4 | inferred_complete_timeline |
| `Action_None` | 305 | 306 | 2 | inferred_complete_timeline |
| `Action_None` | 310 | 449 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 11–158
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 17 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 154 | 131 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 158 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 8–449
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 17 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 154 | 132 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 159 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 196 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 233 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 237 | 238 | 2 | inferred_complete_timeline |
| `Action_None` | 247 | 250 | 4 | inferred_complete_timeline |
| `Action_None` | 272 | 276 | 5 | inferred_complete_timeline |
| `Action_None` | 278 | 449 | 172 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 53 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 88 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 126 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_None` | 162 | 173 | 12 | inferred_complete_timeline |
| `Action_None` | 180 | 187 | 8 | inferred_complete_timeline |
| `Action_None` | 190 | 197 | 8 | inferred_complete_timeline |
| `Action_None` | 204 | 223 | 20 | inferred_complete_timeline |
| `Action_None` | 225 | 227 | 3 | inferred_complete_timeline |
| `Action_None` | 232 | 233 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 247 | 250 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 37 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 54 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 100 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 135 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 149 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 158 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `25`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `25`
- **team_side:** `defense`
- **Visible Frames:** 26–218
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 56 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 100 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 152 | 51 | inferred_complete_timeline |
| `Action_None` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 226 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 200 | 48 | inferred_complete_timeline |
| `Action_None` | 207 | 242 | 36 | inferred_complete_timeline |
| `Action_None` | 247 | 250 | 4 | inferred_complete_timeline |
| `Action_None` | 272 | 276 | 5 | inferred_complete_timeline |
| `Action_None` | 288 | 290 | 3 | inferred_complete_timeline |
| `Action_None` | 292 | 293 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 449 | 297 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 424 | 272 | inferred_complete_timeline |
| `Action_None` | 426 | 441 | 16 | inferred_complete_timeline |
| `Action_None` | 445 | 449 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 319 | 167 | inferred_complete_timeline |
| `Action_None` | 321 | 434 | 114 | inferred_complete_timeline |
| `Action_None` | 436 | 449 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–434
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 335 | 183 | inferred_complete_timeline |
| `Action_None` | 337 | 338 | 2 | inferred_complete_timeline |
| `Action_None` | 341 | 352 | 12 | inferred_complete_timeline |
| `Action_None` | 355 | 378 | 24 | inferred_complete_timeline |
| `Action_None` | 381 | 434 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–397
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 313 | 161 | inferred_complete_timeline |
| `Action_None` | 315 | 318 | 4 | inferred_complete_timeline |
| `Action_None` | 335 | 379 | 45 | inferred_complete_timeline |
| `Action_None` | 381 | 393 | 13 | inferred_complete_timeline |
| `Action_None` | 396 | 397 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `26` | Position_Unknown | Team_Unknown | 185–449 | 265 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 189–257 | 33 | 4 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 191–296 | 92 | 4 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 200–411 | 188 | 8 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 250–344 | 56 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 261–447 | 63 | 11 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 273–296 | 13 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 275–449 | 116 | 7 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 289–290 | 2 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 292–449 | 158 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 307–309 | 3 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 329–336 | 8 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 333–339 | 7 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 338–434 | 34 | 7 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 353–449 | 97 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 356–449 | 88 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 362–449 | 63 | 4 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 375–449 | 63 | 4 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 377–449 | 47 | 3 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 384–385 | 2 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 397–400 | 4 | 1 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 412–449 | 38 | 1 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 449–449 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `31` (7 segments found)

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 177 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [153–167], lower_priority='Action_ZoneBlock' annotated_start=155, effective_Action_ZoneBlock_start=168.
- ⚠️ Action 'Action_None' range [153-337] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-335] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-352] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-378] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-434] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-319] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-434] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-313] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-379] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-393] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-213] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-311] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-326] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-339] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-360] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-385] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-393] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-418] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-186] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-349] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-367] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-385] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-392] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-409] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-234] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-302] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-313] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-332] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-424] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-441] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-449] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-223] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-226] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-26] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-37] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-54] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-100] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-135] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-149] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 153, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [153-158] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [153-160] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [191-197] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [205-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [211-213] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [215-220] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [225-229] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-257] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-277] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-296] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-303] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-200] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-242] for track '14' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-88] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-109] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-126] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-17] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [155-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-196] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [211-213] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [215-233] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [237-238] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-17] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [155-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-197] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [204-213] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [215-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [225-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-260] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-293] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-305] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-358] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-367] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-375] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-394] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-17] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-154] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [155-158] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [155-159] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-100] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-197] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-212] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-257] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-270] for track '23' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-296] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-219] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [232-305] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [310-349] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [355-358] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [360-363] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [365-390] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [392-411] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-297] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-302] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-344] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-265] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-290] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-306] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-402] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-412] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-419] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-443] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-447] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-296] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-311] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-332] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-349] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-336] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-339] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-361] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-379] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-387] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-402] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-424] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-434] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-359] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-449] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-385] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-419] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-379] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-425] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-440] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-449] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-392] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-424] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-400] for track '41' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.

</details>