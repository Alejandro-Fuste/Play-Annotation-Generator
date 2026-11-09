# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_193

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_193`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 149
- **Validation Warnings:** 163
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 106
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_Handoff` | DE1 | defense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | WR1 | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 354 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 161 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 161 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 161 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `21` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 196 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 228 |
| ✅ EXACT | `Action_Handoff` | DE1 | `15` | `15` | 48 | START | 48 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `11` | `11` | 162 | START | 162 | 184 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `14` | 162 | START | 167 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `16` | 162 | START | 167 | 168 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `18` | 162 | START | 162 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 162 | START | 193 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | WR1 | `6` | `6` | 180 | START | 180 | 196 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 245 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 329 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 343 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 348 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 389 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PressEdge` | 180 | 196 | 17 | inferred_complete_timeline |
| `Action_PressEdge` | 201 | 224 | 24 | inferred_complete_timeline |
| `Action_None` | 225 | 297 | 73 | inferred_complete_timeline |
| `Action_None` | 333 | 339 | 7 | inferred_complete_timeline |
| `Action_None` | 341 | 389 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 340 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 355 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 366 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 389 | 20 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 354 | 355 | inferred_complete_timeline |
| `Action_PreSnap` | 362 | 389 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 31 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 69 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 117 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 162 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 290 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 296 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 326 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 329 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 354 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 361 | 389 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 162 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 196 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 208 | 233 | 26 | inferred_complete_timeline |
| `Action_None` | 234 | 296 | 63 | inferred_complete_timeline |
| `Action_None` | 298 | 300 | 3 | inferred_complete_timeline |
| `Action_None` | 303 | 305 | 3 | inferred_complete_timeline |
| `Action_None` | 308 | 314 | 7 | inferred_complete_timeline |
| `Action_None` | 319 | 324 | 6 | inferred_complete_timeline |
| `Action_None` | 330 | 332 | 3 | inferred_complete_timeline |
| `Action_None` | 379 | 385 | 7 | inferred_complete_timeline |
| `Action_None` | 389 | 389 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 170 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 204 | 23 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 233 | 29 | inferred_complete_timeline |
| `Action_None` | 234 | 355 | 122 | inferred_complete_timeline |
| `Action_None` | 357 | 358 | 2 | inferred_complete_timeline |
| `Action_None` | 367 | 389 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 40 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 79 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 160 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 198 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 201 | 233 | 33 | inferred_complete_timeline |
| `Action_None` | 234 | 290 | 57 | inferred_complete_timeline |
| `Action_None` | 292 | 325 | 34 | inferred_complete_timeline |
| `Action_None` | 334 | 335 | 2 | inferred_complete_timeline |
| `Action_None` | 340 | 343 | 4 | inferred_complete_timeline |
| `Action_None` | 345 | 349 | 5 | inferred_complete_timeline |
| `Action_None` | 355 | 359 | 5 | inferred_complete_timeline |
| `Action_None` | 367 | 368 | 2 | inferred_complete_timeline |
| `Action_None` | 370 | 381 | 12 | inferred_complete_timeline |
| `Action_None` | 383 | 388 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 184 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 192 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 198 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 200 | 233 | 34 | inferred_complete_timeline |
| `Action_None` | 234 | 320 | 87 | inferred_complete_timeline |
| `Action_None` | 322 | 341 | 20 | inferred_complete_timeline |
| `Action_None` | 350 | 379 | 30 | inferred_complete_timeline |
| `Action_None` | 386 | 389 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_Handoff` | 48 | 57 | 10 | inferred_complete_timeline |
| `Action_None` | 58 | 279 | 222 | inferred_complete_timeline |
| `Action_None` | 283 | 389 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 196 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 312 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 389 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 216 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 225 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–339
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 296 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 339 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–320
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 311 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 317 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 319 | 320 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–379
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 379 | 380 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 389 | 390 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–350
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 342 | 264 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 346 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 350 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 247 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 290 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 294 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 313 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–362
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 362 | 363 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–376
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 343 | 344 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 349 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 352 | 353 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 366 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 376 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 203–379 | 175 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 243–389 | 147 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 252–389 | 129 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 267–268 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 267–294 | 24 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 286–369 | 31 | 4 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 321–323 | 3 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 329–330 | 2 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 331–332 | 2 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 335–389 | 49 | 6 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 337–379 | 35 | 3 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 366–386 | 19 | 3 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 375–389 | 15 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 387–389 | 3 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 387–389 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 130 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-354] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-340] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-355] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-366] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-343] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-349] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-353] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-366] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-376] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-290] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-296] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-326] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-354] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-389] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-362] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [180-196] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-297] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-339] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-389] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-243] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-247] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-290] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-294] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-313] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-228] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-245] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-343] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-348] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-379] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-186] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-312] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-389] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [186-192] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-198] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-320] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-341] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-379] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-342] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-346] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-350] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-311] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-317] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-320] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [174-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [182-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-279] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-389] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-160] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-168] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-196] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-355] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-389] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-216] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '18' starts at frame 162, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [162-162] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-196] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-296] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-300] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-314] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-324] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-332] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-385] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '19' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-296] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-339] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-40] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-79] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-160] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-198] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [201-233] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-290] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-325] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-343] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-349] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-359] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-381] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-388] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-31] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-117] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-162] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-289] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-379] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-234] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-353] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-268] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-268] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-272] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-294] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-288] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-292] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-323] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-369] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-323] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-330] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-332] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-337] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-340] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-351] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-359] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-379] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-344] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-366] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-379] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-370] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-376] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-386] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-389] for track '35' has 1 frames without a visible bounding box.
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

</details>