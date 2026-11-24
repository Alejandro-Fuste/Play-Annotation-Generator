# Play-Annotation-Generator Annotation Review — FieldGoalBlock_106

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_106`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 67
- **Validation Warnings:** 62
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `6` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `0` | `0` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Position_Unknown | Team_Unknown | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `0` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `1` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `10` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `13` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `14` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `15` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `19` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `2` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `6` | `Group` | 0 | START | 0 | 73 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `0` | `0` | 55 | START | 55 | 69 |
| ✅ EXACT | `Action_KickBall` | Kicker | `1` | `1` | 74 | START | 74 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Position_Unknown | `18` | `18` | 78 | START | 84 | 86 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PlaceBall` | 55 | 69 | 15 | inferred_complete_timeline |
| `Action_None` | 70 | 120 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_KickBall` | 74 | 78 | 5 | inferred_complete_timeline |
| `Action_None` | 79 | 120 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 120 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 77 | 4 | inferred_complete_timeline |
| `Action_None` | 95 | 100 | 6 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 73 | 11 | inferred_complete_timeline |
| `Action_None` | 74 | 77 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 120 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 73 | 34 | inferred_complete_timeline |
| `Action_None` | 74 | 113 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 80 | 7 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 120 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 120 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 120 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_None` | 74 | 120 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 78 | 5 | inferred_complete_timeline |
| `Action_None` | 84 | 120 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 57 | 8 | inferred_complete_timeline |
| `Action_None` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_None` | 97 | 120 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 61 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 73 | 11 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_None` | 82 | 120 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 75 | 81 | 7 | inferred_complete_timeline |
| `Action_None` | 88 | 120 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 120 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 120 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 120 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–120 | 121 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–120 | 94 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 66–79 | 9 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 91–105 | 13 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 98–120 | 23 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockKick` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 213: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ Row 214: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [70-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-120] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-120] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-120] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-81] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-120] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-78] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-120] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-120] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-61] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-120] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-57] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [84-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-120] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-113] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-101] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-120] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Metadata: no Dataset Summary row found for output_file 'FieldGoalBlock_106'; source metadata written as null.

</details>