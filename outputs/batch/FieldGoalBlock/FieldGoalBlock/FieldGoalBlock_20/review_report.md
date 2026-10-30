# Play-Annotation-Generator Annotation Review — FieldGoalBlock_20

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_20`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 131
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 102
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `12` | `12` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `2` | `2` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `1` | `1` |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher1 | defense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `1` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `10` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `11` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `2` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `4` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `7` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `12` | `12` | 2 | START | 2 | 16 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `2` | `2` | 17 | START | 17 | 31 |
| ✅ EXACT | `Action_KickBall` | Kicker | `1` | `1` | 42 | START | 42 | 47 |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher1 | `5` | `5` | 48 | START | 48 | 57 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PlaceBall` | 17 | 31 | 15 | inferred_complete_timeline |
| `Action_None` | 32 | 45 | 14 | inferred_complete_timeline |
| `Action_None` | 47 | 49 | 3 | inferred_complete_timeline |
| `Action_None` | 53 | 56 | 4 | inferred_complete_timeline |
| `Action_None` | 62 | 299 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_KickBall` | 42 | 47 | 6 | inferred_complete_timeline |
| `Action_None` | 48 | 219 | 172 | inferred_complete_timeline |
| `Action_None` | 221 | 224 | 4 | inferred_complete_timeline |
| `Action_None` | 228 | 274 | 47 | inferred_complete_timeline |
| `Action_None` | 285 | 299 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 299 | 298 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 44 | 43 | inferred_complete_timeline |
| `Action_None` | 58 | 185 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 24 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_LongSnap` | 2 | 16 | 15 | inferred_complete_timeline |
| `Action_None` | 17 | 24 | 8 | inferred_complete_timeline |
| `Action_None` | 28 | 31 | 4 | inferred_complete_timeline |
| `Action_None` | 43 | 58 | 16 | inferred_complete_timeline |
| `Action_None` | 74 | 122 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 21 | 20 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_None` | 74 | 79 | 6 | inferred_complete_timeline |
| `Action_None` | 82 | 85 | 4 | inferred_complete_timeline |
| `Action_None` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_None` | 96 | 129 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 31 | 30 | inferred_complete_timeline |
| `Action_None` | 62 | 131 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 299 | 298 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_BlockKick` | 48 | 57 | 10 | inferred_complete_timeline |
| `Action_None` | 58 | 299 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 18 | 17 | inferred_complete_timeline |
| `Action_None` | 22 | 28 | 7 | inferred_complete_timeline |
| `Action_None` | 30 | 40 | 11 | inferred_complete_timeline |
| `Action_None` | 42 | 94 | 53 | inferred_complete_timeline |
| `Action_None` | 97 | 214 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 20 | 19 | inferred_complete_timeline |
| `Action_None` | 31 | 34 | 4 | inferred_complete_timeline |
| `Action_None` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_None` | 40 | 48 | 9 | inferred_complete_timeline |
| `Action_None` | 57 | 62 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 18 | 17 | inferred_complete_timeline |
| `Action_None` | 20 | 221 | 202 | inferred_complete_timeline |
| `Action_None` | 225 | 229 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 52 | 51 | inferred_complete_timeline |
| `Action_None` | 58 | 64 | 7 | inferred_complete_timeline |
| `Action_None` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 173 | 104 | inferred_complete_timeline |
| `Action_None` | 180 | 294 | 115 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 261 | 260 | inferred_complete_timeline |
| `Action_None` | 264 | 265 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–38
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 18 | 17 | inferred_complete_timeline |
| `Action_None` | 22 | 30 | 9 | inferred_complete_timeline |
| `Action_None` | 32 | 38 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–62 | 63 | 2 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–40 | 41 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 6–299 | 292 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 7–207 | 133 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 34–212 | 179 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 40–140 | 63 | 6 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 42–261 | 205 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 42–195 | 153 | 2 | Undefined position; Undefined team |
| `24` | `37` | Position_Unknown | Team_Unknown | 75–82 | 4 | 2 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 76–299 | 224 | 1 | Undefined position; Undefined team |
| `26` | `43` | Position_Unknown | Team_Unknown | 99–149 | 39 | 5 | Undefined position; Undefined team |
| `27` | `44` | Position_Unknown | Team_Unknown | 102–255 | 153 | 2 | Undefined position; Undefined team |
| `28` | `47` | Position_Unknown | Team_Unknown | 114–167 | 35 | 5 | Undefined position; Undefined team |
| `29` | `51` | Position_Unknown | Team_Unknown | 134–203 | 70 | 1 | Undefined position; Undefined team |
| `30` | `52` | Position_Unknown | Team_Unknown | 143–151 | 8 | 2 | Undefined position; Undefined team |
| `31` | `54` | Position_Unknown | Team_Unknown | 149–157 | 9 | 1 | Undefined position; Undefined team |
| `32` | `55` | Position_Unknown | Team_Unknown | 152–153 | 2 | 1 | Undefined position; Undefined team |
| `33` | `56` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `34` | `57` | Position_Unknown | Team_Unknown | 197–201 | 5 | 1 | Undefined position; Undefined team |
| `35` | `58` | Position_Unknown | Team_Unknown | 286–299 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 87 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 42: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 42: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ Row 42: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [2-261] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-274] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-45] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-49] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-299] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-44] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-185] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-62] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-18] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-28] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-40] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-94] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-214] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-40] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-21] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-79] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-24] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [2-16] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-24] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-31] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-58] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-18] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-30] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-38] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-31] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-131] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-52] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-64] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-294] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-34] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-48] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-62] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-18] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-229] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-137] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-11] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-207] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-212] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-43] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-52] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-90] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-99] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-140] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-105] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-261] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-43] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-195] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-142] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-255] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-118] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-146] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-203] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-157] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>