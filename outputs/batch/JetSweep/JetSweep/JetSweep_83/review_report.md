# Play-Annotation-Generator Annotation Review — JetSweep_83

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_83`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 68
- **Validation Warnings:** 56
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 37
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ START CHANGED | `Action_LeadBlock` | TE | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `16` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 79 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 80 | START | 80 | 97 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `19` | `18` | 83 | START | 83 | 114 |
| ⚠️ START CHANGED | `Action_LeadBlock` | TE | `17` | `16` | 89 | START | 93 | 117 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `9` | 89 | START | 89 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `12` | `11` | 89 | START | 89 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `12` | 89 | START | 89 | 142 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `13` | 89 | START | 98 | 155 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `16` | `15` | 89 | START | 89 | 155 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 97 | END | 80 | 97 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 106 | START | 106 | 114 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `10` | `9` | 111 | START | 111 | 155 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `19` | `18` | 115 | START | 115 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 155 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_SnapReceive` | 80 | 97 | 18 | inferred_complete_timeline |
| `Action_None` | 98 | 105 | 8 | inferred_complete_timeline |
| `Action_Toss` | 106 | 114 | 9 | inferred_complete_timeline |
| `Action_None` | 115 | 149 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 158 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_LeadBlock` | 93 | 117 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 133 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 142 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 51 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 79 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 80 | 97 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 155 | 58 | inferred_complete_timeline |
| `Action_None` | 156 | 158 | 3 | inferred_complete_timeline |
| `Action_None` | 161 | 199 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 12 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 88 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 155 | 67 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 176 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 110 | 22 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 111 | 155 | 45 | inferred_complete_timeline |
| `Action_None` | 156 | 239 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 130 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 239 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 138 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 24 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 55 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_None` | 88 | 239 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 239 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 163 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 79 | 39 | inferred_complete_timeline |
| `Action_None` | 80 | 97 | 18 | inferred_complete_timeline |
| `Action_None` | 99 | 130 | 32 | inferred_complete_timeline |
| `Action_None` | 133 | 236 | 104 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 239 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 97 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 80–140 | 12 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 83–239 | 157 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 142–239 | 98 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 148–239 | 92 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 168–230 | 59 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 178–239 | 53 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 205–211 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_LeadBlock` for actor_track_id `17` (TE): Annotated start 89 != Inferred start 93
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 89 != Inferred start 98

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [80–97], lower_priority='Action_ZoneBlock' annotated_start=89, effective_Action_ZoneBlock_start=98.
- ⚠️ Action 'Action_None' range [80-130] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-163] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-97] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-236] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-138] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-158] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-239] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [106-114] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-55] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-59] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-133] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-51] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-12] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-176] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [93-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-140] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-226] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-190] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-211] for track '23' has 1 frames without a visible bounding box.
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

</details>