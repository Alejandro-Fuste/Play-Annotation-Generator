# Play-Annotation-Generator Annotation Review — SplitZone_288

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_288`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 156
- **Validation Warnings:** 129
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 10
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 133
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_PressEdge` | DE1 | defense | `5` | `5` |
| ✅ EXACT | `Action_ReadEdgeDefender` | SAF2 | defense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | SAF2 | defense | `8` | `8` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 155 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `11` | 98 | START | 98 | 146 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `17` | 98 | START | 98 | 146 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `18` | `18` | 98 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LT | `19` | `19` | 98 | START | 98 | 146 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `20` | 98 | START | 98 | 146 |
| ✅ EXACT | `Action_PressEdge` | DE1 | `5` | `5` | 111 | START | 111 | 188 |
| ✅ EXACT | `Action_ReadEdgeDefender` | SAF2 | `8` | `8` | 111 | START | 111 | 121 |
| ✅ EXACT | `Action_Handoff` | SAF2 | `8` | `8` | 122 | START | 122 | 130 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 148 | START | 148 | 160 |
| ✅ EXACT | `Action_SplitBlock` | TE | `7` | `7` | 156 | START | 156 | 198 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 160 | END | 148 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `21` | `21` | 190 | START | 190 | 270 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `20` | `20` | 214 | START | 214 | 234 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_SnapReceive` | 148 | 160 | 13 | inferred_complete_timeline |
| `Action_None` | 161 | 389 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–345
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_BallCarry` | 190 | 270 | 81 | inferred_complete_timeline |
| `Action_BallCarry` | 273 | 274 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 282 | 299 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 301 | 329 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 337 | 341 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 344 | 345 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 271 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 254 | 107 | inferred_complete_timeline |
| `Action_None` | 258 | 271 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 280 | 133 | inferred_complete_timeline |
| `Action_None` | 288 | 389 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_SplitBlock` | 156 | 198 | 43 | inferred_complete_timeline |
| `Action_None` | 199 | 230 | 32 | inferred_complete_timeline |
| `Action_None` | 232 | 246 | 15 | inferred_complete_timeline |
| `Action_None` | 256 | 258 | 3 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 270 | 8 | inferred_complete_timeline |
| `Action_None` | 272 | 290 | 19 | inferred_complete_timeline |
| `Action_None` | 294 | 299 | 6 | inferred_complete_timeline |
| `Action_None` | 301 | 311 | 11 | inferred_complete_timeline |
| `Action_None` | 316 | 317 | 2 | inferred_complete_timeline |
| `Action_None` | 320 | 389 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 146 | 49 | inferred_complete_timeline |
| `Action_None` | 147 | 230 | 84 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 246 | 8 | inferred_complete_timeline |
| `Action_None` | 249 | 270 | 22 | inferred_complete_timeline |
| `Action_None` | 272 | 283 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 146 | 49 | inferred_complete_timeline |
| `Action_None` | 147 | 213 | 67 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 214 | 234 | 21 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 237 | 241 | 5 | inferred_complete_timeline |
| `Action_None` | 242 | 261 | 20 | inferred_complete_timeline |
| `Action_None` | 290 | 291 | 2 | inferred_complete_timeline |
| `Action_None` | 295 | 296 | 2 | inferred_complete_timeline |
| `Action_None` | 308 | 309 | 2 | inferred_complete_timeline |
| `Action_None` | 317 | 319 | 3 | inferred_complete_timeline |
| `Action_None` | 322 | 389 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 147 | 50 | inferred_complete_timeline |
| `Action_BallSnap` | 148 | 160 | 13 | inferred_complete_timeline |
| `Action_None` | 161 | 206 | 46 | inferred_complete_timeline |
| `Action_None` | 217 | 254 | 38 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 268 | 3 | inferred_complete_timeline |
| `Action_None` | 277 | 281 | 5 | inferred_complete_timeline |
| `Action_None` | 291 | 293 | 3 | inferred_complete_timeline |
| `Action_None` | 295 | 353 | 59 | inferred_complete_timeline |
| `Action_None` | 358 | 360 | 3 | inferred_complete_timeline |
| `Action_None` | 362 | 389 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–385
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 146 | 49 | inferred_complete_timeline |
| `Action_None` | 147 | 197 | 51 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_None` | 210 | 230 | 21 | inferred_complete_timeline |
| `Action_None` | 237 | 240 | 4 | inferred_complete_timeline |
| `Action_None` | 244 | 262 | 19 | inferred_complete_timeline |
| `Action_None` | 265 | 351 | 87 | inferred_complete_timeline |
| `Action_None` | 359 | 369 | 11 | inferred_complete_timeline |
| `Action_None` | 371 | 376 | 6 | inferred_complete_timeline |
| `Action_None` | 384 | 385 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 146 | 49 | inferred_complete_timeline |
| `Action_None` | 147 | 205 | 59 | inferred_complete_timeline |
| `Action_None` | 208 | 236 | 29 | inferred_complete_timeline |
| `Action_None` | 239 | 246 | 8 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 268 | 3 | inferred_complete_timeline |
| `Action_None` | 290 | 389 | 100 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PressEdge` | 111 | 188 | 78 | inferred_complete_timeline |
| `Action_None` | 189 | 240 | 52 | inferred_complete_timeline |
| `Action_None` | 250 | 270 | 21 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 281 | 282 | 2 | inferred_complete_timeline |
| `Action_None` | 285 | 294 | 10 | inferred_complete_timeline |
| `Action_None` | 300 | 305 | 6 | inferred_complete_timeline |
| `Action_None` | 308 | 324 | 17 | inferred_complete_timeline |
| `Action_None` | 326 | 389 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 192 | 45 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 180 | 33 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 205 | 58 | inferred_complete_timeline |
| `Action_None` | 208 | 211 | 4 | inferred_complete_timeline |
| `Action_None` | 213 | 240 | 28 | inferred_complete_timeline |
| `Action_None` | 243 | 246 | 4 | inferred_complete_timeline |
| `Action_None` | 251 | 254 | 4 | inferred_complete_timeline |
| `Action_None` | 257 | 264 | 8 | inferred_complete_timeline |
| `Action_None` | 266 | 268 | 3 | inferred_complete_timeline |
| `Action_None` | 292 | 293 | 2 | inferred_complete_timeline |
| `Action_None` | 295 | 389 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 234 | 87 | inferred_complete_timeline |
| `Action_None` | 250 | 284 | 35 | inferred_complete_timeline |
| `Action_None` | 290 | 303 | 14 | inferred_complete_timeline |
| `Action_None` | 308 | 309 | 2 | inferred_complete_timeline |
| `Action_None` | 316 | 317 | 2 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |
| `Action_None` | 331 | 389 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 236 | 89 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 389 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–301
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 301 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 227 | 80 | inferred_complete_timeline |
| `Action_None` | 233 | 278 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 288 | 141 | inferred_complete_timeline |
| `Action_None` | 290 | 389 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 389 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–310
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 111 | 121 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 122 | 130 | 9 | inferred_complete_timeline |
| `Action_None` | 131 | 290 | 160 | inferred_complete_timeline |
| `Action_None` | 292 | 305 | 14 | inferred_complete_timeline |
| `Action_None` | 308 | 310 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 234–389 | 144 | 5 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 288–389 | 102 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 302–389 | 88 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 309–389 | 80 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 309–389 | 70 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 313–389 | 71 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 317–389 | 73 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 327–389 | 63 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 353–380 | 8 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 368–389 | 19 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `18` (C)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 107 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [148–160], lower_priority='Action_ZoneBlock' annotated_start=98, effective_Action_ZoneBlock_start=161.
- ⚠️ Action 'Action_None' range [148-280] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-254] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-271] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-288] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-389] for track '2' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-271] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-192] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-240] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-270] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-294] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-305] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-324] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [156-198] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-230] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-246] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-270] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-290] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-311] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-290] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-305] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-234] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-284] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-303] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-205] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-236] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-246] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-205] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-240] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-264] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-389] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-301] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-236] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-389] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-227] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-278] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-197] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-230] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-262] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-351] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-369] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-376] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-254] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-353] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-360] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-230] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-246] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-270] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-283] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [214-234] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-261] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [190-270] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [273-274] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [282-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [301-329] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [337-341] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [344-345] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-248] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-262] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-291] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-389] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-389] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-320] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-357] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-371] for track '31' has 1 frames without a visible bounding box.
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

</details>