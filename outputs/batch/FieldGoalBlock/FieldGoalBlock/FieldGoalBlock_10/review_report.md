# Play-Annotation-Generator Annotation Review — FieldGoalBlock_10

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_10`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Interior_Rusher2 | defense | `2` | `2` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `5` | `5` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `1` | `1` |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | Team_Unknown | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `1` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `11` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `12` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `5` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `7` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `8` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `9` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_LongSnap` | Interior_Rusher2 | `2` | `2` | 13 | START | 13 | 29 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `5` | `5` | 30 | START | 30 | 39 |
| ✅ EXACT | `Action_KickBall` | Kicker | `1` | `1` | 50 | START | 50 | 56 |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | `14` | `14` | 54 | START | 54 | 61 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PlaceBall` | 30 | 39 | 10 | inferred_complete_timeline |
| `Action_None` | 40 | 120 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_KickBall` | 50 | 56 | 7 | inferred_complete_timeline |
| `Action_None` | 57 | 119 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 55 | 43 | inferred_complete_timeline |
| `Action_None` | 58 | 71 | 14 | inferred_complete_timeline |
| `Action_None` | 76 | 93 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 95 | 83 | inferred_complete_timeline |
| `Action_None` | 98 | 114 | 17 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 66 | 54 | inferred_complete_timeline |
| `Action_None` | 70 | 72 | 3 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 97 | 17 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 56 | 44 | inferred_complete_timeline |
| `Action_None` | 59 | 61 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 55 | 43 | inferred_complete_timeline |
| `Action_None` | 59 | 75 | 17 | inferred_complete_timeline |
| `Action_None` | 79 | 90 | 12 | inferred_complete_timeline |
| `Action_None` | 92 | 120 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 112 | 120 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 41 | 29 | inferred_complete_timeline |
| `Action_None` | 52 | 64 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_LongSnap` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_None` | 30 | 52 | 23 | inferred_complete_timeline |
| `Action_None` | 63 | 66 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 43 | 31 | inferred_complete_timeline |
| `Action_None` | 52 | 54 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 49 | 37 | inferred_complete_timeline |
| `Action_None` | 54 | 120 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 26 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 93 | 81 | inferred_complete_timeline |
| `Action_None` | 108 | 120 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 18–69 | 41 | 5 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 19–120 | 52 | 5 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 22–120 | 92 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 24–120 | 74 | 6 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 27–41 | 5 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 30–119 | 87 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 31–119 | 59 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 36–37 | 2 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 51–120 | 63 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 22: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [13-49] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-119] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-52] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-66] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-76] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-41] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-64] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-26] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-55] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-97] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-56] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-71] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-43] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-33] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-44] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [54-61] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-23] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-24] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-111] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-56] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-72] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-84] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-28] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-41] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-79] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-119] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-38] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-72] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-119] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-70] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-81] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-120] for track '22' has 1 frames without a visible bounding box.
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

</details>