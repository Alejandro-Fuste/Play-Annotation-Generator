# Play-Annotation-Generator Annotation Review — PuntBlock_56

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_56`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 269
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 127
- **Validation Warnings:** 175
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 102
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `8` | `Group` |
| ✅ EXACT | `Action_SnapReceive` | Right_Edge_Rusher1 | defense | `11` | `11` |
| ✅ EXACT | `Action_PuntBall` | Right_Edge_Rusher1 | defense | `11` | `11` |
| ✅ EXACT | `Action_BlockPunt` | Right_Edge_Rusher1 | defense | `11` | `11` |
| ✅ EXACT | `Action_SecureRecovery` | Position_Unknown | Team_Unknown | `43` | `34` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `0` | `Group` | 0 | START | 0 | 254 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `1` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `2` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `3` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `4` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `5` | `Group` | 0 | START | 0 | 237 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `6` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `7` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `8` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_SnapReceive` | Right_Edge_Rusher1 | `11` | `11` | 17 | END | 17 | 17 |
| ✅ EXACT | `Action_PuntBall` | Right_Edge_Rusher1 | `11` | `11` | 86 | START | 86 | 92 |
| ✅ EXACT | `Action_BlockPunt` | Right_Edge_Rusher1 | `11` | `11` | 95 | START | 95 | 101 |
| ✅ EXACT | `Action_SecureRecovery` | Position_Unknown | `43` | `34` | 196 | START | 196 | 209 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 259 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 220 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 245 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 251 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 193 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 254 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 179 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 189 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 208 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 88 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 91 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 161 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 269 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 117 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 140 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 201 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 224 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 249 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 163 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 269 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 244 | 145 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 250 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 259 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 16 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 17 | 1 | inferred_complete_timeline |
| `Action_None` | 18 | 31 | 14 | inferred_complete_timeline |
| `Action_None` | 43 | 46 | 4 | inferred_complete_timeline |
| `Action_None` | 54 | 85 | 32 | inferred_complete_timeline |
| `Action_PuntBall` | 86 | 92 | 7 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_BlockPunt` | 95 | 101 | 7 | inferred_complete_timeline |
| `Action_None` | 102 | 147 | 46 | inferred_complete_timeline |
| `Action_None` | 149 | 157 | 9 | inferred_complete_timeline |
| `Action_None` | 162 | 183 | 22 | inferred_complete_timeline |
| `Action_None` | 188 | 193 | 6 | inferred_complete_timeline |
| `Action_None` | 208 | 269 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 10–213 | 184 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 20–269 | 232 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 29–231 | 173 | 9 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 36–37 | 2 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 45–54 | 10 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 48–51 | 4 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 52–214 | 159 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 55–102 | 17 | 5 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 58–269 | 212 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 81–82 | 2 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 85–256 | 169 | 4 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 90–113 | 23 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 103–205 | 92 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 103–104 | 2 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 114–116 | 3 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 118–127 | 6 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 125–157 | 13 | 5 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 127–248 | 117 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 145–269 | 125 | 3 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 160–254 | 93 | 2 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 165–172 | 7 | 2 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 165–166 | 2 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 170–242 | 73 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 177–193 | 10 | 2 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 183–241 | 12 | 3 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 190–191 | 2 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 208–218 | 5 | 2 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 217–219 | 3 | 1 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 251–254 | 4 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 262–269 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 113 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-254] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-152] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-179] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-208] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-212] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-220] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-245] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-248] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-251] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-193] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-88] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-111] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-259] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-163] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-31] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-46] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-147] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-157] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-117] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-140] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-201] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-204] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-224] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-249] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-98] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-244] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-250] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-259] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-26] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-161] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-22] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-40] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-213] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-123] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-148] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-253] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-260] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-44] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-129] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-146] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-205] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-225] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-231] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-51] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-157] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-214] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-61] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-82] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-93] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-102] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-143] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-205] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-256] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-109] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-113] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-146] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-162] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-205] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-116] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-120] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-127] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-139] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-148] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-157] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-129] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-248] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-171] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-254] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-169] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-242] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-184] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-186] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-196] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-241] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-210] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-218] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-219] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-254] for track '44' has 1 frames without a visible bounding box.
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

</details>