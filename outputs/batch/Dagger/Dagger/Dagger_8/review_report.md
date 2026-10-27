# Play-Annotation-Generator Annotation Review — Dagger_8

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_8`
- **Frame Range:** 0 to 418 (419 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Rec`
- **Result Frame:** 418
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 47
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | TE | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_BreakInside` | WR2 | offense | `9` | `9` |
| ✅ EXACT | `Action_ClearToEdge` | WR1 | offense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `6` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 193 |
| ✅ EXACT | `Action_BallSnap` | TE | `19` | `19` | 182 | START | 182 | 188 |
| ✅ EXACT | `Action_PassBlock` | LT | `15` | `15` | 185 | START | 185 | 381 |
| ✅ EXACT | `Action_PassBlock` | RT | `17` | `17` | 185 | START | 185 | 388 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 185 | START | 185 | 346 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 185 | START | 185 | 270 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 185 | START | 185 | 215 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 188 | END | 182 | 188 |
| ✅ EXACT | `Action_BreakInside` | WR2 | `9` | `9` | 194 | START | 194 | 322 |
| ✅ EXACT | `Action_ClearToEdge` | WR1 | `5` | `5` | 194 | START | 194 | 285 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 276 | START | 276 | 285 |

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
- **Visible Frames:** 0–364
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_SnapReceive` | 182 | 188 | 7 | inferred_complete_timeline |
| `Action_None` | 189 | 275 | 87 | inferred_complete_timeline |
| `Action_ThrowPass` | 276 | 285 | 10 | inferred_complete_timeline |
| `Action_None` | 286 | 364 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–363
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 363 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 266 | 85 | inferred_complete_timeline |
| `Action_None` | 270 | 277 | 8 | inferred_complete_timeline |
| `Action_None` | 279 | 294 | 16 | inferred_complete_timeline |
| `Action_None` | 296 | 297 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_ClearToEdge` | 194 | 285 | 92 | inferred_complete_timeline |
| `Action_None` | 286 | 418 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–380
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_BreakInside` | 194 | 322 | 129 | inferred_complete_timeline |
| `Action_None` | 323 | 350 | 28 | inferred_complete_timeline |
| `Action_None` | 357 | 360 | 4 | inferred_complete_timeline |
| `Action_None` | 362 | 376 | 15 | inferred_complete_timeline |
| `Action_None` | 378 | 380 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–378
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_BallSnap` | 182 | 188 | 7 | inferred_complete_timeline |
| `Action_None` | 189 | 378 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–381
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_PassBlock` | 185 | 381 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–375
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 184 | 181 | inferred_complete_timeline |
| `Action_PassBlock` | 185 | 215 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 219 | 328 | 110 | inferred_complete_timeline |
| `Action_PassBlock` | 331 | 347 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 350 | 375 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–400
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_PassBlock` | 185 | 346 | 162 | inferred_complete_timeline |
| `Action_PassBlock` | 348 | 400 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–381
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_PassBlock` | 185 | 270 | 86 | inferred_complete_timeline |
| `Action_PassBlock` | 276 | 381 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_PassBlock` | 185 | 388 | 204 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 418 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–414
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 414 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–405
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 329 | 148 | inferred_complete_timeline |
| `Action_None` | 331 | 405 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 418 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–384
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 363 | 182 | inferred_complete_timeline |
| `Action_None` | 366 | 379 | 14 | inferred_complete_timeline |
| `Action_None` | 381 | 384 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 418 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–406
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 406 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–364
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 356 | 175 | inferred_complete_timeline |
| `Action_None` | 360 | 364 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 418 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 418 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 418 | 237 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 333–380 | 48 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 371–418 | 43 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 390–418 | 28 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 397–398 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 38 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 418 as fallback play end.
- ⚠️ Action 'Action_None' range [182-356] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-364] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-363] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-379] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-363] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-266] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-277] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-294] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-350] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-360] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-376] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-181] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-406] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-405] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-414] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [185-381] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-364] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [185-388] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [185-346] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [348-400] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-378] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [185-270] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [276-381] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [185-215] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [219-328] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [331-347] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [350-375] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-380] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-398] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>