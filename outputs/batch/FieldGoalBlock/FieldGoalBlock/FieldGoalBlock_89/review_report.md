# Play-Annotation-Generator Annotation Review — FieldGoalBlock_89

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_89`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 139
- **Validation Warnings:** 159
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 121
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `8` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `7` | `7` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `8` | `8` |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | Team_Unknown | `28` | `26` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `0` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `1` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `11` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `13` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `15` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `17` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `2` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `6` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `7` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `8` | `Group` | 0 | START | 0 | 115 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `7` | `7` | 88 | START | 88 | 101 |
| ✅ EXACT | `Action_KickBall` | Kicker | `8` | `8` | 116 | START | 116 | 120 |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | `28` | `26` | 120 | START | 120 | 142 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–311
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PlaceBall` | 88 | 101 | 14 | inferred_complete_timeline |
| `Action_None` | 102 | 293 | 192 | inferred_complete_timeline |
| `Action_None` | 297 | 311 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_KickBall` | 116 | 120 | 5 | inferred_complete_timeline |
| `Action_None` | 121 | 234 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 123 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 115 | 11 | inferred_complete_timeline |
| `Action_None` | 116 | 138 | 23 | inferred_complete_timeline |
| `Action_None` | 140 | 149 | 10 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 159 | 167 | 9 | inferred_complete_timeline |
| `Action_None` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 238 | 67 | inferred_complete_timeline |
| `Action_None` | 241 | 266 | 26 | inferred_complete_timeline |
| `Action_None` | 269 | 313 | 45 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 94 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 329 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 108 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 114 | 4 | inferred_complete_timeline |
| `Action_None` | 169 | 174 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 115 | 8 | inferred_complete_timeline |
| `Action_None` | 116 | 329 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 135 | 20 | inferred_complete_timeline |
| `Action_None` | 148 | 159 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 152 | 37 | inferred_complete_timeline |
| `Action_None` | 154 | 162 | 9 | inferred_complete_timeline |
| `Action_None` | 193 | 238 | 46 | inferred_complete_timeline |
| `Action_None` | 243 | 329 | 87 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 180 | 65 | inferred_complete_timeline |
| `Action_None` | 194 | 261 | 68 | inferred_complete_timeline |
| `Action_None` | 263 | 329 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 329 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 50 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 82 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 94 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 114 | 13 | inferred_complete_timeline |
| `Action_None` | 119 | 154 | 36 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 168 | 4 | inferred_complete_timeline |
| `Action_None` | 170 | 172 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 115 | 6 | inferred_complete_timeline |
| `Action_None` | 116 | 156 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 155 | 40 | inferred_complete_timeline |
| `Action_None` | 163 | 329 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 104 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 115 | 7 | inferred_complete_timeline |
| `Action_None` | 116 | 119 | 4 | inferred_complete_timeline |
| `Action_None` | 125 | 268 | 144 | inferred_complete_timeline |
| `Action_None` | 286 | 298 | 13 | inferred_complete_timeline |
| `Action_None` | 300 | 301 | 2 | inferred_complete_timeline |
| `Action_None` | 310 | 322 | 13 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 301 | 186 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_None` | 309 | 314 | 6 | inferred_complete_timeline |
| `Action_None` | 317 | 329 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 20–83 | 5 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 60–89 | 30 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 86–227 | 141 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 96–155 | 60 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 112–329 | 161 | 8 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 113–329 | 217 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 119–329 | 178 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 120–329 | 210 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 123–127 | 5 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 133–142 | 9 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 140–329 | 183 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 142–329 | 176 | 3 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 153–266 | 114 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 164–169 | 6 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 183–329 | 139 | 3 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 196–329 | 121 | 4 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 220–323 | 12 | 3 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 240–329 | 90 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 279–327 | 6 | 3 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 282–329 | 48 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 293–329 | 37 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 295–315 | 16 | 2 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 297–308 | 11 | 2 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 299–323 | 7 | 2 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 324–328 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 106 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-115] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-123] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-238] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-261] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-301] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-314] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-159] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-293] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-311] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-234] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-115] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-155] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-156] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-138] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-149] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-238] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-266] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-313] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-268] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-298] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-322] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-104] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-50] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-94] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-114] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-154] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-22] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-227] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-264] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-284] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-322] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-257] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-286] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-149] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-232] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-266] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-201] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-243] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-203] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-220] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-317] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-323] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-308] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-304] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-323] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-328] for track '44' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>