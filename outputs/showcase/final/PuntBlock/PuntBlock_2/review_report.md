# Play-Annotation-Generator Annotation Review — PuntBlock_2

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_2`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 269
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 151
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher3 | defense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Position_Unknown | Team_Unknown | `29` | `23` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `0` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `1` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `2` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `4` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `5` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `6` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `7` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `2` | `2` | 18 | START | 18 | 68 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `6` | `6` | 42 | END | 42 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `6` | `6` | 69 | START | 69 | 116 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher3 | `8` | `8` | 82 | START | 82 | 99 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Position_Unknown | `29` | `23` | 223 | START | N/A | N/A |

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
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 129 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 224 | 207 | inferred_complete_timeline |
| `Action_None` | 227 | 234 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_LongSnap` | 18 | 68 | 51 | inferred_complete_timeline |
| `Action_None` | 69 | 180 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 144 | 127 | inferred_complete_timeline |
| `Action_None` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_None` | 154 | 160 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 78 | 61 | inferred_complete_timeline |
| `Action_None` | 132 | 178 | 47 | inferred_complete_timeline |
| `Action_None` | 180 | 228 | 49 | inferred_complete_timeline |
| `Action_None` | 240 | 241 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 246 | 3 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_None` | 43 | 68 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 69 | 116 | 48 | inferred_complete_timeline |
| `Action_PuntBall` | 122 | 133 | 12 | inferred_complete_timeline |
| `Action_PuntBall` | 140 | 269 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 64 | 47 | inferred_complete_timeline |
| `Action_None` | 68 | 177 | 110 | inferred_complete_timeline |
| `Action_None` | 179 | 269 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 85 | 68 | inferred_complete_timeline |
| `Action_None` | 90 | 269 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 37 | 20 | inferred_complete_timeline |
| `Action_None` | 39 | 46 | 8 | inferred_complete_timeline |
| `Action_None` | 48 | 252 | 205 | inferred_complete_timeline |
| `Action_None` | 263 | 269 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_BlockPunt` | 82 | 99 | 18 | inferred_complete_timeline |
| `Action_None` | 100 | 137 | 38 | inferred_complete_timeline |
| `Action_None` | 139 | 197 | 59 | inferred_complete_timeline |
| `Action_None` | 240 | 251 | 12 | inferred_complete_timeline |
| `Action_None` | 263 | 269 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 119 | 102 | inferred_complete_timeline |
| `Action_None` | 122 | 131 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 60 | 43 | inferred_complete_timeline |
| `Action_None` | 66 | 207 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 39 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 98 | 81 | inferred_complete_timeline |
| `Action_None` | 111 | 127 | 17 | inferred_complete_timeline |
| `Action_None` | 129 | 156 | 28 | inferred_complete_timeline |
| `Action_None` | 158 | 178 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–80 | 81 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 19–78 | 44 | 5 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 39–197 | 159 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 60–104 | 44 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 69–94 | 20 | 2 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 83–231 | 119 | 4 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 99–269 | 171 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 102–125 | 24 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 111–269 | 135 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 114–180 | 67 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 118–119 | 2 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 121–140 | 17 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 121–131 | 11 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 123–131 | 9 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 130–132 | 3 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 132–160 | 29 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 142–269 | 70 | 3 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 157–158 | 2 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 161–162 | 2 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 165–168 | 4 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 173–269 | 97 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 174–206 | 13 | 2 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 189–223 | 29 | 2 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 198–263 | 33 | 5 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 211–226 | 16 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 217–269 | 44 | 4 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 218–219 | 2 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 245–269 | 25 | 1 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 255–265 | 11 | 1 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `6` (3 segments found)
- ❌ Missing segment for action `Action_SecureRecovery` on target `29` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Edge_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 5: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureRecovery' for track '23' has invalid range: start=223, end=180. Clamping end to start.
- ⚠️ Action 'Action_None' range [18-64] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-177] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-144] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-160] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-60] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-207] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-78] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-178] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-228] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-224] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-234] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [69-116] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [122-133] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [140-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-197] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-251] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-98] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-156] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-178] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-39] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-131] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-37] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-46] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-252] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-48] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-66] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-78] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-63] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-104] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-94] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-192] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-231] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-157] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-135] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-131] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-131] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-160] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-157] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-206] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-204] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-223] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-207] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-249] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-263] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-226] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-263] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-265] for track '43' has 1 frames without a visible bounding box.
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

</details>