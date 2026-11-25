# Play-Annotation-Generator Annotation Review — InsideZoneRead_143

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_143`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 0
- **Group Expanded Events:** 4
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `30` | `21` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `30` | `21` |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | Team_Unknown | `30` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT | defense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 100 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `19` | `16` | 122 | START | 175 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `2` | 125 | START | 125 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `3` | 125 | START | 125 | 131 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RT | `5` | `4` | 125 | START | 150 | 201 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `30` | `21` | 136 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `30` | `21` | 141 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | `30` | `21` | 154 | START | 228 | 228 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT | `8` | `7` | 159 | START | 159 | 173 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 201 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–241
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 117 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 241 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 201 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 131 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 150 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 201 | 44 | inferred_complete_timeline |
| `Action_None` | 202 | 299 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 201 | 52 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 218 | 220 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 213 | 92 | inferred_complete_timeline |
| `Action_None` | 218 | 224 | 7 | inferred_complete_timeline |
| `Action_None` | 232 | 239 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 141 | 20 | inferred_complete_timeline |
| `Action_None` | 152 | 264 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 158 | 140 | inferred_complete_timeline |
| `Action_BallCarry` | 159 | 173 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 176 | 299 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_None` | 129 | 262 | 134 | inferred_complete_timeline |
| `Action_None` | 274 | 299 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 2–140 | 139 | 2 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 3–235 | 156 | 4 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 9–248 | 224 | 5 | Undefined position; Undefined team |
| `11` | `13` | Position_Unknown | Team_Unknown | 40–106 | 53 | 3 | Undefined position; Undefined team |
| `12` | `14` | Position_Unknown | Team_Unknown | 137–139 | 3 | 1 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 158–299 | 133 | 3 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 168–299 | 115 | 2 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 174–189 | 15 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 175–237 | 63 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 177–246 | 60 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 184–246 | 50 | 3 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 187–256 | 55 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 210–299 | 90 | 1 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 228–260 | 26 | 4 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 229–236 | 8 | 1 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 242–299 | 58 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 273–299 | 27 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `19` (Position_Unknown): Annotated start 122 != Inferred start 175
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (5 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `5` (RT): Annotated start 125 != Inferred start 150
- ❌ Missing segment for action `Action_SnapReceive` on target `21` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `21` (Position_Unknown)
- ⚠️ `Action_Handoff` for actor_track_id `30` (Position_Unknown): Annotated start 154 != Inferred start 228
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '16' has invalid range: start=175, end=136. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '21' has invalid range: start=228, end=136. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '21' has invalid range: start=228, end=153. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '21' has invalid range: start=228, end=158. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-262] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-141] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-264] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-201] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-150] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [152-155] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-213] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-224] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-241] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [159-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-5] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-148] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-235] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-147] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-248] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-89] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-106] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-188] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-274] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-237] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-206] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-246] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-209] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-228] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-246] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-232] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-256] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-244] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-236] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_143'; source metadata written as null.

</details>