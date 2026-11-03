# Play-Annotation-Generator Annotation Review — PuntBlock_32

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_32`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 2
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `13` | `13` |
| ✅ EXACT | `Action_PuntBall` | Position_Unknown | Team_Unknown | `13` | `13` |
| ⚠️ START CHANGED | `Action_BlockPunt` | Interior_Rusher1 | defense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `10` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `11` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `12` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `4` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `9` | `Group` | 0 | START | 0 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `9` | `9` | 19 | START | 19 | 25 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `13` | `13` | 47 | END | 47 | 47 |
| ✅ EXACT | `Action_PuntBall` | Position_Unknown | `13` | `13` | 72 | START | 72 | 109 |
| ⚠️ START CHANGED | `Action_BlockPunt` | Interior_Rusher1 | `7` | `7` | 85 | START | 88 | 88 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 81 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 80 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_LongSnap` | 19 | 25 | 7 | inferred_complete_timeline |
| `Action_LongSnap` | 28 | 71 | 44 | inferred_complete_timeline |
| `Action_None` | 72 | 210 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 91 | 73 | inferred_complete_timeline |
| `Action_None` | 98 | 203 | 106 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 25 | 7 | inferred_complete_timeline |
| `Action_None` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 84 | 5 | inferred_complete_timeline |
| `Action_BlockPunt` | 88 | 88 | 1 | inferred_complete_timeline |
| `Action_None` | 89 | 124 | 36 | inferred_complete_timeline |
| `Action_None` | 128 | 210 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 61 | 43 | inferred_complete_timeline |
| `Action_None` | 65 | 69 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 71 | 53 | inferred_complete_timeline |
| `Action_None` | 77 | 210 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 147 | 129 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 2–109 | 103 | 5 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 6–210 | 198 | 4 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 16–73 | 48 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 46–117 | 41 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 67–210 | 144 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 74–210 | 137 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 86–88 | 3 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 92–210 | 116 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 93–210 | 117 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 101–210 | 110 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 116–210 | 93 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 124–210 | 87 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 131–210 | 80 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 132–210 | 79 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 133–210 | 78 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 152–210 | 59 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 156–208 | 53 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `9` (2 segments found)
- ⚠️ `Action_BlockPunt` for actor_track_id `7` (Interior_Rusher1): Annotated start 85 != Inferred start 88

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Guard` position mapped to `offense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 51 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [19-61] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-69] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-71] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-80] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-147] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [19-25] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [28-71] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-91] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-25] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-33] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-29] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [72-109] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-8] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-22] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-33] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-73] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-48] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-117] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-184] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-208] for track '29' has 1 frames without a visible bounding box.
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