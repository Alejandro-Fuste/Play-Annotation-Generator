# Play-Annotation-Generator Annotation Review — SplitZone_318

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_318`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_ReadEdgeDefender` | RB | offense | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 271 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 279 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 287 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 0 | 271 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 271 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 281 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 276 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 281 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 271 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 272 | START | 272 | 285 |
| ✅ EXACT | `Action_SplitBlock` | TE | `1` | `1` | 280 | START | 280 | 329 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `16` | 282 | START | 315 | 321 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `18` | 282 | START | 282 | 323 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `19` | 282 | START | 282 | 310 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `21` | `21` | 282 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `5` | 282 | START | 282 | 323 |
| ✅ EXACT | `Action_SnapReceive` | RB | `6` | `6` | 285 | END | 272 | 285 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | QB | `11` | `11` | 288 | START | 288 | 305 |
| ✅ EXACT | `Action_ReadEdgeDefender` | RB | `6` | `6` | 292 | START | 292 | 305 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `11` | 306 | START | 306 | 311 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `6` | 310 | START | 310 | 339 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 287 | 288 | inferred_complete_timeline |
| `Action_PressEdge` | 288 | 305 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 306 | 311 | 6 | inferred_complete_timeline |
| `Action_PressEdge` | 312 | 317 | 6 | inferred_complete_timeline |
| `Action_None` | 318 | 449 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 271 | 168 | inferred_complete_timeline |
| `Action_SnapReceive` | 272 | 285 | 14 | inferred_complete_timeline |
| `Action_None` | 286 | 291 | 6 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 292 | 305 | 14 | inferred_complete_timeline |
| `Action_None` | 306 | 309 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 310 | 339 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 342 | 414 | 73 | inferred_complete_timeline |
| `Action_BallCarry` | 421 | 422 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 424 | 425 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 433 | 436 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 439 | 449 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 431

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_None` | 272 | 311 | 40 | inferred_complete_timeline |
| `Action_None` | 320 | 355 | 36 | inferred_complete_timeline |
| `Action_None` | 358 | 361 | 4 | inferred_complete_timeline |
| `Action_None` | 367 | 369 | 3 | inferred_complete_timeline |
| `Action_None` | 373 | 378 | 6 | inferred_complete_timeline |
| `Action_None` | 380 | 449 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_None` | 272 | 354 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_None` | 272 | 332 | 61 | inferred_complete_timeline |
| `Action_None` | 334 | 449 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 279 | 280 | inferred_complete_timeline |
| `Action_SplitBlock` | 280 | 329 | 50 | inferred_complete_timeline |
| `Action_None` | 330 | 449 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 281 | 282 | inferred_complete_timeline |
| `Action_ZoneBlock` | 282 | 323 | 42 | inferred_complete_timeline |
| `Action_None` | 324 | 436 | 113 | inferred_complete_timeline |
| `Action_None` | 439 | 449 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 276 | 277 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 281 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 282 | 310 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 317 | 319 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_BallSnap` | 272 | 285 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 315 | 321 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 323 | 323 | 1 | inferred_complete_timeline |
| `Action_None` | 324 | 342 | 19 | inferred_complete_timeline |
| `Action_None` | 347 | 354 | 8 | inferred_complete_timeline |
| `Action_None` | 359 | 362 | 4 | inferred_complete_timeline |
| `Action_None` | 367 | 369 | 3 | inferred_complete_timeline |
| `Action_None` | 387 | 445 | 59 | inferred_complete_timeline |
| `Action_None` | 447 | 449 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 39 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 97 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 136 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 179 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 281 | 282 | inferred_complete_timeline |
| `Action_ZoneBlock` | 282 | 323 | 42 | inferred_complete_timeline |
| `Action_None` | 324 | 352 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–310
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_None` | 272 | 310 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_None` | 272 | 397 | 126 | inferred_complete_timeline |
| `Action_None` | 408 | 449 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–405
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_None` | 272 | 293 | 22 | inferred_complete_timeline |
| `Action_None` | 312 | 405 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_None` | 272 | 317 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_None` | 272 | 362 | 91 | inferred_complete_timeline |
| `Action_None` | 364 | 405 | 42 | inferred_complete_timeline |
| `Action_None` | 410 | 449 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_None` | 272 | 434 | 163 | inferred_complete_timeline |
| `Action_None` | 436 | 439 | 4 | inferred_complete_timeline |
| `Action_None` | 442 | 449 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–320
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_None` | 272 | 320 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_None` | 272 | 449 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_None` | 272 | 449 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_None` | 272 | 449 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_None` | 272 | 449 | 178 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 295–449 | 135 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 332–449 | 118 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 337–449 | 113 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 347–449 | 103 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 365–449 | 85 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 368–449 | 82 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 372–384 | 13 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 396–401 | 6 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 402–408 | 7 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 403–439 | 31 | 3 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 422–449 | 26 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 431–449 | 16 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `21` (RG)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [272–285], lower_priority='Action_ZoneBlock' annotated_start=282, effective_Action_ZoneBlock_start=286.
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=282, end=179. Clamping end to start.
- ⚠️ Action 'Action_None' range [272-332] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-397] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-352] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [292-305] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [310-339] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [342-414] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [421-422] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [424-425] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [433-436] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-434] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-439] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-311] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-355] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-361] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-369] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-378] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-310] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-362] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-405] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-449] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-354] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-320] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-449] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [272-285] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [315-321] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-342] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-354] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-362] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-369] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-445] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-449] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-293] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-405] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-436] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-276] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [282-310] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [317-319] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-317] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-39] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-63] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-136] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-142] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-332] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-336] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-449] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-449] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-384] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-401] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-408] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-426] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-433] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-427] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-436] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-446] for track '33' has 1 frames without a visible bounding box.
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