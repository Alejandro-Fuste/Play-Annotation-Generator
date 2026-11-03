# Play-Annotation-Generator Annotation Review — PuntBlock_4

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_4`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `2` | `2` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `9` | `Group` |
| ✅ EXACT | `Action_SnapReceive` | Interior_Rusher5 | defense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Interior_Rusher5 | defense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockPunt` | Right_Edge_Rusher1 | defense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Interior_Rusher4 | defense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `2` | `2` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `0` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `1` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `13` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `2` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `3` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `4` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `6` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `7` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `9` | `Group` | 0 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Interior_Rusher5 | `11` | `11` | 25 | END | 25 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Interior_Rusher5 | `11` | `11` | 50 | START | 50 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockPunt` | Right_Edge_Rusher1 | `5` | `5` | 58 | START | 58 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Interior_Rusher4 | `15` | `15` | 180 | START | 180 | 185 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 130 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 62 | 125 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_LongSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 124 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 75 | 139 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 66 | 132 | 67 | inferred_complete_timeline |
| `Action_None` | 134 | 137 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 153 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 138 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 133 | 134 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 14 | 16 | 3 | inferred_complete_timeline |
| `Action_None` | 21 | 55 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 58 | 133 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 56 | 66 | 11 | inferred_complete_timeline |
| `Action_None` | 71 | 269 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 26 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 179 | 101 | inferred_complete_timeline |
| `Action_SecureRecovery` | 180 | 185 | 6 | inferred_complete_timeline |
| `Action_SecureRecovery` | 187 | 196 | 10 | inferred_complete_timeline |
| `Action_SecureRecovery` | 200 | 269 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 24 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 25 | 1 | inferred_complete_timeline |
| `Action_None` | 26 | 49 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 50 | 178 | 129 | inferred_complete_timeline |
| `Action_PuntBall` | 184 | 269 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 25 | 231 | 207 | inferred_complete_timeline |
| `Action_None` | 236 | 241 | 6 | inferred_complete_timeline |
| `Action_None` | 256 | 269 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 128 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_BlockPunt` | 58 | 62 | 5 | inferred_complete_timeline |
| `Action_BlockPunt` | 64 | 64 | 1 | inferred_complete_timeline |
| `Action_None` | 65 | 98 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 4–109 | 62 | 8 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 40–108 | 22 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 71–104 | 34 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 94–127 | 34 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 96–109 | 14 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 97–114 | 18 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 106–110 | 5 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 112–269 | 155 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 121–161 | 41 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 179–263 | 85 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 184–269 | 85 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 189–269 | 81 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 209–269 | 61 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockPunt` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SecureRecovery` and target `15` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 57 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [0-61] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-132] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-124] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-71] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-139] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [58-62] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-138] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-133] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-49] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-133] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-60] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-54] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-66] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [50-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-15] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-231] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-241] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-130] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-179] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [180-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [187-196] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-11] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-16] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-55] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-30] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-36] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-69] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-46] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-56] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-64] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-104] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-127] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-114] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-161] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-248] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '30' has 1 frames without a visible bounding box.
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

</details>