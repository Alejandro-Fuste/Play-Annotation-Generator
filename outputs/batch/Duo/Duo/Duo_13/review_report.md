# Play-Annotation-Generator Annotation Review — Duo_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_13`
- **Frame Range:** 0 to 358 (359 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 358
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `18` | `18` |
| ⚠️ START CHANGED | `Action_ComboBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | TE2 | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 304 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 358 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 227 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 227 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 358 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 245 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 218 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 73 | 345 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 225 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 303 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | `13` | `13` | 228 | START | 228 | 229 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | `15` | `15` | 228 | START | 228 | 230 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | `18` | `18` | 228 | START | 228 | 275 |
| ⚠️ START CHANGED | `Action_ComboBlock` | RG | `20` | `20` | 228 | START | 238 | 243 |
| ✅ EXACT | `Action_BallCarry` | RB | `2` | `2` | 246 | START | 246 | 358 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | TE2 | `3` | `3` | 256 | START | 256 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 295 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 73–345
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 73 | 345 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_BallCarry` | 246 | 358 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 304 | 305 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 340 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 358 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 320 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 325 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 255 | 20 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 256 | 269 | 14 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 271 | 272 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_ComboBlock` | 228 | 230 | 3 | inferred_complete_timeline |
| `Action_ComboBlock` | 232 | 295 | 64 | inferred_complete_timeline |
| `Action_None` | 296 | 358 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_ComboBlock` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 249 | 254 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 218 | 219 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 238 | 243 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 280 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 358 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–290
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 290 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 254 | 255 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 259 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 269 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 275 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 280 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 287 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 295 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 308 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 358 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 321 | 322 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 325 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 285 | 286 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 358 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–293 | 284 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 227–249 | 9 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 254–342 | 7 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 265–267 | 3 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 292–343 | 46 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 305–358 | 54 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 307–358 | 43 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 310–358 | 49 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 316–358 | 43 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 320–321 | 2 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 320–358 | 29 | 4 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 331–358 | 28 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 357–358 | 2 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 357–358 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `18` (2 segments found)
- ⚠️ `Action_ComboBlock` for actor_track_id `20` (RG): Annotated start 228 != Inferred start 238
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 28: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-304] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-340] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-358] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [246-358] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-225] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [256-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [271-272] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-254] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-259] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-275] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-280] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-287] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-295] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-308] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-358] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-303] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-320] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-325] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-285] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-358] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-290] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-321] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-325] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-227] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [228-229] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [236-237] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [249-254] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-227] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [228-230] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [232-295] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-227] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [228-275] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [285-293] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-280] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-218] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [238-243] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-345] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-229] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-249] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-342] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-267] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-305] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-311] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-343] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-358] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-332] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-358] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-358] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-358] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-334] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-355] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-358] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-358] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>