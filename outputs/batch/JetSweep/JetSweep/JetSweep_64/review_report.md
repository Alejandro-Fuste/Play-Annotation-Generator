# Play-Annotation-Generator Annotation Review — JetSweep_64

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_64`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `1` | `0` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Toss` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 117 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `1` | `0` | 80 | START | 80 | 149 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 118 | START | 118 | 132 |
| ✅ EXACT | `Action_LeadBlock` | TE | `2` | `1` | 124 | START | 124 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `16` | 124 | START | 124 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `17` | 124 | START | 124 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 124 | START | 124 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `19` | 124 | START | 124 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 124 | START | 133 | 139 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 132 | END | 118 | 132 |
| ✅ EXACT | `Action_Toss` | QB | `12` | `11` | 136 | START | 136 | 149 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `1` | `0` | 150 | START | 150 | 225 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 173 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_SnapReceive` | 118 | 132 | 15 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_Toss` | 136 | 149 | 14 | inferred_complete_timeline |
| `Action_None` | 150 | 269 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 147 | 30 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 151 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_JetMotion` | 80 | 149 | 70 | inferred_complete_timeline |
| `Action_BallCarry` | 150 | 225 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_LeadBlock` | 124 | 173 | 50 | inferred_complete_timeline |
| `Action_None` | 174 | 234 | 61 | inferred_complete_timeline |
| `Action_None` | 238 | 269 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 173 | 50 | inferred_complete_timeline |
| `Action_None` | 174 | 269 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 143 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 173 | 27 | inferred_complete_timeline |
| `Action_None` | 174 | 269 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_BallSnap` | 118 | 132 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 139 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 152 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 173 | 16 | inferred_complete_timeline |
| `Action_None` | 174 | 231 | 58 | inferred_complete_timeline |
| `Action_None` | 237 | 245 | 9 | inferred_complete_timeline |
| `Action_None` | 248 | 250 | 3 | inferred_complete_timeline |
| `Action_None` | 254 | 257 | 4 | inferred_complete_timeline |
| `Action_None` | 259 | 269 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 130 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 143 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 157 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 173 | 9 | inferred_complete_timeline |
| `Action_None` | 174 | 269 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 173 | 50 | inferred_complete_timeline |
| `Action_None` | 174 | 184 | 11 | inferred_complete_timeline |
| `Action_None` | 188 | 191 | 4 | inferred_complete_timeline |
| `Action_None` | 199 | 269 | 71 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 71 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 89 | 7 | inferred_complete_timeline |
| `Action_None` | 120 | 123 | 4 | inferred_complete_timeline |
| `Action_None` | 129 | 134 | 6 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_None` | 141 | 269 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 153 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 168 | 51 | inferred_complete_timeline |
| `Action_None` | 170 | 178 | 9 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 167 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 117 | 89 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 184 | 67 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 260 | 143 | inferred_complete_timeline |
| `Action_None` | 263 | 264 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 160–269 | 109 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 183–269 | 65 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 184–269 | 78 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 190–269 | 80 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 193–269 | 77 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 264–268 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 130: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [118–132], lower_priority='Action_ZoneBlock' annotated_start=124, effective_Action_ZoneBlock_start=133.
- ⚠️ Action 'Action_BallCarry' range [150-225] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-234] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-168] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-178] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-260] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-153] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-269] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-184] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-173] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-130] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [135-143] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [149-157] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-231] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-245] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-75] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-134] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-265] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-201] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-258] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-202] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-246] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-269] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>