# Play-Annotation-Generator Annotation Review — PuntBlock_20

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_20`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 359
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher1 | defense | `3` | `3` |
| ✅ EXACT | `Action_SecureRecovery` | Personal_Protector2 | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `0` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `1` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `10` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `13` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `15` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `2` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `5` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `6` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `8` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | `13` | `13` | 29 | START | 29 | 81 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `6` | `6` | 58 | END | 58 | 58 |
| ✅ EXACT | `Action_PuntBall` | Punter | `6` | `6` | 82 | START | 82 | 135 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher1 | `3` | `3` | 97 | START | 97 | 99 |
| ✅ EXACT | `Action_SecureRecovery` | Personal_Protector2 | `5` | `5` | 194 | START | 194 | 201 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 225 | 197 | inferred_complete_timeline |
| `Action_None` | 232 | 274 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 194 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 80 | 52 | inferred_complete_timeline |
| `Action_None` | 83 | 129 | 47 | inferred_complete_timeline |
| `Action_None` | 135 | 290 | 156 | inferred_complete_timeline |
| `Action_None` | 294 | 359 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 158 | 130 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 167 | 3 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_None` | 210 | 266 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–315
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 87 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 122 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 176 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 193 | 8 | inferred_complete_timeline |
| `Action_SecureRecovery` | 194 | 201 | 8 | inferred_complete_timeline |
| `Action_None` | 202 | 315 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 359 | 331 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 58 | 1 | inferred_complete_timeline |
| `Action_None` | 59 | 81 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 82 | 135 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_LongSnap` | 29 | 81 | 53 | inferred_complete_timeline |
| `Action_None` | 82 | 197 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 42 | 14 | inferred_complete_timeline |
| `Action_None` | 47 | 52 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_BlockPunt` | 97 | 99 | 3 | inferred_complete_timeline |
| `Action_None` | 100 | 180 | 81 | inferred_complete_timeline |
| `Action_None` | 189 | 359 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–356
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 123 | 95 | inferred_complete_timeline |
| `Action_None` | 126 | 135 | 10 | inferred_complete_timeline |
| `Action_None` | 138 | 167 | 30 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 356 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 219 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 83 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 108 | 80 | inferred_complete_timeline |
| `Action_None` | 110 | 114 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 209 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 280 | 252 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 55–359 | 296 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 58–245 | 188 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 82–359 | 238 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 100–359 | 246 | 6 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 111–358 | 236 | 6 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 115–359 | 245 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 138–186 | 49 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 146–176 | 31 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 147–176 | 30 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 199–346 | 147 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 200–359 | 160 | 1 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 269–282 | 11 | 2 | Undefined position; Undefined team |
| `29` | `48` | Position_Unknown | Team_Unknown | 327–335 | 9 | 1 | Undefined position; Undefined team |
| `30` | `49` | Position_Unknown | Team_Unknown | 328–359 | 32 | 1 | Undefined position; Undefined team |
| `31` | `51` | Position_Unknown | Team_Unknown | 344–359 | 16 | 1 | Undefined position; Undefined team |
| `32` | `52` | Position_Unknown | Team_Unknown | 346–359 | 14 | 1 | Undefined position; Undefined team |
| `33` | `53` | Position_Unknown | Team_Unknown | 347–351 | 5 | 1 | Undefined position; Undefined team |
| `34` | `55` | Position_Unknown | Team_Unknown | 352–359 | 8 | 1 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 353–359 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 67 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [29-225] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-274] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-158] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-266] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-280] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-97] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-122] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-176] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-183] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-315] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [82-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-123] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-135] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-356] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-194] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-209] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-42] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-52] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-108] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-219] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-197] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-80] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-290] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-359] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-245] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-333] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-280] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-300] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-310] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-359] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-178] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-217] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-285] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-358] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-186] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-176] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-346] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-276] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-335] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-359] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-351] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-359] for track '34' has 1 frames without a visible bounding box.
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

</details>