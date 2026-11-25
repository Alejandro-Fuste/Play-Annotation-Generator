# Play-Annotation-Generator Annotation Review — InsideZoneRead_232

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_232`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 1
- **Action Segments:** 53
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 4
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 32
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | DT1 | defense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `6` | `5` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_ReadDefender` | LG | offense | `7` | `6` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | LT | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 66 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | DT1 | `10` | `9` | 138 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `0` | 141 | START | 141 | 210 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `3` | 141 | START | 141 | 173 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `6` | `5` | 141 | START | 141 | 210 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `7` | `6` | 141 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `9` | `8` | 141 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | LG | `7` | `6` | 150 | END | 138 | 144 |
| ✅ EXACT | `Action_ReadDefender` | LG | `7` | `6` | 155 | START | 155 | 167 |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | C | `9` | `8` | 159 | START | N/A | N/A |
| ✅ EXACT | `Action_Handoff` | LG | `7` | `6` | 168 | START | 168 | 173 |
| ✅ EXACT | `Action_BallCarry` | LT | `4` | `3` | 174 | START | 174 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 221 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 137 | 54 | inferred_complete_timeline |
| `Action_None` | 138 | 210 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 84 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 140 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 173 | 33 | inferred_complete_timeline |
| `Action_BallCarry` | 174 | 210 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 137 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 138 | 144 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 150 | 150 | 1 | inferred_complete_timeline |
| `Action_None` | 151 | 154 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 155 | 167 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 168 | 173 | 6 | inferred_complete_timeline |
| `Action_None` | 174 | 183 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 210 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 210 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 137 | 3 | inferred_complete_timeline |
| `Action_None` | 138 | 210 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 210 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 210 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–17
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 73–92 | 20 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 75–210 | 136 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 99–210 | 109 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 109–177 | 68 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 116–206 | 91 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 133–210 | 76 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 142–210 | 69 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 155–210 | 37 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 166–210 | 45 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 171–210 | 40 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 188–210 | 23 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 200–210 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | 8 | 45 | 35 | 92.1% | 12–14 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `10` (DT1)
- ❌ Missing segment for action `Action_ZoneBlock` on target `7` (LG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `9` (C)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `7` (2 segments found)
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `9` (C)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 36 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '6' has invalid range: start=141, end=137. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '8' has invalid range: start=141, end=66. Clamping end to start.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '8' has invalid range: start=159, end=66. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '9' has invalid range: start=138, end=75. Clamping end to start.
- ⚠️ Action 'Action_ZoneBlock' range [141-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-84] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [174-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [141-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [138-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [155-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-183] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-172] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-170] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-206] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-174] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '25' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_232'; source metadata written as null.

</details>