# Play-Annotation-Generator Annotation Review — OutsideZoneRead_29

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_29`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 479
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 133
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 96
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadEdgeDefender` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 285 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 257 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 375 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 249 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 250 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 250 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 477 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 250 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 250 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 254 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `16` | `16` | 251 | START | 278 | 284 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `17` | 251 | START | 251 | 263 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `18` | 251 | START | 254 | 265 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `21` | `21` | 251 | START | 251 | 308 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `5` | 251 | START | 251 | 252 |
| ✅ EXACT | `Action_PressEdge` | RB | `6` | `6` | 255 | START | 255 | 297 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadEdgeDefender` | QB | `14` | `14` | 258 | START | 258 | 261 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `14` | `14` | 283 | START | 283 | 307 |

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
- **Visible Frames:** 0–478
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 257 | 258 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 258 | 261 | 4 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 268 | 282 | 15 | inferred_complete_timeline |
| `Action_Keep` | 283 | 307 | 25 | inferred_complete_timeline |
| `Action_Keep` | 309 | 381 | 73 | inferred_complete_timeline |
| `Action_Keep` | 386 | 462 | 77 | inferred_complete_timeline |
| `Action_Keep` | 464 | 465 | 2 | inferred_complete_timeline |
| `Action_Keep` | 476 | 478 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 254 | 255 | inferred_complete_timeline |
| `Action_PressEdge` | 255 | 297 | 43 | inferred_complete_timeline |
| `Action_None` | 298 | 315 | 18 | inferred_complete_timeline |
| `Action_None` | 318 | 479 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 285 | 286 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 479 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 477 | 478 | inferred_complete_timeline |
| `Action_PreSnap` | 479 | 479 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–381
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 375 | 376 | inferred_complete_timeline |
| `Action_PreSnap` | 378 | 381 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 250 | 251 | inferred_complete_timeline |
| `Action_ZoneBlock` | 251 | 308 | 58 | inferred_complete_timeline |
| `Action_None` | 309 | 342 | 34 | inferred_complete_timeline |
| `Action_None` | 345 | 469 | 125 | inferred_complete_timeline |
| `Action_None` | 479 | 479 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 250 | 251 | inferred_complete_timeline |
| `Action_ZoneBlock` | 254 | 265 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 274 | 275 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 278 | 308 | 31 | inferred_complete_timeline |
| `Action_None` | 309 | 352 | 44 | inferred_complete_timeline |
| `Action_None` | 357 | 365 | 9 | inferred_complete_timeline |
| `Action_None` | 372 | 412 | 41 | inferred_complete_timeline |
| `Action_None` | 424 | 479 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_ZoneBlock` | 278 | 284 | 7 | inferred_complete_timeline |
| `Action_None` | 324 | 326 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 472

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 250 | 251 | inferred_complete_timeline |
| `Action_ZoneBlock` | 251 | 263 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 266 | 291 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 296 | 308 | 13 | inferred_complete_timeline |
| `Action_None` | 309 | 385 | 77 | inferred_complete_timeline |
| `Action_None` | 388 | 479 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 472

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 250 | 251 | inferred_complete_timeline |
| `Action_ZoneBlock` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 256 | 307 | 52 | inferred_complete_timeline |
| `Action_None` | 309 | 389 | 81 | inferred_complete_timeline |
| `Action_None` | 391 | 398 | 8 | inferred_complete_timeline |
| `Action_None` | 401 | 425 | 25 | inferred_complete_timeline |
| `Action_None` | 427 | 479 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 338 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 479 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 479 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 286 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 479 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 325 | 326 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 479 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 282 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 296 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–468
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 468 | 469 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 331 | 332 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 479 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 479 | 480 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 318 | 319 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 430 | 431 | inferred_complete_timeline |
| `Action_PreSnap` | 432 | 433 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 448 | 449 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–479 | 458 | 6 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 48–110 | 11 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 288–292 | 4 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 291–479 | 188 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 291–308 | 8 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 299–359 | 13 | 6 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 307–321 | 14 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 311–479 | 169 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 313–479 | 167 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 329–478 | 144 | 4 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 336–343 | 7 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 383–479 | 39 | 4 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 395–396 | 2 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 414–479 | 66 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 454–479 | 24 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 469–479 | 7 | 2 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 479–479 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `16` (C): Annotated start 251 != Inferred start 278
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ReadEdgeDefender` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `14` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 95 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 60: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-285] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-479] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-324] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-330] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-385] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-407] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-416] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-477] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-331] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-479] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [251-252] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [256-307] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-389] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-398] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-425] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-479] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-315] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-318] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-430] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-433] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [448-449] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-468] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-252] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-257] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-282] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-296] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-325] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-306] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-338] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-479] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-252] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-257] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-479] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [258-261] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [283-307] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [309-381] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [386-462] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [464-465] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [476-478] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-375] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-381] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-249] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [278-284] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [251-263] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [266-291] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-385] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-250] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [254-265] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [274-275] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [278-308] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-352] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-365] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-412] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-253] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-286] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-252] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-250] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-342] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-469] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-57] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-69] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-110] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-289] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-292] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-307] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-479] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-292] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-305] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-308] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-300] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-307] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-340] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-347] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-359] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-314] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-321] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-366] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-462] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [465-470] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [473-478] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-337] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-343] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-384] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-395] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [429-430] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [448-479] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-396] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-479] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-464] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [469-471] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>