# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_158

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_158`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Tackle`
- **Result Frame:** 509
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 186
- **Validation Warnings:** 226
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
- **Inferred Coverage Segments (Action_None):** 150
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `1` | `1` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 313 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 361 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 90 | START | 90 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `15` | `15` | 90 | START | 90 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `17` | 90 | START | 90 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `20` | 90 | START | 90 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `21` | 90 | START | 90 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `1` | `1` | 191 | START | 191 | 212 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 207 | START | 207 | 217 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_Handoff` | 207 | 217 | 11 | inferred_complete_timeline |
| `Action_None` | 218 | 241 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–364
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_PressEdge` | 191 | 212 | 22 | inferred_complete_timeline |
| `Action_PressEdge` | 214 | 220 | 7 | inferred_complete_timeline |
| `Action_PressEdge` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_PressEdge` | 227 | 270 | 44 | inferred_complete_timeline |
| `Action_None` | 271 | 278 | 8 | inferred_complete_timeline |
| `Action_None` | 282 | 364 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 361 | 362 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 382 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 402 | 436 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 442 | 445 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 452 | 453 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 456 | 509 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–504
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 313 | 314 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 344 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 386 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 389 | 432 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 436 | 437 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 482 | 485 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 487 | 488 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 497 | 498 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 503 | 504 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 202 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 203 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 214 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 248 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 253 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 481

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 189 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 199 | 217 | 19 | inferred_complete_timeline |
| `Action_None` | 219 | 223 | 5 | inferred_complete_timeline |
| `Action_None` | 225 | 320 | 96 | inferred_complete_timeline |
| `Action_None` | 322 | 332 | 11 | inferred_complete_timeline |
| `Action_None` | 337 | 342 | 6 | inferred_complete_timeline |
| `Action_None` | 344 | 369 | 26 | inferred_complete_timeline |
| `Action_None` | 373 | 397 | 25 | inferred_complete_timeline |
| `Action_None` | 401 | 404 | 4 | inferred_complete_timeline |
| `Action_None` | 408 | 430 | 23 | inferred_complete_timeline |
| `Action_None` | 432 | 459 | 28 | inferred_complete_timeline |
| `Action_None` | 462 | 509 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 189 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 204 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 189 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 199 | 201 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 217 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 189 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 199 | 201 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 212 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 460

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 189 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 199 | 202 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 217 | 11 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |
| `Action_None` | 253 | 486 | 234 | inferred_complete_timeline |
| `Action_None` | 491 | 509 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 204 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 217 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 235 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 241 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 248 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 280 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 287 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–457
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 202 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 220 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 393 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 395 | 397 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 413 | 457 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 223 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 486

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 204 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 216 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 333 | 107 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 379 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 381 | 494 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 496 | 509 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 265 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 268 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–364
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 364 | 365 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–321
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 321 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–411
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 411 | 412 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–506 | 506 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 200–509 | 247 | 8 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 200–509 | 288 | 7 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 214–434 | 210 | 3 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 216–305 | 81 | 2 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 228–509 | 282 | 1 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 228–506 | 254 | 8 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 231–264 | 7 | 3 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 246–260 | 13 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 255–509 | 255 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 267–492 | 222 | 4 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 270–271 | 2 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 276–509 | 227 | 2 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 284–290 | 7 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 288–509 | 199 | 10 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 304–503 | 171 | 7 | Undefined position; Undefined team |
| `37` | `40` | Position_Unknown | Team_Unknown | 326–327 | 2 | 1 | Undefined position; Undefined team |
| `38` | `41` | Position_Unknown | Team_Unknown | 341–509 | 163 | 3 | Undefined position; Undefined team |
| `39` | `42` | Position_Unknown | Team_Unknown | 358–373 | 16 | 1 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 375–509 | 114 | 6 | Undefined position; Undefined team |
| `41` | `49` | Position_Unknown | Team_Unknown | 381–509 | 116 | 2 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 384–498 | 33 | 6 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 387–500 | 88 | 5 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 396–397 | 2 | 1 | Undefined position; Undefined team |
| `45` | `56` | Position_Unknown | Team_Unknown | 417–509 | 93 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `1` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `SAF1` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 169 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '814' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 128 frames exceeds threshold 90 frames [start=90, end=217].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (RG) duration 123 frames exceeds threshold 90 frames [start=90, end=212].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (LG) duration 115 frames exceeds threshold 90 frames [start=90, end=204].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 129 frames exceeds threshold 90 frames [start=90, end=218].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 129 frames exceeds threshold 90 frames [start=90, end=218].
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-202] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [191-212] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [214-220] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [223-224] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-278] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-364] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-313] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-344] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-386] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-432] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-437] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [482-485] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-488] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [497-498] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [503-504] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-411] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-217] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-235] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-241] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-248] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-280] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-284] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-361] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-382] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-436] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-445] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-453] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [456-509] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-190] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-225] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-268] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-246] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-265] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-202] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-220] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-393] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-397] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-457] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-204] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-216] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-333] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-379] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-494] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-189] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [199-201] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [210-217] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-451] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [453-506] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-189] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [199-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-204] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-212] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-190] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-203] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-214] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-248] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-189] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [199-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-204] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-364] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-321] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [199-217] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-320] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-332] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-342] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-369] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-397] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-404] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-430] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-459] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-509] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-189] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [199-202] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-486] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-205] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-218] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-221] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-333] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-345] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-356] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-384] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-204] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-217] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-257] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-332] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-415] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-509] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-217] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-265] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-434] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-305] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-387] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-393] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-404] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-462] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [465-469] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [471-485] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-489] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [503-506] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-233] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-256] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-260] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-381] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-386] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-488] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [491-492] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-271] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-422] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-509] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-290] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-332] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-366] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-369] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-377] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-381] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-397] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-402] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-405] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-333] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-369] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-375] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-466] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [469-477] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [482-488] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [502-503] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-327] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-344] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-468] for track '38' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [472-509] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-373] for track '39' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-386] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-397] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-413] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-424] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [429-505] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-471] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [485-509] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-397] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-400] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-409] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-417] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-429] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [497-498] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-461] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-467] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-476] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [488-490] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [499-500] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-397] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>