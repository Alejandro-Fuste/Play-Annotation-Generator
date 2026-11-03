# Play-Annotation-Generator Annotation Review — PuntBlock_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_43`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 94
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `10` | `10` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_BlockPunt` | Position_Unknown | Team_Unknown | `20` | `20` |
| ✅ EXACT | `Action_SecureRecovery` | Position_Unknown | Team_Unknown | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `10` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `11` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `12` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `14` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `15` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `16` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `17` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `18` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `19` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `6` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `9` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `14` | `14` | 14 | START | 14 | 66 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `10` | `10` | 40 | END | 40 | 40 |
| ✅ EXACT | `Action_PuntBall` | Punter | `10` | `10` | 67 | START | 67 | 115 |
| ⚠️ START CHANGED | `Action_BlockPunt` | Position_Unknown | `20` | `20` | 77 | START | 78 | 81 |
| ✅ EXACT | `Action_SecureRecovery` | Position_Unknown | `20` | `20` | 183 | START | 183 | 184 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 95 | 82 | inferred_complete_timeline |
| `Action_None` | 104 | 149 | 46 | inferred_complete_timeline |
| `Action_None` | 154 | 210 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 122 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_LongSnap` | 14 | 66 | 53 | inferred_complete_timeline |
| `Action_None` | 67 | 159 | 93 | inferred_complete_timeline |
| `Action_None` | 173 | 176 | 4 | inferred_complete_timeline |
| `Action_None` | 180 | 201 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 95 | 82 | inferred_complete_timeline |
| `Action_None` | 97 | 102 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 62 | 49 | inferred_complete_timeline |
| `Action_None` | 72 | 132 | 61 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 145 | 151 | 7 | inferred_complete_timeline |
| `Action_None` | 156 | 179 | 24 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 202 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 145 | 132 | inferred_complete_timeline |
| `Action_None` | 147 | 151 | 5 | inferred_complete_timeline |
| `Action_None` | 160 | 171 | 12 | inferred_complete_timeline |
| `Action_None` | 175 | 178 | 4 | inferred_complete_timeline |
| `Action_None` | 196 | 201 | 6 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_None` | 41 | 66 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 67 | 115 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 122 | 109 | inferred_complete_timeline |
| `Action_None` | 132 | 135 | 4 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 109 | 96 | inferred_complete_timeline |
| `Action_None` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_None` | 118 | 121 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 156 | 143 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 154 | 141 | inferred_complete_timeline |
| `Action_None` | 160 | 176 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 41 | 28 | inferred_complete_timeline |
| `Action_None` | 51 | 124 | 74 | inferred_complete_timeline |
| `Action_None` | 131 | 134 | 4 | inferred_complete_timeline |
| `Action_None` | 145 | 153 | 9 | inferred_complete_timeline |
| `Action_None` | 155 | 202 | 48 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 147 | 134 | inferred_complete_timeline |
| `Action_None` | 149 | 161 | 13 | inferred_complete_timeline |
| `Action_None` | 167 | 204 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 143 | 130 | inferred_complete_timeline |
| `Action_None` | 145 | 151 | 7 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 164 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 129 | 116 | inferred_complete_timeline |
| `Action_None` | 131 | 135 | 5 | inferred_complete_timeline |
| `Action_None` | 138 | 147 | 10 | inferred_complete_timeline |
| `Action_None` | 155 | 171 | 17 | inferred_complete_timeline |
| `Action_None` | 174 | 178 | 5 | inferred_complete_timeline |
| `Action_None` | 183 | 186 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 117 | 104 | inferred_complete_timeline |
| `Action_None` | 123 | 167 | 45 | inferred_complete_timeline |
| `Action_None` | 171 | 210 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 130 | 117 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 208 | 195 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 37–184 | 121 | 9 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 133–210 | 23 | 4 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 141–146 | 6 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 147–210 | 64 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 157–160 | 4 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 165–166 | 2 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 173–210 | 38 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 175–209 | 34 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 178–187 | 8 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 187–210 | 24 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 193–210 | 14 | 3 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 198–210 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BlockPunt` for actor_track_id `20` (Position_Unknown): Annotated start 77 != Inferred start 78

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Guard` position mapped to `offense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 86 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [14-130] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-147] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-161] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-154] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-143] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-151] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-208] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-109] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-41] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-124] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-202] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [67-115] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-156] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-145] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-171] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-147] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-171] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-201] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-95] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-95] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-62] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-132] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-179] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-122] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-76] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-97] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-124] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-147] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-178] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [183-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-209] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '31' has 3 frames without a visible bounding box.
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

</details>