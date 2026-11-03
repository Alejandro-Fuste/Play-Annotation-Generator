# Play-Annotation-Generator Annotation Review — PuntBlock_62

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_62`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 174
- **Validation Warnings:** 231
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 163
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Left_Guard | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_BlockPunt` | Left_Edge_Rusher1 | defense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `1` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `10` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `11` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `4` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `5` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `6` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `9` | `Group` | 0 | START | 0 | 32 |
| ✅ EXACT | `Action_LongSnap` | Left_Guard | `11` | `11` | 6 | START | 6 | 41 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `9` | `9` | 33 | END | 33 | 33 |
| ✅ EXACT | `Action_PuntBall` | Punter | `9` | `9` | 57 | START | 57 | 64 |
| ✅ EXACT | `Action_BlockPunt` | Left_Edge_Rusher1 | `3` | `3` | 64 | START | 64 | 69 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_LongSnap` | 6 | 41 | 36 | inferred_complete_timeline |
| `Action_None` | 58 | 273 | 216 | inferred_complete_timeline |
| `Action_None` | 275 | 283 | 9 | inferred_complete_timeline |
| `Action_None` | 285 | 329 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 329 | 324 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 56 | 51 | inferred_complete_timeline |
| `Action_None` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_None` | 90 | 107 | 18 | inferred_complete_timeline |
| `Action_None` | 109 | 217 | 109 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 283 | 45 | inferred_complete_timeline |
| `Action_None` | 285 | 287 | 3 | inferred_complete_timeline |
| `Action_None` | 292 | 329 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 66 | 61 | inferred_complete_timeline |
| `Action_None` | 69 | 139 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 38 | 33 | inferred_complete_timeline |
| `Action_None` | 42 | 215 | 174 | inferred_complete_timeline |
| `Action_None` | 217 | 224 | 8 | inferred_complete_timeline |
| `Action_None` | 230 | 241 | 12 | inferred_complete_timeline |
| `Action_None` | 280 | 293 | 14 | inferred_complete_timeline |
| `Action_None` | 307 | 311 | 5 | inferred_complete_timeline |
| `Action_None` | 313 | 314 | 2 | inferred_complete_timeline |
| `Action_None` | 316 | 318 | 3 | inferred_complete_timeline |
| `Action_None` | 320 | 329 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_None` | 34 | 56 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 57 | 64 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–13
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 13 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 125 | 120 | inferred_complete_timeline |
| `Action_None` | 127 | 130 | 4 | inferred_complete_timeline |
| `Action_None` | 133 | 189 | 57 | inferred_complete_timeline |
| `Action_None` | 192 | 198 | 7 | inferred_complete_timeline |
| `Action_None` | 200 | 202 | 3 | inferred_complete_timeline |
| `Action_None` | 226 | 262 | 37 | inferred_complete_timeline |
| `Action_None` | 265 | 274 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 133 | 128 | inferred_complete_timeline |
| `Action_None` | 135 | 148 | 14 | inferred_complete_timeline |
| `Action_None` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_None` | 157 | 160 | 4 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 235 | 63 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |
| `Action_None` | 241 | 263 | 23 | inferred_complete_timeline |
| `Action_None` | 295 | 329 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 146 | 141 | inferred_complete_timeline |
| `Action_None` | 148 | 204 | 57 | inferred_complete_timeline |
| `Action_None` | 215 | 243 | 29 | inferred_complete_timeline |
| `Action_None` | 251 | 267 | 17 | inferred_complete_timeline |
| `Action_None` | 270 | 277 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 36 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_BlockPunt` | 64 | 69 | 6 | inferred_complete_timeline |
| `Action_None` | 70 | 78 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 163 | 158 | inferred_complete_timeline |
| `Action_None` | 167 | 173 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–85 | 73 | 4 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 2–329 | 321 | 6 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 19–21 | 3 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 42–172 | 109 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 49–122 | 74 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 53–315 | 246 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 53–276 | 223 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 61–144 | 84 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 75–306 | 196 | 11 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 78–220 | 44 | 6 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 95–282 | 181 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 103–304 | 201 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 104–282 | 179 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 108–306 | 199 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 109–252 | 126 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 117–202 | 85 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 119–329 | 194 | 5 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 135–295 | 159 | 3 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 138–139 | 2 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 154–253 | 48 | 4 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 170–185 | 16 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 180–215 | 22 | 4 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 187–289 | 52 | 10 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 202–206 | 5 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 209–241 | 25 | 2 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 213–222 | 8 | 2 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 215–226 | 12 | 1 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 220–225 | 6 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 239–283 | 42 | 3 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 244–329 | 79 | 4 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 249–278 | 17 | 3 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 253–255 | 3 | 1 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 261–282 | 10 | 2 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 284–285 | 2 | 1 | Undefined position; Undefined team |
| `47` | `56` | Position_Unknown | Team_Unknown | 286–329 | 43 | 2 | Undefined position; Undefined team |
| `48` | `58` | Position_Unknown | Team_Unknown | 288–289 | 2 | 1 | Undefined position; Undefined team |
| `49` | `61` | Position_Unknown | Team_Unknown | 312–329 | 13 | 2 | Undefined position; Undefined team |
| `50` | `63` | Position_Unknown | Team_Unknown | 320–329 | 10 | 1 | Undefined position; Undefined team |
| `51` | `64` | Position_Unknown | Team_Unknown | 324–329 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ 39 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 39 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 78 |
| Missing visible bounding boxes during action | 150 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [6-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-189] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-198] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-262] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-274] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-56] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-88] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-107] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-217] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-283] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-329] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-133] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-148] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-235] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-263] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [64-69] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-78] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-66] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-139] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-38] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-215] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-224] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-241] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-293] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-311] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-163] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-146] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-204] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-243] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-267] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-277] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [57-64] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-13] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [6-41] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-273] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-283] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-329] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-36] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-49] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-13] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-35] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-43] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-172] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-122] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-186] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-275] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-315] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-150] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-276] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-144] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-78] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-118] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-126] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-240] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-270] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-306] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-220] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-153] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-166] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-282] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-148] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-304] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-282] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-306] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-232] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-126] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-202] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-129] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-147] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-207] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-226] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-329] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-142] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-295] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-166] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-197] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-185] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-203] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-225] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-271] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-289] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-231] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-222] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-226] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-280] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-266] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-280] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-257] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-264] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-282] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-318] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-329] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-329] for track '51' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.

</details>