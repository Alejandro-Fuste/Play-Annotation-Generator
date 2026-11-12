# Play-Annotation-Generator Annotation Review — SplitZone_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_31`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 539
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `17` | `17` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `23` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `16` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 18 | START | 18 | 304 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 18 | START | 18 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 18 | START | 18 | 276 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 18 | START | 18 | 336 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 18 | START | 18 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 18 | START | 18 | 276 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 18 | START | 18 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 18 | START | 37 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 18 | START | 18 | 276 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 18 | START | 18 | 276 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 18 | START | 18 | 299 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 277 | START | 277 | 311 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `13` | 300 | START | 300 | 393 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `17` | `17` | 300 | START | 300 | 331 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `19` | `19` | 300 | START | 312 | 393 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `23` | `21` | 300 | START | 300 | 347 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `7` | 300 | START | 300 | 330 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `10` | `10` | 305 | START | 305 | 393 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 311 | END | 277 | 311 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `20` | 323 | START | 323 | 346 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `7` | `7` | 331 | START | 331 | 393 |
| ✅ EXACT | `Action_BallCarry` | RB | `16` | `16` | 347 | START | 347 | 517 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 393 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 18–466
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 22 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 276 | 250 | inferred_complete_timeline |
| `Action_SnapReceive` | 277 | 311 | 35 | inferred_complete_timeline |
| `Action_None` | 312 | 322 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 323 | 346 | 24 | inferred_complete_timeline |
| `Action_None` | 347 | 466 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 18–517
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 336 | 319 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 346 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 347 | 517 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 18–539
- **Visible Samples:** 522

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 276 | 259 | inferred_complete_timeline |
| `Action_None` | 277 | 539 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 18–539
- **Visible Samples:** 517

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 276 | 259 | inferred_complete_timeline |
| `Action_None` | 277 | 433 | 157 | inferred_complete_timeline |
| `Action_None` | 436 | 528 | 93 | inferred_complete_timeline |
| `Action_None` | 532 | 539 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 18–360
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 276 | 259 | inferred_complete_timeline |
| `Action_None` | 277 | 360 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 18–480
- **Visible Samples:** 460

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 304 | 287 | inferred_complete_timeline |
| `Action_SplitBlock` | 305 | 393 | 89 | inferred_complete_timeline |
| `Action_None` | 394 | 403 | 10 | inferred_complete_timeline |
| `Action_None` | 407 | 480 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 18–360
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 299 | 282 | inferred_complete_timeline |
| `Action_ZoneBlock` | 300 | 331 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 333 | 337 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 344 | 346 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 352 | 360 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 18–539
- **Visible Samples:** 522

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 299 | 282 | inferred_complete_timeline |
| `Action_ZoneBlock` | 300 | 330 | 31 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 331 | 393 | 63 | inferred_complete_timeline |
| `Action_None` | 394 | 539 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 18–482
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 276 | 259 | inferred_complete_timeline |
| `Action_BallSnap` | 277 | 311 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 312 | 393 | 82 | inferred_complete_timeline |
| `Action_None` | 394 | 482 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 37–347
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 48 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 92 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 299 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 300 | 347 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 18–487
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 299 | 282 | inferred_complete_timeline |
| `Action_ZoneBlock` | 300 | 393 | 94 | inferred_complete_timeline |
| `Action_None` | 394 | 487 | 94 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 18–404
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 276 | 259 | inferred_complete_timeline |
| `Action_None` | 277 | 398 | 122 | inferred_complete_timeline |
| `Action_None` | 403 | 404 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 18–539
- **Visible Samples:** 522

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 276 | 259 | inferred_complete_timeline |
| `Action_None` | 277 | 539 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 18–539
- **Visible Samples:** 520

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 276 | 259 | inferred_complete_timeline |
| `Action_None` | 277 | 479 | 203 | inferred_complete_timeline |
| `Action_None` | 481 | 487 | 7 | inferred_complete_timeline |
| `Action_None` | 489 | 539 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 18–492
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 276 | 259 | inferred_complete_timeline |
| `Action_None` | 277 | 371 | 95 | inferred_complete_timeline |
| `Action_None` | 380 | 381 | 2 | inferred_complete_timeline |
| `Action_None` | 383 | 384 | 2 | inferred_complete_timeline |
| `Action_None` | 387 | 492 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 18–486
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 276 | 259 | inferred_complete_timeline |
| `Action_None` | 277 | 486 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 18–539
- **Visible Samples:** 522

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 276 | 259 | inferred_complete_timeline |
| `Action_None` | 277 | 539 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 18–539
- **Visible Samples:** 522

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 276 | 259 | inferred_complete_timeline |
| `Action_None` | 277 | 539 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 18–539
- **Visible Samples:** 516

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 276 | 259 | inferred_complete_timeline |
| `Action_None` | 277 | 509 | 233 | inferred_complete_timeline |
| `Action_None` | 514 | 531 | 18 | inferred_complete_timeline |
| `Action_None` | 534 | 539 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 18–497
- **Visible Samples:** 475

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 276 | 259 | inferred_complete_timeline |
| `Action_None` | 277 | 358 | 82 | inferred_complete_timeline |
| `Action_None` | 364 | 497 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 18–539
- **Visible Samples:** 522

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 276 | 259 | inferred_complete_timeline |
| `Action_None` | 277 | 539 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 18–539
- **Visible Samples:** 522

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 276 | 259 | inferred_complete_timeline |
| `Action_None` | 277 | 539 | 263 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 72–78 | 7 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 130–143 | 14 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 358–539 | 182 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 368–539 | 172 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 369–491 | 88 | 10 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 374–482 | 108 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 389–405 | 4 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 420–481 | 62 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 431–432 | 2 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 483–489 | 7 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 495–521 | 8 | 3 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 505–539 | 35 | 1 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 508–539 | 32 | 1 | Undefined position; Undefined team |
| `36` | `58` | Position_Unknown | Team_Unknown | 510–539 | 30 | 1 | Undefined position; Undefined team |
| `37` | `59` | Position_Unknown | Team_Unknown | 510–539 | 30 | 1 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 510–539 | 30 | 1 | Undefined position; Undefined team |
| `39` | `61` | Position_Unknown | Team_Unknown | 512–533 | 10 | 2 | Undefined position; Undefined team |
| `40` | `62` | Position_Unknown | Team_Unknown | 515–539 | 25 | 1 | Undefined position; Undefined team |
| `41` | `66` | Position_Unknown | Team_Unknown | 523–539 | 17 | 1 | Undefined position; Undefined team |
| `42` | `67` | Position_Unknown | Team_Unknown | 523–524 | 2 | 1 | Undefined position; Undefined team |
| `43` | `70` | Position_Unknown | Team_Unknown | 526–536 | 8 | 2 | Undefined position; Undefined team |
| `44` | `72` | Position_Unknown | Team_Unknown | 535–539 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (4 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `19` (C): Annotated start 300 != Inferred start 312

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (RT) duration 94 frames exceeds threshold 90 frames [start=300, end=393].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (C) duration 94 frames exceeds threshold 90 frames [start=300, end=393].
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [277–311], lower_priority='Action_ZoneBlock' annotated_start=300, effective_Action_ZoneBlock_start=312.
- ⚠️ Action 'Action_None' range [277-371] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-492] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-479] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-487] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-398] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-539] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-433] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-528] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-539] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-403] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-480] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-358] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-497] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-487] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-509] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-531] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-360] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-336] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [347-517] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [300-331] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [333-337] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [344-346] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [352-360] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-486] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-482] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-22] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-466] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [300-347] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-78] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-143] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-373] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-385] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-405] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-426] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-440] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-458] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-473] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-485] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-384] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-482] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-481] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-489] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-496] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-511] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-539] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-539] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-517] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-533] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-524] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-529] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-536] for track '43' has 1 frames without a visible bounding box.
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

</details>