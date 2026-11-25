# Play-Annotation-Generator Annotation Review — InsideZoneRead_246

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_246`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 22
- **Ball Tracks:** 0
- **Action Segments:** 62
- **Validation Warnings:** 65
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | LB2 | defense | `10` | `9` |
| ✅ EXACT | `Action_ReadDefender` | LB2 | defense | `10` | `9` |
| ✅ EXACT | `Action_Keep` | LB2 | defense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | LB2 | defense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 10 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `20` | `17` | 8 | START | 110 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 11 | START | 11 | 13 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `4` | 11 | START | 11 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `8` | `7` | 11 | START | 11 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `9` | `8` | 11 | START | 11 | 39 |
| ✅ EXACT | `Action_SnapReceive` | LB2 | `10` | `9` | 21 | END | 8 | 21 |
| ✅ EXACT | `Action_ReadDefender` | LB2 | `10` | `9` | 25 | START | 25 | 36 |
| ✅ EXACT | `Action_Keep` | LB2 | `10` | `9` | 37 | START | 37 | 62 |
| ✅ EXACT | `Action_BallCarry` | LB2 | `10` | `9` | 63 | START | 63 | 150 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 82 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 150 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 65 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 82 | 16 | inferred_complete_timeline |
| `Action_None` | 83 | 150 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 39 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 82 | 37 | inferred_complete_timeline |
| `Action_None` | 83 | 150 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 13 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 22 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 82 | 56 | inferred_complete_timeline |
| `Action_None` | 83 | 150 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 82 | 72 | inferred_complete_timeline |
| `Action_None` | 83 | 150 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 39 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 35 | 28 | inferred_complete_timeline |
| `Action_None` | 50 | 80 | 31 | inferred_complete_timeline |
| `Action_None` | 82 | 150 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 7 | 3 | inferred_complete_timeline |
| `Action_None` | 8 | 11 | 4 | inferred_complete_timeline |
| `Action_None` | 51 | 64 | 14 | inferred_complete_timeline |
| `Action_None` | 67 | 148 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 10 | 16 | 7 | inferred_complete_timeline |
| `Action_None` | 20 | 150 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 150 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 8 | 21 | 14 | inferred_complete_timeline |
| `Action_None` | 22 | 24 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 25 | 36 | 12 | inferred_complete_timeline |
| `Action_Keep` | 37 | 62 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 63 | 150 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 130 | 123 | inferred_complete_timeline |
| `Action_None` | 132 | 150 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–150 | 148 | 3 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–141 | 138 | 3 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 39–150 | 111 | 2 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 84–150 | 64 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 85–150 | 66 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 110–150 | 40 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 115–150 | 36 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 127–129 | 3 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 145–150 | 6 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 147–150 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `20` (Position_Unknown): Annotated start 8 != Inferred start 110
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 492: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=110, end=21. Clamping end to start.
- ⚠️ Action 'Action_None' range [8-39] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-66] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-35] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-80] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-35] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-141] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-65] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-150] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-39] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [63-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-150] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-13] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [16-17] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-22] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-11] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-148] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-16] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-150] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-52] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-93] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-122] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_246'; source metadata written as null.

</details>