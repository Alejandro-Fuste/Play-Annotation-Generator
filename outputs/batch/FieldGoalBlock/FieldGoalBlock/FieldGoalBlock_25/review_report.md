# Play-Annotation-Generator Annotation Review — FieldGoalBlock_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_25`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 100
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `16` | `16` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `7` | `7` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | Team_Unknown | `26` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `0` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `10` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `16` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `5` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `7` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `9` | `Group` | 0 | START | 0 | 10 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `16` | `16` | 11 | START | 11 | 12 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `7` | `7` | 27 | START | 27 | 40 |
| ✅ EXACT | `Action_KickBall` | Kicker | `5` | `5` | 50 | START | 50 | 55 |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | `26` | `22` | 55 | START | 55 | 65 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PlaceBall` | 27 | 40 | 14 | inferred_complete_timeline |
| `Action_None` | 41 | 49 | 9 | inferred_complete_timeline |
| `Action_None` | 90 | 125 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_KickBall` | 50 | 55 | 6 | inferred_complete_timeline |
| `Action_None` | 56 | 117 | 62 | inferred_complete_timeline |
| `Action_None` | 119 | 128 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 43 | 33 | inferred_complete_timeline |
| `Action_None` | 55 | 59 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–26
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_LongSnap` | 11 | 12 | 2 | inferred_complete_timeline |
| `Action_LongSnap` | 20 | 26 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 20 | 10 | inferred_complete_timeline |
| `Action_None` | 22 | 35 | 14 | inferred_complete_timeline |
| `Action_None` | 40 | 60 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 130 | 120 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 36 | 26 | inferred_complete_timeline |
| `Action_None` | 40 | 42 | 3 | inferred_complete_timeline |
| `Action_None` | 45 | 133 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 39 | 29 | inferred_complete_timeline |
| `Action_None` | 45 | 52 | 8 | inferred_complete_timeline |
| `Action_None` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_None` | 60 | 63 | 4 | inferred_complete_timeline |
| `Action_None` | 65 | 73 | 9 | inferred_complete_timeline |
| `Action_None` | 75 | 82 | 8 | inferred_complete_timeline |
| `Action_None` | 85 | 90 | 6 | inferred_complete_timeline |
| `Action_None` | 94 | 129 | 36 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 31 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 73 | 16 | inferred_complete_timeline |
| `Action_None` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_None` | 94 | 129 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–36
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 17 | 7 | inferred_complete_timeline |
| `Action_None` | 20 | 30 | 11 | inferred_complete_timeline |
| `Action_None` | 35 | 36 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–20
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 18 | 20 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–22
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 22 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 73 | 63 | inferred_complete_timeline |
| `Action_None` | 77 | 134 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 34 | 24 | inferred_complete_timeline |
| `Action_None` | 52 | 55 | 4 | inferred_complete_timeline |
| `Action_None` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_None` | 62 | 66 | 5 | inferred_complete_timeline |
| `Action_None` | 71 | 73 | 3 | inferred_complete_timeline |
| `Action_None` | 79 | 84 | 6 | inferred_complete_timeline |
| `Action_None` | 87 | 131 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 21 | 11 | inferred_complete_timeline |
| `Action_None` | 24 | 32 | 9 | inferred_complete_timeline |
| `Action_None` | 47 | 136 | 90 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–129 | 130 | 2 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–135 | 136 | 2 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–130 | 131 | 2 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–128 | 96 | 6 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 25–138 | 113 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 28–129 | 59 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 38–138 | 80 | 4 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 43–90 | 45 | 4 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 66–129 | 64 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 69–137 | 57 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 79–137 | 4 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 90–140 | 37 | 4 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 103–139 | 26 | 3 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 106–110 | 5 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 108–129 | 22 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 128–130 | 3 | 1 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 134–135 | 2 | 1 | Undefined position; Undefined team |
| `32` | `51` | Position_Unknown | Team_Unknown | 139–142 | 4 | 1 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 149–150 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 88 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 52: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ Row 52: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 52: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [11-130] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-135] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-130] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-48] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-51] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-94] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-128] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-128] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-36] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-42] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-49] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-125] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-31] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-73] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-129] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-43] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-59] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-20] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-35] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-60] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-34] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-55] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-66] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-73] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-131] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-32] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-39] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-52] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-63] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-73] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-129] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-17] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-30] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-22] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [11-12] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [20-26] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-73] for track '17' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-134] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-20] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-29] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-67] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-45] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-81] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-73] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-90] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-129] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-102] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-129] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-120] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-114] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-128] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-129] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>