# Play-Annotation-Generator Annotation Review — PuntBlock_36

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_36`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 1
- **Action Segments:** 79
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `7` | `7` |
| ⚠️ START CHANGED | `Action_BlockPunt` | Position_Unknown | Team_Unknown | `24` | `21` |
| ✅ EXACT | `Action_SecureRecovery` | Interior_Rusher1 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `11` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector | `12` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `13` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `3` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `5` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `6` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `7` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `8` | `Group` | 0 | START | 0 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `13` | `13` | 20 | START | 20 | 52 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `7` | `7` | 46 | END | 46 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `7` | `7` | 75 | START | 75 | 168 |
| ⚠️ START CHANGED | `Action_BlockPunt` | Position_Unknown | `24` | `21` | 89 | START | 100 | 105 |
| ✅ EXACT | `Action_SecureRecovery` | Interior_Rusher1 | `2` | `2` | 170 | START | 170 | 174 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 44 | 25 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_None` | 56 | 174 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 174 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 269 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_LongSnap` | 20 | 52 | 33 | inferred_complete_timeline |
| `Action_LongSnap` | 72 | 74 | 3 | inferred_complete_timeline |
| `Action_None` | 75 | 89 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 46 | 27 | inferred_complete_timeline |
| `Action_None` | 48 | 61 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 46 | 1 | inferred_complete_timeline |
| `Action_None` | 47 | 74 | 28 | inferred_complete_timeline |
| `Action_PuntBall` | 75 | 168 | 94 | inferred_complete_timeline |
| `Action_PuntBall` | 170 | 178 | 9 | inferred_complete_timeline |
| `Action_PuntBall` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_PuntBall` | 195 | 218 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 221 | 224 | 4 | inferred_complete_timeline |
| `Action_PuntBall` | 236 | 243 | 8 | inferred_complete_timeline |
| `Action_PuntBall` | 245 | 269 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 170 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 167 | 148 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_SecureRecovery` | 170 | 174 | 5 | inferred_complete_timeline |
| `Action_None` | 175 | 188 | 14 | inferred_complete_timeline |
| `Action_None` | 212 | 269 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 182 | 163 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_None` | 187 | 202 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 269 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 269 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 92 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 90 | 71 | inferred_complete_timeline |
| `Action_None` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 116 | 97 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 160 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 9–21 | 13 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 35–253 | 151 | 7 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 37–166 | 129 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 80–146 | 66 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 89–269 | 181 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 92–160 | 69 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 100–236 | 98 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 102–160 | 59 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 114–269 | 155 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 188–269 | 77 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 230–231 | 2 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 259–269 | 11 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 265–269 | 5 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 265–269 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `24` | `29` | 153 | 155 | 3 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PuntBall` and target `7` (7 segments found)
- ⚠️ `Action_BlockPunt` for actor_track_id `24` (Position_Unknown): Annotated start 89 != Inferred start 100

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 73: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [20-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-160] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-169] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-167] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-269] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-170] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-174] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [75-168] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [170-178] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [183-184] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [195-218] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [221-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [236-243] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-44] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-90] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-92] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-46] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-61] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [20-52] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-89] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-202] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-64] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-189] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-83] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-146] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-195] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-160] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-261] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-269] for track '27' has 1 frames without a visible bounding box.
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

</details>