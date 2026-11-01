# Play-Annotation-Generator Annotation Review — InsideZoneRead_159

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_159`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 449
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 135
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 250 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 250 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 250 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 127 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 248 | START | 248 | 259 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 251 | START | 251 | 285 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `3` | 251 | START | 251 | 313 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `7` | `6` | 251 | START | 260 | 292 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `7` | 251 | START | 251 | 300 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 251 | START | 251 | 313 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 259 | END | 248 | 259 |
| ✅ EXACT | `Action_ReadDefender` | QB | `5` | `4` | 264 | START | 264 | 283 |
| ✅ EXACT | `Action_BallCarry` | QB | `5` | `4` | 284 | START | 284 | 323 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 313 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_SnapReceive` | 248 | 259 | 12 | inferred_complete_timeline |
| `Action_None` | 260 | 263 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 264 | 283 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 284 | 323 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–310
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 282 | 35 | inferred_complete_timeline |
| `Action_None` | 286 | 302 | 17 | inferred_complete_timeline |
| `Action_None` | 307 | 310 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–338
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 250 | 251 | inferred_complete_timeline |
| `Action_ZoneBlock` | 251 | 313 | 63 | inferred_complete_timeline |
| `Action_None` | 314 | 338 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–300
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 250 | 251 | inferred_complete_timeline |
| `Action_ZoneBlock` | 251 | 300 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–350
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_BallSnap` | 248 | 259 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 260 | 292 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 298 | 313 | 16 | inferred_complete_timeline |
| `Action_None` | 314 | 321 | 8 | inferred_complete_timeline |
| `Action_None` | 347 | 350 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 250 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 251 | 313 | 63 | inferred_complete_timeline |
| `Action_None` | 314 | 336 | 23 | inferred_complete_timeline |
| `Action_None` | 339 | 341 | 3 | inferred_complete_timeline |
| `Action_None` | 345 | 353 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 250 | 251 | inferred_complete_timeline |
| `Action_ZoneBlock` | 251 | 285 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 287 | 313 | 27 | inferred_complete_timeline |
| `Action_None` | 314 | 449 | 136 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 137 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 151 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 174 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 191 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 247 | 48 | inferred_complete_timeline |
| `Action_None` | 248 | 261 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–352
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 323 | 76 | inferred_complete_timeline |
| `Action_None` | 331 | 352 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–350
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 36 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 46 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 77 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 83 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 110 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 135 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 163 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 273 | 24 | inferred_complete_timeline |
| `Action_None` | 275 | 295 | 21 | inferred_complete_timeline |
| `Action_None` | 300 | 317 | 18 | inferred_complete_timeline |
| `Action_None` | 320 | 350 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 273 | 26 | inferred_complete_timeline |
| `Action_None` | 298 | 302 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 176 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 192 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–347
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 298 | 51 | inferred_complete_timeline |
| `Action_None` | 345 | 347 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–423
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 337 | 90 | inferred_complete_timeline |
| `Action_None` | 345 | 348 | 4 | inferred_complete_timeline |
| `Action_None` | 350 | 372 | 23 | inferred_complete_timeline |
| `Action_None` | 374 | 379 | 6 | inferred_complete_timeline |
| `Action_None` | 382 | 383 | 2 | inferred_complete_timeline |
| `Action_None` | 391 | 392 | 2 | inferred_complete_timeline |
| `Action_None` | 405 | 406 | 2 | inferred_complete_timeline |
| `Action_None` | 414 | 423 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–8
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–18 | 19 | 1 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–24 | 25 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–26 | 27 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 261–345 | 85 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 264–347 | 66 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 272–414 | 140 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 273–449 | 176 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 300–351 | 52 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 301–349 | 46 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 311–342 | 32 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 312–449 | 125 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 319–341 | 23 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 341–449 | 109 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 342–449 | 108 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 343–444 | 102 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 348–361 | 14 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 350–355 | 6 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 352–357 | 5 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 358–366 | 9 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 359–449 | 89 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 366–444 | 40 | 5 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 375–449 | 75 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 441–449 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 86 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 318: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [248–259], lower_priority='Action_ZoneBlock' annotated_start=251, effective_Action_ZoneBlock_start=260.
- ⚠️ Action 'Action_None' range [248-337] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-372] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-379] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-423] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-298] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-347] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-338] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [284-323] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-176] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [260-292] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-321] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-350] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [251-300] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-127] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-336] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-341] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-353] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [251-285] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-282] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-302] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-310] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-137] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-191] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-261] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-36] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-46] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-54] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-83] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-110] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-163] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-273] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-295] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-317] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-350] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-273] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-302] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-323] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-352] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-345] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-291] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-307] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-333] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-347] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-338] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-414] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-302] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-351] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-305] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-349] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-342] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-394] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-407] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-341] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-449] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-449] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-444] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-361] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-355] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-357] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-366] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-410] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-387] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-404] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-424] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-432] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-444] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-445] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>