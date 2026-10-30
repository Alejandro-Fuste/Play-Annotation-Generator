# Play-Annotation-Generator Annotation Review — FieldGoalBlock_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_19`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 50
- **Ball Tracks:** 0
- **Action Segments:** 132
- **Validation Warnings:** 181
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 8
- **Exact Matches:** 3
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 122
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Interior_Rusher3 | defense | `12` | `12` |
| ✅ EXACT | `Action_KickBall` | Left_Edge_Rusher | defense | `6` | `6` |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher7 | defense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `1` | `Group` | 5 | START | 5 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `14` | `Group` | 5 | START | 5 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `2` | `Group` | 5 | START | 5 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `4` | `Group` | 5 | START | 5 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `9` | `Group` | 5 | START | 5 | 49 |
| ✅ EXACT | `Action_PlaceBall` | Interior_Rusher3 | `12` | `12` | 43 | START | 43 | 59 |
| ✅ EXACT | `Action_KickBall` | Left_Edge_Rusher | `6` | `6` | 70 | START | 70 | 73 |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher7 | `8` | `8` | 74 | START | 74 | 90 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_End — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 5–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 69 | 65 | inferred_complete_timeline |
| `Action_None` | 70 | 299 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 5–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 46 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 69 | 11 | inferred_complete_timeline |
| `Action_None` | 70 | 77 | 8 | inferred_complete_timeline |
| `Action_None` | 79 | 299 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 5–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 69 | 65 | inferred_complete_timeline |
| `Action_None` | 70 | 299 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 5–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 49 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 69 | 19 | inferred_complete_timeline |
| `Action_None` | 70 | 299 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 5–99
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 69 | 65 | inferred_complete_timeline |
| `Action_None` | 70 | 85 | 16 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_None` | 91 | 99 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 69 | 65 | inferred_complete_timeline |
| `Action_None` | 70 | 299 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 69 | 65 | inferred_complete_timeline |
| `Action_None` | 70 | 82 | 13 | inferred_complete_timeline |
| `Action_None` | 85 | 299 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 5–256
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 42 | 38 | inferred_complete_timeline |
| `Action_PlaceBall` | 43 | 59 | 17 | inferred_complete_timeline |
| `Action_None` | 60 | 256 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 57 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 64 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 68 | 3 | inferred_complete_timeline |
| `Action_None` | 70 | 93 | 24 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 41 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 69 | 1 | inferred_complete_timeline |
| `Action_None` | 70 | 299 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 5–105
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 73 | 69 | inferred_complete_timeline |
| `Action_BlockKick` | 74 | 90 | 17 | inferred_complete_timeline |
| `Action_None` | 91 | 98 | 8 | inferred_complete_timeline |
| `Action_None` | 101 | 105 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 39–72
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 60 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 69 | 6 | inferred_complete_timeline |
| `Action_None` | 70 | 72 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 69 | 65 | inferred_complete_timeline |
| `Action_KickBall` | 70 | 73 | 4 | inferred_complete_timeline |
| `Action_None` | 74 | 299 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 69 | 65 | inferred_complete_timeline |
| `Action_None` | 70 | 299 | 230 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 5–109 | 105 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 5–69 | 62 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 5–44 | 39 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 5–299 | 255 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 5–299 | 263 | 3 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 56–299 | 243 | 3 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 74–89 | 8 | 2 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 78–299 | 214 | 2 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 84–299 | 216 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 84–98 | 9 | 3 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 94–299 | 206 | 1 | Undefined position; Undefined team |
| `25` | `40` | Position_Unknown | Team_Unknown | 107–299 | 137 | 13 | Undefined position; Undefined team |
| `26` | `41` | Position_Unknown | Team_Unknown | 107–299 | 189 | 2 | Undefined position; Undefined team |
| `27` | `42` | Position_Unknown | Team_Unknown | 107–299 | 193 | 1 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 108–112 | 5 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 109–299 | 189 | 3 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 122–153 | 28 | 2 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 124–129 | 6 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 139–145 | 7 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 158–299 | 142 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 180–255 | 43 | 7 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 185–192 | 5 | 2 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 192–229 | 13 | 3 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `39` | `66` | Position_Unknown | Team_Unknown | 223–239 | 11 | 2 | Undefined position; Undefined team |
| `40` | `67` | Position_Unknown | Team_Unknown | 229–233 | 4 | 2 | Undefined position; Undefined team |
| `41` | `70` | Position_Unknown | Team_Unknown | 237–299 | 52 | 6 | Undefined position; Undefined team |
| `42` | `71` | Position_Unknown | Team_Unknown | 238–299 | 55 | 5 | Undefined position; Undefined team |
| `43` | `73` | Position_Unknown | Team_Unknown | 244–268 | 15 | 2 | Undefined position; Undefined team |
| `44` | `74` | Position_Unknown | Team_Unknown | 249–252 | 4 | 1 | Undefined position; Undefined team |
| `45` | `76` | Position_Unknown | Team_Unknown | 260–261 | 2 | 1 | Undefined position; Undefined team |
| `46` | `77` | Position_Unknown | Team_Unknown | 262–299 | 38 | 1 | Undefined position; Undefined team |
| `47` | `78` | Position_Unknown | Team_Unknown | 271–274 | 4 | 1 | Undefined position; Undefined team |
| `48` | `80` | Position_Unknown | Team_Unknown | 286–287 | 2 | 1 | Undefined position; Undefined team |
| `49` | `83` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 103 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 40: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ Row 40: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 40: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 40: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 40: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [70-85] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-99] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-109] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [74-90] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-98] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-105] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-49] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-41] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-57] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-57] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-64] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-68] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-93] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-256] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-60] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-49] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-299] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-25] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-52] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-51] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-60] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-69] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-67] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-86] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-91] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-114] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-187] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-205] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-224] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-234] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-255] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-288] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-124] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-141] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-283] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-145] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-145] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-184] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-209] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-238] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-231] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-246] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-257] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-264] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-275] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-297] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-242] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-265] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-275] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-282] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-299] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-268] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-299] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.

</details>