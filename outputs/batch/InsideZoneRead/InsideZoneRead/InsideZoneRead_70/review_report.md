# Play-Annotation-Generator Annotation Review — InsideZoneRead_70

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_70`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 110
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `2` | `1` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | RB | offense | `11` | `10` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `22` | `20` |
| ❌ MISSING SEGMENT | `Action_Handoff` | RB | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 227 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 53 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 96 | 281 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 0 | START | 0 | 281 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 283 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 283 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 283 |
| ✅ EXACT | `Action_BallSnap` | C | `2` | `1` | 282 | START | 282 | 295 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `15` | `14` | 284 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `2` | `1` | 284 | START | 296 | 339 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 284 | START | 284 | 365 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `4` | 284 | START | 284 | 306 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `8` | `7` | 284 | START | 284 | 295 |
| ✅ EXACT | `Action_SnapReceive` | RB | `11` | `10` | 295 | END | 282 | 295 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | RB | `11` | `10` | 298 | START | 298 | 300 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `22` | `20` | 315 | START | 315 | 354 |
| ❌ MISSING SEGMENT | `Action_Handoff` | RB | `11` | `10` | 315 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `10` | `9` | 323 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 365 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 96–377
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 96 | 281 | 186 | inferred_complete_timeline |
| `Action_None` | 282 | 326 | 45 | inferred_complete_timeline |
| `Action_None` | 337 | 353 | 17 | inferred_complete_timeline |
| `Action_None` | 357 | 359 | 3 | inferred_complete_timeline |
| `Action_None` | 361 | 362 | 2 | inferred_complete_timeline |
| `Action_None` | 364 | 377 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–313
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 281 | 50 | inferred_complete_timeline |
| `Action_SnapReceive` | 282 | 295 | 14 | inferred_complete_timeline |
| `Action_None` | 296 | 297 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 298 | 300 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 303 | 306 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 312 | 313 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 283 | 284 | inferred_complete_timeline |
| `Action_ZoneBlock` | 284 | 365 | 82 | inferred_complete_timeline |
| `Action_None` | 366 | 419 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 53–278
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 53 | 59 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 95 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 134 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 151 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 158 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 165 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 183 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 204 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 223 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 247 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 278 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–339
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 281 | 282 | inferred_complete_timeline |
| `Action_BallSnap` | 282 | 295 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 296 | 339 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 283 | 284 | inferred_complete_timeline |
| `Action_ZoneBlock` | 284 | 295 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 297 | 310 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 315 | 320 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 323 | 365 | 43 | inferred_complete_timeline |
| `Action_None` | 366 | 419 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–337
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 283 | 284 | inferred_complete_timeline |
| `Action_ZoneBlock` | 284 | 306 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 308 | 337 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 281 | 282 | inferred_complete_timeline |
| `Action_None` | 282 | 373 | 92 | inferred_complete_timeline |
| `Action_None` | 396 | 419 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–416
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 281 | 282 | inferred_complete_timeline |
| `Action_None` | 282 | 359 | 78 | inferred_complete_timeline |
| `Action_None` | 361 | 416 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 212–407
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 212 | 220 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 280 | 5 | inferred_complete_timeline |
| `Action_None` | 322 | 323 | 2 | inferred_complete_timeline |
| `Action_None` | 338 | 344 | 7 | inferred_complete_timeline |
| `Action_None` | 346 | 349 | 4 | inferred_complete_timeline |
| `Action_None` | 358 | 407 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 116 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 127 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 158 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 281 | 122 | inferred_complete_timeline |
| `Action_None` | 282 | 292 | 11 | inferred_complete_timeline |
| `Action_None` | 295 | 344 | 50 | inferred_complete_timeline |
| `Action_None` | 360 | 419 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–407
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 281 | 282 | inferred_complete_timeline |
| `Action_None` | 282 | 407 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 2–403
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 7 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 281 | 273 | inferred_complete_timeline |
| `Action_None` | 282 | 362 | 81 | inferred_complete_timeline |
| `Action_None` | 366 | 369 | 4 | inferred_complete_timeline |
| `Action_None` | 371 | 383 | 13 | inferred_complete_timeline |
| `Action_None` | 387 | 388 | 2 | inferred_complete_timeline |
| `Action_None` | 391 | 403 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 277 | 278 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 281 | 1 | inferred_complete_timeline |
| `Action_None` | 282 | 419 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–355 | 351 | 3 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–77 | 67 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 7–99 | 66 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 81–102 | 22 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 287–288 | 2 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 291–419 | 103 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 296–419 | 97 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 312–419 | 108 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 325–401 | 77 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 340–342 | 3 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 363–419 | 57 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 379–419 | 41 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 389–401 | 13 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 394–419 | 26 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 408–417 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `15` (LG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `11` (4 segments found)
- ❌ Missing segment for action `Action_Handoff` on target `11` (RB)
- ❌ Missing segment for action `Action_BallCarry` on target `10` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '1' (C): higher_priority='Action_BallSnap' [282–295], lower_priority='Action_ZoneBlock' annotated_start=284, effective_Action_ZoneBlock_start=296.
- ⚠️ Segment 'Action_BallCarry' for track '9' has invalid range: start=323, end=77. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '10' has invalid range: start=315, end=313. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '14' has invalid range: start=284, end=278. Clamping end to start.
- ⚠️ Action 'Action_None' range [282-359] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-416] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [296-339] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [284-365] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-373] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [284-306] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [308-337] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-277] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-419] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-407] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [284-295] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [297-310] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [315-320] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-348] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-77] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-227] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [298-300] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [303-306] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [309-310] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [312-313] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-127] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-281] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-292] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-344] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-7] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-362] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-369] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-383] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-403] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-11] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-57] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-99] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-134] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-138] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-165] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-247] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-278] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-326] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-353] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-377] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-220] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-251] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-280] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-344] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-349] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-407] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-324] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-339] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [315-354] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-401] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-342] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-419] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-401] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-411] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-417] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>