# Play-Annotation-Generator Annotation Review — InsideZoneRead_236

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_236`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 21
- **Ball Tracks:** 0
- **Action Segments:** 58
- **Validation Warnings:** 54
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 40
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB1 | offense | `12` | `11` |
| ✅ EXACT | `Action_ReadDefender` | QB1 | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB1 | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB2 | offense | `10` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | `10` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | `12` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 11 | START | 11 | 24 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `11` | `10` | 14 | START | 14 | 49 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `12` | 14 | START | 34 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `3` | `2` | 14 | START | 14 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `3` | 14 | START | 14 | 49 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `4` | 14 | START | 14 | 49 |
| ✅ EXACT | `Action_SnapReceive` | QB1 | `12` | `11` | 26 | END | 11 | 26 |
| ✅ EXACT | `Action_ReadDefender` | QB1 | `12` | `11` | 32 | START | 32 | 39 |
| ✅ EXACT | `Action_Handoff` | QB1 | `12` | `11` | 40 | START | 40 | 53 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 49 | BOUNDARY | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB2 | `10` | `9` | 54 | START | 54 | 58 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 26 | 16 | inferred_complete_timeline |
| `Action_None` | 27 | 31 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 32 | 39 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 40 | 53 | 14 | inferred_complete_timeline |
| `Action_None` | 54 | 79 | 26 | inferred_complete_timeline |
| `Action_None` | 82 | 95 | 14 | inferred_complete_timeline |
| `Action_None` | 97 | 118 | 22 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>QB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_BallCarry` | 54 | 58 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 60 | 118 | 59 | inferred_complete_timeline |
| `Action_BallCarry` | 121 | 145 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 152 | 177 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 49 | 36 | inferred_complete_timeline |
| `Action_None` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_None` | 62 | 68 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 49 | 36 | inferred_complete_timeline |
| `Action_None` | 50 | 141 | 92 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 24 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 49 | 16 | inferred_complete_timeline |
| `Action_None` | 50 | 62 | 13 | inferred_complete_timeline |
| `Action_None` | 64 | 169 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 49 | 36 | inferred_complete_timeline |
| `Action_None` | 50 | 180 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 49 | 36 | inferred_complete_timeline |
| `Action_None` | 50 | 88 | 39 | inferred_complete_timeline |
| `Action_None` | 90 | 180 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 81 | 71 | inferred_complete_timeline |
| `Action_None` | 88 | 100 | 13 | inferred_complete_timeline |
| `Action_None` | 119 | 133 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 180 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 180 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 141 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 180 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 158 | 148 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 67–180 | 114 | 1 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 67–149 | 80 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 103–141 | 39 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 105–106 | 2 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 123–160 | 38 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 144–180 | 37 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 155–180 | 24 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 160–180 | 21 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 14 != Inferred start 34
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 36 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [11–26], lower_priority='Action_ZoneBlock' annotated_start=14, effective_Action_ZoneBlock_start=27.
- ⚠️ Action 'Action_None' range [11-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-158] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-88] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-141] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-81] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-100] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-133] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [54-58] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [60-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [121-145] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [152-177] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-79] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-118] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [11-24] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-62] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-169] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-149] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '20' has 1 frames without a visible bounding box.
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

</details>