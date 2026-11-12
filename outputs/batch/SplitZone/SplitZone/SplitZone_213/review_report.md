# Play-Annotation-Generator Annotation Review — SplitZone_213

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_213`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ⚠️ END CHANGED | `Action_SnapReceive` | CB2 | defense | `10` | `10` |
| ✅ EXACT | `Action_BallSnap` | DT2 | defense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LB1 | defense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | CB2 | defense | `10` | `10` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_BlockSecondLevel` | SAF1 | defense | `12` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 265 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 232 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 232 |
| ⚠️ END CHANGED | `Action_SnapReceive` | CB2 | `10` | `10` | 226 | END | 233 | 233 |
| ✅ EXACT | `Action_BallSnap` | DT2 | `16` | `16` | 233 | START | 233 | 233 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `0` | `0` | 235 | START | 235 | 400 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 235 | START | 235 | 366 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `17` | 235 | START | 235 | 353 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 235 | START | 235 | 349 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `19` | 235 | START | 235 | 279 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LB1 | `8` | `8` | 239 | START | 239 | 302 |
| ✅ EXACT | `Action_Handoff` | CB2 | `10` | `10` | 258 | START | 258 | 265 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `1` | `1` | 266 | START | 266 | 479 |
| ✅ EXACT | `Action_BlockSecondLevel` | SAF1 | `12` | `12` | 266 | START | 266 | 400 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 400 | BOUNDARY | N/A | N/A |

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
- **Visible Samples:** 467

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_None` | 233 | 363 | 131 | inferred_complete_timeline |
| `Action_None` | 367 | 368 | 2 | inferred_complete_timeline |
| `Action_None` | 370 | 391 | 22 | inferred_complete_timeline |
| `Action_None` | 401 | 479 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 461

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 35 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 232 | 190 | inferred_complete_timeline |
| `Action_None` | 233 | 356 | 124 | inferred_complete_timeline |
| `Action_None` | 358 | 369 | 12 | inferred_complete_timeline |
| `Action_None` | 374 | 377 | 4 | inferred_complete_timeline |
| `Action_None` | 379 | 414 | 36 | inferred_complete_timeline |
| `Action_None` | 418 | 479 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_None` | 233 | 479 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_BallCarry` | 266 | 479 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–336
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 232 | 149 | inferred_complete_timeline |
| `Action_None` | 233 | 310 | 78 | inferred_complete_timeline |
| `Action_None` | 312 | 336 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 234 | 235 | inferred_complete_timeline |
| `Action_ZoneBlock` | 235 | 279 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 285 | 290 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 292 | 295 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 301 | 302 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 304 | 311 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 314 | 356 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 367 | 368 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 374 | 392 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 394 | 395 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 398 | 400 | 3 | inferred_complete_timeline |
| `Action_None` | 401 | 415 | 15 | inferred_complete_timeline |
| `Action_None` | 420 | 421 | 2 | inferred_complete_timeline |
| `Action_None` | 423 | 479 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–362
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 234 | 194 | inferred_complete_timeline |
| `Action_ZoneBlock` | 235 | 353 | 119 | inferred_complete_timeline |
| `Action_ZoneBlock` | 359 | 362 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 234 | 235 | inferred_complete_timeline |
| `Action_ZoneBlock` | 235 | 366 | 132 | inferred_complete_timeline |
| `Action_ZoneBlock` | 383 | 400 | 18 | inferred_complete_timeline |
| `Action_None` | 401 | 479 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 234 | 235 | inferred_complete_timeline |
| `Action_ZoneBlock` | 235 | 349 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 359 | 400 | 42 | inferred_complete_timeline |
| `Action_None` | 401 | 479 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 234 | 235 | inferred_complete_timeline |
| `Action_ZoneBlock` | 235 | 400 | 166 | inferred_complete_timeline |
| `Action_None` | 401 | 479 | 79 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_None` | 233 | 479 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_None` | 233 | 448 | 216 | inferred_complete_timeline |
| `Action_None` | 450 | 479 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_None` | 233 | 254 | 22 | inferred_complete_timeline |
| `Action_None` | 259 | 479 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–315
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_BallSnap` | 233 | 233 | 1 | inferred_complete_timeline |
| `Action_None` | 234 | 281 | 48 | inferred_complete_timeline |
| `Action_None` | 289 | 306 | 18 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_SplitBlock` | 239 | 302 | 64 | inferred_complete_timeline |
| `Action_SplitBlock` | 306 | 340 | 35 | inferred_complete_timeline |
| `Action_SplitBlock` | 375 | 400 | 26 | inferred_complete_timeline |
| `Action_None` | 401 | 479 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–352
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_None` | 233 | 352 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_None` | 233 | 252 | 20 | inferred_complete_timeline |
| `Action_None` | 280 | 289 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–369
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_SnapReceive` | 233 | 233 | 1 | inferred_complete_timeline |
| `Action_None` | 234 | 257 | 24 | inferred_complete_timeline |
| `Action_Handoff` | 258 | 265 | 8 | inferred_complete_timeline |
| `Action_None` | 266 | 369 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 460

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_None` | 233 | 307 | 75 | inferred_complete_timeline |
| `Action_None` | 326 | 330 | 5 | inferred_complete_timeline |
| `Action_None` | 333 | 479 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 266 | 400 | 135 | inferred_complete_timeline |
| `Action_None` | 401 | 420 | 20 | inferred_complete_timeline |
| `Action_None` | 423 | 424 | 2 | inferred_complete_timeline |
| `Action_None` | 426 | 474 | 49 | inferred_complete_timeline |
| `Action_None` | 476 | 479 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_None` | 233 | 326 | 94 | inferred_complete_timeline |
| `Action_None` | 332 | 334 | 3 | inferred_complete_timeline |
| `Action_None` | 341 | 342 | 2 | inferred_complete_timeline |
| `Action_None` | 349 | 350 | 2 | inferred_complete_timeline |
| `Action_None` | 355 | 356 | 2 | inferred_complete_timeline |
| `Action_None` | 358 | 369 | 12 | inferred_complete_timeline |
| `Action_None` | 372 | 479 | 108 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–479 | 480 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 252–324 | 69 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 338–479 | 138 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 345–369 | 25 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 363–371 | 9 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 380–479 | 100 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 383–479 | 74 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 395–412 | 12 | 4 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 412–479 | 68 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 432–479 | 48 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 451–453 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (10 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 9 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '23' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (RT) duration 166 frames exceeds threshold 90 frames [start=235, end=400].
- ⚠️ Segment 'Action_SnapReceive' for track '10' has invalid range: start=233, end=226. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '12' (SAF1) duration 135 frames exceeds threshold 90 frames [start=266, end=400].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 166 frames exceeds threshold 90 frames [start=235, end=400].
- ⚠️ Segment 'Action_BallSnap' for track '16' has invalid range: start=233, end=226. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (LG) duration 128 frames exceeds threshold 90 frames [start=235, end=362].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RG) duration 166 frames exceeds threshold 90 frames [start=235, end=400].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 166 frames exceeds threshold 90 frames [start=235, end=400].
- ⚠️ Action 'Action_BallCarry' range [266-479] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-310] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-336] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-479] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-352] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-448] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-326] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-334] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-369] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-479] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-307] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-330] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-479] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [239-302] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [306-340] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-254] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-369] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-479] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [266-400] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-420] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-474] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [235-366] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-363] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-391] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-252] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-289] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-281] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-306] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [235-353] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [359-362] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [235-349] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [359-400] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [235-279] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [285-290] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [292-295] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [301-302] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [304-311] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [314-356] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [367-368] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [374-392] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [394-395] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 401, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [401-415] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-421] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-479] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-35] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-356] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-369] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-377] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-414] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-287] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-298] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-324] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-340] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-346] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-479] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-369] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-371] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-406] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-399] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-404] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-479] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-453] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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