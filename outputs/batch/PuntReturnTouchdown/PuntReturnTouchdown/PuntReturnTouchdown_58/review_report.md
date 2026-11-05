# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_58

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_58`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 115
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `41` | `30` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `41` | `30` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `41` | `30` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `0` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `1` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `14` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `17` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `18` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `3` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `4` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `7` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `8` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `9` | `Group` | 0 | START | 0 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `8` | `8` | 20 | START | 20 | 48 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `9` | `9` | 47 | END | 47 | 47 |
| ✅ EXACT | `Action_PuntBall` | Punter | `9` | `9` | 80 | START | 80 | 94 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `41` | `30` | 203 | START | 203 | 218 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `41` | `30` | 227 | START | 227 | 528 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `41` | `30` | 529 | START | 529 | 535 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–457
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 40 | 21 | inferred_complete_timeline |
| `Action_None` | 44 | 55 | 12 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_None` | 83 | 394 | 312 | inferred_complete_timeline |
| `Action_None` | 401 | 457 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 42 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 58 | 39 | inferred_complete_timeline |
| `Action_None` | 62 | 66 | 5 | inferred_complete_timeline |
| `Action_None` | 69 | 71 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_LongSnap` | 20 | 48 | 29 | inferred_complete_timeline |
| `Action_LongSnap` | 59 | 64 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–312
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 312 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 256 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–492
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 492 | 473 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–435
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 47 | 1 | inferred_complete_timeline |
| `Action_None` | 48 | 79 | 32 | inferred_complete_timeline |
| `Action_PuntBall` | 80 | 94 | 15 | inferred_complete_timeline |
| `Action_None` | 95 | 384 | 290 | inferred_complete_timeline |
| `Action_None` | 391 | 435 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 47 | 28 | inferred_complete_timeline |
| `Action_None` | 58 | 60 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 114 | 95 | inferred_complete_timeline |
| `Action_None` | 120 | 132 | 13 | inferred_complete_timeline |
| `Action_None` | 135 | 145 | 11 | inferred_complete_timeline |
| `Action_None` | 206 | 209 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 52 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–506
- **Visible Samples:** 506

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 70 | 51 | inferred_complete_timeline |
| `Action_None` | 72 | 506 | 435 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 156 | 137 | inferred_complete_timeline |
| `Action_None` | 158 | 318 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 282 | 263 | inferred_complete_timeline |
| `Action_None` | 286 | 539 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 76 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–404
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 404 | 385 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–520
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 520 | 501 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–486
- **Visible Samples:** 487

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 486 | 467 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–393
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 393 | 374 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 13–418 | 383 | 6 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 46–140 | 95 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 58–263 | 204 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 74–539 | 466 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 76–77 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 86–454 | 366 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 90–460 | 371 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 112–245 | 134 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 135–478 | 329 | 4 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 146–147 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 154–412 | 259 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 160–539 | 380 | 6 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 213–217 | 5 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 246–250 | 5 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 248–539 | 289 | 3 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 266–539 | 274 | 1 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 289–292 | 4 | 1 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 309–539 | 231 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 325–326 | 2 | 1 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 360–362 | 3 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 371–493 | 123 | 1 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 381–382 | 2 | 1 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 412–414 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `41` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 64 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [20-312] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-114] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-132] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-145] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-404] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-42] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-256] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-70] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-506] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-520] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-47] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [20-48] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [59-64] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-384] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-435] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-486] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-282] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-393] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-156] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-318] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-55] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-394] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-457] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-76] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-52] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-492] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-19] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-206] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-249] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-418] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-263] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-413] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-454] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-460] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-183] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-478] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-412] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-257] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-483] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-362] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-493] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-414] for track '42' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>