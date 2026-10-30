# Play-Annotation-Generator Annotation Review — FieldGoalBlock_28

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_28`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `22` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Interior_Rusher3 | defense | `20` | `20` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `10` | `10` |
| ✅ EXACT | `Action_KickBall` | Right_Edge_Rusher | defense | `6` | `6` |
| ✅ EXACT | `Action_BlockKick` | Right_Guard | offense | `22` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `10` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End1 | `12` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `16` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `18` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `22` | `Group` | 0 | START | 16 | 20 |
| ✅ EXACT | `Action_LongSnap` | Interior_Rusher3 | `20` | `20` | 29 | START | 29 | 41 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `10` | `10` | 42 | START | 42 | 57 |
| ✅ EXACT | `Action_KickBall` | Right_Edge_Rusher | `6` | `6` | 67 | START | 67 | 72 |
| ✅ EXACT | `Action_BlockKick` | Right_Guard | `22` | `21` | 71 | START | 71 | 76 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 41 | 16 | inferred_complete_timeline |
| `Action_PlaceBall` | 42 | 57 | 16 | inferred_complete_timeline |
| `Action_None` | 58 | 180 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 52 | 24 | inferred_complete_timeline |
| `Action_None` | 60 | 72 | 13 | inferred_complete_timeline |
| `Action_None` | 74 | 88 | 15 | inferred_complete_timeline |
| `Action_None` | 90 | 180 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 37 | 9 | inferred_complete_timeline |
| `Action_None` | 42 | 68 | 27 | inferred_complete_timeline |
| `Action_None` | 77 | 135 | 59 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 155 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 52 | 24 | inferred_complete_timeline |
| `Action_None` | 55 | 180 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 16–76
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 20 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 33 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 70 | 19 | inferred_complete_timeline |
| `Action_BlockKick` | 71 | 76 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 37 | 9 | inferred_complete_timeline |
| `Action_None` | 40 | 180 | 141 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 65 | 37 | inferred_complete_timeline |
| `Action_None` | 76 | 136 | 61 | inferred_complete_timeline |
| `Action_None` | 140 | 180 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 7–163
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 28 | 22 | inferred_complete_timeline |
| `Action_LongSnap` | 29 | 41 | 13 | inferred_complete_timeline |
| `Action_None` | 42 | 72 | 31 | inferred_complete_timeline |
| `Action_None` | 82 | 141 | 60 | inferred_complete_timeline |
| `Action_None` | 144 | 163 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 28 | 9 | inferred_complete_timeline |
| `Action_None` | 29 | 42 | 14 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 109 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 72 | 44 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 126 | 23 | inferred_complete_timeline |
| `Action_None` | 128 | 135 | 8 | inferred_complete_timeline |
| `Action_None` | 144 | 156 | 13 | inferred_complete_timeline |
| `Action_None` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_None` | 176 | 180 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 37 | 114 | 78 | inferred_complete_timeline |
| `Action_None` | 119 | 177 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 2–42
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 29 | 42 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_KickBall` | 67 | 72 | 6 | inferred_complete_timeline |
| `Action_None` | 73 | 180 | 108 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–180 | 181 | 2 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–178 | 179 | 2 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–180 | 179 | 3 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–180 | 172 | 5 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–84 | 68 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 91–94 | 4 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 93–133 | 41 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 93–180 | 88 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 93–94 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 129–180 | 35 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 145–180 | 36 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 150–154 | 4 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 160–180 | 21 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 168–180 | 13 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 173–180 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_End1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `22`): `Right_Guard` position mapped to `offense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 58: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 58: Duplicate assignment for track ID '20' in grid. Overwriting previous assignment.
- ⚠️ Row 58: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ Row 58: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ Row 58: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [29-180] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-178] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-72] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-126] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-135] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-61] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-135] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-147] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-114] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-177] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-180] for track '10' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-65] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-52] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-180] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-52] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-72] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-68] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-135] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-42] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-37] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-42] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-141] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-163] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-20] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-33] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' for track '21' starts at frame 71, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BlockKick' range [71-76] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-180] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-180] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>