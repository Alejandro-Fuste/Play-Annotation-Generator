# Play-Annotation-Generator Annotation Review — PuntBlock_30

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_30`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `5` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher5 | defense | `11` | `11` |
| ✅ EXACT | `Action_SecureRecovery` | Interior_Rusher5 | defense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `0` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `10` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `14` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `15` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `17` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `18` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `2` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `3` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `4` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `5` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `5` | `5` | 5 | START | 5 | 63 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `2` | `2` | 38 | END | 38 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `2` | `2` | 64 | START | 64 | 175 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher5 | `11` | `11` | 114 | START | 114 | 131 |
| ✅ EXACT | `Action_SecureRecovery` | Interior_Rusher5 | `11` | `11` | 183 | START | 183 | 190 |

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
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 168 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 162 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 128 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_LongSnap` | 5 | 63 | 59 | inferred_complete_timeline |
| `Action_None` | 64 | 167 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 175 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 65 | 61 | inferred_complete_timeline |
| `Action_None` | 67 | 168 | 102 | inferred_complete_timeline |
| `Action_None` | 175 | 205 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 56 | 52 | inferred_complete_timeline |
| `Action_None` | 61 | 141 | 81 | inferred_complete_timeline |
| `Action_None` | 169 | 299 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_SnapReceive` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_None` | 39 | 63 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 64 | 175 | 112 | inferred_complete_timeline |
| `Action_PuntBall` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_PuntBall` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_PuntBall` | 216 | 220 | 5 | inferred_complete_timeline |
| `Action_PuntBall` | 223 | 253 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 21 | 17 | inferred_complete_timeline |
| `Action_None` | 75 | 212 | 138 | inferred_complete_timeline |
| `Action_None` | 214 | 217 | 4 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 26 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 122 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 80 | 76 | inferred_complete_timeline |
| `Action_None` | 82 | 173 | 92 | inferred_complete_timeline |
| `Action_None` | 175 | 299 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 299 | 295 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_BlockPunt` | 114 | 131 | 18 | inferred_complete_timeline |
| `Action_None` | 132 | 182 | 51 | inferred_complete_timeline |
| `Action_SecureRecovery` | 183 | 190 | 8 | inferred_complete_timeline |
| `Action_None` | 191 | 195 | 5 | inferred_complete_timeline |
| `Action_None` | 200 | 207 | 8 | inferred_complete_timeline |
| `Action_None` | 257 | 299 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 275 | 271 | inferred_complete_timeline |
| `Action_None` | 278 | 285 | 8 | inferred_complete_timeline |
| `Action_None` | 292 | 296 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 135 | 131 | inferred_complete_timeline |
| `Action_None` | 138 | 250 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 197 | 193 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 74 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 34–172 | 139 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 34–299 | 182 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 67–276 | 203 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 103–158 | 55 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 120–299 | 179 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 150–175 | 26 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 177–179 | 3 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 180–181 | 2 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 182–216 | 35 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 202–286 | 11 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 204–238 | 33 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 218–257 | 30 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 235–299 | 61 | 4 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 273–299 | 27 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 289–299 | 11 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 294–296 | 3 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `2` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 66 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [5-175] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [64-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [180-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [184-185] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [216-220] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [223-253] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-21] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-212] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-128] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-167] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-250] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-299] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-76] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-275] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-285] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-168] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-205] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-122] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-74] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-168] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-173] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-299] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-56] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-141] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-299] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-172] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-197] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-103] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-276] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-158] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-133] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-175] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-216] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-230] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-238] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-257] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-290] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '37' has 1 frames without a visible bounding box.
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

</details>