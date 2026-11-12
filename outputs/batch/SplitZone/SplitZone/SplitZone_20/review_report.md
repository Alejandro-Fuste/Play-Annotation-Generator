# Play-Annotation-Generator Annotation Review — SplitZone_20

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_20`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 449
- **Player Tracks:** 39
- **Ball Tracks:** 1
- **Action Segments:** 115
- **Validation Warnings:** 139
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | offense | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 7 | START | 7 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 7 | START | 7 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 7 | START | 7 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 7 | START | 7 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 7 | START | 7 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 7 | START | 7 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 7 | START | 7 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 7 | START | 7 | 219 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 220 | START | 220 | 231 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `11` | `11` | 223 | START | 223 | 326 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `12` | 223 | START | 223 | 260 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `13` | `13` | 223 | START | 223 | 238 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `14` | 223 | START | 258 | 259 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `6` | 223 | START | 223 | 332 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | `15` | `15` | 229 | START | 229 | 251 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 233 | END | 220 | 233 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `16` | 245 | START | 245 | 261 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `21` | `20` | 262 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 351 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 7–335
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 219 | 213 | inferred_complete_timeline |
| `Action_SnapReceive` | 220 | 233 | 14 | inferred_complete_timeline |
| `Action_None` | 234 | 244 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 245 | 261 | 17 | inferred_complete_timeline |
| `Action_None` | 262 | 335 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 7–255
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 199 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 210 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 223 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 228 | 1 | inferred_complete_timeline |
| `Action_SplitBlock` | 229 | 251 | 23 | inferred_complete_timeline |
| `Action_SplitBlock` | 253 | 255 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 7–449
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 219 | 213 | inferred_complete_timeline |
| `Action_None` | 220 | 345 | 126 | inferred_complete_timeline |
| `Action_None` | 349 | 449 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 7–312
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 222 | 216 | inferred_complete_timeline |
| `Action_ZoneBlock` | 223 | 238 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 274 | 279 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 289 | 312 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 7–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 222 | 216 | inferred_complete_timeline |
| `Action_ZoneBlock` | 223 | 326 | 104 | inferred_complete_timeline |
| `Action_ZoneBlock` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 7–259
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 219 | 213 | inferred_complete_timeline |
| `Action_BallSnap` | 220 | 231 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 258 | 259 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 7–375
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 222 | 216 | inferred_complete_timeline |
| `Action_ZoneBlock` | 223 | 260 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 264 | 321 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 349 | 351 | 3 | inferred_complete_timeline |
| `Action_None` | 352 | 372 | 21 | inferred_complete_timeline |
| `Action_None` | 374 | 375 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 7–381
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 222 | 216 | inferred_complete_timeline |
| `Action_ZoneBlock` | 223 | 332 | 110 | inferred_complete_timeline |
| `Action_ZoneBlock` | 334 | 351 | 18 | inferred_complete_timeline |
| `Action_None` | 352 | 381 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 7–397
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 219 | 213 | inferred_complete_timeline |
| `Action_None` | 220 | 318 | 99 | inferred_complete_timeline |
| `Action_None` | 321 | 339 | 19 | inferred_complete_timeline |
| `Action_None` | 345 | 347 | 3 | inferred_complete_timeline |
| `Action_None` | 350 | 397 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 7–285
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 219 | 213 | inferred_complete_timeline |
| `Action_None` | 220 | 262 | 43 | inferred_complete_timeline |
| `Action_None` | 264 | 266 | 3 | inferred_complete_timeline |
| `Action_None` | 272 | 285 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 11–345
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 219 | 209 | inferred_complete_timeline |
| `Action_None` | 220 | 327 | 108 | inferred_complete_timeline |
| `Action_None` | 339 | 340 | 2 | inferred_complete_timeline |
| `Action_None` | 344 | 345 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 7–345
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 219 | 213 | inferred_complete_timeline |
| `Action_None` | 220 | 345 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 7–287
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 219 | 213 | inferred_complete_timeline |
| `Action_None` | 220 | 287 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 7–318
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 219 | 213 | inferred_complete_timeline |
| `Action_None` | 220 | 318 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 7–283
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 219 | 213 | inferred_complete_timeline |
| `Action_None` | 220 | 283 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 7–17
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 17 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 7–449
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 219 | 213 | inferred_complete_timeline |
| `Action_None` | 220 | 281 | 62 | inferred_complete_timeline |
| `Action_None` | 287 | 323 | 37 | inferred_complete_timeline |
| `Action_None` | 326 | 330 | 5 | inferred_complete_timeline |
| `Action_None` | 400 | 449 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 7–449
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 219 | 213 | inferred_complete_timeline |
| `Action_None` | 220 | 341 | 122 | inferred_complete_timeline |
| `Action_None` | 345 | 390 | 46 | inferred_complete_timeline |
| `Action_None` | 393 | 449 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 122–149 | 7 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 226–255 | 4 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 242–449 | 158 | 7 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 250–385 | 69 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 266–287 | 22 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 273–449 | 177 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 285–332 | 40 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 298–341 | 38 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 305–306 | 2 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 308–397 | 86 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 308–449 | 132 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 319–399 | 76 | 4 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 324–370 | 19 | 3 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 333–449 | 117 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 344–439 | 93 | 3 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 346–388 | 43 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 352–391 | 16 | 3 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 358–449 | 90 | 2 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 362–374 | 13 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 371–409 | 30 | 3 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 392–449 | 58 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | 106 | 107 | 2 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (5 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 223 != Inferred start 258
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `15` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `20` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 90 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 42: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 129 frames exceeds threshold 90 frames [start=223, end=351].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (LG) duration 107 frames exceeds threshold 90 frames [start=223, end=329].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (RG) duration 129 frames exceeds threshold 90 frames [start=223, end=351].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [220–233], lower_priority='Action_ZoneBlock' annotated_start=223, effective_Action_ZoneBlock_start=234.
- ⚠️ Segment 'Action_BallCarry' for track '20' has invalid range: start=262, end=255. Clamping end to start.
- ⚠️ Action 'Action_None' range [220-281] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-323] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-330] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-345] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-283] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-318] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-341] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-390] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-449] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-262] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-285] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [223-332] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-381] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-17] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-287] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-345] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-449] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-318] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-339] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-347] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-397] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [223-326] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [328-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [223-260] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [264-321] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-372] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [223-238] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [249-250] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [270-271] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [274-279] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [289-312] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [220-231] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [258-259] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-199] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-223] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [229-251] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [253-255] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-335] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-327] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-126] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-246] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-266] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-302] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-330] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-365] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-449] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-385] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-287] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-449] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-313] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-332] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-305] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-325] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-341] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-321] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-397] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-344] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-449] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-352] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-360] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-364] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-399] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-327] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-354] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-421] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-435] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-439] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-388] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-359] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-391] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-436] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-449] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-374] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-378] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-394] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-409] for track '38' has 1 frames without a visible bounding box.
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

</details>