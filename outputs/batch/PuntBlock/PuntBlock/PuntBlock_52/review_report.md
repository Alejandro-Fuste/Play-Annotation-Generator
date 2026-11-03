# Play-Annotation-Generator Annotation Review — PuntBlock_52

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_52`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockPunt` | Left_Edge_Rusher1 | defense | `9` | `9` |
| ✅ EXACT | `Action_SecureRecovery` | Interior_Rusher1 | defense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `0` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `2` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `4` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `5` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `6` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `7` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `8` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `3` | `3` | 8 | START | 8 | 69 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `2` | `2` | 41 | END | 41 | 41 |
| ✅ EXACT | `Action_PuntBall` | Punter | `2` | `2` | 70 | START | 70 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockPunt` | Left_Edge_Rusher1 | `9` | `9` | 80 | START | 80 | 81 |
| ✅ EXACT | `Action_SecureRecovery` | Interior_Rusher1 | `10` | `10` | 173 | START | 173 | 175 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 139 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 69 | 62 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 90 | 10 | inferred_complete_timeline |
| `Action_None` | 92 | 107 | 16 | inferred_complete_timeline |
| `Action_None` | 110 | 174 | 65 | inferred_complete_timeline |
| `Action_None` | 176 | 210 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_LongSnap` | 8 | 69 | 62 | inferred_complete_timeline |
| `Action_None` | 70 | 148 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 209 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 110 | 103 | inferred_complete_timeline |
| `Action_None` | 112 | 114 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_None` | 42 | 69 | 28 | inferred_complete_timeline |
| `Action_PuntBall` | 70 | 210 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 45 | 38 | inferred_complete_timeline |
| `Action_None` | 49 | 54 | 6 | inferred_complete_timeline |
| `Action_None` | 77 | 79 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 171 | 164 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 112 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 146 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 172 | 15 | inferred_complete_timeline |
| `Action_SecureRecovery` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 38 | 31 | inferred_complete_timeline |
| `Action_None` | 69 | 75 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 119 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 57 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 34 | 27 | inferred_complete_timeline |
| `Action_None` | 68 | 71 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 38 | 31 | inferred_complete_timeline |
| `Action_None` | 45 | 168 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_BlockPunt` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_BlockPunt` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_None` | 87 | 210 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 196 | 189 | inferred_complete_timeline |
| `Action_None` | 198 | 203 | 6 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 33 | 26 | inferred_complete_timeline |
| `Action_None` | 39 | 139 | 101 | inferred_complete_timeline |
| `Action_None` | 146 | 210 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–77 | 78 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–210 | 193 | 5 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 42–202 | 148 | 6 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 45–66 | 22 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 60–207 | 146 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 74–130 | 57 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 80–182 | 103 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 84–116 | 31 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 95–208 | 110 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 95–96 | 2 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 98–210 | 113 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 132–210 | 79 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 157–210 | 54 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 163–165 | 3 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 198–210 | 13 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 206–210 | 5 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockPunt` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 69 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [8-209] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-77] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [70-210] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-148] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-139] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-171] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-69] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-107] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [80-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [84-85] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-112] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-146] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [173-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-119] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-38] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-33] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-139] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-168] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-196] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-57] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-45] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-54] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-47] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-87] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-126] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-90] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-176] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-130] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-182] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-92] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-116] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-108] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-208] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>