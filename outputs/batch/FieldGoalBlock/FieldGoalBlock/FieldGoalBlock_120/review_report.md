# Play-Annotation-Generator Annotation Review — FieldGoalBlock_120

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_120`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `8` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `7` | `7` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `1` | `1` |
| ⚠️ START CHANGED | `Action_BlockKick` | Position_Unknown | Team_Unknown | `22` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `1` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `10` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `11` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `2` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `4` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `6` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `7` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `8` | `Group` | 0 | START | 0 | 51 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `7` | `7` | 35 | START | 35 | 48 |
| ✅ EXACT | `Action_KickBall` | Kicker | `1` | `1` | 57 | START | 57 | 61 |
| ⚠️ START CHANGED | `Action_BlockKick` | Position_Unknown | `22` | `18` | 61 | START | 63 | 64 |

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
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PlaceBall` | 35 | 48 | 14 | inferred_complete_timeline |
| `Action_None` | 49 | 150 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_KickBall` | 57 | 61 | 5 | inferred_complete_timeline |
| `Action_None` | 62 | 144 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 120 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 56 | 3 | inferred_complete_timeline |
| `Action_None` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_None` | 66 | 74 | 9 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_None` | 125 | 150 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 62 | 6 | inferred_complete_timeline |
| `Action_None` | 73 | 84 | 12 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_None` | 114 | 117 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 56 | 33 | inferred_complete_timeline |
| `Action_None` | 57 | 101 | 45 | inferred_complete_timeline |
| `Action_None` | 103 | 140 | 38 | inferred_complete_timeline |
| `Action_None` | 143 | 150 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_None` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_None` | 78 | 81 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 70 | 14 | inferred_complete_timeline |
| `Action_None` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_None` | 82 | 101 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 150 | 94 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 54 | 15 | inferred_complete_timeline |
| `Action_None` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_None` | 62 | 83 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 53 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 150 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 68 | 12 | inferred_complete_timeline |
| `Action_None` | 78 | 80 | 3 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 150 | 94 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 14–150 | 90 | 4 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 23–26 | 4 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 32–96 | 63 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 34–150 | 117 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 57–59 | 3 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 63–150 | 6 | 2 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 105–146 | 18 | 4 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 116–150 | 26 | 3 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 119–145 | 27 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 130–150 | 21 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 143–150 | 8 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 146–150 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BlockKick` for actor_track_id `22` (Position_Unknown): Annotated start 61 != Inferred start 63

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 242: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [57-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-144] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-68] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-120] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-53] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-70] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-101] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-74] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-54] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-83] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-62] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-84] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-101] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-76] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-26] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-36] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-93] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [63-64] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-126] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-138] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-145] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'FieldGoalBlock_120'; source metadata written as null.

</details>