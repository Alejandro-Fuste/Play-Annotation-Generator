# Play-Annotation-Generator Annotation Review — PuntBlock_78

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_78`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `10` | `10` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `9` | `Group` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockPunt` | Punter | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `10` | `10` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `10` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `12` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `15` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `16` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `4` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `7` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `8` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `9` | `Group` | 0 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Punter | `7` | `7` | 25 | END | 25 | 25 |
| ✅ EXACT | `Action_PuntBall` | Punter | `7` | `7` | 52 | START | 52 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockPunt` | Punter | `7` | `7` | 67 | START | 67 | 71 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–26
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 22 | 26 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 28 | 59 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_LongSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 180 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_None` | 41 | 58 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 64 | 77 | 14 | inferred_complete_timeline |
| `Action_None` | 85 | 87 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 25 | 1 | inferred_complete_timeline |
| `Action_None` | 26 | 51 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 52 | 60 | 9 | inferred_complete_timeline |
| `Action_BlockPunt` | 67 | 71 | 5 | inferred_complete_timeline |
| `Action_BlockPunt` | 75 | 75 | 1 | inferred_complete_timeline |
| `Action_None` | 76 | 83 | 8 | inferred_complete_timeline |
| `Action_None` | 85 | 87 | 3 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 126 | 180 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–7
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 7 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 93 | 180 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 56 | 59 | 4 | inferred_complete_timeline |
| `Action_None` | 63 | 72 | 10 | inferred_complete_timeline |
| `Action_None` | 74 | 95 | 22 | inferred_complete_timeline |
| `Action_None` | 101 | 105 | 5 | inferred_complete_timeline |
| `Action_None` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_None` | 111 | 119 | 9 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 154 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–28
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 28 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 13 | 21 | 9 | inferred_complete_timeline |
| `Action_None` | 43 | 68 | 26 | inferred_complete_timeline |
| `Action_None` | 72 | 75 | 4 | inferred_complete_timeline |
| `Action_None` | 77 | 180 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 59 | 180 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 52 | 129 | 78 | inferred_complete_timeline |
| `Action_None` | 134 | 136 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 77 | 78 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 58 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–180 | 181 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 33–180 | 138 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 42–180 | 136 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 42–180 | 139 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 43–45 | 3 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 49–180 | 132 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 66–150 | 76 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 72–180 | 109 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 76–141 | 56 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 82–180 | 99 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 82–104 | 23 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 102–180 | 79 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 114–180 | 64 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 124–125 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 137–180 | 39 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 152–180 | 24 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 165–180 | 13 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 170–176 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockPunt` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 158: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [0-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-58] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-53] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-59] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-72] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-95] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-105] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-119] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-180] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-38] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-129] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-75] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [52-60] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [67-71] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-83] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-60] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-77] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-13] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-59] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-28] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-7] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-7] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-21] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-5] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-58] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-34] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-180] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-180] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-45] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-180] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-101] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-141] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-104] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-175] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-144] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-180] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-163] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-172] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-176] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>