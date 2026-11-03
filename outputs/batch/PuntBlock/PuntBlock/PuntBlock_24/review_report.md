# Play-Annotation-Generator Annotation Review — PuntBlock_24

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_24`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 114
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
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `10` | `10` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `10` | `10` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher4 | defense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `10` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `2` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `5` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `6` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `7` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | `6` | `6` | 8 | START | 8 | 59 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `10` | `10` | 35 | END | 35 | 35 |
| ✅ EXACT | `Action_PuntBall` | Punter | `10` | `10` | 60 | START | 60 | 177 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher4 | `4` | `4` | 67 | START | 67 | 71 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 33 | 26 | inferred_complete_timeline |
| `Action_None` | 41 | 47 | 7 | inferred_complete_timeline |
| `Action_None` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 29 | 22 | inferred_complete_timeline |
| `Action_None` | 35 | 53 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 78 | 71 | inferred_complete_timeline |
| `Action_None` | 82 | 239 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 111 | 104 | inferred_complete_timeline |
| `Action_None` | 113 | 140 | 28 | inferred_complete_timeline |
| `Action_None` | 146 | 164 | 19 | inferred_complete_timeline |
| `Action_None` | 166 | 178 | 13 | inferred_complete_timeline |
| `Action_None` | 180 | 239 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_SnapReceive` | 35 | 35 | 1 | inferred_complete_timeline |
| `Action_None` | 36 | 59 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 60 | 177 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_LongSnap` | 8 | 59 | 52 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 87 | 80 | inferred_complete_timeline |
| `Action_None` | 90 | 111 | 22 | inferred_complete_timeline |
| `Action_None` | 115 | 136 | 22 | inferred_complete_timeline |
| `Action_None` | 139 | 145 | 7 | inferred_complete_timeline |
| `Action_None` | 147 | 154 | 8 | inferred_complete_timeline |
| `Action_None` | 156 | 186 | 31 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 239 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 145 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 82 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 66 | 10 | inferred_complete_timeline |
| `Action_BlockPunt` | 67 | 71 | 5 | inferred_complete_timeline |
| `Action_None` | 72 | 130 | 59 | inferred_complete_timeline |
| `Action_None` | 136 | 164 | 29 | inferred_complete_timeline |
| `Action_None` | 170 | 223 | 54 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 100 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 111 | 104 | inferred_complete_timeline |
| `Action_None` | 113 | 198 | 86 | inferred_complete_timeline |
| `Action_None` | 200 | 203 | 4 | inferred_complete_timeline |
| `Action_None` | 205 | 239 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 239 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 177 | 170 | inferred_complete_timeline |
| `Action_None` | 180 | 184 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–88 | 69 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–145 | 57 | 9 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 13–239 | 227 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 17–238 | 220 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 34–35 | 2 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 73–239 | 167 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 77–113 | 36 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 84–239 | 151 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 88–185 | 98 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 98–229 | 132 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 118–239 | 114 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 137–235 | 99 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 139–239 | 99 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 146–239 | 94 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 199–221 | 21 | 3 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 209–229 | 11 | 3 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 217–239 | 13 | 3 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 223–231 | 9 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 231–236 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Punt_Support2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 50: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 50: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [8-100] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-82] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-87] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-111] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-136] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-145] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-186] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-111] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-140] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-164] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-178] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-164] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-223] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-78] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-239] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-33] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-47] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-239] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [60-177] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-177] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-29] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-27] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-50] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-61] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-183] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-238] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-113] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-133] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-183] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-185] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-229] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-195] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-228] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-235] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-185] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-239] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-218] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-231] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>