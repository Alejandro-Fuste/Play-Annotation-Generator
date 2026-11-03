# Play-Annotation-Generator Annotation Review — PuntBlock_22

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_22`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 67
- **Validation Warnings:** 57
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher3 | defense | `13` | `13` |
| ✅ EXACT | `Action_SecureRecovery` | Punt_Support1 | defense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `0` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `11` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `12` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `17` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `2` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `20` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `6` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `8` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `9` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | `17` | `17` | 25 | START | 25 | 74 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `8` | `8` | 52 | END | 52 | 52 |
| ✅ EXACT | `Action_PuntBall` | Punter | `8` | `8` | 75 | START | 75 | 299 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher3 | `13` | `13` | 89 | START | 89 | 95 |
| ✅ EXACT | `Action_SecureRecovery` | Punt_Support1 | `7` | `7` | 252 | START | 252 | 254 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 76 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 98 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 299 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 299 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 299 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 82 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_SnapReceive` | 52 | 52 | 1 | inferred_complete_timeline |
| `Action_None` | 53 | 74 | 22 | inferred_complete_timeline |
| `Action_PuntBall` | 75 | 299 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_LongSnap` | 25 | 74 | 50 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 78 | 275 | 198 | inferred_complete_timeline |
| `Action_None` | 292 | 299 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 299 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 299 | 275 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 57 | 33 | inferred_complete_timeline |
| `Action_None` | 59 | 269 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_BlockPunt` | 89 | 95 | 7 | inferred_complete_timeline |
| `Action_None` | 96 | 235 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 253 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 278 | 254 | inferred_complete_timeline |
| `Action_None` | 280 | 299 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 251 | 252 | inferred_complete_timeline |
| `Action_SecureRecovery` | 252 | 254 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 187 | 163 | inferred_complete_timeline |
| `Action_None` | 191 | 298 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 53 | 29 | inferred_complete_timeline |
| `Action_None` | 56 | 296 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support4 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 299 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 299 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support6 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 119 | 95 | inferred_complete_timeline |
| `Action_None` | 121 | 256 | 136 | inferred_complete_timeline |
| `Action_None` | 266 | 299 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 51–52 | 2 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 79–82 | 4 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 79–299 | 219 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 92–98 | 7 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 93–299 | 199 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 101–299 | 199 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 124–299 | 176 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 259–260 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punt_Support6` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punt_Support5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Punt_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 29 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 46: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Row 46: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [25-82] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-278] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-119] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-256] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-187] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-298] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-251] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [252-254] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-253] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-235] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-275] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-53] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-296] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-98] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-99] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-98] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>