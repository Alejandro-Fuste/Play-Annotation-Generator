# Play-Annotation-Generator Annotation Review — JetSweep_138

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_138`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 22
- **Ball Tracks:** 0
- **Action Segments:** 63
- **Validation Warnings:** 47
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 42
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `17` | `15` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `4` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 109 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `17` | `15` | 103 | START | 103 | 132 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `4` | 109 | START | 109 | 122 |
| ✅ EXACT | `Action_LeadBlock` | RB | `6` | `5` | 110 | START | 110 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `10` | `9` | 110 | START | 110 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `11` | `10` | 110 | START | 110 | 161 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `12` | `11` | 110 | START | 110 | 175 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `5` | `4` | 110 | START | 123 | 175 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `7` | 110 | START | 110 | 174 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 122 | END | 109 | 122 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 125 | START | 125 | 132 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `17` | `15` | 133 | START | 133 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 175 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_SnapReceive` | 109 | 122 | 14 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_Toss` | 125 | 132 | 8 | inferred_complete_timeline |
| `Action_None` | 133 | 163 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_LeadBlock` | 110 | 175 | 66 | inferred_complete_timeline |
| `Action_None` | 176 | 269 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 269 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 174 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 161 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 175 | 5 | inferred_complete_timeline |
| `Action_None` | 176 | 181 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_BallSnap` | 109 | 122 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 175 | 53 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 175 | 66 | inferred_complete_timeline |
| `Action_None` | 176 | 185 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 175 | 66 | inferred_complete_timeline |
| `Action_None` | 178 | 194 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 13–151
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 41 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 94 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 108 | 12 | inferred_complete_timeline |
| `Action_None` | 109 | 139 | 31 | inferred_complete_timeline |
| `Action_None` | 142 | 145 | 4 | inferred_complete_timeline |
| `Action_None` | 148 | 151 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 269 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 127 | 19 | inferred_complete_timeline |
| `Action_None` | 129 | 149 | 21 | inferred_complete_timeline |
| `Action_None` | 154 | 164 | 11 | inferred_complete_timeline |
| `Action_None` | 166 | 170 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 234 | 126 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |
| `Action_None` | 242 | 269 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 185 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 160 | 52 | inferred_complete_timeline |
| `Action_None` | 162 | 165 | 4 | inferred_complete_timeline |
| `Action_None` | 179 | 269 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 150 | 42 | inferred_complete_timeline |
| `Action_None` | 152 | 160 | 9 | inferred_complete_timeline |
| `Action_None` | 167 | 170 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | Position_Unknown | Team_Unknown | 103–269 | 167 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 114–269 | 156 | 1 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 137–269 | 133 | 1 | Undefined position; Undefined team |
| `18` | `26` | Position_Unknown | Team_Unknown | 168–182 | 13 | 2 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 194–269 | 76 | 1 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 211–269 | 59 | 1 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 214–269 | 56 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `5` (C): Annotated start 110 != Inferred start 123

### Track Identity Issues

- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 30 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 278: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [109–122], lower_priority='Action_ZoneBlock' annotated_start=110, effective_Action_ZoneBlock_start=123.
- ⚠️ Action 'Action_None' range [109-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-185] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-234] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-163] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-185] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-161] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [171-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-181] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-41] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-50] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-94] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-269] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-176] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '18' has 1 frames without a visible bounding box.
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

</details>