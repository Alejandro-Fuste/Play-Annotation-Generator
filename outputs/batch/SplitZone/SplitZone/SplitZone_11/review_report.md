# Play-Annotation-Generator Annotation Review — SplitZone_11

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_11`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 83
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `21` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `22` | `22` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_Handoff` | LB2 | defense | `14` | `14` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `1` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 14 | START | 14 | 335 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 14 | START | 14 | 302 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 14 | START | 14 | 296 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `13` | `Group` | 14 | START | 14 | 293 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 14 | START | 14 | 293 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 14 | START | 14 | 296 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 14 | START | 14 | 293 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 14 | START | 16 | 296 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 14 | START | 20 | 293 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 14 | START | 26 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 14 | START | 14 | 293 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 294 | START | 294 | 299 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `12` | `12` | 297 | START | 297 | 356 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `18` | 297 | START | 297 | 318 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 297 | START | 297 | 352 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `21` | 297 | START | 300 | 306 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `22` | `22` | 297 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 299 | END | 294 | 299 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `10` | `10` | 303 | START | 303 | 363 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | QB | `17` | `17` | 324 | START | 324 | 353 |
| ✅ EXACT | `Action_Handoff` | LB2 | `14` | `14` | 328 | START | 328 | 335 |
| ✅ EXACT | `Action_BallCarry` | RB | `1` | `1` | 336 | START | 336 | 479 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 372 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 14–479
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 293 | 280 | inferred_complete_timeline |
| `Action_SnapReceive` | 294 | 299 | 6 | inferred_complete_timeline |
| `Action_None` | 300 | 323 | 24 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 324 | 353 | 30 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 367 | 372 | 6 | inferred_complete_timeline |
| `Action_None` | 373 | 413 | 41 | inferred_complete_timeline |
| `Action_None` | 415 | 479 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 14–479
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 335 | 322 | inferred_complete_timeline |
| `Action_BallCarry` | 336 | 479 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 14–479
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 293 | 280 | inferred_complete_timeline |
| `Action_None` | 294 | 479 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 14–479
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 293 | 280 | inferred_complete_timeline |
| `Action_None` | 294 | 479 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 14–365
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 293 | 280 | inferred_complete_timeline |
| `Action_None` | 294 | 310 | 17 | inferred_complete_timeline |
| `Action_None` | 318 | 365 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 14–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 302 | 289 | inferred_complete_timeline |
| `Action_SplitBlock` | 303 | 363 | 61 | inferred_complete_timeline |
| `Action_SplitBlock` | 365 | 372 | 8 | inferred_complete_timeline |
| `Action_None` | 373 | 479 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 14–407
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 296 | 283 | inferred_complete_timeline |
| `Action_ZoneBlock` | 297 | 356 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 358 | 372 | 15 | inferred_complete_timeline |
| `Action_None` | 373 | 407 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 16–479
- **Visible Samples:** 459

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 296 | 281 | inferred_complete_timeline |
| `Action_ZoneBlock` | 297 | 352 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 356 | 360 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 363 | 372 | 10 | inferred_complete_timeline |
| `Action_None` | 373 | 479 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 20–326
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 293 | 274 | inferred_complete_timeline |
| `Action_BallSnap` | 294 | 299 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 300 | 306 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 325 | 326 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 26–48
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 43 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 48 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 14–479
- **Visible Samples:** 459

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 296 | 283 | inferred_complete_timeline |
| `Action_ZoneBlock` | 297 | 318 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 326 | 372 | 47 | inferred_complete_timeline |
| `Action_None` | 373 | 479 | 107 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 14–451
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 293 | 280 | inferred_complete_timeline |
| `Action_None` | 294 | 396 | 103 | inferred_complete_timeline |
| `Action_None` | 399 | 451 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 14–479
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 293 | 280 | inferred_complete_timeline |
| `Action_None` | 294 | 353 | 60 | inferred_complete_timeline |
| `Action_None` | 355 | 441 | 87 | inferred_complete_timeline |
| `Action_None` | 452 | 479 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 14–322
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 293 | 280 | inferred_complete_timeline |
| `Action_None` | 294 | 319 | 26 | inferred_complete_timeline |
| `Action_None` | 321 | 322 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 14–358
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 293 | 280 | inferred_complete_timeline |
| `Action_None` | 294 | 314 | 21 | inferred_complete_timeline |
| `Action_None` | 320 | 358 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 14–378
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 293 | 280 | inferred_complete_timeline |
| `Action_None` | 294 | 344 | 51 | inferred_complete_timeline |
| `Action_None` | 350 | 366 | 17 | inferred_complete_timeline |
| `Action_None` | 374 | 378 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 14–479
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 327 | 314 | inferred_complete_timeline |
| `Action_Handoff` | 328 | 335 | 8 | inferred_complete_timeline |
| `Action_None` | 336 | 479 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 14–474
- **Visible Samples:** 459

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 293 | 280 | inferred_complete_timeline |
| `Action_None` | 294 | 464 | 171 | inferred_complete_timeline |
| `Action_None` | 466 | 470 | 5 | inferred_complete_timeline |
| `Action_None` | 472 | 474 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 14–459
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 293 | 280 | inferred_complete_timeline |
| `Action_None` | 294 | 459 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 14–479
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 293 | 280 | inferred_complete_timeline |
| `Action_None` | 294 | 479 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 14–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 293 | 280 | inferred_complete_timeline |
| `Action_None` | 294 | 406 | 113 | inferred_complete_timeline |
| `Action_None` | 408 | 479 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 14–479
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 293 | 280 | inferred_complete_timeline |
| `Action_None` | 294 | 479 | 186 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 14–91 | 21 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 254–479 | 169 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 338–374 | 35 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 376–383 | 8 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 377–479 | 103 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 379–479 | 101 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 385–479 | 95 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 385–479 | 94 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 389–391 | 3 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 400–414 | 8 | 3 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 402–479 | 78 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 423–479 | 57 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 425–479 | 52 | 3 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 467–479 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `22` (RG)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [294–299], lower_priority='Action_ZoneBlock' annotated_start=297, effective_Action_ZoneBlock_start=300.
- ⚠️ Segment 'Action_ZoneBlock' for track '22' has invalid range: start=297, end=48. Clamping end to start.
- ⚠️ Action 'Action_None' range [294-459] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-464] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-470] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-474] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-28] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-88] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-91] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-406] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-344] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-366] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-378] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-479] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [303-363] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [365-372] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-319] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [297-356] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-407] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-310] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-365] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-479] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-396] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-451] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-314] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-358] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [324-353] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-413] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [297-318] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-353] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-441] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [297-352] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [356-360] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [300-306] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [325-326] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-43] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-261] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-279] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-347] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-384] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-368] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-374] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-383] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-391] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-391] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-414] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-455] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-472] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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