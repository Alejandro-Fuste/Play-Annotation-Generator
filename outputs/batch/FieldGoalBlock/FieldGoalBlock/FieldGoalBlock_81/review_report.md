# Play-Annotation-Generator Annotation Review — FieldGoalBlock_81

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_81`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 133
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 107
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `7` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `7` | `7` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `0` | `0` |
| ✅ EXACT | `Action_BlockKick` | FG_Block_Support1 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `0` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `11` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `12` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `13` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `14` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `19` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `20` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `3` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `4` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `7` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `7` | `7` | 18 | START | 18 | 23 |
| ✅ EXACT | `Action_KickBall` | Kicker | `0` | `0` | 36 | START | 36 | 41 |
| ✅ EXACT | `Action_BlockKick` | FG_Block_Support1 | `2` | `2` | 41 | START | 41 | 56 |

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
- **Visible Frames:** 0–109
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PlaceBall` | 18 | 23 | 6 | inferred_complete_timeline |
| `Action_None` | 24 | 42 | 19 | inferred_complete_timeline |
| `Action_None` | 49 | 90 | 42 | inferred_complete_timeline |
| `Action_None` | 100 | 109 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_KickBall` | 36 | 41 | 6 | inferred_complete_timeline |
| `Action_None` | 42 | 74 | 33 | inferred_complete_timeline |
| `Action_None` | 77 | 127 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 70 | 114 | 45 | inferred_complete_timeline |
| `Action_None` | 120 | 125 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 36 | 1 | inferred_complete_timeline |
| `Action_None` | 45 | 52 | 8 | inferred_complete_timeline |
| `Action_None` | 56 | 107 | 52 | inferred_complete_timeline |
| `Action_None` | 110 | 138 | 29 | inferred_complete_timeline |
| `Action_None` | 140 | 142 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 43 | 8 | inferred_complete_timeline |
| `Action_None` | 45 | 52 | 8 | inferred_complete_timeline |
| `Action_None` | 59 | 135 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 26 | 19 | inferred_complete_timeline |
| `Action_None` | 41 | 42 | 2 | inferred_complete_timeline |
| `Action_None` | 47 | 52 | 6 | inferred_complete_timeline |
| `Action_None` | 70 | 74 | 5 | inferred_complete_timeline |
| `Action_None` | 79 | 103 | 25 | inferred_complete_timeline |
| `Action_None` | 107 | 150 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 38 | 42 | 5 | inferred_complete_timeline |
| `Action_None` | 45 | 150 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 45 | 52 | 8 | inferred_complete_timeline |
| `Action_None` | 56 | 103 | 48 | inferred_complete_timeline |
| `Action_None` | 109 | 114 | 6 | inferred_complete_timeline |
| `Action_None` | 117 | 142 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 39 | 4 | inferred_complete_timeline |
| `Action_None` | 41 | 42 | 2 | inferred_complete_timeline |
| `Action_None` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_None` | 50 | 52 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 39 | 4 | inferred_complete_timeline |
| `Action_None` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_None` | 56 | 149 | 94 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_BlockKick` | 41 | 56 | 16 | inferred_complete_timeline |
| `Action_None` | 57 | 133 | 77 | inferred_complete_timeline |
| `Action_None` | 135 | 140 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 126 | 91 | inferred_complete_timeline |
| `Action_None` | 132 | 137 | 6 | inferred_complete_timeline |
| `Action_None` | 141 | 144 | 4 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 150 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 36 | 1 | inferred_complete_timeline |
| `Action_None` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_None` | 56 | 93 | 38 | inferred_complete_timeline |
| `Action_None` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_None` | 109 | 137 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 29 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 34 | 4 | inferred_complete_timeline |
| `Action_None` | 57 | 58 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–10
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 36 | 1 | inferred_complete_timeline |
| `Action_None` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 74 | 113 | 40 | inferred_complete_timeline |
| `Action_None` | 118 | 150 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_None` | 39 | 41 | 3 | inferred_complete_timeline |
| `Action_None` | 43 | 55 | 13 | inferred_complete_timeline |
| `Action_None` | 57 | 150 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 113 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–150 | 74 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 14–135 | 120 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 32–150 | 105 | 7 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 51–54 | 4 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 67–150 | 74 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 68–150 | 79 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 71–142 | 36 | 6 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 75–142 | 63 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 86–149 | 58 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 90–95 | 6 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 106–147 | 25 | 6 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 119–140 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 107 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 164: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [42-74] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-127] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-113] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-133] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-114] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-43] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-52] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-135] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '6' starts at frame 36, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [36-36] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-52] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-137] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-42] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-126] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-137] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-41] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-150] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 36, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [36-36] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-52] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-39] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-52] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-149] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-42] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-52] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-114] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 36, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [36-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-52] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-34] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-52] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-26] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-52] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-74] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-150] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-35] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-107] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-135] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-65] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-54] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-77] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-102] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-126] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-82] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-102] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-137] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-137] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-115] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-142] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-95] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-111] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-140] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-140] for track '31' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.

</details>