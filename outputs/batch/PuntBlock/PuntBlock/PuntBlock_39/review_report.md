# Play-Annotation-Generator Annotation Review — PuntBlock_39

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_39`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 359
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_BlockPunt` | Interior_Rusher3 | defense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Right_Edge_Rusher1 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `0` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `10` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `11` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `14` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `15` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `17` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `18` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `19` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `8` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `9` | `Group` | 0 | START | 0 | 37 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `11` | `11` | 8 | START | 8 | 59 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `9` | `9` | 38 | END | 38 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `9` | `9` | 60 | START | 60 | 199 |
| ❌ MISSING SEGMENT | `Action_BlockPunt` | Interior_Rusher3 | `7` | `7` | 75 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Right_Edge_Rusher1 | `2` | `2` | 188 | START | 188 | 194 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 143 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 212 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 118 | 111 | inferred_complete_timeline |
| `Action_None` | 124 | 128 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_LongSnap` | 8 | 59 | 52 | inferred_complete_timeline |
| `Action_None` | 60 | 162 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 359 | 352 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 214 | 207 | inferred_complete_timeline |
| `Action_None` | 233 | 273 | 41 | inferred_complete_timeline |
| `Action_None` | 275 | 283 | 9 | inferred_complete_timeline |
| `Action_None` | 289 | 348 | 60 | inferred_complete_timeline |
| `Action_None` | 357 | 359 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 85 | 78 | inferred_complete_timeline |
| `Action_None` | 87 | 359 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_SnapReceive` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_None` | 39 | 59 | 21 | inferred_complete_timeline |
| `Action_PuntBall` | 60 | 199 | 140 | inferred_complete_timeline |
| `Action_PuntBall` | 202 | 206 | 5 | inferred_complete_timeline |
| `Action_PuntBall` | 208 | 213 | 6 | inferred_complete_timeline |
| `Action_PuntBall` | 224 | 293 | 70 | inferred_complete_timeline |
| `Action_PuntBall` | 296 | 359 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 173 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 158 | 151 | inferred_complete_timeline |
| `Action_None` | 162 | 168 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 206 | 199 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 106 | 99 | inferred_complete_timeline |
| `Action_None` | 110 | 114 | 5 | inferred_complete_timeline |
| `Action_None` | 118 | 130 | 13 | inferred_complete_timeline |
| `Action_None` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 359 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 26 | 19 | inferred_complete_timeline |
| `Action_None` | 30 | 58 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 65 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 72 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 96 | 174 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 45 | 38 | inferred_complete_timeline |
| `Action_None` | 51 | 71 | 21 | inferred_complete_timeline |
| `Action_None` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_None` | 80 | 359 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 35 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 39 | 32 | inferred_complete_timeline |
| `Action_None` | 42 | 359 | 318 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 67 | 60 | inferred_complete_timeline |
| `Action_None` | 70 | 73 | 4 | inferred_complete_timeline |
| `Action_None` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_None` | 82 | 116 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 36 | 29 | inferred_complete_timeline |
| `Action_None` | 41 | 179 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 114 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 151 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 187 | 35 | inferred_complete_timeline |
| `Action_SecureRecovery` | 188 | 194 | 7 | inferred_complete_timeline |
| `Action_SecureRecovery` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_SecureRecovery` | 209 | 213 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 40–208 | 161 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 81–305 | 156 | 3 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 99–135 | 7 | 2 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 109–295 | 159 | 4 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 112–173 | 13 | 4 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 139–146 | 6 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 146–209 | 62 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 157–159 | 3 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 272–274 | 3 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 297–345 | 31 | 3 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 325–359 | 35 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 328–359 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `9` (5 segments found)
- ❌ Missing segment for action `Action_BlockPunt` on target `7` (Interior_Rusher3)
- ⚠️ Ambiguous match for action `Action_SecureRecovery` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_BlockPunt' for track '7' has invalid range: start=75, end=72. Clamping end to start.
- ⚠️ Action 'Action_None' range [8-158] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-168] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-39] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-114] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-151] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-187] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [188-194] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [201-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [209-213] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-67] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-73] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-116] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-26] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-58] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-130] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-45] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-71] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-359] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-65] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-212] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [60-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [202-206] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [208-213] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [224-293] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-174] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-173] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-214] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-273] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-283] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-348] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-118] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-128] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-206] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-208] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-92] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-233] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-305] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-206] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-295] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-201] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-309] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-337] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-334] for track '32' has 1 frames without a visible bounding box.
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