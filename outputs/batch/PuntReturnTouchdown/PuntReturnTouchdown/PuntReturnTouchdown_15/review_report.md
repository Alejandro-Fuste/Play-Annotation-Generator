# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_15

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_15`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `10` | `10` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `10` | `10` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `27` | `24` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `27` | `24` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `27` | `24` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `10` | `Group` | 0 | START | 0 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `13` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `18` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `19` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `20` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `3` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `6` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `7` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `9` | `Group` | 0 | START | 0 | 138 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `7` | `7` | 139 | START | 139 | 176 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `10` | `10` | 165 | END | 165 | 165 |
| ✅ EXACT | `Action_PuntBall` | Punter | `10` | `10` | 177 | START | 177 | 206 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `27` | `24` | 322 | START | 322 | 334 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `27` | `24` | 347 | START | 347 | 595 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `27` | `24` | 596 | START | 596 | 599 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 596

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 204 | 66 | inferred_complete_timeline |
| `Action_None` | 206 | 435 | 230 | inferred_complete_timeline |
| `Action_None` | 439 | 599 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–406
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 361 | 223 | inferred_complete_timeline |
| `Action_None` | 363 | 406 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 599 | 461 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 599 | 461 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_LongSnap` | 139 | 176 | 38 | inferred_complete_timeline |
| `Action_None` | 177 | 355 | 179 | inferred_complete_timeline |
| `Action_None` | 357 | 599 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 447 | 309 | inferred_complete_timeline |
| `Action_None` | 454 | 599 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_SnapReceive` | 165 | 165 | 1 | inferred_complete_timeline |
| `Action_None` | 166 | 176 | 11 | inferred_complete_timeline |
| `Action_PuntBall` | 177 | 206 | 30 | inferred_complete_timeline |
| `Action_None` | 207 | 273 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 599 | 461 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 584

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 216 | 78 | inferred_complete_timeline |
| `Action_None` | 233 | 599 | 367 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 599 | 461 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–543
- **Visible Samples:** 543

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 468 | 330 | inferred_complete_timeline |
| `Action_None` | 470 | 543 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 599 | 461 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–511
- **Visible Samples:** 512

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 511 | 373 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–462
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 456 | 318 | inferred_complete_timeline |
| `Action_None` | 458 | 462 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–522
- **Visible Samples:** 523

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 522 | 384 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 466 | 328 | inferred_complete_timeline |
| `Action_None` | 468 | 599 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–559
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 559 | 421 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 596

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 222 | 84 | inferred_complete_timeline |
| `Action_None` | 225 | 492 | 268 | inferred_complete_timeline |
| `Action_None` | 495 | 599 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–553 | 543 | 4 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–305 | 306 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–319 | 317 | 4 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 123–130 | 8 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 188–196 | 6 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 253–257 | 5 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 318–599 | 282 | 5 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 394–395 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 402–576 | 175 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 427–563 | 137 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 435–599 | 165 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 455–562 | 108 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 575–599 | 25 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 32: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [139-361] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-406] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-197] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-245] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-553] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-305] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-216] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-599] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-468] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-543] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-599] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-355] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-559] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-273] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-522] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-511] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-447] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-466] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-599] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-222] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-492] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-218] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-227] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-319] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-456] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-462] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-435] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-599] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-599] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-130] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-257] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-576] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-563] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-562] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>