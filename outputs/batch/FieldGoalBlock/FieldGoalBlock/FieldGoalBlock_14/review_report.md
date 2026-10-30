# Play-Annotation-Generator Annotation Review — FieldGoalBlock_14

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_14`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 114
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
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `7` | `7` |
| ✅ EXACT | `Action_PlaceBall` | Interior_Rusher5 | defense | `3` | `3` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `1` | `1` |
| ✅ EXACT | `Action_BlockKick` | Right_Guard | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `1` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `12` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `13` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `5` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `6` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `7` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `8` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `9` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `7` | `7` | 6 | START | 6 | 21 |
| ✅ EXACT | `Action_PlaceBall` | Interior_Rusher5 | `3` | `3` | 22 | START | 22 | 35 |
| ✅ EXACT | `Action_KickBall` | Kicker | `1` | `1` | 45 | START | 45 | 52 |
| ✅ EXACT | `Action_BlockKick` | Right_Guard | `8` | `8` | 53 | START | 53 | 61 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_KickBall` | 45 | 52 | 8 | inferred_complete_timeline |
| `Action_None` | 53 | 85 | 33 | inferred_complete_timeline |
| `Action_None` | 89 | 150 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 111 | 106 | inferred_complete_timeline |
| `Action_None` | 114 | 127 | 14 | inferred_complete_timeline |
| `Action_None` | 135 | 150 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_LongSnap` | 6 | 21 | 16 | inferred_complete_timeline |
| `Action_None` | 22 | 59 | 38 | inferred_complete_timeline |
| `Action_None` | 62 | 84 | 23 | inferred_complete_timeline |
| `Action_None` | 136 | 140 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_BlockKick` | 53 | 61 | 9 | inferred_complete_timeline |
| `Action_None` | 62 | 64 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 134 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 31 | 26 | inferred_complete_timeline |
| `Action_None` | 34 | 58 | 25 | inferred_complete_timeline |
| `Action_None` | 66 | 150 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 26 | 21 | inferred_complete_timeline |
| `Action_None` | 42 | 54 | 13 | inferred_complete_timeline |
| `Action_None` | 64 | 67 | 4 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PlaceBall` | 22 | 35 | 14 | inferred_complete_timeline |
| `Action_None` | 36 | 150 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 23 | 18 | inferred_complete_timeline |
| `Action_None` | 28 | 78 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 34 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 24 | 19 | inferred_complete_timeline |
| `Action_None` | 28 | 70 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 13 | 8 | inferred_complete_timeline |
| `Action_None` | 16 | 150 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 83 | 78 | inferred_complete_timeline |
| `Action_None` | 93 | 96 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 2–41 | 14 | 5 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 17–150 | 132 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 17–150 | 134 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 21–24 | 4 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 39–150 | 81 | 6 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 40–53 | 14 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 61–63 | 3 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 81–117 | 29 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 82–149 | 28 | 5 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 83–150 | 47 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 102–150 | 46 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 103–150 | 48 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 106–127 | 18 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 114–150 | 37 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 115–150 | 22 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 118–135 | 18 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 119–135 | 17 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 132–150 | 19 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 137–150 | 14 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 141–150 | 10 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 148–150 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 30: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [6-83] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-85] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-24] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-70] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-34] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-150] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-111] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-127] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-59] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-23] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-78] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-26] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-54] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-67] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-134] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-31] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-58] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-13] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-4] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-23] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-70] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-24] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-57] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-87] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-144] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-53] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-63] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-92] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-117] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-143] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-92] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-115] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-150] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-127] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-131] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-135] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-135] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-150] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-150] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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