# Play-Annotation-Generator Annotation Review — JetSweep_8

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_8`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 22
- **Ball Tracks:** 0
- **Action Segments:** 68
- **Validation Warnings:** 59
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 26
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 40
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR | offense | `15` | `14` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `2` | `1` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `10` | `9` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `12` | `11` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `14` | `13` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `14` | `13` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `2` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `15` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR | `15` | `14` | 96 | START | 96 | 115 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 104 | START | 104 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `4` | `3` | 105 | START | 105 | 106 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `9` | 105 | START | 105 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `11` | 105 | START | 105 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `12` | 105 | START | 122 | 133 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `13` | 105 | START | 105 | 154 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 105 | START | 105 | 143 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 121 | END | 104 | 121 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 124 | START | 124 | 133 |
| ✅ EXACT | `Action_BallCarry` | C | `13` | `12` | 134 | START | 134 | 168 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `2` | `1` | 144 | START | 144 | 154 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `10` | `9` | 154 | BOUNDARY | N/A | 154 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `12` | `11` | 154 | BOUNDARY | 114 | 154 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `14` | `13` | 154 | BOUNDARY | 105 | 154 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `14` | `13` | 154 | BOUNDARY | 105 | 154 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `2` | `1` | 154 | BOUNDARY | 144 | 154 |

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
- **Visible Frames:** 0–168
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_SnapReceive` | 104 | 121 | 18 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_Toss` | 124 | 133 | 10 | inferred_complete_timeline |
| `Action_None` | 135 | 168 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 96–269
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 96 | 115 | 20 | inferred_complete_timeline |
| `Action_JetMotion` | 117 | 209 | 93 | inferred_complete_timeline |
| `Action_JetMotion` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_JetMotion` | 227 | 230 | 4 | inferred_complete_timeline |
| `Action_JetMotion` | 233 | 269 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 48 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 64 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 90 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 102 | 5 | inferred_complete_timeline |
| `Action_LeadBlock` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_LeadBlock` | 108 | 111 | 4 | inferred_complete_timeline |
| `Action_LeadBlock` | 114 | 154 | 41 | inferred_complete_timeline |
| `Action_None` | 155 | 185 | 31 | inferred_complete_timeline |
| `Action_None` | 187 | 261 | 75 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 143 | 39 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 144 | 154 | 11 | inferred_complete_timeline |
| `Action_None` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_None` | 161 | 204 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 111 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 154 | 41 | inferred_complete_timeline |
| `Action_None` | 155 | 174 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_BallSnap` | 104 | 121 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 133 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 134 | 168 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 115 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 154 | 50 | inferred_complete_timeline |
| `Action_None` | 155 | 158 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 156 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 217 | 114 | inferred_complete_timeline |
| `Action_None` | 219 | 222 | 4 | inferred_complete_timeline |
| `Action_None` | 228 | 269 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 165 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 177 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 161 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 260 | 157 | inferred_complete_timeline |
| `Action_None` | 264 | 267 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 217 | 114 | inferred_complete_timeline |
| `Action_None` | 221 | 269 | 49 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | Position_Unknown | Team_Unknown | 119–164 | 46 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 132–163 | 30 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 153–155 | 3 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 169–225 | 57 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 176–265 | 74 | 4 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 182–269 | 88 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 233–269 | 37 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [104–121], lower_priority='Action_ZoneBlock' annotated_start=105, effective_Action_ZoneBlock_start=122.
- ⚠️ Action 'Action_None' range [104-217] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-165] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-64] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-90] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-102] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [105-106] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [108-111] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-185] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-261] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-156] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-161] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [104-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [124-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-260] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-177] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [105-115] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-217] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [105-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [134-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [96-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [117-209] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [213-214] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [227-230] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [233-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-164] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-141] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-163] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-225] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-192] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-214] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-265] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-269] for track '20' has 1 frames without a visible bounding box.
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