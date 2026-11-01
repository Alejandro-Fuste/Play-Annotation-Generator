# Play-Annotation-Generator Annotation Review — InsideZoneRead_246

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_246`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 22
- **Ball Tracks:** 0
- **Action Segments:** 48
- **Validation Warnings:** 64
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 40
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Keep` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `12` | `11` | 0 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `12` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `4` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `5` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `8` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `9` | `Group` | 0 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `4` | 0 | START | 0 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `8` | `7` | 0 | START | 0 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `9` | `8` | 0 | START | 0 | 39 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 4 | END | 0 | 4 |
| ✅ EXACT | `Action_ReadDefender` | QB | `4` | `3` | 10 | START | 10 | 28 |
| ✅ EXACT | `Action_Keep` | QB | `4` | `3` | 29 | START | 29 | 44 |
| ✅ EXACT | `Action_BallCarry` | QB | `4` | `3` | 45 | START | 45 | 150 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 75 | BOUNDARY | N/A | N/A |

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
| `Action_SnapReceive` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 9 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 10 | 28 | 19 | inferred_complete_timeline |
| `Action_Keep` | 29 | 44 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 45 | 150 | 106 | inferred_complete_timeline |

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
| `Action_ZoneBlock` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 75 | 9 | inferred_complete_timeline |
| `Action_None` | 76 | 150 | 75 | inferred_complete_timeline |

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
| `Action_ZoneBlock` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 75 | 30 | inferred_complete_timeline |
| `Action_None` | 76 | 150 | 75 | inferred_complete_timeline |

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
| `Action_ZoneBlock` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 22 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 75 | 49 | inferred_complete_timeline |
| `Action_None` | 76 | 150 | 75 | inferred_complete_timeline |

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
| `Action_ZoneBlock` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 150 | 75 | inferred_complete_timeline |

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
| `Action_None` | 0 | 39 | 40 | inferred_complete_timeline |

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
| `Action_None` | 0 | 35 | 36 | inferred_complete_timeline |
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
| `Action_None` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 5 | 11 | 7 | inferred_complete_timeline |
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
| `Action_None` | 0 | 2 | 3 | inferred_complete_timeline |
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
| `Action_None` | 0 | 150 | 151 | inferred_complete_timeline |

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
| `Action_None` | 0 | 150 | 151 | inferred_complete_timeline |

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
| `Action_None` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 132 | 150 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–150 | 148 | 2 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–141 | 138 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 39–150 | 111 | 2 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 84–150 | 64 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 85–150 | 66 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 110–150 | 40 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 115–150 | 36 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 127–129 | 3 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 145–150 | 6 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 147–150 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `12` (C)
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
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 492: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Overlapping action conflict at frame 0 for track '11': 'Action_BallSnap' vs 'Action_ZoneBlock'. Overriding with 'Action_ZoneBlock'.
- ⚠️ Action 'Action_None' range [0-39] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-66] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [45-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-35] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-80] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-35] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-141] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [0-65] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-150] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [0-39] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-150] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [0-13] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [16-17] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-22] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-2] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-11] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-148] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-2] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-16] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-150] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-52] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-93] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-122] for track '17' has 1 frames without a visible bounding box.
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

</details>