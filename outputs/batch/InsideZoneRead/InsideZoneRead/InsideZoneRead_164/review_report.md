# Play-Annotation-Generator Annotation Review — InsideZoneRead_164

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_164`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 187
- **Validation Warnings:** 218
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 154
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `17` | `16` |
| ⚠️ START CHANGED | `Action_Handoff` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 206 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 162 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 161 | START | 161 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 163 | START | 163 | 176 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 163 | START | 176 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 163 | START | 163 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `7` | `6` | 163 | START | 163 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `9` | `8` | 163 | START | 163 | 174 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 174 | END | 161 | 174 |
| ✅ EXACT | `Action_ReadDefender` | QB | `17` | `16` | 182 | START | 182 | 194 |
| ⚠️ START CHANGED | `Action_Handoff` | QB | `17` | `16` | 195 | START | 199 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `11` | `10` | 207 | START | 207 | 252 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 254 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–339
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_SnapReceive` | 161 | 174 | 14 | inferred_complete_timeline |
| `Action_None` | 175 | 181 | 7 | inferred_complete_timeline |
| `Action_ReadDefender` | 182 | 194 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 199 | 206 | 8 | inferred_complete_timeline |
| `Action_None` | 207 | 221 | 15 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_None` | 227 | 230 | 4 | inferred_complete_timeline |
| `Action_None` | 235 | 241 | 7 | inferred_complete_timeline |
| `Action_None` | 244 | 291 | 48 | inferred_complete_timeline |
| `Action_None` | 301 | 339 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–348
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_BallCarry` | 207 | 252 | 46 | inferred_complete_timeline |
| `Action_BallCarry` | 311 | 344 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 347 | 348 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 268 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–369
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 369 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 475

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 438 | 278 | inferred_complete_timeline |
| `Action_None` | 444 | 479 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 174 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 193 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 195 | 198 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 219 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 174 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 183 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 246 | 249 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_BallSnap` | 161 | 174 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 180 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 203 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 211 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 219 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 227 | 230 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 234 | 240 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 249 | 254 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 88 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 94 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 99 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 103 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 145 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 162 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 174 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 240 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 176 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 178 | 254 | 77 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_None` | 259 | 269 | 11 | inferred_complete_timeline |
| `Action_None` | 317 | 319 | 3 | inferred_complete_timeline |
| `Action_None` | 324 | 325 | 2 | inferred_complete_timeline |
| `Action_None` | 335 | 479 | 145 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 173 | 13 | inferred_complete_timeline |
| `Action_None` | 215 | 219 | 5 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_None` | 227 | 249 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–445
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 336 | 176 | inferred_complete_timeline |
| `Action_None` | 342 | 363 | 22 | inferred_complete_timeline |
| `Action_None` | 370 | 371 | 2 | inferred_complete_timeline |
| `Action_None` | 373 | 375 | 3 | inferred_complete_timeline |
| `Action_None` | 382 | 394 | 13 | inferred_complete_timeline |
| `Action_None` | 399 | 433 | 35 | inferred_complete_timeline |
| `Action_None` | 443 | 445 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 173 | 13 | inferred_complete_timeline |
| `Action_None` | 183 | 203 | 21 | inferred_complete_timeline |
| `Action_None` | 227 | 232 | 6 | inferred_complete_timeline |
| `Action_None` | 234 | 240 | 7 | inferred_complete_timeline |
| `Action_None` | 244 | 247 | 4 | inferred_complete_timeline |
| `Action_None` | 273 | 280 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 169 | 9 | inferred_complete_timeline |
| `Action_None` | 171 | 175 | 5 | inferred_complete_timeline |
| `Action_None` | 182 | 221 | 40 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_None` | 227 | 230 | 4 | inferred_complete_timeline |
| `Action_None` | 234 | 396 | 163 | inferred_complete_timeline |
| `Action_None` | 399 | 423 | 25 | inferred_complete_timeline |
| `Action_None` | 437 | 479 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 219 | 59 | inferred_complete_timeline |
| `Action_None` | 227 | 229 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 267 | 107 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 479 | 319 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 270 | 110 | inferred_complete_timeline |
| `Action_None` | 272 | 274 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–347
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 347 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 289 | 129 | inferred_complete_timeline |
| `Action_None` | 292 | 295 | 4 | inferred_complete_timeline |
| `Action_None` | 307 | 309 | 3 | inferred_complete_timeline |
| `Action_None` | 338 | 479 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–315
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 252 | 92 | inferred_complete_timeline |
| `Action_None` | 273 | 285 | 13 | inferred_complete_timeline |
| `Action_None` | 288 | 290 | 3 | inferred_complete_timeline |
| `Action_None` | 306 | 311 | 6 | inferred_complete_timeline |
| `Action_None` | 313 | 315 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–173 | 174 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 182–201 | 20 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 187–201 | 11 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 203–373 | 140 | 8 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 228–240 | 11 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 236–240 | 5 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 271–389 | 113 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 274–373 | 100 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 288–479 | 176 | 7 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 290–420 | 78 | 4 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 295–301 | 6 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 299–309 | 10 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 311–374 | 20 | 3 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 324–349 | 8 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 327–479 | 140 | 4 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 328–479 | 133 | 4 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 328–331 | 4 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 345–479 | 133 | 2 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 346–352 | 4 | 2 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 356–479 | 124 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 360–404 | 41 | 2 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 387–479 | 91 | 2 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 390–479 | 66 | 5 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 401–444 | 44 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 402–479 | 23 | 3 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 408–479 | 72 | 1 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 428–479 | 52 | 1 | Undefined position; Undefined team |
| `48` | `62` | Position_Unknown | Team_Unknown | 429–479 | 51 | 1 | Undefined position; Undefined team |
| `49` | `64` | Position_Unknown | Team_Unknown | 432–458 | 13 | 3 | Undefined position; Undefined team |
| `50` | `65` | Position_Unknown | Team_Unknown | 441–442 | 2 | 1 | Undefined position; Undefined team |
| `51` | `66` | Position_Unknown | Team_Unknown | 452–479 | 28 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (9 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `17` (QB): Annotated start 195 != Inferred start 199
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 151 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 328: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RT) duration 92 frames exceeds threshold 90 frames [start=163, end=254].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (C) duration 92 frames exceeds threshold 90 frames [start=163, end=254].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [161–174], lower_priority='Action_ZoneBlock' annotated_start=163, effective_Action_ZoneBlock_start=175.
- ⚠️ Action 'Action_None' range [161-336] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-363] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-375] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-394] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-433] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-445] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-438] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-267] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-203] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-240] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-280] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-268] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-174] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [177-193] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [195-198] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-219] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-270] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [180-183] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [246-249] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-252] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-285] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-311] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-206] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [207-252] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [311-344] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [347-348] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-369] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-289] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-221] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-396] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-423] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-347] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-249] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [182-194] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-221] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-241] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-291] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-339] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-219] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-176] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [178-254] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-479] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [161-174] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [176-180] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-203] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-211] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [215-219] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [227-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [234-240] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [249-254] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-88] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-145] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-174] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-240] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-201] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-201] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-254] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-311] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-323] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-373] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-318] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-366] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-389] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-373] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-315] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-373] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-412] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-458] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-469] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-479] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-341] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-353] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-364] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-420] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-298] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-306] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-319] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-374] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-328] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-371] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-417] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-463] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-479] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-390] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-450] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-468] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-331] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-367] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-372] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-404] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-392] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-479] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-396] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-406] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-432] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-436] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-444] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-416] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-439] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-452] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-458] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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