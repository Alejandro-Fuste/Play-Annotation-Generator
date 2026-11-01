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
- **Action Segments:** 79
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 1
- **Group Expanded Events:** 4
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | Position_Unknown | Team_Unknown | `13` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | Position_Unknown | `13` | `11` | 87 | START | 87 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `2` | 92 | START | 92 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `3` | 92 | START | 92 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `4` | 92 | START | 92 | 106 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `7` | `6` | 104 | END | 87 | 100 |
| ✅ EXACT | `Action_ReadDefender` | QB | `7` | `6` | 108 | START | 108 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `7` | `6` | 117 | START | 117 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `4` | `3` | 121 | START | 121 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `11` | `10` | 133 | START | 136 | 147 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 164 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_SnapReceive` | 87 | 100 | 14 | inferred_complete_timeline |
| `Action_None` | 107 | 107 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 108 | 116 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 117 | 117 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 129 | 132 | 4 | inferred_complete_timeline |
| `Action_None` | 133 | 241 | 109 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 164 | 73 | inferred_complete_timeline |
| `Action_None` | 165 | 201 | 37 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 120 | 29 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 121 | 131 | 11 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 134 | 150 | 17 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 158 | 164 | 7 | inferred_complete_timeline |
| `Action_None` | 165 | 299 | 135 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 106 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 164 | 15 | inferred_complete_timeline |
| `Action_None` | 165 | 203 | 39 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 213 | 127 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 141 | 55 | inferred_complete_timeline |
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
| `Action_PreSnap` | 19 | 86 | 68 | inferred_complete_timeline |
| `Action_None` | 87 | 173 | 87 | inferred_complete_timeline |
| `Action_None` | 176 | 299 | 124 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 127 | 41 | inferred_complete_timeline |
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
| `10` | `11` | Position_Unknown | Team_Unknown | 9–248 | 224 | 4 | Undefined position; Undefined team |
| `11` | `13` | Position_Unknown | Team_Unknown | 40–106 | 53 | 5 | Undefined position; Undefined team |
| `12` | `14` | Position_Unknown | Team_Unknown | 137–139 | 3 | 1 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 158–299 | 133 | 3 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 168–299 | 115 | 2 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 174–189 | 15 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 175–237 | 63 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 177–246 | 60 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 184–246 | 50 | 3 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 187–256 | 55 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 210–299 | 90 | 1 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 228–260 | 26 | 3 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 229–236 | 8 | 1 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 242–299 | 58 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 273–299 | 27 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `4` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 59 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [87-127] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-262] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-141] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-264] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-201] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [121-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [134-150] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [152-155] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-203] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-213] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-224] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [87-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' for track '6' starts at frame 117, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_Handoff' range [117-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [120-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [129-132] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-241] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-5] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-148] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-235] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [136-147] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [150-248] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [87-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-188] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-274] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-237] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-206] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-246] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-209] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-228] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-246] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-232] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-256] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-244] for track '21' has 2 frames without a visible bounding box.
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

</details>