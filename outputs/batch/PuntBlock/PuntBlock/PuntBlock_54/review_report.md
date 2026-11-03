# Play-Annotation-Generator Annotation Review — PuntBlock_54

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_54`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher1 | defense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `0` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `1` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `2` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `3` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `4` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `5` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `6` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `8` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `9` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `0` | `0` | 15 | START | 15 | 72 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `5` | `5` | 44 | END | 44 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `5` | `5` | 73 | START | 73 | 215 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher1 | `12` | `12` | 80 | START | 80 | 82 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 188 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 218 | 204 | inferred_complete_timeline |
| `Action_None` | 220 | 254 | 35 | inferred_complete_timeline |
| `Action_None` | 256 | 291 | 36 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 256 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_LongSnap` | 15 | 72 | 58 | inferred_complete_timeline |
| `Action_None` | 73 | 163 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 195 | 181 | inferred_complete_timeline |
| `Action_None` | 199 | 236 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 299 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_SnapReceive` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_None` | 45 | 72 | 28 | inferred_complete_timeline |
| `Action_PuntBall` | 73 | 215 | 143 | inferred_complete_timeline |
| `Action_PuntBall` | 217 | 228 | 12 | inferred_complete_timeline |
| `Action_PuntBall` | 232 | 239 | 8 | inferred_complete_timeline |
| `Action_PuntBall` | 244 | 245 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 299 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 180 | 166 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 75 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_BlockPunt` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_None` | 90 | 113 | 24 | inferred_complete_timeline |
| `Action_None` | 122 | 124 | 3 | inferred_complete_timeline |
| `Action_None` | 126 | 233 | 108 | inferred_complete_timeline |
| `Action_None` | 235 | 270 | 36 | inferred_complete_timeline |
| `Action_None` | 290 | 291 | 2 | inferred_complete_timeline |
| `Action_None` | 293 | 299 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 72 | 58 | inferred_complete_timeline |
| `Action_None` | 77 | 83 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 299 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 77 | 63 | inferred_complete_timeline |
| `Action_None` | 83 | 293 | 211 | inferred_complete_timeline |
| `Action_None` | 295 | 299 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 65 | 51 | inferred_complete_timeline |
| `Action_None` | 68 | 97 | 30 | inferred_complete_timeline |
| `Action_None` | 99 | 230 | 132 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_None` | 262 | 266 | 5 | inferred_complete_timeline |
| `Action_None` | 274 | 278 | 5 | inferred_complete_timeline |
| `Action_None` | 282 | 299 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 212 | 198 | inferred_complete_timeline |
| `Action_None` | 215 | 231 | 17 | inferred_complete_timeline |
| `Action_None` | 233 | 247 | 15 | inferred_complete_timeline |
| `Action_None` | 251 | 276 | 26 | inferred_complete_timeline |
| `Action_None` | 278 | 281 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 136 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 167 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 182 | 168 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 38–67 | 30 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 40–54 | 6 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 44–299 | 256 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 76–185 | 110 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 101–299 | 178 | 5 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 128–185 | 33 | 7 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 217–236 | 20 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 221–299 | 12 | 3 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 237–299 | 63 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 237–299 | 62 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 261–299 | 38 | 2 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 267–299 | 32 | 2 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 285–299 | 15 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 289–299 | 9 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `5` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Punt_Support1` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 66 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [73-163] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-299] for track '1' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-218] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-254] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-291] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-256] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-188] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [73-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [217-228] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [232-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [244-245] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-212] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-231] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-247] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-276] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-236] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-180] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-72] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-182] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-75] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [80-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-113] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-233] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-270] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-136] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-77] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-293] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-299] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-97] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-230] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-278] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-42] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-185] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-115] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-142] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-163] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-181] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-163] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-236] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-299] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-251] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-295] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-275] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-296] for track '32' has 1 frames without a visible bounding box.
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

</details>