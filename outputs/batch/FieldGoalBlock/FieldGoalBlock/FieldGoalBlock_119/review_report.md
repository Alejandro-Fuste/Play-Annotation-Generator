# Play-Annotation-Generator Annotation Review — FieldGoalBlock_119

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_119`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 111
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
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `7` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `10` | `10` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `6` | `6` |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher7 | defense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `10` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `12` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `18` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `3` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `4` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `5` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `6` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `7` | `Group` | 0 | START | 0 | 44 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `10` | `10` | 29 | START | 29 | 45 |
| ✅ EXACT | `Action_KickBall` | Kicker | `6` | `6` | 50 | START | 50 | 55 |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher7 | `17` | `17` | 55 | START | 55 | 64 |

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
- **Visible Frames:** 0–150
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PlaceBall` | 29 | 45 | 17 | inferred_complete_timeline |
| `Action_None` | 46 | 49 | 4 | inferred_complete_timeline |
| `Action_None` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_None` | 58 | 150 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_KickBall` | 50 | 55 | 6 | inferred_complete_timeline |
| `Action_None` | 56 | 131 | 76 | inferred_complete_timeline |
| `Action_None` | 141 | 150 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 150 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 49 | 6 | inferred_complete_timeline |
| `Action_None` | 50 | 55 | 6 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 66 | 77 | 12 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 150 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 57 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 49 | 4 | inferred_complete_timeline |
| `Action_None` | 50 | 63 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 35 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 49 | 10 | inferred_complete_timeline |
| `Action_None` | 50 | 81 | 32 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 113 | 28 | inferred_complete_timeline |
| `Action_None` | 115 | 117 | 3 | inferred_complete_timeline |
| `Action_None` | 122 | 128 | 7 | inferred_complete_timeline |
| `Action_None` | 130 | 136 | 7 | inferred_complete_timeline |
| `Action_None` | 143 | 150 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 57 | 8 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 66 | 75 | 10 | inferred_complete_timeline |
| `Action_None` | 81 | 117 | 37 | inferred_complete_timeline |
| `Action_None` | 132 | 150 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 150 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 149 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 150 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 90 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 49 | 17 | inferred_complete_timeline |
| `Action_None` | 50 | 58 | 9 | inferred_complete_timeline |
| `Action_None` | 64 | 150 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 50 | 1 | inferred_complete_timeline |
| `Action_None` | 53 | 56 | 4 | inferred_complete_timeline |
| `Action_None` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 47 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–20
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 20 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_BlockKick` | 55 | 64 | 10 | inferred_complete_timeline |
| `Action_None` | 65 | 73 | 9 | inferred_complete_timeline |
| `Action_None` | 75 | 98 | 24 | inferred_complete_timeline |
| `Action_None` | 100 | 149 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 64 | 15 | inferred_complete_timeline |
| `Action_None` | 67 | 140 | 74 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 130 | 81 | inferred_complete_timeline |
| `Action_None` | 132 | 138 | 7 | inferred_complete_timeline |
| `Action_None` | 147 | 149 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 26–144 | 90 | 8 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 66–69 | 4 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 68–84 | 17 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 87–106 | 20 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 91–150 | 60 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 93–150 | 39 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 98–105 | 8 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 106–150 | 36 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 112–117 | 6 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 123–150 | 28 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 132–137 | 5 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 143–150 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 240: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [50-64] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-140] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-149] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-138] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-63] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-90] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-49] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 50, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [50-50] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-57] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-35] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-81] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-136] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-47] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [55-64] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 65, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [65-73] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-57] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-20] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-79] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-111] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-84] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-106] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-105] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-105] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-116] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-117] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '31' has 1 frames without a visible bounding box.
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