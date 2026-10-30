# Play-Annotation-Generator Annotation Review — FieldGoalBlock_6

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_6`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 113
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
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `12` | `12` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `7` | `7` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher3 | defense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `14` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `15` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `17` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `5` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `7` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `9` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `12` | `12` | 4 | START | 4 | 18 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `7` | `7` | 19 | START | 19 | 28 |
| ✅ EXACT | `Action_KickBall` | Kicker | `5` | `5` | 42 | START | 42 | 50 |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher3 | `10` | `10` | 50 | START | 50 | 68 |

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
- **Visible Frames:** 0–133
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PlaceBall` | 19 | 28 | 10 | inferred_complete_timeline |
| `Action_None` | 29 | 83 | 55 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 92 | 122 | 31 | inferred_complete_timeline |
| `Action_None` | 129 | 133 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_KickBall` | 42 | 50 | 9 | inferred_complete_timeline |
| `Action_None` | 51 | 66 | 16 | inferred_complete_timeline |
| `Action_None` | 68 | 80 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 11 | 8 | inferred_complete_timeline |
| `Action_None` | 13 | 19 | 7 | inferred_complete_timeline |
| `Action_None` | 25 | 44 | 20 | inferred_complete_timeline |
| `Action_None` | 70 | 132 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_LongSnap` | 4 | 18 | 15 | inferred_complete_timeline |
| `Action_None` | 19 | 82 | 64 | inferred_complete_timeline |
| `Action_None` | 84 | 120 | 37 | inferred_complete_timeline |
| `Action_None` | 125 | 139 | 15 | inferred_complete_timeline |
| `Action_None` | 143 | 150 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 23 | 20 | inferred_complete_timeline |
| `Action_None` | 25 | 31 | 7 | inferred_complete_timeline |
| `Action_None` | 37 | 53 | 17 | inferred_complete_timeline |
| `Action_None` | 58 | 80 | 23 | inferred_complete_timeline |
| `Action_None` | 91 | 150 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 134 | 131 | inferred_complete_timeline |
| `Action_None` | 143 | 146 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 10 | 7 | inferred_complete_timeline |
| `Action_None` | 13 | 15 | 3 | inferred_complete_timeline |
| `Action_None` | 17 | 44 | 28 | inferred_complete_timeline |
| `Action_None` | 48 | 80 | 33 | inferred_complete_timeline |
| `Action_None` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_None` | 88 | 90 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–31
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 18 | 15 | inferred_complete_timeline |
| `Action_None` | 26 | 31 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 141 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 71 | 68 | inferred_complete_timeline |
| `Action_None` | 75 | 85 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–30
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 22 | 19 | inferred_complete_timeline |
| `Action_None` | 27 | 30 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_BlockKick` | 50 | 68 | 19 | inferred_complete_timeline |
| `Action_None` | 69 | 80 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 6 | 3 | inferred_complete_timeline |
| `Action_None` | 10 | 18 | 9 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_None` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_None` | 88 | 94 | 7 | inferred_complete_timeline |
| `Action_None` | 97 | 150 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 103 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 67 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 79 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 116 | 113 | inferred_complete_timeline |
| `Action_None` | 130 | 141 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 5–150 | 134 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 22–32 | 11 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 32–150 | 76 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 57–147 | 67 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 62–150 | 87 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 86–150 | 59 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 89–149 | 52 | 5 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 97–150 | 53 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 98–99 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 99–150 | 49 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 99–134 | 36 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 108–150 | 37 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 108–150 | 43 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 110–150 | 25 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 14: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [4-150] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-116] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-141] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-141] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-103] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-66] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-80] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-67] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-79] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-83] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-71] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-85] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-134] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-22] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-30] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-23] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-31] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-53] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-150] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-11] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-19] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-18] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-6] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-18] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-94] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-10] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-15] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-80] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-106] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-32] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-34] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-89] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-101] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-146] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-67] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-147] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-85] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-125] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-100] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-113] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-129] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-119] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-134] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-131] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-150] for track '31' has 1 frames without a visible bounding box.
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

</details>