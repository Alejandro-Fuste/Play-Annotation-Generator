# Play-Annotation-Generator Annotation Review — Draw_85

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_85`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 62
- **Validation Warnings:** 59
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 43
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `1` | `0` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 34 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 32 | START | 32 | 45 |
| ✅ EXACT | `Action_PassBlock` | RG | `1` | `0` | 35 | START | 35 | 87 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `11` | `10` | 35 | START | 46 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `5` | `4` | 35 | START | 35 | 155 |
| ✅ EXACT | `Action_PassBlock` | RT | `6` | `5` | 35 | START | 35 | 155 |
| ✅ EXACT | `Action_PassBlock` | LG | `8` | `7` | 35 | START | 35 | 155 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 45 | END | 32 | 45 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `10` | `9` | 49 | START | 49 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `10` | `9` | 86 | START | 86 | 221 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 155 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 45 | 14 | inferred_complete_timeline |
| `Action_None` | 46 | 48 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 49 | 85 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 86 | 221 | 136 | inferred_complete_timeline |
| `Action_BallCarry` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 139 | 108 | inferred_complete_timeline |
| `Action_None` | 143 | 203 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 155 | 121 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 239 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 155 | 121 | inferred_complete_timeline |
| `Action_None` | 156 | 189 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 45 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 77 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 87 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 155 | 121 | inferred_complete_timeline |
| `Action_None` | 156 | 181 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 38 | 7 | inferred_complete_timeline |
| `Action_None` | 42 | 226 | 185 | inferred_complete_timeline |
| `Action_None` | 229 | 239 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 60 | 29 | inferred_complete_timeline |
| `Action_None` | 63 | 68 | 6 | inferred_complete_timeline |
| `Action_None` | 87 | 197 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 146 | 115 | inferred_complete_timeline |
| `Action_None` | 148 | 151 | 4 | inferred_complete_timeline |
| `Action_None` | 154 | 214 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 59 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 224 | 193 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 42–54 | 12 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 55–239 | 184 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 65–192 | 122 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 78–193 | 116 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 80–119 | 38 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 129–130 | 2 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 138–183 | 46 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 156–239 | 74 | 4 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 166–195 | 30 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 199–239 | 41 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `11` (C): Annotated start 35 != Inferred start 46
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 37 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [32–45], lower_priority='Action_PassBlock' annotated_start=35, effective_Action_PassBlock_start=46.
- ⚠️ Action 'Action_PassBlock' range [35-87] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-146] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-214] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-59] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-139] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-203] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-189] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-224] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [86-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [224-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [32-45] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-38] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-226] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-197] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-44] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-54] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-116] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-146] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-192] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-193] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-119] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-195] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>