# Play-Annotation-Generator Annotation Review — FieldGoalBlock_104

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_104`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 123
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 110
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `0` | `0` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `2` | `2` |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | Team_Unknown | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `0` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `10` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `13` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `14` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `2` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `7` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `9` | `Group` | 0 | START | 0 | 29 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `0` | `0` | 7 | START | 7 | 15 |
| ✅ EXACT | `Action_KickBall` | Kicker | `2` | `2` | 30 | START | 30 | 34 |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | `17` | `17` | 34 | START | 34 | 48 |

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
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PlaceBall` | 7 | 15 | 9 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_KickBall` | 30 | 34 | 5 | inferred_complete_timeline |
| `Action_None` | 35 | 151 | 117 | inferred_complete_timeline |
| `Action_None` | 156 | 269 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 67 | 38 | inferred_complete_timeline |
| `Action_None` | 81 | 84 | 4 | inferred_complete_timeline |
| `Action_None` | 117 | 163 | 47 | inferred_complete_timeline |
| `Action_None` | 166 | 184 | 19 | inferred_complete_timeline |
| `Action_None` | 190 | 269 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 127 | 98 | inferred_complete_timeline |
| `Action_None` | 135 | 269 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 91 | 62 | inferred_complete_timeline |
| `Action_None` | 93 | 269 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 127 | 98 | inferred_complete_timeline |
| `Action_None` | 134 | 269 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 60 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 38 | 9 | inferred_complete_timeline |
| `Action_None` | 46 | 269 | 224 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 64 | 35 | inferred_complete_timeline |
| `Action_None` | 84 | 96 | 13 | inferred_complete_timeline |
| `Action_None` | 102 | 150 | 49 | inferred_complete_timeline |
| `Action_None` | 236 | 269 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 50 | 21 | inferred_complete_timeline |
| `Action_None` | 118 | 148 | 31 | inferred_complete_timeline |
| `Action_None` | 152 | 185 | 34 | inferred_complete_timeline |
| `Action_None` | 199 | 233 | 35 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 242 | 269 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 52 | 23 | inferred_complete_timeline |
| `Action_None` | 55 | 75 | 21 | inferred_complete_timeline |
| `Action_None` | 82 | 122 | 41 | inferred_complete_timeline |
| `Action_None` | 124 | 145 | 22 | inferred_complete_timeline |
| `Action_None` | 147 | 151 | 5 | inferred_complete_timeline |
| `Action_None` | 154 | 191 | 38 | inferred_complete_timeline |
| `Action_None` | 201 | 269 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 29 | 7 | inferred_complete_timeline |
| `Action_None` | 30 | 50 | 21 | inferred_complete_timeline |
| `Action_None` | 60 | 168 | 109 | inferred_complete_timeline |
| `Action_None` | 178 | 234 | 57 | inferred_complete_timeline |
| `Action_None` | 238 | 269 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 129 | 100 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 148 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 114 | 85 | inferred_complete_timeline |
| `Action_None` | 120 | 172 | 53 | inferred_complete_timeline |
| `Action_None` | 176 | 269 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 41 | 12 | inferred_complete_timeline |
| `Action_None` | 43 | 226 | 184 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–43 | 30 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–14 | 14 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 3–246 | 213 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 3–105 | 97 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 31–269 | 186 | 8 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 41–57 | 14 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 53–67 | 15 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 57–269 | 203 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 59–130 | 68 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 80–269 | 186 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 93–269 | 172 | 4 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 103–269 | 155 | 6 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 134–234 | 89 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 151–152 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 153–269 | 87 | 3 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 170–269 | 99 | 2 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 171–269 | 96 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 237–269 | 31 | 2 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 262–269 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 210: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-43] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-151] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-52] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-75] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-145] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-64] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-96] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-114] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-172] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-50] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-148] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-185] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-233] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-127] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-41] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-226] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-91] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-38] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-129] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-148] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-67] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-184] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-168] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-234] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-14] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-242] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-11] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-105] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-37] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-64] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-95] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-67] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-166] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-218] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-252] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-124] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-105] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-164] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-202] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-231] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-115] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-125] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-135] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-148] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-269] for track '26' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-185] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-202] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-234] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-162] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-194] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-218] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-269] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-269] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>