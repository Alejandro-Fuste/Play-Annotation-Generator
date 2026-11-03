# Play-Annotation-Generator Annotation Review — PuntBlock_23

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_23`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 269
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | offense | `19` | `19` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `9` | `Group` |
| ✅ EXACT | `Action_SnapReceive` | Left_Gunner | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Left_Gunner | offense | `10` | `10` |
| ✅ EXACT | `Action_BlockPunt` | Position_Unknown | Team_Unknown | `23` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Right_Guard | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | `19` | `19` | 21 | START | 21 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `10` | `Group` | 21 | START | 21 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `11` | `Group` | 21 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `12` | `Group` | 21 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `15` | `Group` | 21 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 21 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `4` | `Group` | 21 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `5` | `Group` | 21 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `6` | `Group` | 21 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `7` | `Group` | 21 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `8` | `Group` | 21 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `9` | `Group` | 21 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Left_Gunner | `10` | `10` | 47 | END | 47 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Left_Gunner | `10` | `10` | 70 | START | 70 | 189 |
| ✅ EXACT | `Action_BlockPunt` | Position_Unknown | `23` | `21` | 83 | START | 83 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Right_Guard | `19` | `19` | 166 | START | 166 | 182 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>? — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 21–112
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 112 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 21–141
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 141 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 21–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 46 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 47 | 1 | inferred_complete_timeline |
| `Action_None` | 48 | 69 | 22 | inferred_complete_timeline |
| `Action_PuntBall` | 70 | 189 | 120 | inferred_complete_timeline |
| `Action_PuntBall` | 193 | 269 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 21–137
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 137 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 21–105
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 105 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 21–269
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 50 | 30 | inferred_complete_timeline |
| `Action_None` | 55 | 58 | 4 | inferred_complete_timeline |
| `Action_None` | 60 | 103 | 44 | inferred_complete_timeline |
| `Action_None` | 107 | 269 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 21–220
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 69 | 49 | inferred_complete_timeline |
| `Action_None` | 73 | 204 | 132 | inferred_complete_timeline |
| `Action_None` | 210 | 220 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 21–83
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 77 | 57 | inferred_complete_timeline |
| `Action_None` | 81 | 83 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 21–194
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_LongSnap` | 21 | 164 | 144 | inferred_complete_timeline |
| `Action_SecureRecovery` | 166 | 182 | 17 | inferred_complete_timeline |
| `Action_SecureRecovery` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_None` | 189 | 194 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 21–210
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 108 | 88 | inferred_complete_timeline |
| `Action_None` | 116 | 175 | 60 | inferred_complete_timeline |
| `Action_None` | 178 | 210 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 21–101
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 101 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 21–139
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 39 | 19 | inferred_complete_timeline |
| `Action_None` | 47 | 139 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 21–143
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 27 | 7 | inferred_complete_timeline |
| `Action_None` | 31 | 50 | 20 | inferred_complete_timeline |
| `Action_None` | 52 | 143 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 21–52
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 52 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 21–45
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 45 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 21–165
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 108 | 88 | inferred_complete_timeline |
| `Action_None` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_None` | 115 | 162 | 48 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 21–135
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 135 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 21–114
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 109 | 89 | inferred_complete_timeline |
| `Action_None` | 111 | 114 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 21–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 269 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 21–108
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 21 | 93 | 73 | inferred_complete_timeline |
| `Action_None` | 95 | 108 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 21–114 | 89 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 50–202 | 146 | 4 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 56–269 | 214 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 81–269 | 186 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 112–124 | 13 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 127–232 | 106 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 170–221 | 37 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 223–269 | 44 | 4 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 227–269 | 43 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 229–239 | 9 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 235–269 | 35 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 259–269 | 4 | 2 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SecureRecovery` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `?` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 58 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [21-52] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-32] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-114] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-135] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-45] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-108] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-141] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-137] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-105] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-101] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-204] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-220] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [70-189] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-50] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-58] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-39] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-139] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-162] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-112] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [21-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [166-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [184-186] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-194] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-50] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-143] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-116] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-202] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-114] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-124] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-232] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-208] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-250] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-258] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-269] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-235] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>