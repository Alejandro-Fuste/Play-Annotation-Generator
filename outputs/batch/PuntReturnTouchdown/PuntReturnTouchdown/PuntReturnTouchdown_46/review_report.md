# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_46

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_46`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 479
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 151
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Left_Edge_Rusher | defense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `34` | `27` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `34` | `27` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `0` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `10` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `2` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `3` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `5` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `6` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `7` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `8` | `Group` | 0 | START | 0 | 50 |
| ✅ EXACT | `Action_LongSnap` | Left_Edge_Rusher | `1` | `1` | 26 | START | 26 | 76 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `8` | `8` | 51 | END | 51 | 51 |
| ✅ EXACT | `Action_PuntBall` | Punter | `8` | `8` | 77 | START | 77 | 88 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `34` | `27` | 165 | START | 165 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `34` | `27` | 185 | START | 185 | 318 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `11` | `11` | 477 | START | 477 | 479 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 80 | 55 | inferred_complete_timeline |
| `Action_None` | 82 | 479 | 398 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 377 | 352 | inferred_complete_timeline |
| `Action_None` | 381 | 479 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–470
- **Visible Samples:** 467

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 346 | 321 | inferred_complete_timeline |
| `Action_None` | 349 | 379 | 31 | inferred_complete_timeline |
| `Action_None` | 381 | 382 | 2 | inferred_complete_timeline |
| `Action_None` | 384 | 470 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 479 | 454 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 281 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 479 | 454 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–456
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_SnapReceive` | 51 | 51 | 1 | inferred_complete_timeline |
| `Action_None` | 52 | 76 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 77 | 88 | 12 | inferred_complete_timeline |
| `Action_None` | 89 | 373 | 285 | inferred_complete_timeline |
| `Action_None` | 378 | 456 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–344
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 75 | 50 | inferred_complete_timeline |
| `Action_None` | 85 | 344 | 260 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–383
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 267 | 242 | inferred_complete_timeline |
| `Action_None` | 272 | 274 | 3 | inferred_complete_timeline |
| `Action_None` | 276 | 294 | 19 | inferred_complete_timeline |
| `Action_None` | 296 | 318 | 23 | inferred_complete_timeline |
| `Action_None` | 321 | 322 | 2 | inferred_complete_timeline |
| `Action_None` | 324 | 383 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 50 | 25 | inferred_complete_timeline |
| `Action_None` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_None` | 65 | 85 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 383 | 358 | inferred_complete_timeline |
| `Action_None` | 385 | 408 | 24 | inferred_complete_timeline |
| `Action_None` | 411 | 413 | 3 | inferred_complete_timeline |
| `Action_None` | 415 | 424 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 58 | 33 | inferred_complete_timeline |
| `Action_None` | 64 | 212 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 68 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 82 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 479 | 454 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_LongSnap` | 26 | 76 | 51 | inferred_complete_timeline |
| `Action_None` | 77 | 314 | 238 | inferred_complete_timeline |
| `Action_None` | 316 | 396 | 81 | inferred_complete_timeline |
| `Action_None` | 399 | 479 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 106 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–479 | 475 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–447 | 444 | 6 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 72–240 | 169 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 77–287 | 208 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 80–470 | 389 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 85–479 | 390 | 3 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 90–91 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 92–95 | 4 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 94–213 | 119 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 101–107 | 7 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 111–374 | 257 | 8 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 115–460 | 346 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 236–338 | 91 | 4 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 238–479 | 242 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 250–479 | 228 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 307–311 | 5 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 339–342 | 4 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 356–358 | 3 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 359–361 | 3 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 362–479 | 118 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 362–377 | 16 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 362–479 | 117 | 2 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 375–479 | 105 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 384–479 | 96 | 1 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 388–467 | 80 | 1 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 390–479 | 84 | 2 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 430–438 | 9 | 1 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 430–460 | 28 | 2 | Undefined position; Undefined team |
| `45` | `66` | Position_Unknown | Team_Unknown | 432–449 | 18 | 1 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 436–437 | 2 | 1 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 439–473 | 35 | 1 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 446–462 | 8 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `34` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 82 |
| Track-related warning | 2 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 94: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Row 94: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [77-314] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-396] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-75] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-344] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-346] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-379] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-470] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-383] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-408] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-413] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-424] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-281] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-80] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-479] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-373] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-456] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-479] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-377] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-216] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-212] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-304] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-310] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-447] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-267] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-294] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-318] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-383] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-50] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-240] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-268] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-287] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-216] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-470] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-379] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-396] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-479] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-107] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [185-318] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [321-328] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [331-344] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [347-371] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [373-374] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-460] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-308] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-319] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-333] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-338] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-311] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-342] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-358] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-361] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-377] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-371] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-479] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-467] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-465] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-438] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-455] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-449] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-437] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-473] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-448] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-453] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-462] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>