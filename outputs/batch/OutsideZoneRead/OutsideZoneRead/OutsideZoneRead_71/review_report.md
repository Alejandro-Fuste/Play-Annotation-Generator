# Play-Annotation-Generator Annotation Review — OutsideZoneRead_71

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_71`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 142
- **Validation Warnings:** 147
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 118
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 479 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 191 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 479 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 445 |
| ✅ EXACT | `Action_PressEdge` | RB | `3` | `3` | 187 | START | 187 | 250 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `10` | 187 | START | 187 | 205 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `11` | 187 | START | 187 | 204 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `17` | 187 | START | 187 | 237 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `21` | 187 | START | 187 | 222 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `5` | 187 | START | 187 | 237 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `14` | `14` | 192 | START | 192 | 205 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `14` | 206 | START | 206 | 214 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 192 | 205 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 206 | 214 | 9 | inferred_complete_timeline |
| `Action_None` | 215 | 379 | 165 | inferred_complete_timeline |
| `Action_None` | 382 | 437 | 56 | inferred_complete_timeline |
| `Action_None` | 440 | 479 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_PressEdge` | 187 | 250 | 64 | inferred_complete_timeline |
| `Action_None` | 251 | 436 | 186 | inferred_complete_timeline |
| `Action_None` | 438 | 479 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 479 | 480 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 479 | 480 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 445 | 446 | inferred_complete_timeline |
| `Action_PreSnap` | 447 | 479 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 213 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 217 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 371 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 479 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 475

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 222 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 225 | 237 | 13 | inferred_complete_timeline |
| `Action_None` | 238 | 436 | 199 | inferred_complete_timeline |
| `Action_None` | 438 | 463 | 26 | inferred_complete_timeline |
| `Action_None` | 466 | 479 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 205 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 222 | 237 | 16 | inferred_complete_timeline |
| `Action_None` | 238 | 251 | 14 | inferred_complete_timeline |
| `Action_None` | 258 | 384 | 127 | inferred_complete_timeline |
| `Action_None` | 408 | 432 | 25 | inferred_complete_timeline |
| `Action_None` | 435 | 436 | 2 | inferred_complete_timeline |
| `Action_None` | 441 | 446 | 6 | inferred_complete_timeline |
| `Action_None` | 457 | 461 | 5 | inferred_complete_timeline |
| `Action_None` | 468 | 469 | 2 | inferred_complete_timeline |
| `Action_None` | 471 | 479 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 204 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 209 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 231 | 237 | 7 | inferred_complete_timeline |
| `Action_None` | 238 | 238 | 1 | inferred_complete_timeline |
| `Action_None` | 241 | 247 | 7 | inferred_complete_timeline |
| `Action_None` | 250 | 252 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 237 | 51 | inferred_complete_timeline |
| `Action_None` | 238 | 277 | 40 | inferred_complete_timeline |
| `Action_None` | 280 | 371 | 92 | inferred_complete_timeline |
| `Action_None` | 373 | 479 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–422
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 237 | 51 | inferred_complete_timeline |
| `Action_None` | 238 | 369 | 132 | inferred_complete_timeline |
| `Action_None` | 373 | 422 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–478
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 262 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 446 | 176 | inferred_complete_timeline |
| `Action_PreSnap` | 449 | 466 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 468 | 472 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 474 | 478 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 219 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 233 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 334 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 344 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 346 | 352 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 363 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 366 | 479 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–320
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 219 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 315 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 320 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–339
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 332 | 333 | inferred_complete_timeline |
| `Action_PreSnap` | 337 | 339 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 332 | 333 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 377 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 380 | 479 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 460

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 337 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 341 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 357 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 364 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 368 | 479 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 372 | 373 | inferred_complete_timeline |
| `Action_PreSnap` | 375 | 377 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 382 | 387 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 390 | 392 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 395 | 416 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 418 | 419 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 424 | 428 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 443 | 445 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 450 | 456 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 458 | 479 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–414
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 372 | 373 | inferred_complete_timeline |
| `Action_PreSnap` | 375 | 379 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 383 | 385 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 391 | 392 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 397 | 399 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 404 | 405 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 409 | 414 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–434
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 434 | 435 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 262 | 263 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 479 | 214 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 259–431 | 157 | 8 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 271–473 | 182 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 272–274 | 3 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 334–430 | 83 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 339–360 | 22 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 384–475 | 24 | 6 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 398–399 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 433–444 | 9 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 437–476 | 39 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 446–448 | 3 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 458–479 | 19 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 461–466 | 5 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 476–479 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 120 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-479] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-332] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-377] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-479] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-436] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-213] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-217] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-371] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-479] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-369] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-422] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-213] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-219] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-233] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-328] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-334] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-344] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-352] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-363] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-479] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-445] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-212] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-219] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-315] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-320] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [187-205] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [212-213] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [216-217] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [219-220] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-251] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-384] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-432] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-446] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-461] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [187-204] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-209] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [216-218] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [224-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 238, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [238-238] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-247] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-332] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-339] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-262] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-379] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-437] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-479] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-372] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-377] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-387] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-392] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-416] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-419] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-428] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-445] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-456] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-206] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-337] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-341] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-357] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-364] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-479] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-277] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-371] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-372] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-379] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-385] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-392] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-399] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-405] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-414] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-208] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-262] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-446] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [449-466] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [468-472] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-478] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-434] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [187-222] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-436] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-463] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-309] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-371] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-377] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-380] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-392] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-400] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-422] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-431] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-368] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-442] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-445] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [458-461] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [469-473] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-274] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-344] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-430] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-360] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-385] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-391] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-416] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-429] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-446] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-475] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-399] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-439] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-444] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-473] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [475-476] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-448] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [458-462] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-479] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-463] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [465-466] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-479] for track '34' has 1 frames without a visible bounding box.
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