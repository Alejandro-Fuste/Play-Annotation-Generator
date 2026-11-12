# Play-Annotation-Generator Annotation Review — SplitZone_103

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_103`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 449
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | TE1 | offense | `7` | `7` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 23 | START | 24 | 277 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 23 | START | 24 | 271 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 23 | START | 24 | 271 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 23 | START | 24 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 23 | START | 24 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 23 | START | 24 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 23 | START | 24 | 271 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 23 | START | 24 | 271 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 23 | START | 24 | 296 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `7` | `Group` | 23 | START | 24 | 294 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 23 | START | 24 | 268 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 269 | START | 269 | 283 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `10` | 272 | START | 272 | 339 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `13` | `13` | 272 | START | 272 | 315 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 272 | START | 284 | 325 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 272 | START | 272 | 300 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `3` | 272 | START | 272 | 293 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `1` | `1` | 278 | START | 278 | 388 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 283 | END | 269 | 283 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `18` | 286 | START | 286 | 296 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | TE1 | `7` | `7` | 295 | START | 295 | 337 |
| ✅ EXACT | `Action_BallCarry` | RB | `5` | `5` | 297 | START | 297 | 449 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 388 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 24–448
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 268 | 245 | inferred_complete_timeline |
| `Action_SnapReceive` | 269 | 283 | 15 | inferred_complete_timeline |
| `Action_None` | 284 | 285 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 286 | 296 | 11 | inferred_complete_timeline |
| `Action_None` | 297 | 448 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 24–449
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 296 | 273 | inferred_complete_timeline |
| `Action_BallCarry` | 297 | 449 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 24–378
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 268 | 245 | inferred_complete_timeline |
| `Action_None` | 269 | 378 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 24–372
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 268 | 245 | inferred_complete_timeline |
| `Action_None` | 269 | 372 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 24–347
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 294 | 271 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 295 | 337 | 43 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 341 | 347 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 24–449
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 277 | 254 | inferred_complete_timeline |
| `Action_SplitBlock` | 278 | 388 | 111 | inferred_complete_timeline |
| `Action_None` | 389 | 398 | 10 | inferred_complete_timeline |
| `Action_None` | 402 | 405 | 4 | inferred_complete_timeline |
| `Action_None` | 408 | 449 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 24–449
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 271 | 248 | inferred_complete_timeline |
| `Action_ZoneBlock` | 272 | 315 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 321 | 388 | 68 | inferred_complete_timeline |
| `Action_None` | 389 | 449 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 24–449
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 271 | 248 | inferred_complete_timeline |
| `Action_ZoneBlock` | 272 | 293 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 296 | 300 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 302 | 388 | 87 | inferred_complete_timeline |
| `Action_None` | 389 | 449 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 24–449
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 268 | 245 | inferred_complete_timeline |
| `Action_BallSnap` | 269 | 283 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 284 | 325 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 329 | 388 | 60 | inferred_complete_timeline |
| `Action_None` | 389 | 449 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 24–449
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 271 | 248 | inferred_complete_timeline |
| `Action_ZoneBlock` | 272 | 300 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 306 | 356 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 363 | 388 | 26 | inferred_complete_timeline |
| `Action_None` | 389 | 449 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 24–449
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 271 | 248 | inferred_complete_timeline |
| `Action_ZoneBlock` | 272 | 339 | 68 | inferred_complete_timeline |
| `Action_ZoneBlock` | 374 | 388 | 15 | inferred_complete_timeline |
| `Action_None` | 389 | 392 | 4 | inferred_complete_timeline |
| `Action_None` | 394 | 449 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 24–312
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 268 | 245 | inferred_complete_timeline |
| `Action_None` | 269 | 312 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 24–358
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 268 | 245 | inferred_complete_timeline |
| `Action_None` | 269 | 358 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 24–288
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 268 | 245 | inferred_complete_timeline |
| `Action_None` | 269 | 288 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 24–307
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 268 | 245 | inferred_complete_timeline |
| `Action_None` | 269 | 298 | 30 | inferred_complete_timeline |
| `Action_None` | 302 | 307 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 24–307
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 268 | 245 | inferred_complete_timeline |
| `Action_None` | 269 | 307 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 24–449
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 268 | 245 | inferred_complete_timeline |
| `Action_None` | 269 | 449 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 24–449
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 268 | 245 | inferred_complete_timeline |
| `Action_None` | 269 | 306 | 38 | inferred_complete_timeline |
| `Action_None` | 308 | 323 | 16 | inferred_complete_timeline |
| `Action_None` | 329 | 449 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 24–381
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 268 | 245 | inferred_complete_timeline |
| `Action_None` | 269 | 325 | 57 | inferred_complete_timeline |
| `Action_None` | 329 | 332 | 4 | inferred_complete_timeline |
| `Action_None` | 335 | 341 | 7 | inferred_complete_timeline |
| `Action_None` | 343 | 381 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 24–378
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 268 | 245 | inferred_complete_timeline |
| `Action_None` | 269 | 304 | 36 | inferred_complete_timeline |
| `Action_None` | 310 | 312 | 3 | inferred_complete_timeline |
| `Action_None` | 314 | 358 | 45 | inferred_complete_timeline |
| `Action_None` | 363 | 364 | 2 | inferred_complete_timeline |
| `Action_None` | 371 | 378 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 24–449
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 268 | 245 | inferred_complete_timeline |
| `Action_None` | 269 | 449 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 24–449
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 268 | 245 | inferred_complete_timeline |
| `Action_None` | 269 | 449 | 181 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 63–68 | 6 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 299–449 | 136 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 301–312 | 12 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 319–365 | 38 | 4 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 333–344 | 5 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 338–363 | 8 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 346–449 | 81 | 2 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 366–449 | 83 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 382–386 | 5 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 390–392 | 3 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 390–449 | 60 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 395–449 | 55 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 423–449 | 27 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 434–449 | 16 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 436–449 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LG) duration 117 frames exceeds threshold 90 frames [start=272, end=388].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 117 frames exceeds threshold 90 frames [start=272, end=388].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (LT) duration 117 frames exceeds threshold 90 frames [start=272, end=388].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (C) duration 117 frames exceeds threshold 90 frames [start=272, end=388].
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [269–283], lower_priority='Action_ZoneBlock' annotated_start=272, effective_Action_ZoneBlock_start=284.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RG) duration 117 frames exceeds threshold 90 frames [start=272, end=388].
- ⚠️ Action 'Action_None' range [389-398] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-405] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-358] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [272-293] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [296-300] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-312] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-298] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-307] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [295-337] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [341-347] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-372] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [272-339] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-392] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-307] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-304] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-358] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-378] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [272-315] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-378] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-306] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-323] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-325] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-332] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-341] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-381] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-448] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [284-325] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [272-300] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [306-356] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-288] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-68] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-303] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-394] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-312] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-326] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-332] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-342] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-365] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-363] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-386] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-392] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-449] for track '33' has 1 frames without a visible bounding box.
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

</details>