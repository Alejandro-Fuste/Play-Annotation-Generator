# Play-Annotation-Generator Annotation Review — InsideZoneRead_326

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_326`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 104
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
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_Keep` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 1 | START | 1 | 10 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `12` | 4 | START | 11 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `17` | 4 | START | 4 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 4 | START | 4 | 13 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 4 | START | 4 | 19 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 10 | END | 1 | 10 |
| ✅ EXACT | `Action_ReadDefender` | QB | `4` | `3` | 15 | START | 15 | 22 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `6` | `5` | 20 | START | 20 | 78 |
| ✅ EXACT | `Action_Keep` | QB | `4` | `3` | 23 | START | 23 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `4` | `3` | 44 | START | 44 | 46 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 78 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–131
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 10 | 10 | inferred_complete_timeline |
| `Action_None` | 11 | 14 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 15 | 22 | 8 | inferred_complete_timeline |
| `Action_Keep` | 23 | 43 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 44 | 46 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 102 | 131 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 58 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 37 | 37 | inferred_complete_timeline |
| `Action_None` | 39 | 180 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 19 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 20 | 78 | 59 | inferred_complete_timeline |
| `Action_None` | 79 | 179 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 10 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 63 | 53 | inferred_complete_timeline |
| `Action_None` | 80 | 91 | 12 | inferred_complete_timeline |
| `Action_None` | 102 | 123 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 78 | 75 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 121 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–18
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 13 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 15 | 18 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 113 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 53 | 53 | inferred_complete_timeline |
| `Action_None` | 55 | 131 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 56 | 56 | inferred_complete_timeline |
| `Action_None` | 58 | 113 | 56 | inferred_complete_timeline |
| `Action_None` | 120 | 142 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 148 | 148 | inferred_complete_timeline |
| `Action_None` | 151 | 179 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 79 | 79 | inferred_complete_timeline |
| `Action_None` | 88 | 159 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 58 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 95 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 109 | 5 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 114 | 150 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–67 | 66 | 3 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–73 | 47 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–48 | 40 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 5–7 | 3 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 40–129 | 68 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 44–180 | 137 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 44–80 | 19 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 53–111 | 46 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 59–116 | 55 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 61–179 | 119 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 66–67 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 68–82 | 15 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 74–179 | 106 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 88–95 | 8 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 91–167 | 77 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 101–119 | 18 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 110–116 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 4 != Inferred start 11
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 651: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ Row 651: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [1–10], lower_priority='Action_ZoneBlock' annotated_start=4, effective_Action_ZoneBlock_start=11.
- ⚠️ Action 'Action_None' range [1-58] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-148] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-179] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-79] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-159] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [44-46] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [48-49] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [98-100] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [102-131] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-179] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-53] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-67] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-58] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-109] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-150] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-18] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-56] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-73] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-113] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-56] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-63] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-123] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-37] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-180] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-33] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-48] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-53] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-131] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-78] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-13] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [15-18] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-7] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-42] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-79] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-129] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-60] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-65] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-80] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-91] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-84] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-116] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-179] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-82] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-179] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-95] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-167] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-113] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-116] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.

</details>