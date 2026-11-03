# Play-Annotation-Generator Annotation Review — PuntBlock_12

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_12`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 269
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 167
- **Validation Warnings:** 204
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 153
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher5 | defense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Left_Edge_Rusher1 | defense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `0` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `1` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `10` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `13` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `2` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `3` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `4` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `7` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `8` | `Group` | 0 | START | 0 | 20 |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | `1` | `1` | 21 | START | 21 | 81 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `3` | `3` | 48 | END | 48 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `3` | `3` | 82 | START | 82 | 231 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher5 | `12` | `12` | 91 | START | 91 | 96 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Left_Edge_Rusher1 | `17` | `17` | 202 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 85 | 65 | inferred_complete_timeline |
| `Action_None` | 89 | 269 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 269 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 177 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 91 | 71 | inferred_complete_timeline |
| `Action_None` | 93 | 269 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 269 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 255 | 235 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SnapReceive` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_None` | 49 | 81 | 33 | inferred_complete_timeline |
| `Action_PuntBall` | 82 | 231 | 150 | inferred_complete_timeline |
| `Action_PuntBall` | 235 | 269 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_LongSnap` | 21 | 81 | 61 | inferred_complete_timeline |
| `Action_None` | 82 | 171 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 39 | 19 | inferred_complete_timeline |
| `Action_None` | 41 | 269 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 269 | 249 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 83 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 65 | 45 | inferred_complete_timeline |
| `Action_None` | 67 | 269 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 46 | 26 | inferred_complete_timeline |
| `Action_None` | 59 | 66 | 8 | inferred_complete_timeline |
| `Action_None` | 68 | 269 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 232 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_BlockPunt` | 91 | 96 | 6 | inferred_complete_timeline |
| `Action_None` | 97 | 187 | 91 | inferred_complete_timeline |
| `Action_None` | 189 | 269 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 257 | 237 | inferred_complete_timeline |
| `Action_None` | 260 | 264 | 5 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 249 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 269 | 249 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `21` | Position_Unknown | Team_Unknown | 98–144 | 47 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 106–130 | 5 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 107–269 | 131 | 7 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 108–129 | 21 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 115–269 | 97 | 7 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 120–269 | 136 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 128–152 | 9 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 130–263 | 111 | 9 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 131–223 | 89 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 131–248 | 54 | 7 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 132–244 | 92 | 3 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 139–269 | 101 | 8 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 142–263 | 119 | 2 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 149–250 | 88 | 4 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 150–229 | 38 | 3 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 151–244 | 94 | 1 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 154–252 | 88 | 4 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 154–178 | 9 | 3 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 157–167 | 11 | 1 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 159–263 | 67 | 3 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 163–178 | 11 | 3 | Undefined position; Undefined team |
| `40` | `60` | Position_Unknown | Team_Unknown | 163–242 | 13 | 6 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 164–183 | 20 | 1 | Undefined position; Undefined team |
| `42` | `64` | Position_Unknown | Team_Unknown | 170–225 | 25 | 6 | Undefined position; Undefined team |
| `43` | `66` | Position_Unknown | Team_Unknown | 172–228 | 26 | 8 | Undefined position; Undefined team |
| `44` | `68` | Position_Unknown | Team_Unknown | 177–263 | 69 | 6 | Undefined position; Undefined team |
| `45` | `71` | Position_Unknown | Team_Unknown | 182–240 | 58 | 2 | Undefined position; Undefined team |
| `46` | `74` | Position_Unknown | Team_Unknown | 202–204 | 3 | 1 | Undefined position; Undefined team |
| `47` | `76` | Position_Unknown | Team_Unknown | 207–269 | 60 | 2 | Undefined position; Undefined team |
| `48` | `77` | Position_Unknown | Team_Unknown | 208–224 | 17 | 1 | Undefined position; Undefined team |
| `49` | `79` | Position_Unknown | Team_Unknown | 218–230 | 13 | 1 | Undefined position; Undefined team |
| `50` | `80` | Position_Unknown | Team_Unknown | 240–269 | 13 | 3 | Undefined position; Undefined team |
| `51` | `83` | Position_Unknown | Team_Unknown | 256–269 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `3` (2 segments found)
- ❌ Missing segment for action `Action_SecureRecovery` on target `17` (Left_Edge_Rusher1)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 135 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureRecovery' for track '17' has invalid range: start=202, end=192. Clamping end to start.
- ⚠️ Action 'Action_None' range [21-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [82-231] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-255] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-257] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-177] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-249] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-39] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-46] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-66] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [91-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-232] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-85] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-144] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-194] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-260] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-126] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-143] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-188] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-253] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-263] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-269] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-153] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-212] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-220] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-204] for track '27' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-223] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-154] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-227] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-248] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-219] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-206] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-225] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-239] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-224] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-263] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-185] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-250] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-183] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-229] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-244] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-161] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-206] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-228] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-252] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-167] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-166] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-218] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-263] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-183] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-183] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-186] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-205] for track '44' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-228] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-250] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-240] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-217] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-269] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-224] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-230] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-245] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-258] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-262] for track '51' has 2 frames without a visible bounding box.
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