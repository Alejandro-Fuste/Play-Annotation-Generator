# Play-Annotation-Generator Annotation Review — Draw_77

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_77`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 124
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `1` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 50 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 51 | START | 51 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `13` | `12` | 54 | START | 97 | 98 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 64 | END | 51 | 64 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `5` | `4` | 73 | START | 73 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `5` | `4` | 85 | START | 85 | 97 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 150 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_SnapReceive` | 51 | 64 | 14 | inferred_complete_timeline |
| `Action_None` | 65 | 72 | 8 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 73 | 84 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 85 | 97 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 169 | 173 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 175 | 179 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 181 | 193 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 196 | 239 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 131 | 81 | inferred_complete_timeline |
| `Action_None` | 136 | 143 | 8 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 174 | 124 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 109 | 59 | inferred_complete_timeline |
| `Action_None` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_None` | 115 | 119 | 5 | inferred_complete_timeline |
| `Action_None` | 121 | 153 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 86 | 36 | inferred_complete_timeline |
| `Action_None` | 88 | 221 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 232 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_BallSnap` | 51 | 58 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 102 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 142 | 92 | inferred_complete_timeline |
| `Action_None` | 145 | 177 | 33 | inferred_complete_timeline |
| `Action_None` | 179 | 184 | 6 | inferred_complete_timeline |
| `Action_None` | 186 | 197 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 193 | 143 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 206 | 239 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 154 | 104 | inferred_complete_timeline |
| `Action_None` | 161 | 163 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 239 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 239 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 225 | 175 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 239 | 189 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 65–66 | 2 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 103–163 | 61 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 143–157 | 15 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 148–225 | 63 | 5 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 151–216 | 48 | 5 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 156–218 | 49 | 8 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 170–239 | 64 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 173–205 | 29 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 174–227 | 51 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 176–225 | 43 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 189–214 | 24 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 204–239 | 36 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 206–239 | 34 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 211–239 | 29 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 212–227 | 16 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 216–237 | 22 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 216–218 | 3 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 228–230 | 3 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 228–233 | 6 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 154: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 154: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [51–64], lower_priority='Action_PassBlock' annotated_start=54, effective_Action_PassBlock_start=65.
- ⚠️ Action 'Action_None' range [51-232] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-193] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-86] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-221] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [85-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [169-173] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [175-179] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [181-193] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-225] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-131] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-143] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-142] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-177] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-174] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [51-58] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [101-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-154] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-179] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-194] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-225] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-159] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-216] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-199] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-214] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-192] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-197] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-227] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-225] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-194] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-214] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-227] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-237] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-233] for track '35' has 1 frames without a visible bounding box.
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

</details>