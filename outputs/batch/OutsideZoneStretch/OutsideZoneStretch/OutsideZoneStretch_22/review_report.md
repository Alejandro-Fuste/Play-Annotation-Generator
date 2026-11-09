# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_22

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_22`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 60
- **Ball Tracks:** 0
- **Action Segments:** 238
- **Validation Warnings:** 312
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 214
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `3` | `3` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 207 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 88 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `13` | `13` | 89 | START | 89 | 118 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | `18` | `18` | 89 | START | 90 | 107 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `7` | 89 | START | 89 | 128 |
| ✅ EXACT | `Action_ZoneBlock` | C | `9` | `9` | 89 | START | 89 | 102 |
| ✅ EXACT | `Action_PressEdge` | RB | `3` | `3` | 97 | START | 97 | 157 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `19` | `19` | 109 | START | 109 | 126 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PressEdge` | 97 | 157 | 61 | inferred_complete_timeline |
| `Action_None` | 158 | 449 | 292 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–417
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 205 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 227 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 283 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 333 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 337 | 417 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 283 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 330 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 379 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 383 | 387 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 389 | 449 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 128 | 40 | inferred_complete_timeline |
| `Action_None` | 129 | 153 | 25 | inferred_complete_timeline |
| `Action_None` | 156 | 158 | 3 | inferred_complete_timeline |
| `Action_None` | 164 | 205 | 42 | inferred_complete_timeline |
| `Action_None` | 227 | 229 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 118 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 102 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 107 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 316 | 317 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 427 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 439 | 449 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 327 | 328 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 345 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 350 | 353 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 356 | 390 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 393 | 399 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 401 | 408 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 412 | 428 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 435 | 440 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 443 | 449 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 174 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 195 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 201 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 207 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 238 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 247 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 257 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 449 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 194 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 314 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 340 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 356 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 449 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 342 | 343 | inferred_complete_timeline |
| `Action_PreSnap` | 344 | 384 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 386 | 412 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 414 | 449 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 449 | 450 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 335 | 336 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 342 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 344 | 347 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 359 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 362 | 366 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 374 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 377 | 379 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 383 | 403 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 422 | 437 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 439 | 449 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 206 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 216 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 310 | 311 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 341 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 361 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 367 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 375 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 379 | 382 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 384 | 385 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 390 | 391 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 396 | 398 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 405 | 411 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 413 | 426 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 431 | 449 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–131 | 132 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 3–449 | 444 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 3–107 | 98 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 5–422 | 370 | 15 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 114–207 | 61 | 8 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 128–434 | 282 | 8 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 149–449 | 271 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 152–449 | 220 | 17 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 160–206 | 36 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 199–408 | 203 | 7 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 206–272 | 8 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 214–217 | 4 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 215–449 | 223 | 6 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 218–449 | 203 | 10 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 228–233 | 6 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 229–449 | 213 | 5 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 240–241 | 2 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 244–417 | 159 | 3 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 245–246 | 2 | 1 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 249–250 | 2 | 1 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 260–261 | 2 | 1 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 263–264 | 2 | 1 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 302–308 | 6 | 2 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 303–407 | 38 | 10 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 304–449 | 144 | 3 | Undefined position; Undefined team |
| `45` | `57` | Position_Unknown | Team_Unknown | 322–335 | 13 | 2 | Undefined position; Undefined team |
| `46` | `58` | Position_Unknown | Team_Unknown | 324–326 | 3 | 1 | Undefined position; Undefined team |
| `47` | `59` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |
| `48` | `60` | Position_Unknown | Team_Unknown | 337–382 | 11 | 4 | Undefined position; Undefined team |
| `49` | `62` | Position_Unknown | Team_Unknown | 341–342 | 2 | 1 | Undefined position; Undefined team |
| `50` | `64` | Position_Unknown | Team_Unknown | 348–363 | 13 | 3 | Undefined position; Undefined team |
| `51` | `67` | Position_Unknown | Team_Unknown | 369–370 | 2 | 1 | Undefined position; Undefined team |
| `52` | `70` | Position_Unknown | Team_Unknown | 388–415 | 4 | 2 | Undefined position; Undefined team |
| `53` | `72` | Position_Unknown | Team_Unknown | 396–434 | 26 | 4 | Undefined position; Undefined team |
| `54` | `75` | Position_Unknown | Team_Unknown | 408–443 | 19 | 2 | Undefined position; Undefined team |
| `55` | `78` | Position_Unknown | Team_Unknown | 414–416 | 3 | 1 | Undefined position; Undefined team |
| `56` | `82` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `57` | `83` | Position_Unknown | Team_Unknown | 431–434 | 4 | 1 | Undefined position; Undefined team |
| `58` | `84` | Position_Unknown | Team_Unknown | 433–449 | 14 | 3 | Undefined position; Undefined team |
| `59` | `86` | Position_Unknown | Team_Unknown | 448–449 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `18` (RG): Annotated start 89 != Inferred start 90

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 42 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 42 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 84 |
| Missing visible bounding boxes during action | 227 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-184] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-205] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-227] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-283] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-333] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-417] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-449] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-184] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-206] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-216] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [97-157] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-449] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-335] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-342] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-347] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-359] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-366] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-374] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-379] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-403] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-437] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-207] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-283] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-330] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-379] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-387] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-449] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-205] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-310] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-341] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-361] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-367] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-375] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-382] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-385] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-391] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-398] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-411] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-426] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-449] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-342] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-384] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-412] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-164] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-314] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-340] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-356] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-316] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-427] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-449] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-195] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-201] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-207] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-238] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-247] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-257] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-449] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-174] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-131] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-327] for track '17' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-345] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-353] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-390] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-399] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-408] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-428] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-440] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-88] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-379] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-449] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-12] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-29] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-85] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-101] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-107] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-8] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-12] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-115] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-127] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-194] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-201] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-207] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-409] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-417] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-422] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-140] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-167] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-172] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-194] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-201] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-140] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-263] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-270] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-308] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-336] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-342] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-434] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-224] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-232] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-429] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-449] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-219] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-226] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-232] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-241] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-244] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-257] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-261] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-297] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-313] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-333] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-372] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-401] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-410] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-413] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-449] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-182] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-194] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-204] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-231] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-390] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-393] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-403] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-408] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-272] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-217] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-337] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-349] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-353] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-361] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-411] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-449] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-234] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-241] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-258] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-286] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-372] for track '32' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-379] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-387] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-400] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-233] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-235] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-379] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-387] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-398] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-449] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-241] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-295] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-314] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-417] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-261] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-305] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-308] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-309] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-312] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-329] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-342] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-349] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-353] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-365] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-376] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-400] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-407] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-306] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-315] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-449] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-323] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-335] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-326] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-329] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-341] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-350] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-378] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-382] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-342] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-352] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-357] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-363] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-370] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-389] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-415] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-407] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-414] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-422] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-434] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-423] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-443] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-416] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-434] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-434] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-445] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-449] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [448-449] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.

</details>