# Play-Annotation-Generator Annotation Review — SplitZone_79

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_79`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 509
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 124
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | DT1 | defense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `16` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 11 | START | 12 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 11 | START | 12 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 11 | START | 12 | 291 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 11 | START | 12 | 278 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 11 | START | 12 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 11 | START | 12 | 205 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 11 | START | 12 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 11 | START | 12 | 278 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 11 | START | 12 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 11 | START | 12 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 11 | START | 12 | 279 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 276 | START | 276 | 288 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `14` | 279 | START | 279 | 292 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `18` | 279 | START | 281 | 300 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 279 | START | 289 | 306 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 279 | START | 279 | 284 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `21` | 279 | START | 279 | 332 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `8` | `8` | 280 | START | 280 | 283 |
| ✅ EXACT | `Action_SnapReceive` | DT1 | `12` | `12` | 288 | END | 276 | 288 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `13` | 292 | START | 292 | 299 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `16` | `16` | 300 | START | 300 | 311 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 430 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 12–509
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 291 | 280 | inferred_complete_timeline |
| `Action_Handoff` | 292 | 299 | 8 | inferred_complete_timeline |
| `Action_None` | 300 | 509 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 12–509
- **Visible Samples:** 494

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 299 | 288 | inferred_complete_timeline |
| `Action_BallCarry` | 300 | 311 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 316 | 509 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 12–509
- **Visible Samples:** 491

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 275 | 264 | inferred_complete_timeline |
| `Action_None` | 276 | 480 | 205 | inferred_complete_timeline |
| `Action_None` | 483 | 495 | 13 | inferred_complete_timeline |
| `Action_None` | 497 | 500 | 4 | inferred_complete_timeline |
| `Action_None` | 505 | 509 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 12–323
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 275 | 264 | inferred_complete_timeline |
| `Action_None` | 276 | 323 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 12–509
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 275 | 264 | inferred_complete_timeline |
| `Action_None` | 276 | 509 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 12–509
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 279 | 268 | inferred_complete_timeline |
| `Action_SplitBlock` | 280 | 283 | 4 | inferred_complete_timeline |
| `Action_SplitBlock` | 341 | 344 | 4 | inferred_complete_timeline |
| `Action_SplitBlock` | 348 | 350 | 3 | inferred_complete_timeline |
| `Action_SplitBlock` | 353 | 430 | 78 | inferred_complete_timeline |
| `Action_None` | 431 | 441 | 11 | inferred_complete_timeline |
| `Action_None` | 447 | 473 | 27 | inferred_complete_timeline |
| `Action_None` | 480 | 482 | 3 | inferred_complete_timeline |
| `Action_None` | 489 | 494 | 6 | inferred_complete_timeline |
| `Action_None` | 500 | 509 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 12–330
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 205 | 194 | inferred_complete_timeline |
| `Action_ZoneBlock` | 281 | 300 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 324 | 330 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 12–505
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 278 | 267 | inferred_complete_timeline |
| `Action_ZoneBlock` | 279 | 292 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 294 | 297 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 299 | 300 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 303 | 334 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 337 | 339 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 344 | 430 | 87 | inferred_complete_timeline |
| `Action_None` | 431 | 476 | 46 | inferred_complete_timeline |
| `Action_None` | 504 | 505 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 12–311
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 275 | 264 | inferred_complete_timeline |
| `Action_BallSnap` | 276 | 288 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 289 | 306 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 310 | 311 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 12–509
- **Visible Samples:** 490

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 278 | 267 | inferred_complete_timeline |
| `Action_ZoneBlock` | 279 | 284 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 287 | 295 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 299 | 301 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 306 | 358 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 360 | 430 | 71 | inferred_complete_timeline |
| `Action_None` | 431 | 509 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 12–509
- **Visible Samples:** 486

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 63 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 278 | 212 | inferred_complete_timeline |
| `Action_ZoneBlock` | 279 | 332 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 335 | 430 | 96 | inferred_complete_timeline |
| `Action_None` | 431 | 509 | 79 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 12–398
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 275 | 264 | inferred_complete_timeline |
| `Action_None` | 276 | 326 | 51 | inferred_complete_timeline |
| `Action_None` | 328 | 398 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 12–504
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 275 | 264 | inferred_complete_timeline |
| `Action_None` | 276 | 504 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 12–357
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 275 | 264 | inferred_complete_timeline |
| `Action_SnapReceive` | 276 | 288 | 13 | inferred_complete_timeline |
| `Action_None` | 289 | 344 | 56 | inferred_complete_timeline |
| `Action_None` | 347 | 348 | 2 | inferred_complete_timeline |
| `Action_None` | 352 | 357 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 12–509
- **Visible Samples:** 473

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 275 | 264 | inferred_complete_timeline |
| `Action_None` | 276 | 384 | 109 | inferred_complete_timeline |
| `Action_None` | 392 | 397 | 6 | inferred_complete_timeline |
| `Action_None` | 415 | 416 | 2 | inferred_complete_timeline |
| `Action_None` | 418 | 509 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 12–509
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 275 | 264 | inferred_complete_timeline |
| `Action_None` | 276 | 481 | 206 | inferred_complete_timeline |
| `Action_None` | 483 | 509 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 12–509
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 275 | 264 | inferred_complete_timeline |
| `Action_None` | 276 | 373 | 98 | inferred_complete_timeline |
| `Action_None` | 404 | 419 | 16 | inferred_complete_timeline |
| `Action_None` | 435 | 442 | 8 | inferred_complete_timeline |
| `Action_None` | 448 | 451 | 4 | inferred_complete_timeline |
| `Action_None` | 464 | 472 | 9 | inferred_complete_timeline |
| `Action_None` | 474 | 475 | 2 | inferred_complete_timeline |
| `Action_None` | 484 | 509 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 12–492
- **Visible Samples:** 481

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 275 | 264 | inferred_complete_timeline |
| `Action_None` | 276 | 492 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 12–509
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 275 | 264 | inferred_complete_timeline |
| `Action_None` | 276 | 509 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 12–509
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 275 | 264 | inferred_complete_timeline |
| `Action_None` | 276 | 324 | 49 | inferred_complete_timeline |
| `Action_None` | 330 | 369 | 40 | inferred_complete_timeline |
| `Action_None` | 389 | 440 | 52 | inferred_complete_timeline |
| `Action_None` | 445 | 509 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 12–509
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 275 | 264 | inferred_complete_timeline |
| `Action_None` | 276 | 400 | 125 | inferred_complete_timeline |
| `Action_None` | 402 | 421 | 20 | inferred_complete_timeline |
| `Action_None` | 424 | 500 | 77 | inferred_complete_timeline |
| `Action_None` | 504 | 509 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 12–509 | 497 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 313–509 | 170 | 7 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 325–329 | 5 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 330–331 | 2 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 347–348 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 361–390 | 17 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 361–375 | 13 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 381–460 | 80 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 394–509 | 108 | 3 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 417–509 | 93 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 430–431 | 2 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 471–509 | 35 | 3 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 484–509 | 26 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `8` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 82 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (LG) duration 152 frames exceeds threshold 90 frames [start=279, end=430].
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [276–288], lower_priority='Action_ZoneBlock' annotated_start=279, effective_Action_ZoneBlock_start=289.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RG) duration 152 frames exceeds threshold 90 frames [start=279, end=430].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 152 frames exceeds threshold 90 frames [start=279, end=430].
- ⚠️ Action 'Action_None' range [276-323] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-324] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-369] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-440] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-504] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-480] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-495] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-500] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-322] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-481] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [280-283] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [341-344] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [348-350] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-441] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-473] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-482] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-494] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-400] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-421] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-500] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-492] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-326] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-398] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-344] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-357] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [279-292] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [294-297] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [299-300] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [303-334] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [337-339] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [344-430] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-476] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-505] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-373] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-419] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-442] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-451] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-472] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [300-311] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [316-509] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-384] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-397] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-509] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [281-300] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [324-330] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [289-306] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [310-311] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [279-284] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [287-295] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [299-301] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [303-304] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [306-358] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-509] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-63] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [279-332] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-360] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-389] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-402] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-476] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-368] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-376] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-390] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-364] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-369] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-375] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-460] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-439] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-462] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-509] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-474] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-480] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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

</details>