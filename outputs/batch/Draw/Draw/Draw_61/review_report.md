# Play-Annotation-Generator Annotation Review — Draw_61

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_61`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `11` | `10` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 38 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 39 | START | 39 | 54 |
| ✅ EXACT | `Action_PassBlock` | LT | `11` | `10` | 42 | START | 42 | 83 |
| ✅ EXACT | `Action_PassBlock` | RT | `14` | `13` | 42 | START | 42 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `19` | 42 | START | 42 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `20` | 42 | START | 55 | 94 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 54 | END | 39 | 54 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `13` | `12` | 60 | START | 60 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `13` | `12` | 74 | START | 74 | 96 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 104 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_SnapReceive` | 39 | 54 | 16 | inferred_complete_timeline |
| `Action_None` | 55 | 59 | 5 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 60 | 73 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 74 | 96 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 100 | 108 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 122 | 239 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 177 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 215 | 177 | inferred_complete_timeline |
| `Action_None` | 217 | 239 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 150 | 112 | inferred_complete_timeline |
| `Action_None` | 156 | 158 | 3 | inferred_complete_timeline |
| `Action_None` | 160 | 212 | 53 | inferred_complete_timeline |
| `Action_None` | 215 | 229 | 15 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 239 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 83 | 42 | inferred_complete_timeline |
| `Action_None` | 108 | 112 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_BallSnap` | 39 | 54 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 94 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 99 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 104 | 63 | inferred_complete_timeline |
| `Action_None` | 105 | 189 | 85 | inferred_complete_timeline |
| `Action_None` | 192 | 239 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 104 | 63 | inferred_complete_timeline |
| `Action_None` | 105 | 239 | 135 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 239 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 74 | 36 | inferred_complete_timeline |
| `Action_None` | 77 | 122 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 56 | 18 | inferred_complete_timeline |
| `Action_None` | 59 | 66 | 8 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 72 | 79 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 58 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 239 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 196 | 158 | inferred_complete_timeline |
| `Action_None` | 200 | 239 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 239 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 67 | 29 | inferred_complete_timeline |
| `Action_None` | 69 | 167 | 99 | inferred_complete_timeline |
| `Action_None` | 170 | 239 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 228 | 190 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 224 | 186 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 227 | 189 | inferred_complete_timeline |
| `Action_None` | 229 | 233 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 45–239 | 191 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 88–110 | 19 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 92–239 | 148 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 101–239 | 139 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 104–239 | 136 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 114–239 | 102 | 3 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 120–122 | 3 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 143–170 | 6 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 147–239 | 93 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 188–196 | 9 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 121: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [39–54], lower_priority='Action_PassBlock' annotated_start=42, effective_Action_PassBlock_start=55.
- ⚠️ Action 'Action_None' range [39-215] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-212] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-229] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-228] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-177] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-227] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-233] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-83] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-224] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [74-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [100-108] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-56] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-79] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-196] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-58] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [39-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-94] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-99] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-52] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-65] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-74] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-98] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-204] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-196] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>