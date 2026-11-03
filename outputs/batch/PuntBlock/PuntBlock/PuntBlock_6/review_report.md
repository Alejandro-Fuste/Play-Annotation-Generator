# Play-Annotation-Generator Annotation Review — PuntBlock_6

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_6`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_BlockPunt` | Right_Edge_Rusher1 | defense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Left_Edge_Rusher1 | defense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `0` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `11` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `12` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `3` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `4` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `5` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `6` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `7` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `0` | `0` | 2 | START | 2 | 56 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `12` | `12` | 33 | END | 33 | 33 |
| ✅ EXACT | `Action_PuntBall` | Punter | `12` | `12` | 57 | START | 57 | 199 |
| ✅ EXACT | `Action_BlockPunt` | Right_Edge_Rusher1 | `9` | `9` | 63 | START | 63 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Left_Edge_Rusher1 | `8` | `8` | 143 | START | 143 | 173 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 51 | 50 | inferred_complete_timeline |
| `Action_None` | 53 | 239 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_LongSnap` | 2 | 56 | 55 | inferred_complete_timeline |
| `Action_None` | 57 | 239 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 213 | 212 | inferred_complete_timeline |
| `Action_None` | 216 | 239 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_None` | 34 | 56 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 57 | 199 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 43 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 21 | 20 | inferred_complete_timeline |
| `Action_None` | 24 | 239 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 63 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 39 | 38 | inferred_complete_timeline |
| `Action_None` | 41 | 168 | 128 | inferred_complete_timeline |
| `Action_None` | 170 | 182 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 202 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 24 | 23 | inferred_complete_timeline |
| `Action_None` | 89 | 152 | 64 | inferred_complete_timeline |
| `Action_None` | 154 | 239 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 142 | 9 | inferred_complete_timeline |
| `Action_SecureRecovery` | 143 | 173 | 31 | inferred_complete_timeline |
| `Action_SecureRecovery` | 175 | 179 | 5 | inferred_complete_timeline |
| `Action_SecureRecovery` | 182 | 190 | 9 | inferred_complete_timeline |
| `Action_SecureRecovery` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_SecureRecovery` | 206 | 208 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_BlockPunt` | 63 | 71 | 9 | inferred_complete_timeline |
| `Action_None` | 73 | 79 | 7 | inferred_complete_timeline |
| `Action_None` | 81 | 93 | 13 | inferred_complete_timeline |
| `Action_None` | 98 | 105 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–90 | 68 | 5 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 20–22 | 3 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 20–23 | 4 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 30–239 | 187 | 10 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 41–239 | 199 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 46–57 | 10 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 46–239 | 194 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 46–47 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 60–239 | 175 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 86–239 | 154 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 95–239 | 144 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 132–134 | 3 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 134–163 | 6 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 135–239 | 102 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 151–153 | 3 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 225–226 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SecureRecovery` and target `8` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 14: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [2-202] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-51] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-213] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [143-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [175-179] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [182-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [194-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [206-208] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [63-71] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-79] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-105] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [57-199] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-43] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-29] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-39] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-168] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-182] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-24] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-21] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-22] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-23] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-31] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-140] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-199] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-217] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-53] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-129] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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