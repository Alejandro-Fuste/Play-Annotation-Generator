# Play-Annotation-Generator Annotation Review — PuntBlock_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_25`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Right_Guard | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `10` | `10` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_BlockPunt` | Interior_Rusher8 | defense | `4` | `4` |
| ✅ EXACT | `Action_SecureRecovery` | Position_Unknown | Team_Unknown | `40` | `25` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `10` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `11` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `13` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `16` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `17` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `18` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `19` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `7` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `8` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `9` | `Group` | 0 | START | 0 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Right_Guard | `12` | `12` | 24 | START | 24 | 43 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `10` | `10` | 52 | END | 52 | 52 |
| ✅ EXACT | `Action_PuntBall` | Punter | `10` | `10` | 79 | START | 79 | 188 |
| ⚠️ START CHANGED | `Action_BlockPunt` | Interior_Rusher8 | `4` | `4` | 89 | START | 90 | 92 |
| ✅ EXACT | `Action_SecureRecovery` | Position_Unknown | `40` | `25` | 178 | START | 178 | 180 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 210 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 210 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 62 | 39 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 198 | 41 | inferred_complete_timeline |
| `Action_None` | 200 | 202 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 210 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 188 | 165 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 210 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 90 | 67 | inferred_complete_timeline |
| `Action_None` | 92 | 100 | 9 | inferred_complete_timeline |
| `Action_None` | 102 | 182 | 81 | inferred_complete_timeline |
| `Action_None` | 184 | 188 | 5 | inferred_complete_timeline |
| `Action_None` | 198 | 203 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 103 | 80 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_SnapReceive` | 52 | 52 | 1 | inferred_complete_timeline |
| `Action_None` | 53 | 78 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 79 | 188 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_LongSnap` | 24 | 43 | 20 | inferred_complete_timeline |
| `Action_LongSnap` | 45 | 76 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 78 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 210 | 187 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 158 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 210 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 175 | 152 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 210 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 47 | 24 | inferred_complete_timeline |
| `Action_None` | 49 | 209 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 50 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 202 | 179 | inferred_complete_timeline |
| `Action_None` | 205 | 209 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 54 | 31 | inferred_complete_timeline |
| `Action_None` | 60 | 210 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_BlockPunt` | 90 | 92 | 3 | inferred_complete_timeline |
| `Action_None` | 93 | 171 | 79 | inferred_complete_timeline |
| `Action_None` | 186 | 196 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 210 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 210 | 187 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `24` | Position_Unknown | Team_Unknown | 51–210 | 160 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 73–209 | 137 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 82–210 | 118 | 4 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 94–95 | 2 | 1 | Undefined position; Undefined team |
| `25` | `40` | Position_Unknown | Team_Unknown | 98–180 | 82 | 3 | Undefined position; Undefined team |
| `26` | `45` | Position_Unknown | Team_Unknown | 110–210 | 101 | 1 | Undefined position; Undefined team |
| `27` | `55` | Position_Unknown | Team_Unknown | 150–161 | 7 | 3 | Undefined position; Undefined team |
| `28` | `56` | Position_Unknown | Team_Unknown | 154–175 | 14 | 4 | Undefined position; Undefined team |
| `29` | `59` | Position_Unknown | Team_Unknown | 170–210 | 31 | 5 | Undefined position; Undefined team |
| `30` | `60` | Position_Unknown | Team_Unknown | 175–176 | 2 | 1 | Undefined position; Undefined team |
| `31` | `63` | Position_Unknown | Team_Unknown | 193–197 | 5 | 1 | Undefined position; Undefined team |
| `32` | `64` | Position_Unknown | Team_Unknown | 196–198 | 3 | 1 | Undefined position; Undefined team |
| `33` | `65` | Position_Unknown | Team_Unknown | 200–210 | 11 | 1 | Undefined position; Undefined team |
| `34` | `66` | Position_Unknown | Team_Unknown | 200–210 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `12` (2 segments found)
- ⚠️ `Action_BlockPunt` for actor_track_id `4` (Interior_Rusher8): Annotated start 89 != Inferred start 90

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 67 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [24-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-47] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-209] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-54] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-88] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [90-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-196] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-175] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-210] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-78] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-188] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [79-188] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [24-43] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [45-76] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-90] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-100] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-182] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-62] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-198] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-202] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-209] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-187] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-174] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [178-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-184] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '34' has 2 frames without a visible bounding box.
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