# Play-Annotation-Generator Annotation Review — InsideZoneRead_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_19`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 479
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `15` | `14` |
| ⚠️ START CHANGED | `Action_Handoff` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 252 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 0 | START | 0 | 252 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 252 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 252 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 252 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 254 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 254 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 289 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 254 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `9` | `Group` | 0 | START | 0 | 252 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 253 | START | 253 | 265 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `18` | 255 | START | 286 | 289 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 255 | START | 255 | 343 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 255 | START | 255 | 267 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 255 | START | 255 | 278 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `7` | `6` | 255 | START | 255 | 303 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 265 | END | 253 | 265 |
| ✅ EXACT | `Action_ReadDefender` | QB | `15` | `14` | 268 | START | 268 | 280 |
| ⚠️ START CHANGED | `Action_Handoff` | QB | `15` | `14` | 284 | START | 285 | 289 |
| ✅ EXACT | `Action_BallCarry` | RB | `4` | `3` | 290 | START | 290 | 384 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `19` | `18` | 290 | START | 290 | 325 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 360 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–453
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_SnapReceive` | 253 | 265 | 13 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 268 | 280 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 285 | 289 | 5 | inferred_complete_timeline |
| `Action_None` | 290 | 453 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–384
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 289 | 290 | inferred_complete_timeline |
| `Action_BallCarry` | 290 | 384 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_None` | 253 | 479 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_None` | 253 | 295 | 43 | inferred_complete_timeline |
| `Action_None` | 297 | 479 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–386
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_None` | 253 | 386 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 472

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_None` | 253 | 440 | 188 | inferred_complete_timeline |
| `Action_None` | 445 | 451 | 7 | inferred_complete_timeline |
| `Action_None` | 453 | 454 | 2 | inferred_complete_timeline |
| `Action_None` | 458 | 479 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 254 | 255 | inferred_complete_timeline |
| `Action_ZoneBlock` | 255 | 303 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 315 | 354 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–369
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 254 | 255 | inferred_complete_timeline |
| `Action_ZoneBlock` | 255 | 343 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 347 | 357 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 360 | 360 | 1 | inferred_complete_timeline |
| `Action_None` | 361 | 361 | 1 | inferred_complete_timeline |
| `Action_None` | 368 | 369 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_BallSnap` | 253 | 265 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 286 | 289 | 4 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 290 | 325 | 36 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 354 | 355 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 254 | 181 | inferred_complete_timeline |
| `Action_ZoneBlock` | 255 | 278 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 282 | 360 | 79 | inferred_complete_timeline |
| `Action_None` | 361 | 449 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 254 | 255 | inferred_complete_timeline |
| `Action_ZoneBlock` | 255 | 267 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 271 | 295 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 302 | 360 | 59 | inferred_complete_timeline |
| `Action_None` | 361 | 448 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–464
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_None` | 253 | 354 | 102 | inferred_complete_timeline |
| `Action_None` | 358 | 362 | 5 | inferred_complete_timeline |
| `Action_None` | 367 | 373 | 7 | inferred_complete_timeline |
| `Action_None` | 375 | 464 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–311
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_None` | 253 | 281 | 29 | inferred_complete_timeline |
| `Action_None` | 285 | 288 | 4 | inferred_complete_timeline |
| `Action_None` | 306 | 311 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–429
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_None` | 253 | 355 | 103 | inferred_complete_timeline |
| `Action_None` | 382 | 429 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–404
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_None` | 253 | 366 | 114 | inferred_complete_timeline |
| `Action_None` | 380 | 386 | 7 | inferred_complete_timeline |
| `Action_None` | 392 | 397 | 6 | inferred_complete_timeline |
| `Action_None` | 399 | 404 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_None` | 253 | 479 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_None` | 253 | 479 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_None` | 253 | 479 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_None` | 253 | 295 | 43 | inferred_complete_timeline |
| `Action_None` | 297 | 479 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–457
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_None` | 253 | 445 | 193 | inferred_complete_timeline |
| `Action_None` | 454 | 457 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–477
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_None` | 253 | 477 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_None` | 253 | 379 | 127 | inferred_complete_timeline |
| `Action_None` | 386 | 404 | 19 | inferred_complete_timeline |
| `Action_None` | 406 | 407 | 2 | inferred_complete_timeline |
| `Action_None` | 415 | 417 | 3 | inferred_complete_timeline |
| `Action_None` | 419 | 479 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 289–323 | 34 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 328–479 | 152 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 340–463 | 122 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 383–430 | 48 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 383–418 | 36 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 388–457 | 69 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 389–390 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 397–479 | 83 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 455–471 | 17 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 457–463 | 7 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 461–462 | 2 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 466–479 | 9 | 3 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 472–473 | 2 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 479–479 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `15` (QB): Annotated start 284 != Inferred start 285
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (LT) duration 100 frames exceeds threshold 90 frames [start=255, end=354].
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [253–265], lower_priority='Action_ZoneBlock' annotated_start=255, effective_Action_ZoneBlock_start=266.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 106 frames exceeds threshold 90 frames [start=255, end=360].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RT) duration 106 frames exceeds threshold 90 frames [start=255, end=360].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 106 frames exceeds threshold 90 frames [start=255, end=360].
- ⚠️ Action 'Action_None' range [253-295] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-477] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [290-384] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-445] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-457] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [255-303] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [315-354] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-440] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-451] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-386] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-295] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-379] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-404] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-417] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-479] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-281] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-311] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [268-280] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-453] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-366] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-386] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-397] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-404] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-354] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-362] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-373] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-464] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-355] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-429] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [253-265] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [290-325] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [354-355] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [255-343] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [347-357] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 361, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [361-361] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [255-267] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [271-295] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [302-360] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-448] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-254] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [255-278] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [282-360] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-449] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-320] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-347] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-463] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-430] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-418] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-402] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-457] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-471] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-463] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-462] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-468] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-475] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-479] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '34' has 1 frames without a visible bounding box.
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

</details>