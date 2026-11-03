# Play-Annotation-Generator Annotation Review — PuntBlock_44

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_44`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 124
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | Left_Edge_Rusher1 | defense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Left_Edge_Rusher1 | defense | `4` | `4` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher3 | defense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `10` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `11` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `5` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `7` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `8` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `9` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `5` | `5` | 5 | START | 5 | 56 |
| ✅ EXACT | `Action_SnapReceive` | Left_Edge_Rusher1 | `4` | `4` | 33 | END | 33 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Left_Edge_Rusher1 | `4` | `4` | 57 | START | 57 | 62 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher3 | `6` | `6` | 70 | START | 70 | 75 |

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
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 10 | 6 | inferred_complete_timeline |
| `Action_None` | 13 | 95 | 83 | inferred_complete_timeline |
| `Action_None` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_None` | 104 | 137 | 34 | inferred_complete_timeline |
| `Action_None` | 142 | 146 | 5 | inferred_complete_timeline |
| `Action_None` | 151 | 210 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_LongSnap` | 5 | 56 | 52 | inferred_complete_timeline |
| `Action_None` | 57 | 92 | 36 | inferred_complete_timeline |
| `Action_None` | 95 | 104 | 10 | inferred_complete_timeline |
| `Action_None` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_None` | 112 | 210 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 210 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 83 | 79 | inferred_complete_timeline |
| `Action_None` | 95 | 99 | 5 | inferred_complete_timeline |
| `Action_None` | 101 | 120 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 46 | 42 | inferred_complete_timeline |
| `Action_None` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 105 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 62 | 58 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 69 | 73 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 47 | 43 | inferred_complete_timeline |
| `Action_None` | 50 | 163 | 114 | inferred_complete_timeline |
| `Action_None` | 175 | 210 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_BlockPunt` | 70 | 75 | 6 | inferred_complete_timeline |
| `Action_None` | 76 | 126 | 51 | inferred_complete_timeline |
| `Action_None` | 129 | 135 | 7 | inferred_complete_timeline |
| `Action_None` | 137 | 142 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 13 | 9 | inferred_complete_timeline |
| `Action_None` | 15 | 23 | 9 | inferred_complete_timeline |
| `Action_None` | 25 | 95 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 110 | 106 | inferred_complete_timeline |
| `Action_None` | 113 | 161 | 49 | inferred_complete_timeline |
| `Action_None` | 170 | 210 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_None` | 34 | 56 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 57 | 62 | 6 | inferred_complete_timeline |
| `Action_PuntBall` | 67 | 108 | 42 | inferred_complete_timeline |
| `Action_PuntBall` | 110 | 141 | 32 | inferred_complete_timeline |
| `Action_PuntBall` | 156 | 167 | 12 | inferred_complete_timeline |
| `Action_PuntBall` | 170 | 210 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 119 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 151 | 147 | inferred_complete_timeline |
| `Action_None` | 154 | 160 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–210 | 198 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 32–60 | 20 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 45–210 | 166 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 50–153 | 104 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 54–162 | 105 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 68–189 | 117 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 68–210 | 142 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 89–90 | 2 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 93–94 | 2 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 96–210 | 100 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 104–106 | 3 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 114–119 | 6 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 115–210 | 96 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 121–206 | 86 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 121–133 | 11 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 125–153 | 29 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 125–210 | 85 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 132–210 | 79 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 159–210 | 52 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 165–210 | 46 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 171–210 | 38 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 174–199 | 20 | 3 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 202–206 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `4` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 90: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [5-151] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-119] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-110] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-161] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [57-62] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [67-108] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [110-141] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [156-167] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [170-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-104] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-62] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-73] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-105] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-46] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-52] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-163] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-10] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-137] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-13] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-23] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-95] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-46] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-162] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-79] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-210] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-119] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-206] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-126] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-153] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-184] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-189] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>