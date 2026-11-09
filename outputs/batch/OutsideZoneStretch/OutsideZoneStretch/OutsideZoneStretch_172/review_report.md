# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_172

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_172`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 479
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 121
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 241 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 300 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 479 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 395 |
| ✅ EXACT | `Action_ZoneBlock` | C | `14` | `14` | 203 | START | 203 | 235 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `17` | 203 | START | 203 | 217 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `19` | `19` | 203 | START | 203 | 235 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `20` | 203 | START | 203 | 235 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 203 | START | 203 | 225 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `15` | 223 | START | 223 | 229 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–437
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |
| `Action_Handoff` | 223 | 229 | 7 | inferred_complete_timeline |
| `Action_None` | 230 | 437 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–310
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 300 | 301 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 310 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–477
- **Visible Samples:** 460

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 395 | 396 | inferred_complete_timeline |
| `Action_PreSnap` | 400 | 402 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 415 | 472 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 475 | 477 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

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
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 241 | 242 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 303 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 311 | 337 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 344 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 361 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 363 | 364 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 378 | 382 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 384 | 389 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 397 | 403 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 405 | 409 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 411 | 479 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–371
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 235 | 33 | inferred_complete_timeline |
| `Action_None` | 236 | 263 | 28 | inferred_complete_timeline |
| `Action_None` | 265 | 364 | 100 | inferred_complete_timeline |
| `Action_None` | 369 | 371 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 459

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 235 | 33 | inferred_complete_timeline |
| `Action_None` | 236 | 257 | 22 | inferred_complete_timeline |
| `Action_None` | 265 | 289 | 25 | inferred_complete_timeline |
| `Action_None` | 297 | 300 | 4 | inferred_complete_timeline |
| `Action_None` | 308 | 479 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 235 | 33 | inferred_complete_timeline |
| `Action_None` | 236 | 281 | 46 | inferred_complete_timeline |
| `Action_None` | 285 | 479 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 225 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 229 | 235 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 217 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 219 | 235 | 17 | inferred_complete_timeline |
| `Action_None` | 236 | 410 | 175 | inferred_complete_timeline |
| `Action_None` | 421 | 479 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 236 | 237 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 289 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 298 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 461

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 344 | 345 | inferred_complete_timeline |
| `Action_PreSnap` | 346 | 398 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 417 | 479 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 274 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 305 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 313 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–343
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 216 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 343 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 292 | 293 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 479 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 337 | 338 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 362 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 367 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 374 | 378 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 399 | 401 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 406 | 479 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–367
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 302 | 303 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 350 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 363 | 367 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 479 | 480 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–391
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 315 | 316 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 391 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–372
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 372 | 373 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–477 | 467 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 45–48 | 4 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 242–479 | 232 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 308–479 | 172 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 312–479 | 153 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 316–328 | 13 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 322–465 | 101 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 331–345 | 15 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 343–479 | 91 | 3 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 376–395 | 17 | 2 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 405–409 | 5 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 406–479 | 12 | 2 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 406–479 | 74 | 1 | Undefined position; Undefined team |
| `34` | `36` | Position_Unknown | Team_Unknown | 416–478 | 50 | 4 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 440–452 | 9 | 2 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 451–479 | 29 | 1 | Undefined position; Undefined team |
| `37` | `40` | Position_Unknown | Team_Unknown | 458–479 | 22 | 1 | Undefined position; Undefined team |
| `38` | `41` | Position_Unknown | Team_Unknown | 469–479 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 346: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-410] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-426] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [429-430] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-477] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-372] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-395] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-402] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-472] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [475-477] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-337] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-362] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-367] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-378] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-401] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-302] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-350] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-367] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-292] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-479] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-216] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-343] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-298] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-305] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-313] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-241] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-303] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-337] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-344] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-361] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-364] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-382] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-403] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-409] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-344] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-398] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-479] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-236] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-289] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-298] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-315] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-391] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-281] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-437] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-258] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-274] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-410] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-300] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-310] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-263] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-364] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-371] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-235] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-257] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-289] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-300] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-225] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [229-235] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-48] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-252] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-479] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-323] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-479] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-328] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-412] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [456-465] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-345] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-355] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-396] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-390] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-395] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-409] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-408] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-449] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [460-464] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-470] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [473-478] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-444] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [449-452] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [458-479] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [469-479] for track '38' has 2 frames without a visible bounding box.
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