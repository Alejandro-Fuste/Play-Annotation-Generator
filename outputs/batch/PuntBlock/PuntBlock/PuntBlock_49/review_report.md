# Play-Annotation-Generator Annotation Review — PuntBlock_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_49`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_LongSnap` | Left_Guard | offense | `17` | `17` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `9` | `Group` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `14` | `14` |
| ✅ EXACT | `Action_BlockPunt` | Left_Edge_Rusher1 | defense | `7` | `7` |
| ✅ EXACT | `Action_SecureRecovery` | Left_Edge_Rusher1 | defense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_LongSnap` | Left_Guard | `17` | `17` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `1` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `10` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `11` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `13` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `14` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `16` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `3` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `4` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `9` | `Group` | 0 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Punter | `14` | `14` | 22 | END | 22 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `14` | `14` | 70 | START | 70 | 169 |
| ✅ EXACT | `Action_BlockPunt` | Left_Edge_Rusher1 | `7` | `7` | 83 | START | 83 | 88 |
| ✅ EXACT | `Action_SecureRecovery` | Left_Edge_Rusher1 | `7` | `7` | 155 | START | 155 | 162 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_LongSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 239 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 61 | 72 | 12 | inferred_complete_timeline |
| `Action_None` | 77 | 82 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 229 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–16
- **Visible Samples:** 17

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 16 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 182 | 239 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 219 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 22 | 1 | inferred_complete_timeline |
| `Action_None` | 23 | 69 | 47 | inferred_complete_timeline |
| `Action_PuntBall` | 70 | 169 | 100 | inferred_complete_timeline |
| `Action_PuntBall` | 172 | 173 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 225 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 38 | 239 | 202 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 106 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 46 | 169 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_BlockPunt` | 83 | 88 | 6 | inferred_complete_timeline |
| `Action_None` | 89 | 154 | 66 | inferred_complete_timeline |
| `Action_SecureRecovery` | 155 | 162 | 8 | inferred_complete_timeline |
| `Action_None` | 163 | 189 | 27 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 72 | 217 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 194 | 212 | 19 | inferred_complete_timeline |
| `Action_None` | 214 | 225 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_None` | 177 | 239 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 199 | 239 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_None` | 166 | 190 | 25 | inferred_complete_timeline |
| `Action_None` | 199 | 210 | 12 | inferred_complete_timeline |
| `Action_None` | 212 | 217 | 6 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 15–230 | 214 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 29–46 | 18 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 39–41 | 3 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 71–72 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 84–86 | 3 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 107–158 | 49 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 120–211 | 91 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 123–127 | 5 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 126–137 | 12 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 129–130 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 133–229 | 78 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 134–231 | 59 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 175–239 | 62 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 185–239 | 55 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 186–239 | 14 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 203–228 | 17 | 2 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 210–216 | 7 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 234–239 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 59 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [0-164] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-190] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-217] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-225] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-31] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-169] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-16] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-57] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-72] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-175] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-189] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-67] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-217] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-33] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-229] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-190] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-179] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [70-169] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [172-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-192] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-212] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-225] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-219] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-16] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-46] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-41] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-86] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-139] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-154] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-135] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-137] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-139] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-229] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-190] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-195] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-193] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-228] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '37' has 1 frames without a visible bounding box.
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

</details>