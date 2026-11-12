# Play-Annotation-Generator Annotation Review — SplitZone_16

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_16`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 32
- **Ball Tracks:** 1
- **Action Segments:** 79
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `13` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 170 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `9` | 171 | START | 171 | 187 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `11` | 174 | START | 174 | 268 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `12` | 174 | START | 174 | 240 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `15` | 174 | START | 174 | 256 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `3` | 174 | START | 174 | 182 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `9` | `9` | 174 | START | 188 | 220 |
| ✅ EXACT | `Action_SplitBlock` | LT | `3` | `3` | 183 | START | 183 | 268 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 187 | END | 171 | 187 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `7` | 197 | START | 197 | 222 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `9` | `9` | 221 | START | 221 | 263 |
| ✅ EXACT | `Action_BallCarry` | RB | `4` | `4` | 223 | START | 223 | 278 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 268 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_SnapReceive` | 171 | 187 | 17 | inferred_complete_timeline |
| `Action_None` | 188 | 196 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 197 | 222 | 26 | inferred_complete_timeline |
| `Action_None` | 223 | 379 | 157 | inferred_complete_timeline |
| `Action_None` | 381 | 407 | 27 | inferred_complete_timeline |
| `Action_None` | 410 | 419 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |
| `Action_BallCarry` | 223 | 278 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 216 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–368
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 182 | 9 | inferred_complete_timeline |
| `Action_SplitBlock` | 183 | 268 | 86 | inferred_complete_timeline |
| `Action_None` | 269 | 368 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–364
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 256 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 258 | 268 | 11 | inferred_complete_timeline |
| `Action_None` | 269 | 350 | 82 | inferred_complete_timeline |
| `Action_None` | 356 | 364 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_BallSnap` | 171 | 187 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 220 | 33 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 221 | 263 | 43 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 265 | 266 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 240 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 268 | 95 | inferred_complete_timeline |
| `Action_None` | 269 | 399 | 131 | inferred_complete_timeline |
| `Action_None` | 407 | 419 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–397
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 397 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 419 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 288 | 118 | inferred_complete_timeline |
| `Action_None` | 290 | 292 | 3 | inferred_complete_timeline |
| `Action_None` | 294 | 419 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–339
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 339 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 289 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–364
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 355 | 185 | inferred_complete_timeline |
| `Action_None` | 361 | 364 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 419 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–343
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 294 | 124 | inferred_complete_timeline |
| `Action_None` | 296 | 343 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 64–174 | 44 | 8 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 227–361 | 113 | 4 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 240–308 | 69 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 243–244 | 2 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 271–272 | 2 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 274–286 | 13 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 284–302 | 14 | 3 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 307–349 | 43 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 315–345 | 31 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 325–338 | 14 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 338–417 | 80 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 346–419 | 74 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 380–419 | 40 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 380–382 | 3 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 394–419 | 26 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 416–419 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | 65 | 154 | 18 | 20.0% | 66–75, 77, 79, 83–97, 108–152 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `9` (C): Annotated start 174 != Inferred start 188
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [171–187], lower_priority='Action_ZoneBlock' annotated_start=174, effective_Action_ZoneBlock_start=188.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (RT) duration 95 frames exceeds threshold 90 frames [start=174, end=268].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (LG) duration 95 frames exceeds threshold 90 frames [start=174, end=268].
- ⚠️ Action 'Action_None' range [171-294] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-343] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-355] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-364] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-339] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [183-268] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-368] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [223-278] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-289] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-397] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-379] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-407] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-419] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [221-263] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [265-266] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-288] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-419] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-399] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [174-240] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-216] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-419] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [174-256] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-350] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-364] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-66] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-160] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-170] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-270] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-351] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-361] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-308] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-286] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-288] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-349] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-345] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-338] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-417] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-419] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-382] for track '30' has 1 frames without a visible bounding box.
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

</details>